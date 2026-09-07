from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_workspace_sources_api_ingestion_workspaces_workspace_id_sources_get_response_list_workspace_sources_api_ingestion_workspaces_workspace_id_sources_get import (
    ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    source_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_source_type: None | str | Unset
    if isinstance(source_type, Unset):
        json_source_type = UNSET
    else:
        json_source_type = source_type
    params["source_type"] = json_source_type

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ingestion/workspaces/{workspace_id}/sources".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
    | None
):
    if response.status_code == 200:
        response_200 = ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet.from_dict(
            response.json()
        )

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
) -> Response[
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    source_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
]:
    """List Workspace Sources

     List all sources for a workspace.

    Args:
        workspace_id (str):
        source_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_type=source_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    source_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
    | None
):
    """List Workspace Sources

     List all sources for a workspace.

    Args:
        workspace_id (str):
        source_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        source_type=source_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    source_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
]:
    """List Workspace Sources

     List all sources for a workspace.

    Args:
        workspace_id (str):
        source_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_type=source_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    source_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
    | None
):
    """List Workspace Sources

     List all sources for a workspace.

    Args:
        workspace_id (str):
        source_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGetResponseListWorkspaceSourcesApiIngestionWorkspacesWorkspaceIdSourcesGet
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            source_type=source_type,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
