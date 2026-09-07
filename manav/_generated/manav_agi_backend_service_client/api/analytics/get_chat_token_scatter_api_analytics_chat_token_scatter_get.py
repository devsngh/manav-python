from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_token_scatter_response import ChatTokenScatterResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 30,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/analytics/chat/token-scatter",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChatTokenScatterResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ChatTokenScatterResponse.from_dict(response.json())

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
) -> Response[ChatTokenScatterResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[ChatTokenScatterResponse | HTTPValidationError]:
    """Get Chat Token Scatter

     Sample of (query_tokens, response_tokens, bot_id) per dialogue for the scatter plot.

    Args:
        days (int | Unset):  Default: 30.
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatTokenScatterResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> ChatTokenScatterResponse | HTTPValidationError | None:
    """Get Chat Token Scatter

     Sample of (query_tokens, response_tokens, bot_id) per dialogue for the scatter plot.

    Args:
        days (int | Unset):  Default: 30.
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatTokenScatterResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        days=days,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[ChatTokenScatterResponse | HTTPValidationError]:
    """Get Chat Token Scatter

     Sample of (query_tokens, response_tokens, bot_id) per dialogue for the scatter plot.

    Args:
        days (int | Unset):  Default: 30.
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatTokenScatterResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> ChatTokenScatterResponse | HTTPValidationError | None:
    """Get Chat Token Scatter

     Sample of (query_tokens, response_tokens, bot_id) per dialogue for the scatter plot.

    Args:
        days (int | Unset):  Default: 30.
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatTokenScatterResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
