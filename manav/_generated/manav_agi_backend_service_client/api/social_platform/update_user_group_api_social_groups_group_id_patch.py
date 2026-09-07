from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_group_response import UserGroupResponse
from ...models.user_group_update import UserGroupUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: UUID,
    *,
    body: UserGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/social/groups/{group_id}".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserGroupResponse | None:
    if response.status_code == 200:
        response_200 = UserGroupResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserGroupResponse]:
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
    body: UserGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserGroupResponse]:
    """Update User Group

     Update group details (admin only)

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserGroupUpdate): Schema for updating a user group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupResponse]
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
    body: UserGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserGroupResponse | None:
    """Update User Group

     Update group details (admin only)

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserGroupUpdate): Schema for updating a user group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupResponse
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
    body: UserGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserGroupResponse]:
    """Update User Group

     Update group details (admin only)

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserGroupUpdate): Schema for updating a user group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupResponse]
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
    body: UserGroupUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserGroupResponse | None:
    """Update User Group

     Update group details (admin only)

    Args:
        group_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserGroupUpdate): Schema for updating a user group

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
