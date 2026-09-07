from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_message_list_response import BotMessageListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    conversation_id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/bots/conversations/{conversation_id}/messages".format(
            conversation_id=quote(str(conversation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BotMessageListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BotMessageListResponse.from_dict(response.json())

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
) -> Response[BotMessageListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BotMessageListResponse | HTTPValidationError]:
    """Get Bot Conversation Messages

     Get messages in a bot conversation. User (any bot participant),
    bot (impersonation), or super-admin observer.

    Args:
        conversation_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotMessageListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BotMessageListResponse | HTTPValidationError | None:
    """Get Bot Conversation Messages

     Get messages in a bot conversation. User (any bot participant),
    bot (impersonation), or super-admin observer.

    Args:
        conversation_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotMessageListResponse | HTTPValidationError
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BotMessageListResponse | HTTPValidationError]:
    """Get Bot Conversation Messages

     Get messages in a bot conversation. User (any bot participant),
    bot (impersonation), or super-admin observer.

    Args:
        conversation_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotMessageListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BotMessageListResponse | HTTPValidationError | None:
    """Get Bot Conversation Messages

     Get messages in a bot conversation. User (any bot participant),
    bot (impersonation), or super-admin observer.

    Args:
        conversation_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotMessageListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
