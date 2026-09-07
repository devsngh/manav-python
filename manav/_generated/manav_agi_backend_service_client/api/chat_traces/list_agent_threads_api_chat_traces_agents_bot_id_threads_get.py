from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    source_type: list[str] | None | Unset = UNSET,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_source_type: list[str] | None | Unset
    if isinstance(source_type, Unset):
        json_source_type = UNSET
    elif isinstance(source_type, list):
        json_source_type = source_type

    else:
        json_source_type = source_type
    params["source_type"] = json_source_type

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat-traces/agents/{bot_id}/threads".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Agent Threads

     Panel 1 expand — threads for the picked agent.

    Reject with 404 if bot_id is not in caller's visible_bots (avoids
    revealing that a bot exists in a different org).

    Args:
        bot_id (UUID):
        source_type (list[str] | None | Unset): Optional source_type filter
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        source_type=source_type,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Agent Threads

     Panel 1 expand — threads for the picked agent.

    Reject with 404 if bot_id is not in caller's visible_bots (avoids
    revealing that a bot exists in a different org).

    Args:
        bot_id (UUID):
        source_type (list[str] | None | Unset): Optional source_type filter
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        source_type=source_type,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Agent Threads

     Panel 1 expand — threads for the picked agent.

    Reject with 404 if bot_id is not in caller's visible_bots (avoids
    revealing that a bot exists in a different org).

    Args:
        bot_id (UUID):
        source_type (list[str] | None | Unset): Optional source_type filter
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        source_type=source_type,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Agent Threads

     Panel 1 expand — threads for the picked agent.

    Reject with 404 if bot_id is not in caller's visible_bots (avoids
    revealing that a bot exists in a different org).

    Args:
        bot_id (UUID):
        source_type (list[str] | None | Unset): Optional source_type filter
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            source_type=source_type,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
