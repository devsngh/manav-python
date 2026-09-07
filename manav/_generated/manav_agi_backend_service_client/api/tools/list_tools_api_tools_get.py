from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tool_list_response import ToolListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    tool_type: None | str | Unset = UNSET,
    datasource_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
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

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = status

    else:
        json_status = status
    params["status"] = json_status

    json_tool_type: None | str | Unset
    if isinstance(tool_type, Unset):
        json_tool_type = UNSET
    else:
        json_tool_type = tool_type
    params["tool_type"] = json_tool_type

    json_datasource_id: None | str | Unset
    if isinstance(datasource_id, Unset):
        json_datasource_id = UNSET
    else:
        json_datasource_id = datasource_id
    params["datasource_id"] = json_datasource_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tools",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ToolListResponse | None:
    if response.status_code == 200:
        response_200 = ToolListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ToolListResponse]:
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
    status: list[str] | None | Unset = UNSET,
    tool_type: None | str | Unset = UNSET,
    datasource_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ToolListResponse]:
    """List Tools

     List tools. Own-scoped: a plan user sees only tools they created; admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        tool_type (None | str | Unset): Filter by tool type
        datasource_id (None | str | Unset): Filter by datasource
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        tool_type=tool_type,
        datasource_id=datasource_id,
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
    status: list[str] | None | Unset = UNSET,
    tool_type: None | str | Unset = UNSET,
    datasource_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ToolListResponse | None:
    """List Tools

     List tools. Own-scoped: a plan user sees only tools they created; admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        tool_type (None | str | Unset): Filter by tool type
        datasource_id (None | str | Unset): Filter by datasource
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolListResponse
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        tool_type=tool_type,
        datasource_id=datasource_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    tool_type: None | str | Unset = UNSET,
    datasource_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ToolListResponse]:
    """List Tools

     List tools. Own-scoped: a plan user sees only tools they created; admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        tool_type (None | str | Unset): Filter by tool type
        datasource_id (None | str | Unset): Filter by datasource
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        tool_type=tool_type,
        datasource_id=datasource_id,
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
    status: list[str] | None | Unset = UNSET,
    tool_type: None | str | Unset = UNSET,
    datasource_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ToolListResponse | None:
    """List Tools

     List tools. Own-scoped: a plan user sees only tools they created; admin sees all.

    Args:
        search (None | str | Unset): Search term
        status (list[str] | None | Unset): Filter by status
        tool_type (None | str | Unset): Filter by tool type
        datasource_id (None | str | Unset): Filter by datasource
        page (int | Unset): Page number Default: 1.
        page_size (int | Unset): Items per page Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            tool_type=tool_type,
            datasource_id=datasource_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
