from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_node import FileNode
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    path: str | Unset = "",
    depth: int | Unset = 1,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["path"] = path

    params["depth"] = depth

    params["project"] = project

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ide/tree",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[FileNode] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FileNode.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[FileNode]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "",
    depth: int | Unset = 1,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[FileNode]]:
    """Get Tree

     List directory contents — lazy loaded.

    Args:
        path (str | Unset): Subdirectory path relative to project root Default: ''.
        depth (int | Unset): How deep to load (1=immediate children) Default: 1.
        project (str | Unset): Project root path override
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FileNode]]
    """

    kwargs = _get_kwargs(
        path=path,
        depth=depth,
        project=project,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "",
    depth: int | Unset = 1,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[FileNode] | None:
    """Get Tree

     List directory contents — lazy loaded.

    Args:
        path (str | Unset): Subdirectory path relative to project root Default: ''.
        depth (int | Unset): How deep to load (1=immediate children) Default: 1.
        project (str | Unset): Project root path override
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FileNode]
    """

    return sync_detailed(
        client=client,
        path=path,
        depth=depth,
        project=project,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "",
    depth: int | Unset = 1,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[FileNode]]:
    """Get Tree

     List directory contents — lazy loaded.

    Args:
        path (str | Unset): Subdirectory path relative to project root Default: ''.
        depth (int | Unset): How deep to load (1=immediate children) Default: 1.
        project (str | Unset): Project root path override
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[FileNode]]
    """

    kwargs = _get_kwargs(
        path=path,
        depth=depth,
        project=project,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = "",
    depth: int | Unset = 1,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[FileNode] | None:
    """Get Tree

     List directory contents — lazy loaded.

    Args:
        path (str | Unset): Subdirectory path relative to project root Default: ''.
        depth (int | Unset): How deep to load (1=immediate children) Default: 1.
        project (str | Unset): Project root path override
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[FileNode]
    """

    return (
        await asyncio_detailed(
            client=client,
            path=path,
            depth=depth,
            project=project,
            authorization=authorization,
        )
    ).parsed
