from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ip_asset_list_response import IPAssetListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ip_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    jurisdiction: None | str | Unset = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_ip_type: None | str | Unset
    if isinstance(ip_type, Unset):
        json_ip_type = UNSET
    else:
        json_ip_type = ip_type
    params["ip_type"] = json_ip_type

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_jurisdiction: None | str | Unset
    if isinstance(jurisdiction, Unset):
        json_jurisdiction = UNSET
    else:
        json_jurisdiction = jurisdiction
    params["jurisdiction"] = json_jurisdiction

    json_related_product_id: None | str | Unset
    if isinstance(related_product_id, Unset):
        json_related_product_id = UNSET
    elif isinstance(related_product_id, UUID):
        json_related_product_id = str(related_product_id)
    else:
        json_related_product_id = related_product_id
    params["related_product_id"] = json_related_product_id

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ip-assets",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | IPAssetListResponse | None:
    if response.status_code == 200:
        response_200 = IPAssetListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | IPAssetListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    ip_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    jurisdiction: None | str | Unset = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IPAssetListResponse]:
    """List Ip Assets

    Args:
        ip_type (None | str | Unset):
        status (None | str | Unset):
        jurisdiction (None | str | Unset):
        related_product_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IPAssetListResponse]
    """

    kwargs = _get_kwargs(
        ip_type=ip_type,
        status=status,
        jurisdiction=jurisdiction,
        related_product_id=related_product_id,
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
    ip_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    jurisdiction: None | str | Unset = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | IPAssetListResponse | None:
    """List Ip Assets

    Args:
        ip_type (None | str | Unset):
        status (None | str | Unset):
        jurisdiction (None | str | Unset):
        related_product_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IPAssetListResponse
    """

    return sync_detailed(
        client=client,
        ip_type=ip_type,
        status=status,
        jurisdiction=jurisdiction,
        related_product_id=related_product_id,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    ip_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    jurisdiction: None | str | Unset = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IPAssetListResponse]:
    """List Ip Assets

    Args:
        ip_type (None | str | Unset):
        status (None | str | Unset):
        jurisdiction (None | str | Unset):
        related_product_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IPAssetListResponse]
    """

    kwargs = _get_kwargs(
        ip_type=ip_type,
        status=status,
        jurisdiction=jurisdiction,
        related_product_id=related_product_id,
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
    ip_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    jurisdiction: None | str | Unset = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | IPAssetListResponse | None:
    """List Ip Assets

    Args:
        ip_type (None | str | Unset):
        status (None | str | Unset):
        jurisdiction (None | str | Unset):
        related_product_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IPAssetListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ip_type=ip_type,
            status=status,
            jurisdiction=jurisdiction,
            related_product_id=related_product_id,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
