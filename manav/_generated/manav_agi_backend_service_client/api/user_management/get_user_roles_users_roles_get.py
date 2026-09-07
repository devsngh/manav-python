from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_user_roles_users_roles_get_response_200_item import GetUserRolesUsersRolesGetResponse200Item
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/roles",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetUserRolesUsersRolesGetResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]]:
    """Get User Roles

     Return the org-level (org_id IS NULL) roles the admin can pick from
    when creating or editing a user. Each entry has:
      - id: role UUID (used for user_roles assignment)
      - name: display label (e.g., "Super Admin", "User", "Marketing Agent")
      - description: optional short description of the role

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item] | None:
    """Get User Roles

     Return the org-level (org_id IS NULL) roles the admin can pick from
    when creating or editing a user. Each entry has:
      - id: role UUID (used for user_roles assignment)
      - name: display label (e.g., "Super Admin", "User", "Marketing Agent")
      - description: optional short description of the role

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]]:
    """Get User Roles

     Return the org-level (org_id IS NULL) roles the admin can pick from
    when creating or editing a user. Each entry has:
      - id: role UUID (used for user_roles assignment)
      - name: display label (e.g., "Super Admin", "User", "Marketing Agent")
      - description: optional short description of the role

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item] | None:
    """Get User Roles

     Return the org-level (org_id IS NULL) roles the admin can pick from
    when creating or editing a user. Each entry has:
      - id: role UUID (used for user_roles assignment)
      - name: display label (e.g., "Super Admin", "User", "Marketing Agent")
      - description: optional short description of the role

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[GetUserRolesUsersRolesGetResponse200Item]
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
