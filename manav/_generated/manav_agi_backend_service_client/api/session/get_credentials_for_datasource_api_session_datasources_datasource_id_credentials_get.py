from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    datasource_id: str,
    *,
    user_id: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/datasources/{datasource_id}/credentials".format(
            datasource_id=quote(str(datasource_id), safe=""),
        ),
        "params": params,
    }

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
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Response[Any | HTTPValidationError]:
    """Get Credentials For Datasource

     Fetch decrypted credentials for a datasource from the user's connections.

    Used by the orchestrator's MCP client to get OAuth tokens for connecting
    to MCP servers. Looks up the user's connection for this datasource and
    resolves OAuth tokens if present.

    Autonomous cron runs may pass an empty user_id — treat that as "no
    user connection" so the caller falls through to its session-token
    fallback instead of getting a 500 from asyncpg on `''::UUID`.

    Args:
        datasource_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Any | HTTPValidationError | None:
    """Get Credentials For Datasource

     Fetch decrypted credentials for a datasource from the user's connections.

    Used by the orchestrator's MCP client to get OAuth tokens for connecting
    to MCP servers. Looks up the user's connection for this datasource and
    resolves OAuth tokens if present.

    Autonomous cron runs may pass an empty user_id — treat that as "no
    user connection" so the caller falls through to its session-token
    fallback instead of getting a 500 from asyncpg on `''::UUID`.

    Args:
        datasource_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        datasource_id=datasource_id,
        client=client,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Response[Any | HTTPValidationError]:
    """Get Credentials For Datasource

     Fetch decrypted credentials for a datasource from the user's connections.

    Used by the orchestrator's MCP client to get OAuth tokens for connecting
    to MCP servers. Looks up the user's connection for this datasource and
    resolves OAuth tokens if present.

    Autonomous cron runs may pass an empty user_id — treat that as "no
    user connection" so the caller falls through to its session-token
    fallback instead of getting a 500 from asyncpg on `''::UUID`.

    Args:
        datasource_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Any | HTTPValidationError | None:
    """Get Credentials For Datasource

     Fetch decrypted credentials for a datasource from the user's connections.

    Used by the orchestrator's MCP client to get OAuth tokens for connecting
    to MCP servers. Looks up the user's connection for this datasource and
    resolves OAuth tokens if present.

    Autonomous cron runs may pass an empty user_id — treat that as "no
    user connection" so the caller falls through to its session-token
    fallback instead of getting a 500 from asyncpg on `''::UUID`.

    Args:
        datasource_id (str):
        user_id (str | Unset): User UUID whose datasource connections to look up (empty = no
            connection) Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            datasource_id=datasource_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
