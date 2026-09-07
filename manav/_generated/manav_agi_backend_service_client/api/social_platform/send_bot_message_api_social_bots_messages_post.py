from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_message_create import BotMessageCreate
from ...models.bot_message_response import BotMessageResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BotMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/social/bots/messages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BotMessageResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = BotMessageResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BotMessageResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BotMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[BotMessageResponse | HTTPValidationError]:
    """Send Bot Message

     Send a message between bots.

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header — trusted MCP path. Orchestrator sets
        this to the currently-running agent's bot_id so LLM calls made
        from within agent A's session attribute to agent A, not the
        outer HTTP caller. Only honored if the target bot is a
        participant of THIS conversation.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BotMessageCreate): Schema for sending a bot message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BotMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> BotMessageResponse | HTTPValidationError | None:
    """Send Bot Message

     Send a message between bots.

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header — trusted MCP path. Orchestrator sets
        this to the currently-running agent's bot_id so LLM calls made
        from within agent A's session attribute to agent A, not the
        outer HTTP caller. Only honored if the target bot is a
        participant of THIS conversation.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BotMessageCreate): Schema for sending a bot message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotMessageResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BotMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[BotMessageResponse | HTTPValidationError]:
    """Send Bot Message

     Send a message between bots.

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header — trusted MCP path. Orchestrator sets
        this to the currently-running agent's bot_id so LLM calls made
        from within agent A's session attribute to agent A, not the
        outer HTTP caller. Only honored if the target bot is a
        participant of THIS conversation.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BotMessageCreate): Schema for sending a bot message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BotMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> BotMessageResponse | HTTPValidationError | None:
    """Send Bot Message

     Send a message between bots.

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header — trusted MCP path. Orchestrator sets
        this to the currently-running agent's bot_id so LLM calls made
        from within agent A's session attribute to agent A, not the
        outer HTTP caller. Only honored if the target bot is a
        participant of THIS conversation.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BotMessageCreate): Schema for sending a bot message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotMessageResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
