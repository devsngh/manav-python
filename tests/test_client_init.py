"""Smoke tests — no live API calls, just config wiring."""

import pytest

from manav import (
    AsyncClient,
    AuthenticationError,
    Client,
    ManavError,
    NotFoundError,
    RateLimitError,
    __version__,
)


def test_version_is_string():
    assert isinstance(__version__, str)
    assert __version__.count(".") >= 2


def test_client_requires_api_key(monkeypatch):
    monkeypatch.delenv("MANAV_API_KEY", raising=False)
    with pytest.raises(AuthenticationError, match="No API key"):
        Client()


def test_client_reads_env_var(monkeypatch):
    monkeypatch.setenv("MANAV_API_KEY", "mnv_test_from_env")
    c = Client()
    assert c.api_key == "mnv_test_from_env"
    c.close()


def test_client_explicit_api_key_wins(monkeypatch):
    monkeypatch.setenv("MANAV_API_KEY", "mnv_env")
    c = Client(api_key="mnv_explicit")
    assert c.api_key == "mnv_explicit"
    c.close()


def test_client_default_base_url():
    c = Client(api_key="mnv_x")
    assert c.base_url == "https://api.manavagi.com"
    c.close()


def test_client_base_url_strips_trailing_slash():
    c = Client(api_key="mnv_x", base_url="https://custom.example.com/")
    assert c.base_url == "https://custom.example.com"
    c.close()


def test_client_sends_expected_headers():
    c = Client(api_key="mnv_test_hdr")
    hdrs = c._headers()
    assert hdrs["X-API-Key"] == "mnv_test_hdr"
    assert hdrs["User-Agent"].startswith("manav-python/")
    assert hdrs["Accept"] == "application/json"
    c.close()


def test_async_client_context_manager_works():
    """Just verify it can be constructed + entered without a live API."""
    import asyncio

    async def _go():
        async with AsyncClient(api_key="mnv_test") as client:
            assert client.api_key == "mnv_test"

    asyncio.run(_go())


def test_exception_hierarchy():
    assert issubclass(AuthenticationError, ManavError)
    assert issubclass(NotFoundError, ManavError)
    assert issubclass(RateLimitError, ManavError)


def test_rate_limit_error_carries_retry_after():
    err = RateLimitError("too many", retry_after=42)
    assert err.retry_after == 42
