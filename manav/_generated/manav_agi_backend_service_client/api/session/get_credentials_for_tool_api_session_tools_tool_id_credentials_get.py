from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tool_credential import ToolCredential
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tool_id: str,
    *,
    user_id: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/tools/{tool_id}/credentials".format(
            tool_id=quote(str(tool_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ToolCredential | None:
    if response.status_code == 200:
        response_200 = ToolCredential.from_dict(response.json())

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
) -> Response[HTTPValidationError | ToolCredential]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Response[HTTPValidationError | ToolCredential]:
    """Get Credentials For Tool

     Fetch decrypted credentials for a specific tool from the user's datasource connections.

    Chain: tool_id → ToolDatasourceMapping → datasource_id → UserDatasourceConnection → credentials

    Called by the orchestrator on-demand before each MCP tool invocation.
    The orchestrator should cache these within a session to avoid repeated DB calls.

    Returns has_connection=false (with no credentials) if the user has not connected
    to the tool's datasource.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolCredential]
    """

    kwargs = _get_kwargs(
        tool_id=tool_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> HTTPValidationError | ToolCredential | None:
    """Get Credentials For Tool

     Fetch decrypted credentials for a specific tool from the user's datasource connections.

    Chain: tool_id → ToolDatasourceMapping → datasource_id → UserDatasourceConnection → credentials

    Called by the orchestrator on-demand before each MCP tool invocation.
    The orchestrator should cache these within a session to avoid repeated DB calls.

    Returns has_connection=false (with no credentials) if the user has not connected
    to the tool's datasource.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolCredential
    """

    return sync_detailed(
        tool_id=tool_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Response[HTTPValidationError | ToolCredential]:
    """Get Credentials For Tool

     Fetch decrypted credentials for a specific tool from the user's datasource connections.

    Chain: tool_id → ToolDatasourceMapping → datasource_id → UserDatasourceConnection → credentials

    Called by the orchestrator on-demand before each MCP tool invocation.
    The orchestrator should cache these within a session to avoid repeated DB calls.

    Returns has_connection=false (with no credentials) if the user has not connected
    to the tool's datasource.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolCredential]
    """

    kwargs = _get_kwargs(
        tool_id=tool_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> HTTPValidationError | ToolCredential | None:
    """Get Credentials For Tool

     Fetch decrypted credentials for a specific tool from the user's datasource connections.

    Chain: tool_id → ToolDatasourceMapping → datasource_id → UserDatasourceConnection → credentials

    Called by the orchestrator on-demand before each MCP tool invocation.
    The orchestrator should cache these within a session to avoid repeated DB calls.

    Returns has_connection=false (with no credentials) if the user has not connected
    to the tool's datasource.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolCredential
    """

    return (
        await asyncio_detailed(
            tool_id=tool_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
