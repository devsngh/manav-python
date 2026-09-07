from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.formula_list_response import FormulaListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    executor_type: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_executor_type: None | str | Unset
    if isinstance(executor_type, Unset):
        json_executor_type = UNSET
    else:
        json_executor_type = executor_type
    params["executor_type"] = json_executor_type

    params["active_only"] = active_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/registry/formulas/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FormulaListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FormulaListResponse.from_dict(response.json())

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
) -> Response[FormulaListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    executor_type: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[FormulaListResponse | HTTPValidationError]:
    """List Formulas

     List formulas with optional filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        category (None | str | Unset):
        executor_type (None | str | Unset):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormulaListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        search=search,
        category=category,
        executor_type=executor_type,
        active_only=active_only,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    executor_type: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> FormulaListResponse | HTTPValidationError | None:
    """List Formulas

     List formulas with optional filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        category (None | str | Unset):
        executor_type (None | str | Unset):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormulaListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        search=search,
        category=category,
        executor_type=executor_type,
        active_only=active_only,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    executor_type: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[FormulaListResponse | HTTPValidationError]:
    """List Formulas

     List formulas with optional filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        category (None | str | Unset):
        executor_type (None | str | Unset):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormulaListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        search=search,
        category=category,
        executor_type=executor_type,
        active_only=active_only,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    executor_type: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> FormulaListResponse | HTTPValidationError | None:
    """List Formulas

     List formulas with optional filters.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        category (None | str | Unset):
        executor_type (None | str | Unset):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormulaListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            search=search,
            category=category,
            executor_type=executor_type,
            active_only=active_only,
            authorization=authorization,
        )
    ).parsed
