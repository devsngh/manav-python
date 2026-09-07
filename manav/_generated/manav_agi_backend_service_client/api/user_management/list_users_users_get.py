from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_list_with_filters_response import UserListWithFiltersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    org_id: None | Unset | UUID = UNSET,
    role: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_role: None | str | Unset
    if isinstance(role, Unset):
        json_role = UNSET
    else:
        json_role = role
    params["role"] = json_role

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    json_is_verified: bool | None | Unset
    if isinstance(is_verified, Unset):
        json_is_verified = UNSET
    else:
        json_is_verified = is_verified
    params["is_verified"] = json_is_verified

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserListWithFiltersResponse | None:
    if response.status_code == 200:
        response_200 = UserListWithFiltersResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserListWithFiltersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    org_id: None | Unset | UUID = UNSET,
    role: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserListWithFiltersResponse]:
    """List Users

     List users. Visibility depends on tier:

      - Platform admin      → every user (may filter by org_id).
      - Org admin           → their org's users only.
      - Regular User        → only their own user row (server-forced,
                              ignores any client-side org_id override).

    This lets pages like the Playground "assign to user" dropdown render
    without a 403 for plan users, while never leaking other users' data.

    Args:
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 20.
        org_id (None | Unset | UUID): Filter by organization
        role (None | str | Unset): Filter by role NAME as it appears in the roles table (e.g.
            'Super Admin', 'User', 'Marketing Agent')
        is_active (bool | None | Unset): Filter by active status
        is_verified (bool | None | Unset): Filter by verified status
        search (None | str | Unset): Search by email or name
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserListWithFiltersResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        org_id=org_id,
        role=role,
        is_active=is_active,
        is_verified=is_verified,
        search=search,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    org_id: None | Unset | UUID = UNSET,
    role: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserListWithFiltersResponse | None:
    """List Users

     List users. Visibility depends on tier:

      - Platform admin      → every user (may filter by org_id).
      - Org admin           → their org's users only.
      - Regular User        → only their own user row (server-forced,
                              ignores any client-side org_id override).

    This lets pages like the Playground "assign to user" dropdown render
    without a 403 for plan users, while never leaking other users' data.

    Args:
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 20.
        org_id (None | Unset | UUID): Filter by organization
        role (None | str | Unset): Filter by role NAME as it appears in the roles table (e.g.
            'Super Admin', 'User', 'Marketing Agent')
        is_active (bool | None | Unset): Filter by active status
        is_verified (bool | None | Unset): Filter by verified status
        search (None | str | Unset): Search by email or name
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserListWithFiltersResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        org_id=org_id,
        role=role,
        is_active=is_active,
        is_verified=is_verified,
        search=search,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    org_id: None | Unset | UUID = UNSET,
    role: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserListWithFiltersResponse]:
    """List Users

     List users. Visibility depends on tier:

      - Platform admin      → every user (may filter by org_id).
      - Org admin           → their org's users only.
      - Regular User        → only their own user row (server-forced,
                              ignores any client-side org_id override).

    This lets pages like the Playground "assign to user" dropdown render
    without a 403 for plan users, while never leaking other users' data.

    Args:
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 20.
        org_id (None | Unset | UUID): Filter by organization
        role (None | str | Unset): Filter by role NAME as it appears in the roles table (e.g.
            'Super Admin', 'User', 'Marketing Agent')
        is_active (bool | None | Unset): Filter by active status
        is_verified (bool | None | Unset): Filter by verified status
        search (None | str | Unset): Search by email or name
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserListWithFiltersResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        org_id=org_id,
        role=role,
        is_active=is_active,
        is_verified=is_verified,
        search=search,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    org_id: None | Unset | UUID = UNSET,
    role: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserListWithFiltersResponse | None:
    """List Users

     List users. Visibility depends on tier:

      - Platform admin      → every user (may filter by org_id).
      - Org admin           → their org's users only.
      - Regular User        → only their own user row (server-forced,
                              ignores any client-side org_id override).

    This lets pages like the Playground "assign to user" dropdown render
    without a 403 for plan users, while never leaking other users' data.

    Args:
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 20.
        org_id (None | Unset | UUID): Filter by organization
        role (None | str | Unset): Filter by role NAME as it appears in the roles table (e.g.
            'Super Admin', 'User', 'Marketing Agent')
        is_active (bool | None | Unset): Filter by active status
        is_verified (bool | None | Unset): Filter by verified status
        search (None | str | Unset): Search by email or name
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserListWithFiltersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            org_id=org_id,
            role=role,
            is_active=is_active,
            is_verified=is_verified,
            search=search,
            authorization=authorization,
        )
    ).parsed
