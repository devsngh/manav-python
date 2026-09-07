from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.role_permission_assign import RolePermissionAssign
from ...models.role_permission_response import RolePermissionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RolePermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/permissions/assign-to-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RolePermissionResponse | None:
    if response.status_code == 201:
        response_201 = RolePermissionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | RolePermissionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RolePermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RolePermissionResponse]:
    """Assign Permission To Role

     Assign a permission to a role. Platform admin: any. Org-admin (delegated): may only
    grant a permission they THEMSELVES hold (no escalation) and only onto a role in their
    OWN org (never a system/global role or another org's).

    Args:
        authorization (None | str | Unset): Bearer token
        body (RolePermissionAssign): Assign permission to role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RolePermissionResponse]
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
    body: RolePermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RolePermissionResponse | None:
    """Assign Permission To Role

     Assign a permission to a role. Platform admin: any. Org-admin (delegated): may only
    grant a permission they THEMSELVES hold (no escalation) and only onto a role in their
    OWN org (never a system/global role or another org's).

    Args:
        authorization (None | str | Unset): Bearer token
        body (RolePermissionAssign): Assign permission to role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RolePermissionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RolePermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RolePermissionResponse]:
    """Assign Permission To Role

     Assign a permission to a role. Platform admin: any. Org-admin (delegated): may only
    grant a permission they THEMSELVES hold (no escalation) and only onto a role in their
    OWN org (never a system/global role or another org's).

    Args:
        authorization (None | str | Unset): Bearer token
        body (RolePermissionAssign): Assign permission to role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RolePermissionResponse]
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
    body: RolePermissionAssign,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RolePermissionResponse | None:
    """Assign Permission To Role

     Assign a permission to a role. Platform admin: any. Org-admin (delegated): may only
    grant a permission they THEMSELVES hold (no escalation) and only onto a role in their
    OWN org (never a system/global role or another org's).

    Args:
        authorization (None | str | Unset): Bearer token
        body (RolePermissionAssign): Assign permission to role

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RolePermissionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
