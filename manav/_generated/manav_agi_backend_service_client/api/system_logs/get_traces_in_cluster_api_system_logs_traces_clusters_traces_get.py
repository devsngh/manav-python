import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cluster_by: str | Unset = "endpoint",
    cluster_key: str,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    max_duration_ms: float | None | Unset = UNSET,
    cross_service_only: bool | Unset = False,
    initiator_kind: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["cluster_by"] = cluster_by

    params["cluster_key"] = cluster_key

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

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

    json_min_duration_ms: float | None | Unset
    if isinstance(min_duration_ms, Unset):
        json_min_duration_ms = UNSET
    else:
        json_min_duration_ms = min_duration_ms
    params["min_duration_ms"] = json_min_duration_ms

    json_focus_user_id: None | str | Unset
    if isinstance(focus_user_id, Unset):
        json_focus_user_id = UNSET
    else:
        json_focus_user_id = focus_user_id
    params["focus_user_id"] = json_focus_user_id

    json_focus_bot_id: None | str | Unset
    if isinstance(focus_bot_id, Unset):
        json_focus_bot_id = UNSET
    else:
        json_focus_bot_id = focus_bot_id
    params["focus_bot_id"] = json_focus_bot_id

    json_focus_org_id: None | str | Unset
    if isinstance(focus_org_id, Unset):
        json_focus_org_id = UNSET
    else:
        json_focus_org_id = focus_org_id
    params["focus_org_id"] = json_focus_org_id

    json_method: None | str | Unset
    if isinstance(method, Unset):
        json_method = UNSET
    else:
        json_method = method
    params["method"] = json_method

    json_max_duration_ms: float | None | Unset
    if isinstance(max_duration_ms, Unset):
        json_max_duration_ms = UNSET
    else:
        json_max_duration_ms = max_duration_ms
    params["max_duration_ms"] = json_max_duration_ms

    params["cross_service_only"] = cross_service_only

    json_initiator_kind: None | str | Unset
    if isinstance(initiator_kind, Unset):
        json_initiator_kind = UNSET
    else:
        json_initiator_kind = initiator_kind
    params["initiator_kind"] = json_initiator_kind

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/system-logs/traces/clusters/traces",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_by: str | Unset = "endpoint",
    cluster_key: str,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    max_duration_ms: float | None | Unset = UNSET,
    cross_service_only: bool | Unset = False,
    initiator_kind: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Traces In Cluster

     Panel 1 Level 1 — individual traces belonging to a picked cluster row.

    Args:
        cluster_by (str | Unset):  Default: 'endpoint'.
        cluster_key (str): Exact cluster label to drill into
        search (None | str | Unset):
        status (None | str | Unset):
        service (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        min_duration_ms (float | None | Unset):
        focus_user_id (None | str | Unset):
        focus_bot_id (None | str | Unset):
        focus_org_id (None | str | Unset):
        method (None | str | Unset):
        max_duration_ms (float | None | Unset):
        cross_service_only (bool | Unset):  Default: False.
        initiator_kind (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        cluster_by=cluster_by,
        cluster_key=cluster_key,
        search=search,
        status=status,
        service=service,
        date_from=date_from,
        date_to=date_to,
        min_duration_ms=min_duration_ms,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        method=method,
        max_duration_ms=max_duration_ms,
        cross_service_only=cross_service_only,
        initiator_kind=initiator_kind,
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
    cluster_by: str | Unset = "endpoint",
    cluster_key: str,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    max_duration_ms: float | None | Unset = UNSET,
    cross_service_only: bool | Unset = False,
    initiator_kind: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Traces In Cluster

     Panel 1 Level 1 — individual traces belonging to a picked cluster row.

    Args:
        cluster_by (str | Unset):  Default: 'endpoint'.
        cluster_key (str): Exact cluster label to drill into
        search (None | str | Unset):
        status (None | str | Unset):
        service (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        min_duration_ms (float | None | Unset):
        focus_user_id (None | str | Unset):
        focus_bot_id (None | str | Unset):
        focus_org_id (None | str | Unset):
        method (None | str | Unset):
        max_duration_ms (float | None | Unset):
        cross_service_only (bool | Unset):  Default: False.
        initiator_kind (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        cluster_by=cluster_by,
        cluster_key=cluster_key,
        search=search,
        status=status,
        service=service,
        date_from=date_from,
        date_to=date_to,
        min_duration_ms=min_duration_ms,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        method=method,
        max_duration_ms=max_duration_ms,
        cross_service_only=cross_service_only,
        initiator_kind=initiator_kind,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cluster_by: str | Unset = "endpoint",
    cluster_key: str,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    max_duration_ms: float | None | Unset = UNSET,
    cross_service_only: bool | Unset = False,
    initiator_kind: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Traces In Cluster

     Panel 1 Level 1 — individual traces belonging to a picked cluster row.

    Args:
        cluster_by (str | Unset):  Default: 'endpoint'.
        cluster_key (str): Exact cluster label to drill into
        search (None | str | Unset):
        status (None | str | Unset):
        service (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        min_duration_ms (float | None | Unset):
        focus_user_id (None | str | Unset):
        focus_bot_id (None | str | Unset):
        focus_org_id (None | str | Unset):
        method (None | str | Unset):
        max_duration_ms (float | None | Unset):
        cross_service_only (bool | Unset):  Default: False.
        initiator_kind (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        cluster_by=cluster_by,
        cluster_key=cluster_key,
        search=search,
        status=status,
        service=service,
        date_from=date_from,
        date_to=date_to,
        min_duration_ms=min_duration_ms,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        method=method,
        max_duration_ms=max_duration_ms,
        cross_service_only=cross_service_only,
        initiator_kind=initiator_kind,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cluster_by: str | Unset = "endpoint",
    cluster_key: str,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    service: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    min_duration_ms: float | None | Unset = UNSET,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    method: None | str | Unset = UNSET,
    max_duration_ms: float | None | Unset = UNSET,
    cross_service_only: bool | Unset = False,
    initiator_kind: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Traces In Cluster

     Panel 1 Level 1 — individual traces belonging to a picked cluster row.

    Args:
        cluster_by (str | Unset):  Default: 'endpoint'.
        cluster_key (str): Exact cluster label to drill into
        search (None | str | Unset):
        status (None | str | Unset):
        service (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        min_duration_ms (float | None | Unset):
        focus_user_id (None | str | Unset):
        focus_bot_id (None | str | Unset):
        focus_org_id (None | str | Unset):
        method (None | str | Unset):
        max_duration_ms (float | None | Unset):
        cross_service_only (bool | Unset):  Default: False.
        initiator_kind (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            cluster_by=cluster_by,
            cluster_key=cluster_key,
            search=search,
            status=status,
            service=service,
            date_from=date_from,
            date_to=date_to,
            min_duration_ms=min_duration_ms,
            focus_user_id=focus_user_id,
            focus_bot_id=focus_bot_id,
            focus_org_id=focus_org_id,
            method=method,
            max_duration_ms=max_duration_ms,
            cross_service_only=cross_service_only,
            initiator_kind=initiator_kind,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
