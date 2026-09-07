from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.brand_mark_list_response import BrandMarkListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mark_type: None | str | Unset = UNSET,
    variant: None | str | Unset = UNSET,
    is_primary: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_mark_type: None | str | Unset
    if isinstance(mark_type, Unset):
        json_mark_type = UNSET
    else:
        json_mark_type = mark_type
    params["mark_type"] = json_mark_type

    json_variant: None | str | Unset
    if isinstance(variant, Unset):
        json_variant = UNSET
    else:
        json_variant = variant
    params["variant"] = json_variant

    json_is_primary: bool | None | Unset
    if isinstance(is_primary, Unset):
        json_is_primary = UNSET
    else:
        json_is_primary = is_primary
    params["is_primary"] = json_is_primary

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/brand/marks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrandMarkListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BrandMarkListResponse.from_dict(response.json())

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
) -> Response[BrandMarkListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    mark_type: None | str | Unset = UNSET,
    variant: None | str | Unset = UNSET,
    is_primary: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandMarkListResponse | HTTPValidationError]:
    """List Brand Marks

    Args:
        mark_type (None | str | Unset):
        variant (None | str | Unset):
        is_primary (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandMarkListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        mark_type=mark_type,
        variant=variant,
        is_primary=is_primary,
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
    mark_type: None | str | Unset = UNSET,
    variant: None | str | Unset = UNSET,
    is_primary: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> BrandMarkListResponse | HTTPValidationError | None:
    """List Brand Marks

    Args:
        mark_type (None | str | Unset):
        variant (None | str | Unset):
        is_primary (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandMarkListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        mark_type=mark_type,
        variant=variant,
        is_primary=is_primary,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    mark_type: None | str | Unset = UNSET,
    variant: None | str | Unset = UNSET,
    is_primary: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandMarkListResponse | HTTPValidationError]:
    """List Brand Marks

    Args:
        mark_type (None | str | Unset):
        variant (None | str | Unset):
        is_primary (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandMarkListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        mark_type=mark_type,
        variant=variant,
        is_primary=is_primary,
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
    mark_type: None | str | Unset = UNSET,
    variant: None | str | Unset = UNSET,
    is_primary: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> BrandMarkListResponse | HTTPValidationError | None:
    """List Brand Marks

    Args:
        mark_type (None | str | Unset):
        variant (None | str | Unset):
        is_primary (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandMarkListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            mark_type=mark_type,
            variant=variant,
            is_primary=is_primary,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
