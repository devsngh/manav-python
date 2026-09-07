from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_status_update import UserStatusUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: UUID,
    *,
    body: UserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/users/{user_id}/status".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update User Status

     Enable/Disable user (Super Admin only)

    - **is_active**: true to enable, false to disable

    Disabled users cannot:
    - Log in
    - Access any resources
    - Perform any actions

    Cannot disable Super Admin users

    Args:
        user_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserStatusUpdate): Update user status (enable/disable)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Update User Status

     Enable/Disable user (Super Admin only)

    - **is_active**: true to enable, false to disable

    Disabled users cannot:
    - Log in
    - Access any resources
    - Perform any actions

    Cannot disable Super Admin users

    Args:
        user_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserStatusUpdate): Update user status (enable/disable)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Update User Status

     Enable/Disable user (Super Admin only)

    - **is_active**: true to enable, false to disable

    Disabled users cannot:
    - Log in
    - Access any resources
    - Perform any actions

    Cannot disable Super Admin users

    Args:
        user_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserStatusUpdate): Update user status (enable/disable)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Update User Status

     Enable/Disable user (Super Admin only)

    - **is_active**: true to enable, false to disable

    Disabled users cannot:
    - Log in
    - Access any resources
    - Perform any actions

    Cannot disable Super Admin users

    Args:
        user_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UserStatusUpdate): Update user status (enable/disable)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
