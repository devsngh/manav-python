import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.trace_list_response import TraceListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    method: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
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

    json_method: None | str | Unset
    if isinstance(method, Unset):
        json_method = UNSET
    else:
        json_method = method
    params["method"] = json_method

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_service: None | str | Unset
    if isinstance(service, Unset):
        json_service = UNSET
    else:
        json_service = service
    params["service"] = json_service

    json_min_duration_ms: float | None | Unset
    if isinstance(min_duration_ms, Unset):
        json_min_duration_ms = UNSET
    else:
        json_min_duration_ms = min_duration_ms
    params["min_duration_ms"] = json_min_duration_ms

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
        "url": "/api/system-logs/traces",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TraceListResponse | None:
    if response.status_code == 200:
        response_200 = TraceListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TraceListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    method: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceListResponse]:
    """List Traces

     Paginated list of request traces with span counts.

    Args:
        method (None | str | Unset): Filter by HTTP method
        path (None | str | Unset): Filter by path (substring)
        status (None | str | Unset): Filter by status (OK, ERROR)
        service (None | str | Unset): Filter by service (backend, orchestrator)
        min_duration_ms (float | None | Unset): Minimum duration in ms
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceListResponse]
    """

    kwargs = _get_kwargs(
        method=method,
        path=path,
        status=status,
        service=service,
        min_duration_ms=min_duration_ms,
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
    method: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceListResponse | None:
    """List Traces

     Paginated list of request traces with span counts.

    Args:
        method (None | str | Unset): Filter by HTTP method
        path (None | str | Unset): Filter by path (substring)
        status (None | str | Unset): Filter by status (OK, ERROR)
        service (None | str | Unset): Filter by service (backend, orchestrator)
        min_duration_ms (float | None | Unset): Minimum duration in ms
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceListResponse
    """

    return sync_detailed(
        client=client,
        method=method,
        path=path,
        status=status,
        service=service,
        min_duration_ms=min_duration_ms,
        date_from=date_from,
        date_to=date_to,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    method: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TraceListResponse]:
    """List Traces

     Paginated list of request traces with span counts.

    Args:
        method (None | str | Unset): Filter by HTTP method
        path (None | str | Unset): Filter by path (substring)
        status (None | str | Unset): Filter by status (OK, ERROR)
        service (None | str | Unset): Filter by service (backend, orchestrator)
        min_duration_ms (float | None | Unset): Minimum duration in ms
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TraceListResponse]
    """

    kwargs = _get_kwargs(
        method=method,
        path=path,
        status=status,
        service=service,
        min_duration_ms=min_duration_ms,
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
    method: None | str | Unset = UNSET,
    path: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TraceListResponse | None:
    """List Traces

     Paginated list of request traces with span counts.

    Args:
        method (None | str | Unset): Filter by HTTP method
        path (None | str | Unset): Filter by path (substring)
        status (None | str | Unset): Filter by status (OK, ERROR)
        service (None | str | Unset): Filter by service (backend, orchestrator)
        min_duration_ms (float | None | Unset): Minimum duration in ms
        date_from (datetime.datetime | None | Unset): Start date filter
        date_to (datetime.datetime | None | Unset): End date filter
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TraceListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            method=method,
            path=path,
            status=status,
            service=service,
            min_duration_ms=min_duration_ms,
            date_from=date_from,
            date_to=date_to,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
