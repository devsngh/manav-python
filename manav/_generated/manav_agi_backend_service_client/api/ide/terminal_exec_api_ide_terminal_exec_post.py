from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.terminal_exec_request import TerminalExecRequest
from ...models.terminal_exec_response import TerminalExecResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TerminalExecRequest,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["project"] = project

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ide/terminal/exec",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TerminalExecResponse | None:
    if response.status_code == 200:
        response_200 = TerminalExecResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TerminalExecResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TerminalExecRequest,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TerminalExecResponse]:
    """Terminal Exec

     Execute a shell command and return output.

    Args:
        project (str | Unset):
        authorization (None | str | Unset): Bearer token
        body (TerminalExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TerminalExecResponse]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: TerminalExecRequest,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TerminalExecResponse | None:
    """Terminal Exec

     Execute a shell command and return output.

    Args:
        project (str | Unset):
        authorization (None | str | Unset): Bearer token
        body (TerminalExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TerminalExecResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        project=project,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TerminalExecRequest,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TerminalExecResponse]:
    """Terminal Exec

     Execute a shell command and return output.

    Args:
        project (str | Unset):
        authorization (None | str | Unset): Bearer token
        body (TerminalExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TerminalExecResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        project=project,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TerminalExecRequest,
    project: str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TerminalExecResponse | None:
    """Terminal Exec

     Execute a shell command and return output.

    Args:
        project (str | Unset):
        authorization (None | str | Unset): Bearer token
        body (TerminalExecRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TerminalExecResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project=project,
            authorization=authorization,
        )
    ).parsed
