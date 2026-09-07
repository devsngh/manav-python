from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/health/ready",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Health Ready

     Readiness probe — can we actually serve requests?

    K8s / load balancers use this to decide if traffic should be routed
    here. Returns 503 (not 200) on degraded so the LB pulls us OUT of
    rotation instead of letting requests fail downstream.

    T2.9: includes per-engine pool stats so ops sees pool exhaustion BEFORE
    users do. A pool whose checkout >= size + 0.8*max_overflow is flagged
    "saturated" (warning, not failure); only an unreachable DB is "down".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Health Ready

     Readiness probe — can we actually serve requests?

    K8s / load balancers use this to decide if traffic should be routed
    here. Returns 503 (not 200) on degraded so the LB pulls us OUT of
    rotation instead of letting requests fail downstream.

    T2.9: includes per-engine pool stats so ops sees pool exhaustion BEFORE
    users do. A pool whose checkout >= size + 0.8*max_overflow is flagged
    "saturated" (warning, not failure); only an unreachable DB is "down".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
