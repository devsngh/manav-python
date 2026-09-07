from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.trace_detail_response import TraceDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trace_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/system-logs/traces/{trace_id}".format(
            trace_id=quote(str(trace_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TraceDetailResponse | None:
    if response.status_code == 200:
        response_200 = TraceDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | TraceDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceDetailResponse]:
    """Get Trace

     All spans for a given trace (for waterfall view).

    `trace_id` is a plain string (36-char UUIDs OR 32-char no-dash hex OR
    other client-supplied ids). We do NOT constrain to UUID because
    ~5.5% of historical traces were ingested with non-UUID `trace_id`
    values (X-Request-Id headers from external clients, etc).

    Args:
        trace_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceDetailResponse]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceDetailResponse | None:
    """Get Trace

     All spans for a given trace (for waterfall view).

    `trace_id` is a plain string (36-char UUIDs OR 32-char no-dash hex OR
    other client-supplied ids). We do NOT constrain to UUID because
    ~5.5% of historical traces were ingested with non-UUID `trace_id`
    values (X-Request-Id headers from external clients, etc).

    Args:
        trace_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceDetailResponse
    """

    return sync_detailed(
        trace_id=trace_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceDetailResponse]:
    """Get Trace

     All spans for a given trace (for waterfall view).

    `trace_id` is a plain string (36-char UUIDs OR 32-char no-dash hex OR
    other client-supplied ids). We do NOT constrain to UUID because
    ~5.5% of historical traces were ingested with non-UUID `trace_id`
    values (X-Request-Id headers from external clients, etc).

    Args:
        trace_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceDetailResponse]
    """

    kwargs = _get_kwargs(
        trace_id=trace_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trace_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceDetailResponse | None:
    """Get Trace

     All spans for a given trace (for waterfall view).

    `trace_id` is a plain string (36-char UUIDs OR 32-char no-dash hex OR
    other client-supplied ids). We do NOT constrain to UUID because
    ~5.5% of historical traces were ingested with non-UUID `trace_id`
    values (X-Request-Id headers from external clients, etc).

    Args:
        trace_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceDetailResponse
    """

    return (
        await asyncio_detailed(
            trace_id=trace_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
