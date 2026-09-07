from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.organization_create import OrganizationCreate
from ...models.organization_response import OrganizationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OrganizationCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/orgs",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OrganizationResponse | None:
    if response.status_code == 201:
        response_201 = OrganizationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | OrganizationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationResponse]:
    """Create Organization

     Create a new organization (Super Admin only)

    - **name**: Organization name (required)
    - **type**: Organization type (internal, corporate, family, individual)
    - **logo_url**: URL to organization logo
    - **registration_number**: Business registration number
    - **tax_id**: Tax identification number
    - **email**: Contact email
    - **phone**: Contact phone
    - **website**: Organization website
    - **address**: Full address details
    - **established_date**: Date organization was established
    - **employee_count_range**: Employee count range
    - **annual_revenue_range**: Annual revenue range
    - **description**: Organization description
    - **tags**: List of tags/categories
    - **metadata**: Additional custom metadata (JSON)

    Args:
        authorization (None | str | Unset): Bearer token
        body (OrganizationCreate): Schema for creating organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationResponse]
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
    body: OrganizationCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | OrganizationResponse | None:
    """Create Organization

     Create a new organization (Super Admin only)

    - **name**: Organization name (required)
    - **type**: Organization type (internal, corporate, family, individual)
    - **logo_url**: URL to organization logo
    - **registration_number**: Business registration number
    - **tax_id**: Tax identification number
    - **email**: Contact email
    - **phone**: Contact phone
    - **website**: Organization website
    - **address**: Full address details
    - **established_date**: Date organization was established
    - **employee_count_range**: Employee count range
    - **annual_revenue_range**: Annual revenue range
    - **description**: Organization description
    - **tags**: List of tags/categories
    - **metadata**: Additional custom metadata (JSON)

    Args:
        authorization (None | str | Unset): Bearer token
        body (OrganizationCreate): Schema for creating organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OrganizationCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OrganizationResponse]:
    """Create Organization

     Create a new organization (Super Admin only)

    - **name**: Organization name (required)
    - **type**: Organization type (internal, corporate, family, individual)
    - **logo_url**: URL to organization logo
    - **registration_number**: Business registration number
    - **tax_id**: Tax identification number
    - **email**: Contact email
    - **phone**: Contact phone
    - **website**: Organization website
    - **address**: Full address details
    - **established_date**: Date organization was established
    - **employee_count_range**: Employee count range
    - **annual_revenue_range**: Annual revenue range
    - **description**: Organization description
    - **tags**: List of tags/categories
    - **metadata**: Additional custom metadata (JSON)

    Args:
        authorization (None | str | Unset): Bearer token
        body (OrganizationCreate): Schema for creating organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OrganizationResponse]
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
    body: OrganizationCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | OrganizationResponse | None:
    """Create Organization

     Create a new organization (Super Admin only)

    - **name**: Organization name (required)
    - **type**: Organization type (internal, corporate, family, individual)
    - **logo_url**: URL to organization logo
    - **registration_number**: Business registration number
    - **tax_id**: Tax identification number
    - **email**: Contact email
    - **phone**: Contact phone
    - **website**: Organization website
    - **address**: Full address details
    - **established_date**: Date organization was established
    - **employee_count_range**: Employee count range
    - **annual_revenue_range**: Annual revenue range
    - **description**: Organization description
    - **tags**: List of tags/categories
    - **metadata**: Additional custom metadata (JSON)

    Args:
        authorization (None | str | Unset): Bearer token
        body (OrganizationCreate): Schema for creating organization

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OrganizationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
