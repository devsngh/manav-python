import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.system_log_list_response import SystemLogListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    level: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_level: None | str | Unset
    if isinstance(level, Unset):
        json_level = UNSET
    else:
        json_level = level
    params["level"] = json_level

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    json_method: None | str | Unset
    if isinstance(method, Unset):
        json_method = UNSET
    else:
        json_method = method
    params["method"] = json_method

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_request_id: None | str | Unset
    if isinstance(request_id, Unset):
        json_request_id = UNSET
    else:
        json_request_id = request_id
    params["request_id"] = json_request_id

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_date_from: None | str | Unset
    if isinstance(date_from, Unset):
        json_date_from = UNSET
    elif isinstance(date_from, datetime.datetime):
        json_date_from = date_from.isoformat()
    else:
        json_date_from = date_from
    params["date_from"] = json_date_from

    json_date_to: None | str | Unset
    if isinstance(date_to, Unset):
        json_date_to = UNSET
    elif isinstance(date_to, datetime.datetime):
        json_date_to = date_to.isoformat()
    else:
        json_date_to = date_to
    params["date_to"] = json_date_to

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/system-logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SystemLogListResponse | None:
    if response.status_code == 200:
        response_200 = SystemLogListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SystemLogListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    level: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SystemLogListResponse]:
    """List System Logs

     Paginated system logs with filters.

    Args:
        level (None | str | Unset): Filter by log level (ERROR, WARNING, INFO, CRITICAL)
        category (None | str | Unset): Filter by category (request, auth, security, etc.)
        path (None | str | Unset): Filter by request path (substring match)
        method (None | str | Unset): Filter by HTTP method
        user_id (None | str | Unset): Filter by user ID
        request_id (None | str | Unset): Filter by correlation request ID
        search (None | str | Unset): Search in message, exception, path
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SystemLogListResponse]
    """

    kwargs = _get_kwargs(
        level=level,
        category=category,
        path=path,
        method=method,
        user_id=user_id,
        request_id=request_id,
        search=search,
        date_from=date_from,
        date_to=date_to,
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
    level: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SystemLogListResponse | None:
    """List System Logs

     Paginated system logs with filters.

    Args:
        level (None | str | Unset): Filter by log level (ERROR, WARNING, INFO, CRITICAL)
        category (None | str | Unset): Filter by category (request, auth, security, etc.)
        path (None | str | Unset): Filter by request path (substring match)
        method (None | str | Unset): Filter by HTTP method
        user_id (None | str | Unset): Filter by user ID
        request_id (None | str | Unset): Filter by correlation request ID
        search (None | str | Unset): Search in message, exception, path
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SystemLogListResponse
    """

    return sync_detailed(
        client=client,
        level=level,
        category=category,
        path=path,
        method=method,
        user_id=user_id,
        request_id=request_id,
        search=search,
        date_from=date_from,
        date_to=date_to,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    level: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SystemLogListResponse]:
    """List System Logs

     Paginated system logs with filters.

    Args:
        level (None | str | Unset): Filter by log level (ERROR, WARNING, INFO, CRITICAL)
        category (None | str | Unset): Filter by category (request, auth, security, etc.)
        path (None | str | Unset): Filter by request path (substring match)
        method (None | str | Unset): Filter by HTTP method
        user_id (None | str | Unset): Filter by user ID
        request_id (None | str | Unset): Filter by correlation request ID
        search (None | str | Unset): Search in message, exception, path
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SystemLogListResponse]
    """

    kwargs = _get_kwargs(
        level=level,
        category=category,
        path=path,
        method=method,
        user_id=user_id,
        request_id=request_id,
        search=search,
        date_from=date_from,
        date_to=date_to,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    level: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    request_id: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SystemLogListResponse | None:
    """List System Logs

     Paginated system logs with filters.

    Args:
        level (None | str | Unset): Filter by log level (ERROR, WARNING, INFO, CRITICAL)
        category (None | str | Unset): Filter by category (request, auth, security, etc.)
        path (None | str | Unset): Filter by request path (substring match)
        method (None | str | Unset): Filter by HTTP method
        user_id (None | str | Unset): Filter by user ID
        request_id (None | str | Unset): Filter by correlation request ID
        search (None | str | Unset): Search in message, exception, path
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SystemLogListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            level=level,
            category=category,
            path=path,
            method=method,
            user_id=user_id,
            request_id=request_id,
            search=search,
            date_from=date_from,
            date_to=date_to,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
