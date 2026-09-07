from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.inbox_response import InboxResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: None | Unset | UUID = UNSET,
    as_bot_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_as_bot_id: None | str | Unset
    if isinstance(as_bot_id, Unset):
        json_as_bot_id = UNSET
    elif isinstance(as_bot_id, UUID):
        json_as_bot_id = str(as_bot_id)
    else:
        json_as_bot_id = as_bot_id
    params["as_bot_id"] = json_as_bot_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/aggregators/inbox",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InboxResponse | None:
    if response.status_code == 200:
        response_200 = InboxResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | InboxResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    as_bot_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InboxResponse]:
    """Get Inbox

     One-call read of every conversation the caller can see, bucketed
    into the 6 launcher sections + the org main channel.

    Society section is populated only for SUPER_ADMIN observers; everyone
    else gets an empty Society section (the bots-only space is read-only
    to humans and only super-admin needs the observer view).

    SUPER_ADMIN may pass `?org_id=<uuid>` to observe any org's inbox even
    when their own `users.org_id` is NULL (platform-level admins).

    SUPER_ADMIN may also pass `?as_bot_id=<uuid>` to audit another bot's
    social feed WITHOUT logging in as that bot's owner. The selected bot
    becomes the "viewer" — bot-DM titles show the OTHER party from that
    bot's perspective, and user_dm/user_group sections use the linked
    owner's participation. Ignored for non-super-admin callers.

    Args:
        org_id (None | Unset | UUID): SUPER_ADMIN observer override — pick the org to read
        as_bot_id (None | Unset | UUID): SUPER_ADMIN audit override — view the inbox as if this
            bot were the viewer
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InboxResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        as_bot_id=as_bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    as_bot_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InboxResponse | None:
    """Get Inbox

     One-call read of every conversation the caller can see, bucketed
    into the 6 launcher sections + the org main channel.

    Society section is populated only for SUPER_ADMIN observers; everyone
    else gets an empty Society section (the bots-only space is read-only
    to humans and only super-admin needs the observer view).

    SUPER_ADMIN may pass `?org_id=<uuid>` to observe any org's inbox even
    when their own `users.org_id` is NULL (platform-level admins).

    SUPER_ADMIN may also pass `?as_bot_id=<uuid>` to audit another bot's
    social feed WITHOUT logging in as that bot's owner. The selected bot
    becomes the "viewer" — bot-DM titles show the OTHER party from that
    bot's perspective, and user_dm/user_group sections use the linked
    owner's participation. Ignored for non-super-admin callers.

    Args:
        org_id (None | Unset | UUID): SUPER_ADMIN observer override — pick the org to read
        as_bot_id (None | Unset | UUID): SUPER_ADMIN audit override — view the inbox as if this
            bot were the viewer
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InboxResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        as_bot_id=as_bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    as_bot_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InboxResponse]:
    """Get Inbox

     One-call read of every conversation the caller can see, bucketed
    into the 6 launcher sections + the org main channel.

    Society section is populated only for SUPER_ADMIN observers; everyone
    else gets an empty Society section (the bots-only space is read-only
    to humans and only super-admin needs the observer view).

    SUPER_ADMIN may pass `?org_id=<uuid>` to observe any org's inbox even
    when their own `users.org_id` is NULL (platform-level admins).

    SUPER_ADMIN may also pass `?as_bot_id=<uuid>` to audit another bot's
    social feed WITHOUT logging in as that bot's owner. The selected bot
    becomes the "viewer" — bot-DM titles show the OTHER party from that
    bot's perspective, and user_dm/user_group sections use the linked
    owner's participation. Ignored for non-super-admin callers.

    Args:
        org_id (None | Unset | UUID): SUPER_ADMIN observer override — pick the org to read
        as_bot_id (None | Unset | UUID): SUPER_ADMIN audit override — view the inbox as if this
            bot were the viewer
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InboxResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        as_bot_id=as_bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    as_bot_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InboxResponse | None:
    """Get Inbox

     One-call read of every conversation the caller can see, bucketed
    into the 6 launcher sections + the org main channel.

    Society section is populated only for SUPER_ADMIN observers; everyone
    else gets an empty Society section (the bots-only space is read-only
    to humans and only super-admin needs the observer view).

    SUPER_ADMIN may pass `?org_id=<uuid>` to observe any org's inbox even
    when their own `users.org_id` is NULL (platform-level admins).

    SUPER_ADMIN may also pass `?as_bot_id=<uuid>` to audit another bot's
    social feed WITHOUT logging in as that bot's owner. The selected bot
    becomes the "viewer" — bot-DM titles show the OTHER party from that
    bot's perspective, and user_dm/user_group sections use the linked
    owner's participation. Ignored for non-super-admin callers.

    Args:
        org_id (None | Unset | UUID): SUPER_ADMIN observer override — pick the org to read
        as_bot_id (None | Unset | UUID): SUPER_ADMIN audit override — view the inbox as if this
            bot were the viewer
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InboxResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            as_bot_id=as_bot_id,
            authorization=authorization,
        )
    ).parsed
