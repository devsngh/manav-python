from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_bot_group_create import UserBotGroupCreate
from ...models.user_bot_group_response import UserBotGroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserBotGroupCreate,
    org_id: UUID,
    creator_id: UUID,
    creator_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_creator_id = str(creator_id)
    params["creator_id"] = json_creator_id

    params["creator_type"] = creator_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/social/user-bot-groups",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserBotGroupResponse | None:
    if response.status_code == 201:
        response_201 = UserBotGroupResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserBotGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupCreate,
    org_id: UUID,
    creator_id: UUID,
    creator_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupResponse]:
    """Create User Bot Group

     Create a mixed-membership group (Owner + bots).

    Use group_type to indicate purpose: training | debate | review | crisis | meeting | ad_hoc.
    Pass members[] for initial population (the chair is auto-added if specified).

    Args:
        org_id (UUID): Organization scope
        creator_id (UUID): Who is creating this group
        creator_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupCreate): Schema for creating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        org_id=org_id,
        creator_id=creator_id,
        creator_type=creator_type,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupCreate,
    org_id: UUID,
    creator_id: UUID,
    creator_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupResponse | None:
    """Create User Bot Group

     Create a mixed-membership group (Owner + bots).

    Use group_type to indicate purpose: training | debate | review | crisis | meeting | ad_hoc.
    Pass members[] for initial population (the chair is auto-added if specified).

    Args:
        org_id (UUID): Organization scope
        creator_id (UUID): Who is creating this group
        creator_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupCreate): Schema for creating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        org_id=org_id,
        creator_id=creator_id,
        creator_type=creator_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupCreate,
    org_id: UUID,
    creator_id: UUID,
    creator_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserBotGroupResponse]:
    """Create User Bot Group

     Create a mixed-membership group (Owner + bots).

    Use group_type to indicate purpose: training | debate | review | crisis | meeting | ad_hoc.
    Pass members[] for initial population (the chair is auto-added if specified).

    Args:
        org_id (UUID): Organization scope
        creator_id (UUID): Who is creating this group
        creator_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupCreate): Schema for creating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserBotGroupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        org_id=org_id,
        creator_id=creator_id,
        creator_type=creator_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserBotGroupCreate,
    org_id: UUID,
    creator_id: UUID,
    creator_type: str | Unset = "user",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserBotGroupResponse | None:
    """Create User Bot Group

     Create a mixed-membership group (Owner + bots).

    Use group_type to indicate purpose: training | debate | review | crisis | meeting | ad_hoc.
    Pass members[] for initial population (the chair is auto-added if specified).

    Args:
        org_id (UUID): Organization scope
        creator_id (UUID): Who is creating this group
        creator_type (str | Unset):  Default: 'user'.
        authorization (None | str | Unset): Bearer token
        body (UserBotGroupCreate): Schema for creating a user-bot group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserBotGroupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            org_id=org_id,
            creator_id=creator_id,
            creator_type=creator_type,
            authorization=authorization,
        )
    ).parsed
