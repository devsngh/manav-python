from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    subcategory_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = status

    else:
        json_status = status
    params["status"] = json_status

    json_category_id: None | str | Unset
    if isinstance(category_id, Unset):
        json_category_id = UNSET
    else:
        json_category_id = category_id
    params["category_id"] = json_category_id

    json_subcategory_id: None | str | Unset
    if isinstance(subcategory_id, Unset):
        json_subcategory_id = UNSET
    else:
        json_subcategory_id = subcategory_id
    params["subcategory_id"] = json_subcategory_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasources",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    subcategory_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Datasources

     List datasources. Own-scoped: a plan user sees only datasources they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        subcategory_id (None | str | Unset): Filter by subcategory
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        category_id=category_id,
        subcategory_id=subcategory_id,
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
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    subcategory_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Datasources

     List datasources. Own-scoped: a plan user sees only datasources they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        subcategory_id (None | str | Unset): Filter by subcategory
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        category_id=category_id,
        subcategory_id=subcategory_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    subcategory_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Datasources

     List datasources. Own-scoped: a plan user sees only datasources they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        subcategory_id (None | str | Unset): Filter by subcategory
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        category_id=category_id,
        subcategory_id=subcategory_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    category_id: None | str | Unset = UNSET,
    subcategory_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Datasources

     List datasources. Own-scoped: a plan user sees only datasources they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        category_id (None | str | Unset): Filter by category
        subcategory_id (None | str | Unset): Filter by subcategory
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            category_id=category_id,
            subcategory_id=subcategory_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
