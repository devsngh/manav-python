from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/resolve-bot",
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
    *,
    client: AuthenticatedClient | Client,
    query: str,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Resolve Bot

     Fuzzy resolve a bot by name, position, or department — scoped to the CALLER's org.

    Org isolation (#16, option C): the caller's org is DERIVED, never trusted from a
    parameter the LLM could supply. For agent (MCP) calls the orchestrator injects the
    calling agent's OWN bot via the `X-Actor-Bot-Id` header; we resolve that bot → its
    org. For direct UI calls we use the logged-in user's org. If neither is present,
    resolution is empty (deny-by-default) — an agent can never resolve/assign across orgs.

    Returns the best match with bot_id, bot_name, department, position, user_id.

    Args:
        query (str): Bot name, position title, or department head to search for
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        query=query,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Resolve Bot

     Fuzzy resolve a bot by name, position, or department — scoped to the CALLER's org.

    Org isolation (#16, option C): the caller's org is DERIVED, never trusted from a
    parameter the LLM could supply. For agent (MCP) calls the orchestrator injects the
    calling agent's OWN bot via the `X-Actor-Bot-Id` header; we resolve that bot → its
    org. For direct UI calls we use the logged-in user's org. If neither is present,
    resolution is empty (deny-by-default) — an agent can never resolve/assign across orgs.

    Returns the best match with bot_id, bot_name, department, position, user_id.

    Args:
        query (str): Bot name, position title, or department head to search for
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        query=query,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Resolve Bot

     Fuzzy resolve a bot by name, position, or department — scoped to the CALLER's org.

    Org isolation (#16, option C): the caller's org is DERIVED, never trusted from a
    parameter the LLM could supply. For agent (MCP) calls the orchestrator injects the
    calling agent's OWN bot via the `X-Actor-Bot-Id` header; we resolve that bot → its
    org. For direct UI calls we use the logged-in user's org. If neither is present,
    resolution is empty (deny-by-default) — an agent can never resolve/assign across orgs.

    Returns the best match with bot_id, bot_name, department, position, user_id.

    Args:
        query (str): Bot name, position title, or department head to search for
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        query=query,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    query: str,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Resolve Bot

     Fuzzy resolve a bot by name, position, or department — scoped to the CALLER's org.

    Org isolation (#16, option C): the caller's org is DERIVED, never trusted from a
    parameter the LLM could supply. For agent (MCP) calls the orchestrator injects the
    calling agent's OWN bot via the `X-Actor-Bot-Id` header; we resolve that bot → its
    org. For direct UI calls we use the logged-in user's org. If neither is present,
    resolution is empty (deny-by-default) — an agent can never resolve/assign across orgs.

    Returns the best match with bot_id, bot_name, department, position, user_id.

    Args:
        query (str): Bot name, position title, or department head to search for
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            authorization=authorization,
        )
    ).parsed
