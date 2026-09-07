from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.job_list_response import JobListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    workspace_id: None | str | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_workspace_id: None | str | Unset
    if isinstance(workspace_id, Unset):
        json_workspace_id = UNSET
    else:
        json_workspace_id = workspace_id
    params["workspace_id"] = json_workspace_id

    json_source_id: None | str | Unset
    if isinstance(source_id, Unset):
        json_source_id = UNSET
    else:
        json_source_id = source_id
    params["source_id"] = json_source_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ingestion/jobs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | JobListResponse | None:
    if response.status_code == 200:
        response_200 = JobListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | JobListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: None | str | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | JobListResponse]:
    """List Jobs

    Args:
        workspace_id (None | str | Unset):
        source_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | JobListResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_id=source_id,
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
    workspace_id: None | str | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | JobListResponse | None:
    """List Jobs

    Args:
        workspace_id (None | str | Unset):
        source_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | JobListResponse
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        source_id=source_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: None | str | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | JobListResponse]:
    """List Jobs

    Args:
        workspace_id (None | str | Unset):
        source_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | JobListResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        source_id=source_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    workspace_id: None | str | Unset = UNSET,
    source_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | JobListResponse | None:
    """List Jobs

    Args:
        workspace_id (None | str | Unset):
        source_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | JobListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            source_id=source_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
