from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.live_state_response import LiveStateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    stuck_threshold_seconds: int | Unset = 600,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["stuck_threshold_seconds"] = stuck_threshold_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agents/{bot_id}/live-state".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LiveStateResponse | None:
    if response.status_code == 200:
        response_200 = LiveStateResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LiveStateResponse]:
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
    stuck_threshold_seconds: int | Unset = 600,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LiveStateResponse]:
    """Snapshot of what a bot is doing right now

     Return a snapshot of what `bot_id` is doing right now.

    The single `state` field collapses tasks + events + HIL + errors into
    one of: active | idle | blocked_hil | stuck | errored | completed.

    Designed for use by manager agents monitoring delegated work — one call
    replaces ~6 separate calls to task / audit / hil tools.

    Args:
        bot_id (UUID):
        stuck_threshold_seconds (int | Unset): Override the inactivity threshold for 'stuck'
            classification Default: 600.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiveStateResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        stuck_threshold_seconds=stuck_threshold_seconds,
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
    stuck_threshold_seconds: int | Unset = 600,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LiveStateResponse | None:
    """Snapshot of what a bot is doing right now

     Return a snapshot of what `bot_id` is doing right now.

    The single `state` field collapses tasks + events + HIL + errors into
    one of: active | idle | blocked_hil | stuck | errored | completed.

    Designed for use by manager agents monitoring delegated work — one call
    replaces ~6 separate calls to task / audit / hil tools.

    Args:
        bot_id (UUID):
        stuck_threshold_seconds (int | Unset): Override the inactivity threshold for 'stuck'
            classification Default: 600.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiveStateResponse
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        stuck_threshold_seconds=stuck_threshold_seconds,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    stuck_threshold_seconds: int | Unset = 600,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LiveStateResponse]:
    """Snapshot of what a bot is doing right now

     Return a snapshot of what `bot_id` is doing right now.

    The single `state` field collapses tasks + events + HIL + errors into
    one of: active | idle | blocked_hil | stuck | errored | completed.

    Designed for use by manager agents monitoring delegated work — one call
    replaces ~6 separate calls to task / audit / hil tools.

    Args:
        bot_id (UUID):
        stuck_threshold_seconds (int | Unset): Override the inactivity threshold for 'stuck'
            classification Default: 600.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LiveStateResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        stuck_threshold_seconds=stuck_threshold_seconds,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    stuck_threshold_seconds: int | Unset = 600,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LiveStateResponse | None:
    """Snapshot of what a bot is doing right now

     Return a snapshot of what `bot_id` is doing right now.

    The single `state` field collapses tasks + events + HIL + errors into
    one of: active | idle | blocked_hil | stuck | errored | completed.

    Designed for use by manager agents monitoring delegated work — one call
    replaces ~6 separate calls to task / audit / hil tools.

    Args:
        bot_id (UUID):
        stuck_threshold_seconds (int | Unset): Override the inactivity threshold for 'stuck'
            classification Default: 600.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LiveStateResponse
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            stuck_threshold_seconds=stuck_threshold_seconds,
            authorization=authorization,
        )
    ).parsed
