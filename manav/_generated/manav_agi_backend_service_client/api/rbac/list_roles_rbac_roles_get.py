from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.role_list_response import RoleListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: None | Unset | UUID = UNSET,
    include_system: bool | Unset = True,
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

    params["include_system"] = include_system

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rbac/roles",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RoleListResponse | None:
    if response.status_code == 200:
        response_200 = RoleListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | RoleListResponse]:
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
    include_system: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RoleListResponse]:
    """List Roles

     List roles. Multi-tenancy: a non-admin org-admin sees only THEIR org's roles (plus
    system roles); a platform admin may filter by org_id (None => all).

    Args:
        org_id (None | Unset | UUID): Filter by organization
        include_system (bool | Unset): Include system roles Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RoleListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        include_system=include_system,
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
    include_system: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RoleListResponse | None:
    """List Roles

     List roles. Multi-tenancy: a non-admin org-admin sees only THEIR org's roles (plus
    system roles); a platform admin may filter by org_id (None => all).

    Args:
        org_id (None | Unset | UUID): Filter by organization
        include_system (bool | Unset): Include system roles Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RoleListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        include_system=include_system,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    include_system: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RoleListResponse]:
    """List Roles

     List roles. Multi-tenancy: a non-admin org-admin sees only THEIR org's roles (plus
    system roles); a platform admin may filter by org_id (None => all).

    Args:
        org_id (None | Unset | UUID): Filter by organization
        include_system (bool | Unset): Include system roles Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RoleListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        include_system=include_system,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    include_system: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RoleListResponse | None:
    """List Roles

     List roles. Multi-tenancy: a non-admin org-admin sees only THEIR org's roles (plus
    system roles); a platform admin may filter by org_id (None => all).

    Args:
        org_id (None | Unset | UUID): Filter by organization
        include_system (bool | Unset): Include system roles Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RoleListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            include_system=include_system,
            authorization=authorization,
        )
    ).parsed
