from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.task_list_response import TaskListResponse
from ...models.task_priority import TaskPriority
from ...models.task_status import TaskStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | TaskStatus | Unset = UNSET,
    priority: None | TaskPriority | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, TaskStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_priority: None | str | Unset
    if isinstance(priority, Unset):
        json_priority = UNSET
    elif isinstance(priority, TaskPriority):
        json_priority = priority.value
    else:
        json_priority = priority
    params["priority"] = json_priority

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
        "url": "/api/tasks/my",
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
    status: None | TaskStatus | Unset = UNSET,
    priority: None | TaskPriority | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskListResponse]:
    """List My Scoped Tasks

     Position-scoped task list (#18). Returns the caller's OWN tasks + their
    SUBORDINATES' tasks (via position_reporting) + tasks they created — so a manager
    sees their team's work and a regular member sees just their own. Powers the inbox's
    "my tasks". (Distinct from GET "" which is the org-wide admin list.)

    Args:
        status (None | TaskStatus | Unset):
        priority (None | TaskPriority | Unset):
        search (None | str | Unset):
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
        status=status,
        priority=priority,
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
    status: None | TaskStatus | Unset = UNSET,
    priority: None | TaskPriority | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskListResponse | None:
    """List My Scoped Tasks

     Position-scoped task list (#18). Returns the caller's OWN tasks + their
    SUBORDINATES' tasks (via position_reporting) + tasks they created — so a manager
    sees their team's work and a regular member sees just their own. Powers the inbox's
    "my tasks". (Distinct from GET "" which is the org-wide admin list.)

    Args:
        status (None | TaskStatus | Unset):
        priority (None | TaskPriority | Unset):
        search (None | str | Unset):
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
        status=status,
        priority=priority,
        search=search,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | TaskStatus | Unset = UNSET,
    priority: None | TaskPriority | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskListResponse]:
    """List My Scoped Tasks

     Position-scoped task list (#18). Returns the caller's OWN tasks + their
    SUBORDINATES' tasks (via position_reporting) + tasks they created — so a manager
    sees their team's work and a regular member sees just their own. Powers the inbox's
    "my tasks". (Distinct from GET "" which is the org-wide admin list.)

    Args:
        status (None | TaskStatus | Unset):
        priority (None | TaskPriority | Unset):
        search (None | str | Unset):
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
        status=status,
        priority=priority,
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
    status: None | TaskStatus | Unset = UNSET,
    priority: None | TaskPriority | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskListResponse | None:
    """List My Scoped Tasks

     Position-scoped task list (#18). Returns the caller's OWN tasks + their
    SUBORDINATES' tasks (via position_reporting) + tasks they created — so a manager
    sees their team's work and a regular member sees just their own. Powers the inbox's
    "my tasks". (Distinct from GET "" which is the org-wide admin list.)

    Args:
        status (None | TaskStatus | Unset):
        priority (None | TaskPriority | Unset):
        search (None | str | Unset):
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
            status=status,
            priority=priority,
            search=search,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
