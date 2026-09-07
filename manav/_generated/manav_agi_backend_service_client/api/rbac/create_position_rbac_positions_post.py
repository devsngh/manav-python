from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.position_create import PositionCreate
from ...models.position_response import PositionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PositionCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/positions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PositionResponse | None:
    if response.status_code == 201:
        response_201 = PositionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PositionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PositionCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PositionResponse]:
    """Create Position

     Create a new position (Super Admin only)

    - **title**: Position title (required)
    - **description**: Position description
    - **department**: Department name
    - **seniority_level**: Seniority level (junior, mid, senior, lead, executive)
    - **reports_to_position_id**: ID of position this position reports to
    - **responsibilities**: Position responsibilities
    - **org_id**: Organization ID

    Args:
        authorization (None | str | Unset): Bearer token
        body (PositionCreate): Create position schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PositionResponse]
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
    body: PositionCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PositionResponse | None:
    """Create Position

     Create a new position (Super Admin only)

    - **title**: Position title (required)
    - **description**: Position description
    - **department**: Department name
    - **seniority_level**: Seniority level (junior, mid, senior, lead, executive)
    - **reports_to_position_id**: ID of position this position reports to
    - **responsibilities**: Position responsibilities
    - **org_id**: Organization ID

    Args:
        authorization (None | str | Unset): Bearer token
        body (PositionCreate): Create position schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PositionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PositionCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PositionResponse]:
    """Create Position

     Create a new position (Super Admin only)

    - **title**: Position title (required)
    - **description**: Position description
    - **department**: Department name
    - **seniority_level**: Seniority level (junior, mid, senior, lead, executive)
    - **reports_to_position_id**: ID of position this position reports to
    - **responsibilities**: Position responsibilities
    - **org_id**: Organization ID

    Args:
        authorization (None | str | Unset): Bearer token
        body (PositionCreate): Create position schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PositionResponse]
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
    body: PositionCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PositionResponse | None:
    """Create Position

     Create a new position (Super Admin only)

    - **title**: Position title (required)
    - **description**: Position description
    - **department**: Department name
    - **seniority_level**: Seniority level (junior, mid, senior, lead, executive)
    - **reports_to_position_id**: ID of position this position reports to
    - **responsibilities**: Position responsibilities
    - **org_id**: Organization ID

    Args:
        authorization (None | str | Unset): Bearer token
        body (PositionCreate): Create position schema

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PositionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
