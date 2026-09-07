from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
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
        "method": "post",
        "url": "/api/session/credentials/{tool_id}/refresh".format(
            tool_id=quote(str(tool_id), safe=""),
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
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    user_id: str | Unset = "",
) -> Response[Any | HTTPValidationError]:
    """Refresh Tool Credentials

     Refresh OAuth token for a tool's datasource connection.
    Called by the orchestrator when an OAuth token has expired mid-session.
    Uses the existing OAuthHandler.refresh_access_token() mechanism.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose OAuth token to refresh Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
) -> Any | HTTPValidationError | None:
    """Refresh Tool Credentials

     Refresh OAuth token for a tool's datasource connection.
    Called by the orchestrator when an OAuth token has expired mid-session.
    Uses the existing OAuthHandler.refresh_access_token() mechanism.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose OAuth token to refresh Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
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
) -> Response[Any | HTTPValidationError]:
    """Refresh Tool Credentials

     Refresh OAuth token for a tool's datasource connection.
    Called by the orchestrator when an OAuth token has expired mid-session.
    Uses the existing OAuthHandler.refresh_access_token() mechanism.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose OAuth token to refresh Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
) -> Any | HTTPValidationError | None:
    """Refresh Tool Credentials

     Refresh OAuth token for a tool's datasource connection.
    Called by the orchestrator when an OAuth token has expired mid-session.
    Uses the existing OAuthHandler.refresh_access_token() mechanism.

    Args:
        tool_id (str):
        user_id (str | Unset): User UUID whose OAuth token to refresh Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            tool_id=tool_id,
            client=client,
            user_id=user_id,
        )
    ).parsed
