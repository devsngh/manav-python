"""Manav client — top-level entry point.

Wraps httpx to add:
  - X-API-Key auth on every request
  - JSON body decoding
  - Error responses mapped to typed exceptions
  - Simple retry on 429 / 5xx with exponential backoff

The `.agents`, `.chat`, `.tasks`, ... namespaces are placeholders here.
Once the openapi-python-client generator lands, they're wired to the
generated low-level API modules — but the top-level ergonomic surface
stays stable across regenerations.
"""

from __future__ import annotations

import asyncio
import os
import time
from typing import Any

import httpx

from manav._version import __version__
from manav.exceptions import (
    APIError,
    AuthenticationError,
    ManavError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)

DEFAULT_BASE_URL = "https://api.manavagi.com"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 2
USER_AGENT = f"manav-python/{__version__}"


def _api_key_from_env() -> str | None:
    return os.environ.get("MANAV_API_KEY")


def _raise_for_status(resp: httpx.Response) -> None:
    """Map HTTP status → typed SDK exception."""
    if resp.status_code < 400:
        return

    # Try to extract a useful error message from JSON body
    body: Any = None
    message = f"HTTP {resp.status_code}"
    try:
        body = resp.json()
        if isinstance(body, dict):
            message = body.get("detail") or body.get("message") or message
    except Exception:  # noqa: BLE001 — body may be non-JSON
        body = resp.text or None

    kwargs = {"status_code": resp.status_code, "body": body}

    if resp.status_code == 401:
        raise AuthenticationError(message, **kwargs)
    if resp.status_code == 404:
        raise NotFoundError(message, **kwargs)
    if resp.status_code == 429:
        retry_after_hdr = resp.headers.get("Retry-After")
        retry_after = int(retry_after_hdr) if retry_after_hdr and retry_after_hdr.isdigit() else None
        raise RateLimitError(message, retry_after=retry_after, **kwargs)
    if 400 <= resp.status_code < 500:
        raise ValidationError(message, **kwargs)
    raise APIError(message, **kwargs)


class _BaseClient:
    """Shared init / config for sync and async clients."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ):
        api_key = api_key or _api_key_from_env()
        if not api_key:
            raise AuthenticationError(
                "No API key provided. Pass api_key='mnv_...' or set MANAV_API_KEY env var. "
                "Generate a key at https://platform.manavagi.com/settings/api-keys"
            )
        self.api_key = api_key
        self.base_url = (base_url or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries

    def _headers(self) -> dict[str, str]:
        return {
            "X-API-Key": self.api_key,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        }


class Client(_BaseClient):
    """Synchronous Manav client.

    Example:
        from manav import Client

        client = Client(api_key="mnv_...")
        agents = client.get("/api/agents")

    (Once codegen lands, high-level namespaces will be:
        client.agents.list(), client.chat.send(...), etc.)
    """

    def __init__(self, api_key: str | None = None, **kwargs: Any):
        super().__init__(api_key, **kwargs)
        self._http = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self._headers(),
        )

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        """Low-level request with retry-on-429/5xx. Use only if a
        high-level namespace doesn't cover what you need."""
        attempt = 0
        while True:
            resp = self._http.request(method, path, **kwargs)
            if resp.status_code < 429 or attempt >= self.max_retries:
                _raise_for_status(resp)
                return resp
            # Backoff: use Retry-After hint or exponential
            retry_after_hdr = resp.headers.get("Retry-After")
            delay = (
                int(retry_after_hdr)
                if retry_after_hdr and retry_after_hdr.isdigit()
                else 2**attempt
            )
            time.sleep(delay)
            attempt += 1

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs).json()

    def post(self, path: str, json: Any = None, **kwargs: Any) -> Any:
        return self.request("POST", path, json=json, **kwargs).json()


class AsyncClient(_BaseClient):
    """Async Manav client. Same surface as Client but every I/O method is a coroutine.

    Example:
        from manav import AsyncClient

        async with AsyncClient(api_key="mnv_...") as client:
            agents = await client.get("/api/agents")
    """

    def __init__(self, api_key: str | None = None, **kwargs: Any):
        super().__init__(api_key, **kwargs)
        self._http = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self._headers(),
        )

    async def close(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        attempt = 0
        while True:
            resp = await self._http.request(method, path, **kwargs)
            if resp.status_code < 429 or attempt >= self.max_retries:
                _raise_for_status(resp)
                return resp
            retry_after_hdr = resp.headers.get("Retry-After")
            delay = (
                int(retry_after_hdr)
                if retry_after_hdr and retry_after_hdr.isdigit()
                else 2**attempt
            )
            await asyncio.sleep(delay)
            attempt += 1

    async def get(self, path: str, **kwargs: Any) -> Any:
        return (await self.request("GET", path, **kwargs)).json()

    async def post(self, path: str, json: Any = None, **kwargs: Any) -> Any:
        return (await self.request("POST", path, json=json, **kwargs)).json()
