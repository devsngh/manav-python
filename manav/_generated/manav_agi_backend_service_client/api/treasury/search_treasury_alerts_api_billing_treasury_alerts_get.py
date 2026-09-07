import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.treasury_alert_list_response import TreasuryAlertListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    alert_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    authoring_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_alert_type: None | str | Unset
    if isinstance(alert_type, Unset):
        json_alert_type = UNSET
    else:
        json_alert_type = alert_type
    params["alert_type"] = json_alert_type

    json_severity: None | str | Unset
    if isinstance(severity, Unset):
        json_severity = UNSET
    else:
        json_severity = severity
    params["severity"] = json_severity

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_authoring_bot_id: None | str | Unset
    if isinstance(authoring_bot_id, Unset):
        json_authoring_bot_id = UNSET
    elif isinstance(authoring_bot_id, UUID):
        json_authoring_bot_id = str(authoring_bot_id)
    else:
        json_authoring_bot_id = authoring_bot_id
    params["authoring_bot_id"] = json_authoring_bot_id

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/billing/treasury-alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TreasuryAlertListResponse | None:
    if response.status_code == 200:
        response_200 = TreasuryAlertListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TreasuryAlertListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    alert_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    authoring_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[HTTPValidationError | TreasuryAlertListResponse]:
    """Search Treasury Alerts

    Args:
        org_id (UUID):
        alert_type (None | str | Unset):
        severity (None | str | Unset):
        status (None | str | Unset):
        authoring_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TreasuryAlertListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        alert_type=alert_type,
        severity=severity,
        status=status,
        authoring_bot_id=authoring_bot_id,
        since=since,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    alert_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    authoring_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> HTTPValidationError | TreasuryAlertListResponse | None:
    """Search Treasury Alerts

    Args:
        org_id (UUID):
        alert_type (None | str | Unset):
        severity (None | str | Unset):
        status (None | str | Unset):
        authoring_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TreasuryAlertListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        alert_type=alert_type,
        severity=severity,
        status=status,
        authoring_bot_id=authoring_bot_id,
        since=since,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    alert_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    authoring_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[HTTPValidationError | TreasuryAlertListResponse]:
    """Search Treasury Alerts

    Args:
        org_id (UUID):
        alert_type (None | str | Unset):
        severity (None | str | Unset):
        status (None | str | Unset):
        authoring_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TreasuryAlertListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        alert_type=alert_type,
        severity=severity,
        status=status,
        authoring_bot_id=authoring_bot_id,
        since=since,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    alert_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    authoring_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> HTTPValidationError | TreasuryAlertListResponse | None:
    """Search Treasury Alerts

    Args:
        org_id (UUID):
        alert_type (None | str | Unset):
        severity (None | str | Unset):
        status (None | str | Unset):
        authoring_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TreasuryAlertListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            alert_type=alert_type,
            severity=severity,
            status=status,
            authoring_bot_id=authoring_bot_id,
            since=since,
            page=page,
            page_size=page_size,
        )
    ).parsed
