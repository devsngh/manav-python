from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.span_detail_response import SpanDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    span_id: UUID,
    *,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_bot_id, Unset):
        headers["X-Bot-Id"] = x_bot_id

    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent-traces/spans/{span_id}".format(
            span_id=quote(str(span_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SpanDetailResponse | None:
    if response.status_code == 200:
        response_200 = SpanDetailResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SpanDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    span_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SpanDetailResponse]:
    """Get Span

     Pane-3: full span detail including raw attributes JSONB.

    Args:
        span_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpanDetailResponse]
    """

    kwargs = _get_kwargs(
        span_id=span_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    span_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SpanDetailResponse | None:
    """Get Span

     Pane-3: full span detail including raw attributes JSONB.

    Args:
        span_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpanDetailResponse
    """

    return sync_detailed(
        span_id=span_id,
        client=client,
        x_bot_id=x_bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    span_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SpanDetailResponse]:
    """Get Span

     Pane-3: full span detail including raw attributes JSONB.

    Args:
        span_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SpanDetailResponse]
    """

    kwargs = _get_kwargs(
        span_id=span_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    span_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SpanDetailResponse | None:
    """Get Span

     Pane-3: full span detail including raw attributes JSONB.

    Args:
        span_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SpanDetailResponse
    """

    return (
        await asyncio_detailed(
            span_id=span_id,
            client=client,
            x_bot_id=x_bot_id,
            authorization=authorization,
        )
    ).parsed
