from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    tail_lines: int | Unset = 100,
    since_seconds: int | Unset = 300,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["tail_lines"] = tail_lines

    params["since_seconds"] = since_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/devops/services/{name}/logs".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    tail_lines: int | Unset = 100,
    since_seconds: int | Unset = 300,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Logs

    Args:
        name (str):
        tail_lines (int | Unset):  Default: 100.
        since_seconds (int | Unset):  Default: 300.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        tail_lines=tail_lines,
        since_seconds=since_seconds,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    tail_lines: int | Unset = 100,
    since_seconds: int | Unset = 300,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Logs

    Args:
        name (str):
        tail_lines (int | Unset):  Default: 100.
        since_seconds (int | Unset):  Default: 300.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        name=name,
        client=client,
        tail_lines=tail_lines,
        since_seconds=since_seconds,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    tail_lines: int | Unset = 100,
    since_seconds: int | Unset = 300,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Logs

    Args:
        name (str):
        tail_lines (int | Unset):  Default: 100.
        since_seconds (int | Unset):  Default: 300.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        tail_lines=tail_lines,
        since_seconds=since_seconds,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    tail_lines: int | Unset = 100,
    since_seconds: int | Unset = 300,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Logs

    Args:
        name (str):
        tail_lines (int | Unset):  Default: 100.
        since_seconds (int | Unset):  Default: 300.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            tail_lines=tail_lines,
            since_seconds=since_seconds,
            authorization=authorization,
        )
    ).parsed
