from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_workspaces_api_ingestion_workspaces_get_response_list_workspaces_api_ingestion_workspaces_get import (
    ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tenant_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_tenant_id: None | str | Unset
    if isinstance(tenant_id, Unset):
        json_tenant_id = UNSET
    else:
        json_tenant_id = tenant_id
    params["tenant_id"] = json_tenant_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ingestion/workspaces",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet | None
):
    if response.status_code == 200:
        response_200 = ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet.from_dict(
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
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet
]:
    """List Workspaces

     List workspaces. Org-scoped: a plan user sees only their org's workspaces;
    a platform admin sees all (optionally filtered by the tenant_id query param).

    Args:
        tenant_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
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
    tenant_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet | None
):
    """List Workspaces

     List workspaces. Org-scoped: a plan user sees only their org's workspaces;
    a platform admin sees all (optionally filtered by the tenant_id query param).

    Args:
        tenant_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet
    """

    return sync_detailed(
        client=client,
        tenant_id=tenant_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet
]:
    """List Workspaces

     List workspaces. Org-scoped: a plan user sees only their org's workspaces;
    a platform admin sees all (optionally filtered by the tenant_id query param).

    Args:
        tenant_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    tenant_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet | None
):
    """List Workspaces

     List workspaces. Org-scoped: a plan user sees only their org's workspaces;
    a platform admin sees all (optionally filtered by the tenant_id query param).

    Args:
        tenant_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListWorkspacesApiIngestionWorkspacesGetResponseListWorkspacesApiIngestionWorkspacesGet
    """

    return (
        await asyncio_detailed(
            client=client,
            tenant_id=tenant_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
