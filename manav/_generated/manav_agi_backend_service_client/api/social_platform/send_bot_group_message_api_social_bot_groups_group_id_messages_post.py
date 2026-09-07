from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_group_message_create import BotGroupMessageCreate
from ...models.bot_group_message_response import BotGroupMessageResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: UUID,
    *,
    body: BotGroupMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/social/bot-groups/{group_id}/messages".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BotGroupMessageResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = BotGroupMessageResponse.from_dict(response.json())

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
) -> Response[BotGroupMessageResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BotGroupMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[BotGroupMessageResponse | HTTPValidationError]:
    """Send Bot Group Message

     Send a message to a bot group.

    The group is identified by the URL path. If the request body also carries
    a `group_id`, it must match — a mismatch is rejected with 400 instead of
    silently overwritten (was a real client-bug-masking hole).

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header (trusted MCP path — orchestrator sets this
        to the currently-running agent's bot_id so LLM calls made from within
        agent A's session attribute to agent A, not to the outer HTTP caller).
        Only honored if the header value is a valid bot_id of an active bot
        that IS a member of this group — prevents impersonation.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BotGroupMessageCreate): Schema for sending a bot group message.

            `group_id` is optional in the body — the path parameter is canonical.
            The route validates a mismatch with 400 if callers send both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotGroupMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BotGroupMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> BotGroupMessageResponse | HTTPValidationError | None:
    """Send Bot Group Message

     Send a message to a bot group.

    The group is identified by the URL path. If the request body also carries
    a `group_id`, it must match — a mismatch is rejected with 400 instead of
    silently overwritten (was a real client-bug-masking hole).

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header (trusted MCP path — orchestrator sets this
        to the currently-running agent's bot_id so LLM calls made from within
        agent A's session attribute to agent A, not to the outer HTTP caller).
        Only honored if the header value is a valid bot_id of an active bot
        that IS a member of this group — prevents impersonation.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BotGroupMessageCreate): Schema for sending a bot group message.

            `group_id` is optional in the body — the path parameter is canonical.
            The route validates a mismatch with 400 if callers send both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotGroupMessageResponse | HTTPValidationError
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BotGroupMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[BotGroupMessageResponse | HTTPValidationError]:
    """Send Bot Group Message

     Send a message to a bot group.

    The group is identified by the URL path. If the request body also carries
    a `group_id`, it must match — a mismatch is rejected with 400 instead of
    silently overwritten (was a real client-bug-masking hole).

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header (trusted MCP path — orchestrator sets this
        to the currently-running agent's bot_id so LLM calls made from within
        agent A's session attribute to agent A, not to the outer HTTP caller).
        Only honored if the header value is a valid bot_id of an active bot
        that IS a member of this group — prevents impersonation.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BotGroupMessageCreate): Schema for sending a bot group message.

            `group_id` is optional in the body — the path parameter is canonical.
            The route validates a mismatch with 400 if callers send both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotGroupMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BotGroupMessageCreate,
    authorization: None | str | Unset = UNSET,
) -> BotGroupMessageResponse | HTTPValidationError | None:
    """Send Bot Group Message

     Send a message to a bot group.

    The group is identified by the URL path. If the request body also carries
    a `group_id`, it must match — a mismatch is rejected with 400 instead of
    silently overwritten (was a real client-bug-masking hole).

    Sender attribution:
      - Default: JWT-resolved bot (whichever bot the caller's JWT points to)
      - Override: `X-Bot-ID` header (trusted MCP path — orchestrator sets this
        to the currently-running agent's bot_id so LLM calls made from within
        agent A's session attribute to agent A, not to the outer HTTP caller).
        Only honored if the header value is a valid bot_id of an active bot
        that IS a member of this group — prevents impersonation.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BotGroupMessageCreate): Schema for sending a bot group message.

            `group_id` is optional in the body — the path parameter is canonical.
            The route validates a mismatch with 400 if callers send both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotGroupMessageResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
