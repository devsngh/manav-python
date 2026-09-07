from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.permission_request_create import PermissionRequestCreate
from ...models.permission_request_response import PermissionRequestResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PermissionRequestCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/permission-requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PermissionRequestResponse | None:
    if response.status_code == 201:
        response_201 = PermissionRequestResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PermissionRequestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PermissionRequestCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PermissionRequestResponse]:
    """Create Request

     Any authenticated user (human or agent-user) can raise a request.

    Deliberately NOT gated behind a `permission:X` check — raising a request
    is a base capability everyone has, otherwise there's a chicken-and-egg
    for the very permission the requester is asking for.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PermissionRequestCreate): Body for POST /api/permission-requests — either a human or
            an
            agent submitting a self-service request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PermissionRequestResponse]
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
    body: PermissionRequestCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PermissionRequestResponse | None:
    """Create Request

     Any authenticated user (human or agent-user) can raise a request.

    Deliberately NOT gated behind a `permission:X` check — raising a request
    is a base capability everyone has, otherwise there's a chicken-and-egg
    for the very permission the requester is asking for.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PermissionRequestCreate): Body for POST /api/permission-requests — either a human or
            an
            agent submitting a self-service request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PermissionRequestResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PermissionRequestCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PermissionRequestResponse]:
    """Create Request

     Any authenticated user (human or agent-user) can raise a request.

    Deliberately NOT gated behind a `permission:X` check — raising a request
    is a base capability everyone has, otherwise there's a chicken-and-egg
    for the very permission the requester is asking for.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PermissionRequestCreate): Body for POST /api/permission-requests — either a human or
            an
            agent submitting a self-service request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PermissionRequestResponse]
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
    body: PermissionRequestCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PermissionRequestResponse | None:
    """Create Request

     Any authenticated user (human or agent-user) can raise a request.

    Deliberately NOT gated behind a `permission:X` check — raising a request
    is a base capability everyone has, otherwise there's a chicken-and-egg
    for the very permission the requester is asking for.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PermissionRequestCreate): Body for POST /api/permission-requests — either a human or
            an
            agent submitting a self-service request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PermissionRequestResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
