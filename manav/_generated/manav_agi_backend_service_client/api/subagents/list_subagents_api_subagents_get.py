from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sub_agent_list_response import SubAgentListResponse
from ...models.sub_agent_status import SubAgentStatus
from ...models.sub_agent_type import SubAgentType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: None | SubAgentStatus | Unset = UNSET,
    agent_type: None | SubAgentType | Unset = UNSET,
    include_shared: bool | Unset = True,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, SubAgentStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_agent_type: None | str | Unset
    if isinstance(agent_type, Unset):
        json_agent_type = UNSET
    elif isinstance(agent_type, SubAgentType):
        json_agent_type = agent_type.value
    else:
        json_agent_type = agent_type
    params["agent_type"] = json_agent_type

    params["include_shared"] = include_shared

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/subagents",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SubAgentListResponse | None:
    if response.status_code == 200:
        response_200 = SubAgentListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SubAgentListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: None | SubAgentStatus | Unset = UNSET,
    agent_type: None | SubAgentType | Unset = UNSET,
    include_shared: bool | Unset = True,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SubAgentListResponse]:
    """List Subagents

     List subagents.

    Plan user (non-admin) scope depends on ``include_shared``:
      * true (default) — owned + shared platform catalog. Powers the
        playground subagent picker.
      * false — owned only. Powers the registry page so pagination +
        empty-state stay consistent with the own-scoped metrics.
    Platform admin sees everything regardless of the flag.

    Args:
        search (None | str | Unset):
        status (None | SubAgentStatus | Unset):
        agent_type (None | SubAgentType | Unset):
        include_shared (bool | Unset): Plan users: include platform-shared subagents (created_by
            IS NULL). Default true for playground pickers; the registry page passes false so its list
            stays own-only and matches the own-scoped metrics. Default: True.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        agent_type=agent_type,
        include_shared=include_shared,
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
    search: None | str | Unset = UNSET,
    status: None | SubAgentStatus | Unset = UNSET,
    agent_type: None | SubAgentType | Unset = UNSET,
    include_shared: bool | Unset = True,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SubAgentListResponse | None:
    """List Subagents

     List subagents.

    Plan user (non-admin) scope depends on ``include_shared``:
      * true (default) — owned + shared platform catalog. Powers the
        playground subagent picker.
      * false — owned only. Powers the registry page so pagination +
        empty-state stay consistent with the own-scoped metrics.
    Platform admin sees everything regardless of the flag.

    Args:
        search (None | str | Unset):
        status (None | SubAgentStatus | Unset):
        agent_type (None | SubAgentType | Unset):
        include_shared (bool | Unset): Plan users: include platform-shared subagents (created_by
            IS NULL). Default true for playground pickers; the registry page passes false so its list
            stays own-only and matches the own-scoped metrics. Default: True.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentListResponse
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        agent_type=agent_type,
        include_shared=include_shared,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: None | SubAgentStatus | Unset = UNSET,
    agent_type: None | SubAgentType | Unset = UNSET,
    include_shared: bool | Unset = True,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SubAgentListResponse]:
    """List Subagents

     List subagents.

    Plan user (non-admin) scope depends on ``include_shared``:
      * true (default) — owned + shared platform catalog. Powers the
        playground subagent picker.
      * false — owned only. Powers the registry page so pagination +
        empty-state stay consistent with the own-scoped metrics.
    Platform admin sees everything regardless of the flag.

    Args:
        search (None | str | Unset):
        status (None | SubAgentStatus | Unset):
        agent_type (None | SubAgentType | Unset):
        include_shared (bool | Unset): Plan users: include platform-shared subagents (created_by
            IS NULL). Default true for playground pickers; the registry page passes false so its list
            stays own-only and matches the own-scoped metrics. Default: True.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        agent_type=agent_type,
        include_shared=include_shared,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: None | SubAgentStatus | Unset = UNSET,
    agent_type: None | SubAgentType | Unset = UNSET,
    include_shared: bool | Unset = True,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SubAgentListResponse | None:
    """List Subagents

     List subagents.

    Plan user (non-admin) scope depends on ``include_shared``:
      * true (default) — owned + shared platform catalog. Powers the
        playground subagent picker.
      * false — owned only. Powers the registry page so pagination +
        empty-state stay consistent with the own-scoped metrics.
    Platform admin sees everything regardless of the flag.

    Args:
        search (None | str | Unset):
        status (None | SubAgentStatus | Unset):
        agent_type (None | SubAgentType | Unset):
        include_shared (bool | Unset): Plan users: include platform-shared subagents (created_by
            IS NULL). Default true for playground pickers; the registry page passes false so its list
            stays own-only and matches the own-scoped metrics. Default: True.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            agent_type=agent_type,
            include_shared=include_shared,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
