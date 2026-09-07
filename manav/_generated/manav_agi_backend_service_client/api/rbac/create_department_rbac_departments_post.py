from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.department_create import DepartmentCreate
from ...models.department_response import DepartmentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DepartmentCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/departments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DepartmentResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = DepartmentResponse.from_dict(response.json())

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
) -> Response[DepartmentResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DepartmentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[DepartmentResponse | HTTPValidationError]:
    """Create Department

     Create a new department

    - **name**: Department name (required)
    - **description**: Department description
    - **org_id**: Organization ID (required)
    - **head_position_id**: ID of the head position for this department

    Args:
        authorization (None | str | Unset): Bearer token
        body (DepartmentCreate): Create department schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DepartmentResponse | HTTPValidationError]
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
    body: DepartmentCreate,
    authorization: None | str | Unset = UNSET,
) -> DepartmentResponse | HTTPValidationError | None:
    """Create Department

     Create a new department

    - **name**: Department name (required)
    - **description**: Department description
    - **org_id**: Organization ID (required)
    - **head_position_id**: ID of the head position for this department

    Args:
        authorization (None | str | Unset): Bearer token
        body (DepartmentCreate): Create department schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DepartmentResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DepartmentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[DepartmentResponse | HTTPValidationError]:
    """Create Department

     Create a new department

    - **name**: Department name (required)
    - **description**: Department description
    - **org_id**: Organization ID (required)
    - **head_position_id**: ID of the head position for this department

    Args:
        authorization (None | str | Unset): Bearer token
        body (DepartmentCreate): Create department schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DepartmentResponse | HTTPValidationError]
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
    body: DepartmentCreate,
    authorization: None | str | Unset = UNSET,
) -> DepartmentResponse | HTTPValidationError | None:
    """Create Department

     Create a new department

    - **name**: Department name (required)
    - **description**: Department description
    - **org_id**: Organization ID (required)
    - **head_position_id**: ID of the head position for this department

    Args:
        authorization (None | str | Unset): Bearer token
        body (DepartmentCreate): Create department schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DepartmentResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
