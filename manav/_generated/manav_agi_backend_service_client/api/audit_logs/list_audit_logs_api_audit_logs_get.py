import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_log_list_response import AuditLogListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_resource_type: None | str | Unset
    if isinstance(resource_type, Unset):
        json_resource_type = UNSET
    else:
        json_resource_type = resource_type
    params["resource_type"] = json_resource_type

    json_action: None | str | Unset
    if isinstance(action, Unset):
        json_action = UNSET
    else:
        json_action = action
    params["action"] = json_action

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

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

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/audit-logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditLogListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AuditLogListResponse.from_dict(response.json())

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
) -> Response[AuditLogListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[AuditLogListResponse | HTTPValidationError]:
    """List Audit Logs

     List audit logs with filters + pagination

    Args:
        user_id (None | str | Unset):
        resource_type (None | str | Unset):
        action (None | str | Unset):
        org_id (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        resource_type=resource_type,
        action=action,
        org_id=org_id,
        date_from=date_from,
        date_to=date_to,
        search=search,
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
    user_id: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> AuditLogListResponse | HTTPValidationError | None:
    """List Audit Logs

     List audit logs with filters + pagination

    Args:
        user_id (None | str | Unset):
        resource_type (None | str | Unset):
        action (None | str | Unset):
        org_id (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        resource_type=resource_type,
        action=action,
        org_id=org_id,
        date_from=date_from,
        date_to=date_to,
        search=search,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[AuditLogListResponse | HTTPValidationError]:
    """List Audit Logs

     List audit logs with filters + pagination

    Args:
        user_id (None | str | Unset):
        resource_type (None | str | Unset):
        action (None | str | Unset):
        org_id (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        resource_type=resource_type,
        action=action,
        org_id=org_id,
        date_from=date_from,
        date_to=date_to,
        search=search,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    action: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    date_from: datetime.datetime | None | Unset = UNSET,
    date_to: datetime.datetime | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> AuditLogListResponse | HTTPValidationError | None:
    """List Audit Logs

     List audit logs with filters + pagination

    Args:
        user_id (None | str | Unset):
        resource_type (None | str | Unset):
        action (None | str | Unset):
        org_id (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            resource_type=resource_type,
            action=action,
            org_id=org_id,
            date_from=date_from,
            date_to=date_to,
            search=search,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
