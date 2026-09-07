from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_permission_assign import UserPermissionAssign
from ...models.user_permission_response import UserPermissionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserPermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/permissions/assign-to-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserPermissionResponse | None:
    if response.status_code == 201:
        response_201 = UserPermissionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserPermissionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserPermissionResponse]:
    """Assign Permission To User

     Assign permission to user (Super Admin only)

    User-specific permission overrides

    - **user_id**: User ID (required)
    - **permission_id**: Permission ID (required)
    - **org_id**: Organization ID (NULL = applies to all orgs)
    - **is_granted**: True to grant, False to explicitly deny

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserPermissionAssign): Assign permission to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserPermissionResponse]
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
    body: UserPermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserPermissionResponse | None:
    """Assign Permission To User

     Assign permission to user (Super Admin only)

    User-specific permission overrides

    - **user_id**: User ID (required)
    - **permission_id**: Permission ID (required)
    - **org_id**: Organization ID (NULL = applies to all orgs)
    - **is_granted**: True to grant, False to explicitly deny

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserPermissionAssign): Assign permission to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserPermissionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserPermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserPermissionResponse]:
    """Assign Permission To User

     Assign permission to user (Super Admin only)

    User-specific permission overrides

    - **user_id**: User ID (required)
    - **permission_id**: Permission ID (required)
    - **org_id**: Organization ID (NULL = applies to all orgs)
    - **is_granted**: True to grant, False to explicitly deny

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserPermissionAssign): Assign permission to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserPermissionResponse]
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
    body: UserPermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserPermissionResponse | None:
    """Assign Permission To User

     Assign permission to user (Super Admin only)

    User-specific permission overrides

    - **user_id**: User ID (required)
    - **permission_id**: Permission ID (required)
    - **org_id**: Organization ID (NULL = applies to all orgs)
    - **is_granted**: True to grant, False to explicitly deny

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserPermissionAssign): Assign permission to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserPermissionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
