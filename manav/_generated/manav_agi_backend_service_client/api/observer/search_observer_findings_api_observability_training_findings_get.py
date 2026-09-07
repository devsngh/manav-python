from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.observer_finding_list_response import ObserverFindingListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    observed_bot_id: None | Unset | UUID = UNSET,
    training_round_id: None | Unset | UUID = UNSET,
    observer_id: None | Unset | UUID = UNSET,
    observer_role: None | str | Unset = UNSET,
    finding_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_observed_bot_id: None | str | Unset
    if isinstance(observed_bot_id, Unset):
        json_observed_bot_id = UNSET
    elif isinstance(observed_bot_id, UUID):
        json_observed_bot_id = str(observed_bot_id)
    else:
        json_observed_bot_id = observed_bot_id
    params["observed_bot_id"] = json_observed_bot_id

    json_training_round_id: None | str | Unset
    if isinstance(training_round_id, Unset):
        json_training_round_id = UNSET
    elif isinstance(training_round_id, UUID):
        json_training_round_id = str(training_round_id)
    else:
        json_training_round_id = training_round_id
    params["training_round_id"] = json_training_round_id

    json_observer_id: None | str | Unset
    if isinstance(observer_id, Unset):
        json_observer_id = UNSET
    elif isinstance(observer_id, UUID):
        json_observer_id = str(observer_id)
    else:
        json_observer_id = observer_id
    params["observer_id"] = json_observer_id

    json_observer_role: None | str | Unset
    if isinstance(observer_role, Unset):
        json_observer_role = UNSET
    else:
        json_observer_role = observer_role
    params["observer_role"] = json_observer_role

    json_finding_type: None | str | Unset
    if isinstance(finding_type, Unset):
        json_finding_type = UNSET
    else:
        json_finding_type = finding_type
    params["finding_type"] = json_finding_type

    json_severity: None | str | Unset
    if isinstance(severity, Unset):
        json_severity = UNSET
    else:
        json_severity = severity
    params["severity"] = json_severity

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/training/findings",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ObserverFindingListResponse | None:
    if response.status_code == 200:
        response_200 = ObserverFindingListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ObserverFindingListResponse]:
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
    observed_bot_id: None | Unset | UUID = UNSET,
    training_round_id: None | Unset | UUID = UNSET,
    observer_id: None | Unset | UUID = UNSET,
    observer_role: None | str | Unset = UNSET,
    finding_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ObserverFindingListResponse]:
    """Search Observer Findings

    Args:
        org_id (UUID):
        observed_bot_id (None | Unset | UUID):
        training_round_id (None | Unset | UUID):
        observer_id (None | Unset | UUID):
        observer_role (None | str | Unset):
        finding_type (None | str | Unset):
        severity (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ObserverFindingListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        observed_bot_id=observed_bot_id,
        training_round_id=training_round_id,
        observer_id=observer_id,
        observer_role=observer_role,
        finding_type=finding_type,
        severity=severity,
        since=since,
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
    org_id: UUID,
    observed_bot_id: None | Unset | UUID = UNSET,
    training_round_id: None | Unset | UUID = UNSET,
    observer_id: None | Unset | UUID = UNSET,
    observer_role: None | str | Unset = UNSET,
    finding_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ObserverFindingListResponse | None:
    """Search Observer Findings

    Args:
        org_id (UUID):
        observed_bot_id (None | Unset | UUID):
        training_round_id (None | Unset | UUID):
        observer_id (None | Unset | UUID):
        observer_role (None | str | Unset):
        finding_type (None | str | Unset):
        severity (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ObserverFindingListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        observed_bot_id=observed_bot_id,
        training_round_id=training_round_id,
        observer_id=observer_id,
        observer_role=observer_role,
        finding_type=finding_type,
        severity=severity,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    observed_bot_id: None | Unset | UUID = UNSET,
    training_round_id: None | Unset | UUID = UNSET,
    observer_id: None | Unset | UUID = UNSET,
    observer_role: None | str | Unset = UNSET,
    finding_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ObserverFindingListResponse]:
    """Search Observer Findings

    Args:
        org_id (UUID):
        observed_bot_id (None | Unset | UUID):
        training_round_id (None | Unset | UUID):
        observer_id (None | Unset | UUID):
        observer_role (None | str | Unset):
        finding_type (None | str | Unset):
        severity (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ObserverFindingListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        observed_bot_id=observed_bot_id,
        training_round_id=training_round_id,
        observer_id=observer_id,
        observer_role=observer_role,
        finding_type=finding_type,
        severity=severity,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    observed_bot_id: None | Unset | UUID = UNSET,
    training_round_id: None | Unset | UUID = UNSET,
    observer_id: None | Unset | UUID = UNSET,
    observer_role: None | str | Unset = UNSET,
    finding_type: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ObserverFindingListResponse | None:
    """Search Observer Findings

    Args:
        org_id (UUID):
        observed_bot_id (None | Unset | UUID):
        training_round_id (None | Unset | UUID):
        observer_id (None | Unset | UUID):
        observer_role (None | str | Unset):
        finding_type (None | str | Unset):
        severity (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ObserverFindingListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            observed_bot_id=observed_bot_id,
            training_round_id=training_round_id,
            observer_id=observer_id,
            observer_role=observer_role,
            finding_type=finding_type,
            severity=severity,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
