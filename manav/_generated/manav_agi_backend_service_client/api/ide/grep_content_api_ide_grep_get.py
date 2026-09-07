from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.grep_response import GrepResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pattern: str,
    path: str | Unset = "",
    glob: str | Unset = "",
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["pattern"] = pattern

    params["path"] = path

    params["glob"] = glob

    params["project"] = project

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ide/grep",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GrepResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = GrepResponse.from_dict(response.json())

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
) -> Response[GrepResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    pattern: str,
    path: str | Unset = "",
    glob: str | Unset = "",
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[GrepResponse | HTTPValidationError]:
    """Grep Content

     Search file contents with regex.

    Args:
        pattern (str): Regex pattern to search for
        path (str | Unset): Subdirectory to search in Default: ''.
        glob (str | Unset): File glob filter (e.g. *.py, *.ts) Default: ''.
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrepResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pattern=pattern,
        path=path,
        glob=glob,
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
    pattern: str,
    path: str | Unset = "",
    glob: str | Unset = "",
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> GrepResponse | HTTPValidationError | None:
    """Grep Content

     Search file contents with regex.

    Args:
        pattern (str): Regex pattern to search for
        path (str | Unset): Subdirectory to search in Default: ''.
        glob (str | Unset): File glob filter (e.g. *.py, *.ts) Default: ''.
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrepResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        pattern=pattern,
        path=path,
        glob=glob,
        project=project,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    pattern: str,
    path: str | Unset = "",
    glob: str | Unset = "",
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[GrepResponse | HTTPValidationError]:
    """Grep Content

     Search file contents with regex.

    Args:
        pattern (str): Regex pattern to search for
        path (str | Unset): Subdirectory to search in Default: ''.
        glob (str | Unset): File glob filter (e.g. *.py, *.ts) Default: ''.
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GrepResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pattern=pattern,
        path=path,
        glob=glob,
        project=project,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    pattern: str,
    path: str | Unset = "",
    glob: str | Unset = "",
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> GrepResponse | HTTPValidationError | None:
    """Grep Content

     Search file contents with regex.

    Args:
        pattern (str): Regex pattern to search for
        path (str | Unset): Subdirectory to search in Default: ''.
        glob (str | Unset): File glob filter (e.g. *.py, *.ts) Default: ''.
        project (str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GrepResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            pattern=pattern,
            path=path,
            glob=glob,
            project=project,
            authorization=authorization,
        )
    ).parsed
