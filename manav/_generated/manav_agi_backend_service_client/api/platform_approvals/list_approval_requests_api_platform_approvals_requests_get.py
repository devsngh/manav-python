import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approval_request_list_response import ApprovalRequestListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    requested_by_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_resource_type: None | str | Unset
    if isinstance(resource_type, Unset):
        json_resource_type = UNSET
    else:
        json_resource_type = resource_type
    params["resource_type"] = json_resource_type

    json_policy_id: None | str | Unset
    if isinstance(policy_id, Unset):
        json_policy_id = UNSET
    elif isinstance(policy_id, UUID):
        json_policy_id = str(policy_id)
    else:
        json_policy_id = policy_id
    params["policy_id"] = json_policy_id

    json_requested_by_bot_id: None | str | Unset
    if isinstance(requested_by_bot_id, Unset):
        json_requested_by_bot_id = UNSET
    elif isinstance(requested_by_bot_id, UUID):
        json_requested_by_bot_id = str(requested_by_bot_id)
    else:
        json_requested_by_bot_id = requested_by_bot_id
    params["requested_by_bot_id"] = json_requested_by_bot_id

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
        "url": "/api/platform/approvals/requests",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApprovalRequestListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ApprovalRequestListResponse.from_dict(response.json())

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
) -> Response[ApprovalRequestListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    requested_by_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ApprovalRequestListResponse | HTTPValidationError]:
    """List Approval Requests

    Args:
        status (None | str | Unset):
        resource_type (None | str | Unset):
        policy_id (None | Unset | UUID):
        requested_by_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalRequestListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        status=status,
        resource_type=resource_type,
        policy_id=policy_id,
        requested_by_bot_id=requested_by_bot_id,
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
    status: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    requested_by_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ApprovalRequestListResponse | HTTPValidationError | None:
    """List Approval Requests

    Args:
        status (None | str | Unset):
        resource_type (None | str | Unset):
        policy_id (None | Unset | UUID):
        requested_by_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalRequestListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        status=status,
        resource_type=resource_type,
        policy_id=policy_id,
        requested_by_bot_id=requested_by_bot_id,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    requested_by_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ApprovalRequestListResponse | HTTPValidationError]:
    """List Approval Requests

    Args:
        status (None | str | Unset):
        resource_type (None | str | Unset):
        policy_id (None | Unset | UUID):
        requested_by_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApprovalRequestListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        status=status,
        resource_type=resource_type,
        policy_id=policy_id,
        requested_by_bot_id=requested_by_bot_id,
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
    status: None | str | Unset = UNSET,
    resource_type: None | str | Unset = UNSET,
    policy_id: None | Unset | UUID = UNSET,
    requested_by_bot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ApprovalRequestListResponse | HTTPValidationError | None:
    """List Approval Requests

    Args:
        status (None | str | Unset):
        resource_type (None | str | Unset):
        policy_id (None | Unset | UUID):
        requested_by_bot_id (None | Unset | UUID):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApprovalRequestListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            resource_type=resource_type,
            policy_id=policy_id,
            requested_by_bot_id=requested_by_bot_id,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
