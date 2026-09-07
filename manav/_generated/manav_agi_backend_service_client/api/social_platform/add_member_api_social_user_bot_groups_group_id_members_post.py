from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_bot_group_member_add import UserBotGroupMemberAdd
from ...models.user_bot_group_member_response import UserBotGroupMemberResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: UUID,
    *,
    body: UserBotGroupMemberAdd,
    added_by_id: UUID,
    added_by_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_added_by_id = str(added_by_id)
    params["added_by_id"] = json_added_by_id

    params["added_by_type"] = added_by_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/social/user-bot-groups/{group_id}/members".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserBotGroupMemberResponse | None:
    if response.status_code == 201:
        response_201 = UserBotGroupMemberResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserBotGroupMemberResponse]:
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
    body: UserBotGroupMemberAdd,
    added_by_id: UUID,
    added_by_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupMemberResponse]:
    """Add Member

     Add a user or bot member to a group (Owner can join training as optional_trainer).

    Args:
        group_id (UUID):
        added_by_id (UUID):
        added_by_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupMemberAdd): Schema for adding a member to an existing user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupMemberResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        added_by_id=added_by_id,
        added_by_type=added_by_type,
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
    body: UserBotGroupMemberAdd,
    added_by_id: UUID,
    added_by_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupMemberResponse | None:
    """Add Member

     Add a user or bot member to a group (Owner can join training as optional_trainer).

    Args:
        group_id (UUID):
        added_by_id (UUID):
        added_by_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupMemberAdd): Schema for adding a member to an existing user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupMemberResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        added_by_id=added_by_id,
        added_by_type=added_by_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupMemberAdd,
    added_by_id: UUID,
    added_by_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupMemberResponse]:
    """Add Member

     Add a user or bot member to a group (Owner can join training as optional_trainer).

    Args:
        group_id (UUID):
        added_by_id (UUID):
        added_by_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupMemberAdd): Schema for adding a member to an existing user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupMemberResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        added_by_id=added_by_id,
        added_by_type=added_by_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupMemberAdd,
    added_by_id: UUID,
    added_by_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupMemberResponse | None:
    """Add Member

     Add a user or bot member to a group (Owner can join training as optional_trainer).

    Args:
        group_id (UUID):
        added_by_id (UUID):
        added_by_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupMemberAdd): Schema for adding a member to an existing user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupMemberResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            added_by_id=added_by_id,
            added_by_type=added_by_type,
            authorization=authorization,
        )
    ).parsed
