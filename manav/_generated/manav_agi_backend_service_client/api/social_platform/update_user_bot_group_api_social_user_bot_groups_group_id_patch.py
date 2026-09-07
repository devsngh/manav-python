from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_bot_group_response import UserBotGroupResponse
from ...models.user_bot_group_update import UserBotGroupUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: UUID,
    *,
    body: UserBotGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/social/user-bot-groups/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserBotGroupResponse | None:
    if response.status_code == 200:
        response_200 = UserBotGroupResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserBotGroupResponse]:
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
    body: UserBotGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupResponse]:
    """Update User Bot Group

     Update group name / description / archive status.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupUpdate): Schema for updating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupResponse]
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
    body: UserBotGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupResponse | None:
    """Update User Bot Group

     Update group name / description / archive status.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupUpdate): Schema for updating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupResponse
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
    body: UserBotGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupResponse]:
    """Update User Bot Group

     Update group name / description / archive status.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupUpdate): Schema for updating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupResponse]
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
    body: UserBotGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupResponse | None:
    """Update User Bot Group

     Update group name / description / archive status.

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupUpdate): Schema for updating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
