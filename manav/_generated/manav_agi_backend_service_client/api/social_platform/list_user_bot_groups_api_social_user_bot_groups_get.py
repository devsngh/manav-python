from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_bot_group_list_response import UserBotGroupListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID | Unset = UNSET,
    member_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,
    group_type: str | Unset = UNSET,
    include_archived: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: str | Unset = UNSET
    if not isinstance(org_id, Unset):
        json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_member_id: str | Unset = UNSET
    if not isinstance(member_id, Unset):
        json_member_id = str(member_id)
    params["member_id"] = json_member_id

    params["member_type"] = member_type

    params["group_type"] = group_type

    params["include_archived"] = include_archived

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/user-bot-groups",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserBotGroupListResponse | None:
    if response.status_code == 200:
        response_200 = UserBotGroupListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserBotGroupListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID | Unset = UNSET,
    member_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,
    group_type: str | Unset = UNSET,
    include_archived: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupListResponse]:
    """List User Bot Groups

     List user-bot groups with optional filters.

    Args:
        org_id (UUID | Unset):
        member_id (UUID | Unset): Filter to groups this member belongs to
        member_type (str | Unset):
        group_type (str | Unset):
        include_archived (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        member_id=member_id,
        member_type=member_type,
        group_type=group_type,
        include_archived=include_archived,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID | Unset = UNSET,
    member_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,
    group_type: str | Unset = UNSET,
    include_archived: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupListResponse | None:
    """List User Bot Groups

     List user-bot groups with optional filters.

    Args:
        org_id (UUID | Unset):
        member_id (UUID | Unset): Filter to groups this member belongs to
        member_type (str | Unset):
        group_type (str | Unset):
        include_archived (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        member_id=member_id,
        member_type=member_type,
        group_type=group_type,
        include_archived=include_archived,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID | Unset = UNSET,
    member_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,
    group_type: str | Unset = UNSET,
    include_archived: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupListResponse]:
    """List User Bot Groups

     List user-bot groups with optional filters.

    Args:
        org_id (UUID | Unset):
        member_id (UUID | Unset): Filter to groups this member belongs to
        member_type (str | Unset):
        group_type (str | Unset):
        include_archived (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        member_id=member_id,
        member_type=member_type,
        group_type=group_type,
        include_archived=include_archived,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID | Unset = UNSET,
    member_id: UUID | Unset = UNSET,
    member_type: str | Unset = UNSET,
    group_type: str | Unset = UNSET,
    include_archived: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupListResponse | None:
    """List User Bot Groups

     List user-bot groups with optional filters.

    Args:
        org_id (UUID | Unset):
        member_id (UUID | Unset): Filter to groups this member belongs to
        member_type (str | Unset):
        group_type (str | Unset):
        include_archived (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            member_id=member_id,
            member_type=member_type,
            group_type=group_type,
            include_archived=include_archived,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
