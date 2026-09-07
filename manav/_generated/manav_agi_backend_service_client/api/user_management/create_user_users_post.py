from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_create_by_admin import UserCreateByAdmin
from ...models.user_with_details import UserWithDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserCreateByAdmin,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserWithDetails | None:
    if response.status_code == 201:
        response_201 = UserWithDetails.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserWithDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserCreateByAdmin,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserWithDetails]:
    """Create User

     Create user by admin and send invite email (Super Admin only)

    Creates user with:
    - Invite email sent to user
    - User must set password via invite link
    - Automatically created bot
    - Specified role

    - **email**: User email (required, unique)
    - **full_name**: User full name (required)
    - **role**: User role (default: USER)
    - **phone**: Phone number
    - **address**: Address
    - **city**: City
    - **country**: Country
    - **bio**: Bio/description

    Note: Password is NOT required - user will set it via invite link

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserCreateByAdmin): Create user by admin - sends invite email, user sets password
            via link.
            role_id is picked from GET /users/roles (roles table, org_id IS NULL).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserWithDetails]
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
    body: UserCreateByAdmin,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserWithDetails | None:
    """Create User

     Create user by admin and send invite email (Super Admin only)

    Creates user with:
    - Invite email sent to user
    - User must set password via invite link
    - Automatically created bot
    - Specified role

    - **email**: User email (required, unique)
    - **full_name**: User full name (required)
    - **role**: User role (default: USER)
    - **phone**: Phone number
    - **address**: Address
    - **city**: City
    - **country**: Country
    - **bio**: Bio/description

    Note: Password is NOT required - user will set it via invite link

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserCreateByAdmin): Create user by admin - sends invite email, user sets password
            via link.
            role_id is picked from GET /users/roles (roles table, org_id IS NULL).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserWithDetails
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserCreateByAdmin,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserWithDetails]:
    """Create User

     Create user by admin and send invite email (Super Admin only)

    Creates user with:
    - Invite email sent to user
    - User must set password via invite link
    - Automatically created bot
    - Specified role

    - **email**: User email (required, unique)
    - **full_name**: User full name (required)
    - **role**: User role (default: USER)
    - **phone**: Phone number
    - **address**: Address
    - **city**: City
    - **country**: Country
    - **bio**: Bio/description

    Note: Password is NOT required - user will set it via invite link

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserCreateByAdmin): Create user by admin - sends invite email, user sets password
            via link.
            role_id is picked from GET /users/roles (roles table, org_id IS NULL).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserWithDetails]
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
    body: UserCreateByAdmin,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserWithDetails | None:
    """Create User

     Create user by admin and send invite email (Super Admin only)

    Creates user with:
    - Invite email sent to user
    - User must set password via invite link
    - Automatically created bot
    - Specified role

    - **email**: User email (required, unique)
    - **full_name**: User full name (required)
    - **role**: User role (default: USER)
    - **phone**: Phone number
    - **address**: Address
    - **city**: City
    - **country**: Country
    - **bio**: Bio/description

    Note: Password is NOT required - user will set it via invite link

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserCreateByAdmin): Create user by admin - sends invite email, user sets password
            via link.
            role_id is picked from GET /users/roles (roles table, org_id IS NULL).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserWithDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
