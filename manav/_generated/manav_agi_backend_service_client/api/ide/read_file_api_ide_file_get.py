from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_content import FileContent
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    path: str,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["path"] = path

    params["project"] = project

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ide/file",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileContent | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FileContent.from_dict(response.json())

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
) -> Response[FileContent | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    path: str,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[FileContent | HTTPValidationError]:
    """Read File

     Read a file's content.

    Args:
        path (str): File path relative to project root
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileContent | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        path=path,
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
    path: str,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> FileContent | HTTPValidationError | None:
    """Read File

     Read a file's content.

    Args:
        path (str): File path relative to project root
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileContent | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        path=path,
        project=project,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    path: str,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[FileContent | HTTPValidationError]:
    """Read File

     Read a file's content.

    Args:
        path (str): File path relative to project root
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileContent | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        path=path,
        project=project,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    path: str,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> FileContent | HTTPValidationError | None:
    """Read File

     Read a file's content.

    Args:
        path (str): File path relative to project root
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileContent | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            path=path,
            project=project,
            authorization=authorization,
        )
    ).parsed
