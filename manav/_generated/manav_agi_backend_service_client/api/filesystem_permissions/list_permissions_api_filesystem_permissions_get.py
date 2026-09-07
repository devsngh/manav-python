from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_filesystem_permission_list_response import AgentFilesystemPermissionListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | Unset | UUID = UNSET,
    role_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    elif isinstance(agent_id, UUID):
        json_agent_id = str(agent_id)
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_role_id: None | str | Unset
    if isinstance(role_id, Unset):
        json_role_id = UNSET
    elif isinstance(role_id, UUID):
        json_role_id = str(role_id)
    else:
        json_role_id = role_id
    params["role_id"] = json_role_id

    params["active_only"] = active_only

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/filesystem-permissions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentFilesystemPermissionListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentFilesystemPermissionListResponse.from_dict(response.json())

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
) -> Response[AgentFilesystemPermissionListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    role_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentFilesystemPermissionListResponse | HTTPValidationError]:
    """List Permissions

    Args:
        agent_id (None | Unset | UUID): Filter by per-agent rules
        role_id (None | Unset | UUID): Filter by per-role rules
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentFilesystemPermissionListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        role_id=role_id,
        active_only=active_only,
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
    agent_id: None | Unset | UUID = UNSET,
    role_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AgentFilesystemPermissionListResponse | HTTPValidationError | None:
    """List Permissions

    Args:
        agent_id (None | Unset | UUID): Filter by per-agent rules
        role_id (None | Unset | UUID): Filter by per-role rules
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentFilesystemPermissionListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        role_id=role_id,
        active_only=active_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    role_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentFilesystemPermissionListResponse | HTTPValidationError]:
    """List Permissions

    Args:
        agent_id (None | Unset | UUID): Filter by per-agent rules
        role_id (None | Unset | UUID): Filter by per-role rules
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentFilesystemPermissionListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        role_id=role_id,
        active_only=active_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    role_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AgentFilesystemPermissionListResponse | HTTPValidationError | None:
    """List Permissions

    Args:
        agent_id (None | Unset | UUID): Filter by per-agent rules
        role_id (None | Unset | UUID): Filter by per-role rules
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentFilesystemPermissionListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            role_id=role_id,
            active_only=active_only,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
