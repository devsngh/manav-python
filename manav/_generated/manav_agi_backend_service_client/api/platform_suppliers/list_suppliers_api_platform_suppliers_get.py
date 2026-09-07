from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.supplier_list_response import SupplierListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    is_preferred: bool | None | Unset = UNSET,
    is_diversity_owned: bool | None | Unset = UNSET,
    sanctions_check_status: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_is_preferred: bool | None | Unset
    if isinstance(is_preferred, Unset):
        json_is_preferred = UNSET
    else:
        json_is_preferred = is_preferred
    params["is_preferred"] = json_is_preferred

    json_is_diversity_owned: bool | None | Unset
    if isinstance(is_diversity_owned, Unset):
        json_is_diversity_owned = UNSET
    else:
        json_is_diversity_owned = is_diversity_owned
    params["is_diversity_owned"] = json_is_diversity_owned

    json_sanctions_check_status: None | str | Unset
    if isinstance(sanctions_check_status, Unset):
        json_sanctions_check_status = UNSET
    else:
        json_sanctions_check_status = sanctions_check_status
    params["sanctions_check_status"] = json_sanctions_check_status

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/suppliers",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SupplierListResponse | None:
    if response.status_code == 200:
        response_200 = SupplierListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SupplierListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    is_preferred: bool | None | Unset = UNSET,
    is_diversity_owned: bool | None | Unset = UNSET,
    sanctions_check_status: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SupplierListResponse]:
    """List Suppliers

    Args:
        status (None | str | Unset):
        category (None | str | Unset):
        is_preferred (bool | None | Unset):
        is_diversity_owned (bool | None | Unset):
        sanctions_check_status (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SupplierListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        is_preferred=is_preferred,
        is_diversity_owned=is_diversity_owned,
        sanctions_check_status=sanctions_check_status,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    is_preferred: bool | None | Unset = UNSET,
    is_diversity_owned: bool | None | Unset = UNSET,
    sanctions_check_status: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SupplierListResponse | None:
    """List Suppliers

    Args:
        status (None | str | Unset):
        category (None | str | Unset):
        is_preferred (bool | None | Unset):
        is_diversity_owned (bool | None | Unset):
        sanctions_check_status (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SupplierListResponse
    """

    return sync_detailed(
        client=client,
        status=status,
        category=category,
        is_preferred=is_preferred,
        is_diversity_owned=is_diversity_owned,
        sanctions_check_status=sanctions_check_status,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    is_preferred: bool | None | Unset = UNSET,
    is_diversity_owned: bool | None | Unset = UNSET,
    sanctions_check_status: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SupplierListResponse]:
    """List Suppliers

    Args:
        status (None | str | Unset):
        category (None | str | Unset):
        is_preferred (bool | None | Unset):
        is_diversity_owned (bool | None | Unset):
        sanctions_check_status (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SupplierListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        is_preferred=is_preferred,
        is_diversity_owned=is_diversity_owned,
        sanctions_check_status=sanctions_check_status,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    is_preferred: bool | None | Unset = UNSET,
    is_diversity_owned: bool | None | Unset = UNSET,
    sanctions_check_status: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SupplierListResponse | None:
    """List Suppliers

    Args:
        status (None | str | Unset):
        category (None | str | Unset):
        is_preferred (bool | None | Unset):
        is_diversity_owned (bool | None | Unset):
        sanctions_check_status (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SupplierListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            category=category,
            is_preferred=is_preferred,
            is_diversity_owned=is_diversity_owned,
            sanctions_check_status=sanctions_check_status,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
