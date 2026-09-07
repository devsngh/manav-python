from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.thread_summary import ThreadSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source_type: str,
    source_id: UUID,
    *,
    bot_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_bot_id = str(bot_id)
    params["bot_id"] = json_bot_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat-traces/threads/{source_type}/{source_id}/summary".format(
            source_type=quote(str(source_type), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ThreadSummary | None:
    if response.status_code == 200:
        response_200 = ThreadSummary.from_dict(response.json())

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
) -> Response[HTTPValidationError | ThreadSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    bot_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ThreadSummary]:
    """Thread Summary

     Panel-2 hero card metrics for one thread. bot_id required because
    a thread can be visible under multiple agents (e.g., group room) —
    the summary is per-agent-in-thread.

    Enforces:
      - bot_id must be in caller's visible_bots (404 otherwise)
      - source_type must pass the beta whitelist for plan-tier (404 otherwise)

    Args:
        source_type (str):
        source_id (UUID):
        bot_id (UUID): Agent's bot_id — required to scope the summary
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ThreadSummary]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        source_id=source_id,
        bot_id=bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    bot_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ThreadSummary | None:
    """Thread Summary

     Panel-2 hero card metrics for one thread. bot_id required because
    a thread can be visible under multiple agents (e.g., group room) —
    the summary is per-agent-in-thread.

    Enforces:
      - bot_id must be in caller's visible_bots (404 otherwise)
      - source_type must pass the beta whitelist for plan-tier (404 otherwise)

    Args:
        source_type (str):
        source_id (UUID):
        bot_id (UUID): Agent's bot_id — required to scope the summary
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ThreadSummary
    """

    return sync_detailed(
        source_type=source_type,
        source_id=source_id,
        client=client,
        bot_id=bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    bot_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ThreadSummary]:
    """Thread Summary

     Panel-2 hero card metrics for one thread. bot_id required because
    a thread can be visible under multiple agents (e.g., group room) —
    the summary is per-agent-in-thread.

    Enforces:
      - bot_id must be in caller's visible_bots (404 otherwise)
      - source_type must pass the beta whitelist for plan-tier (404 otherwise)

    Args:
        source_type (str):
        source_id (UUID):
        bot_id (UUID): Agent's bot_id — required to scope the summary
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ThreadSummary]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        source_id=source_id,
        bot_id=bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    bot_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ThreadSummary | None:
    """Thread Summary

     Panel-2 hero card metrics for one thread. bot_id required because
    a thread can be visible under multiple agents (e.g., group room) —
    the summary is per-agent-in-thread.

    Enforces:
      - bot_id must be in caller's visible_bots (404 otherwise)
      - source_type must pass the beta whitelist for plan-tier (404 otherwise)

    Args:
        source_type (str):
        source_id (UUID):
        bot_id (UUID): Agent's bot_id — required to scope the summary
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ThreadSummary
    """

    return (
        await asyncio_detailed(
            source_type=source_type,
            source_id=source_id,
            client=client,
            bot_id=bot_id,
            authorization=authorization,
        )
    ).parsed
