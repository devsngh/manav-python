from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_operation_response import BulkOperationResponse
from ...models.bulk_user_status_update import BulkUserStatusUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkUserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/users/bulk/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkOperationResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkOperationResponse.from_dict(response.json())

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
) -> Response[BulkOperationResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkUserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[BulkOperationResponse | HTTPValidationError]:
    """Bulk Update User Status

     Bulk update user status (Super Admin only)

    Enable or disable multiple users at once

    - **user_ids**: List of user IDs to update
    - **is_active**: true to enable, false to disable

    Returns:
    - Success count
    - Failed count
    - List of failed users with reasons

    Skips Super Admin users automatically

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkUserStatusUpdate): Bulk update user status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkOperationResponse | HTTPValidationError]
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
    body: BulkUserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> BulkOperationResponse | HTTPValidationError | None:
    """Bulk Update User Status

     Bulk update user status (Super Admin only)

    Enable or disable multiple users at once

    - **user_ids**: List of user IDs to update
    - **is_active**: true to enable, false to disable

    Returns:
    - Success count
    - Failed count
    - List of failed users with reasons

    Skips Super Admin users automatically

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkUserStatusUpdate): Bulk update user status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkOperationResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkUserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[BulkOperationResponse | HTTPValidationError]:
    """Bulk Update User Status

     Bulk update user status (Super Admin only)

    Enable or disable multiple users at once

    - **user_ids**: List of user IDs to update
    - **is_active**: true to enable, false to disable

    Returns:
    - Success count
    - Failed count
    - List of failed users with reasons

    Skips Super Admin users automatically

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkUserStatusUpdate): Bulk update user status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkOperationResponse | HTTPValidationError]
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
    body: BulkUserStatusUpdate,
    authorization: None | str | Unset = UNSET,
) -> BulkOperationResponse | HTTPValidationError | None:
    """Bulk Update User Status

     Bulk update user status (Super Admin only)

    Enable or disable multiple users at once

    - **user_ids**: List of user IDs to update
    - **is_active**: true to enable, false to disable

    Returns:
    - Success count
    - Failed count
    - List of failed users with reasons

    Skips Super Admin users automatically

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkUserStatusUpdate): Bulk update user status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkOperationResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
