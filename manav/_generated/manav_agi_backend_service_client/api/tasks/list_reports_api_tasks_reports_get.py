from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.task_list_response import TaskListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    bot_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    report_status: None | str | Unset = UNSET,
    parent_task_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_period: None | str | Unset
    if isinstance(period, Unset):
        json_period = UNSET
    else:
        json_period = period
    params["period"] = json_period

    json_department_id: None | str | Unset
    if isinstance(department_id, Unset):
        json_department_id = UNSET
    elif isinstance(department_id, UUID):
        json_department_id = str(department_id)
    else:
        json_department_id = department_id
    params["department_id"] = json_department_id

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    elif isinstance(bot_id, UUID):
        json_bot_id = str(bot_id)
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_target_id: None | str | Unset
    if isinstance(target_id, Unset):
        json_target_id = UNSET
    elif isinstance(target_id, UUID):
        json_target_id = str(target_id)
    else:
        json_target_id = target_id
    params["target_id"] = json_target_id

    json_date_from: None | str | Unset
    if isinstance(date_from, Unset):
        json_date_from = UNSET
    else:
        json_date_from = date_from
    params["date_from"] = json_date_from

    json_date_to: None | str | Unset
    if isinstance(date_to, Unset):
        json_date_to = UNSET
    else:
        json_date_to = date_to
    params["date_to"] = json_date_to

    json_report_status: None | str | Unset
    if isinstance(report_status, Unset):
        json_report_status = UNSET
    else:
        json_report_status = report_status
    params["report_status"] = json_report_status

    json_parent_task_id: None | str | Unset
    if isinstance(parent_task_id, Unset):
        json_parent_task_id = UNSET
    elif isinstance(parent_task_id, UUID):
        json_parent_task_id = str(parent_task_id)
    else:
        json_parent_task_id = parent_task_id
    params["parent_task_id"] = json_parent_task_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/reports",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TaskListResponse | None:
    if response.status_code == 200:
        response_200 = TaskListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TaskListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    bot_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    report_status: None | str | Unset = UNSET,
    parent_task_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskListResponse]:
    """List Reports

    Args:
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        report_status (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskListResponse]
    """

    kwargs = _get_kwargs(
        period=period,
        department_id=department_id,
        bot_id=bot_id,
        target_id=target_id,
        date_from=date_from,
        date_to=date_to,
        report_status=report_status,
        parent_task_id=parent_task_id,
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
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    bot_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    report_status: None | str | Unset = UNSET,
    parent_task_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskListResponse | None:
    """List Reports

    Args:
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        report_status (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskListResponse
    """

    return sync_detailed(
        client=client,
        period=period,
        department_id=department_id,
        bot_id=bot_id,
        target_id=target_id,
        date_from=date_from,
        date_to=date_to,
        report_status=report_status,
        parent_task_id=parent_task_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    bot_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    report_status: None | str | Unset = UNSET,
    parent_task_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskListResponse]:
    """List Reports

    Args:
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        report_status (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskListResponse]
    """

    kwargs = _get_kwargs(
        period=period,
        department_id=department_id,
        bot_id=bot_id,
        target_id=target_id,
        date_from=date_from,
        date_to=date_to,
        report_status=report_status,
        parent_task_id=parent_task_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    bot_id: None | Unset | UUID = UNSET,
    target_id: None | Unset | UUID = UNSET,
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    report_status: None | str | Unset = UNSET,
    parent_task_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskListResponse | None:
    """List Reports

    Args:
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        target_id (None | Unset | UUID):
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        report_status (None | str | Unset):
        parent_task_id (None | Unset | UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            period=period,
            department_id=department_id,
            bot_id=bot_id,
            target_id=target_id,
            date_from=date_from,
            date_to=date_to,
            report_status=report_status,
            parent_task_id=parent_task_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
