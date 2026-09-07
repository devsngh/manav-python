from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_role_assign import UserRoleAssign
from ...models.user_role_response import UserRoleResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserRoleAssign,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/roles/assign-to-user",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserRoleResponse | None:
    if response.status_code == 201:
        response_201 = UserRoleResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserRoleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserRoleAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserRoleResponse]:
    """Assign Role To User

     Assign role to user (Super Admin only)

    - **user_id**: User ID (required)
    - **role_id**: Role ID (required)
    - **org_id**: Organization ID (NULL = global assignment)

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserRoleAssign): Assign role to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserRoleResponse]
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
    body: UserRoleAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserRoleResponse | None:
    """Assign Role To User

     Assign role to user (Super Admin only)

    - **user_id**: User ID (required)
    - **role_id**: Role ID (required)
    - **org_id**: Organization ID (NULL = global assignment)

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserRoleAssign): Assign role to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserRoleResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserRoleAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserRoleResponse]:
    """Assign Role To User

     Assign role to user (Super Admin only)

    - **user_id**: User ID (required)
    - **role_id**: Role ID (required)
    - **org_id**: Organization ID (NULL = global assignment)

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserRoleAssign): Assign role to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserRoleResponse]
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
    body: UserRoleAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserRoleResponse | None:
    """Assign Role To User

     Assign role to user (Super Admin only)

    - **user_id**: User ID (required)
    - **role_id**: Role ID (required)
    - **org_id**: Organization ID (NULL = global assignment)

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserRoleAssign): Assign role to user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserRoleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
