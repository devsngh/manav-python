from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_direct_create import UserDirectCreate
from ...models.user_with_details import UserWithDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserDirectCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/direct-create",
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
    body: UserDirectCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserWithDetails]:
    """Direct Create User

     Create user directly with password. No invite email. User can log in immediately.

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserDirectCreate): Create user directly with password — no invite email, immediately
            active & verified.
            role_id is picked from GET /users/roles.

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
    body: UserDirectCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserWithDetails | None:
    """Direct Create User

     Create user directly with password. No invite email. User can log in immediately.

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserDirectCreate): Create user directly with password — no invite email, immediately
            active & verified.
            role_id is picked from GET /users/roles.

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
    body: UserDirectCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserWithDetails]:
    """Direct Create User

     Create user directly with password. No invite email. User can log in immediately.

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserDirectCreate): Create user directly with password — no invite email, immediately
            active & verified.
            role_id is picked from GET /users/roles.

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
    body: UserDirectCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserWithDetails | None:
    """Direct Create User

     Create user directly with password. No invite email. User can log in immediately.

    Args:
        authorization (None | str | Unset): Bearer token
        body (UserDirectCreate): Create user directly with password — no invite email, immediately
            active & verified.
            role_id is picked from GET /users/roles.

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
