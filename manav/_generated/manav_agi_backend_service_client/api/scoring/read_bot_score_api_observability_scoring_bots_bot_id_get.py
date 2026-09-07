from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_score_with_events_response import BotScoreWithEventsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    org_id: UUID,
    recent_events_limit: int | Unset = 10,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    params["recent_events_limit"] = recent_events_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/scoring/bots/{bot_id}".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BotScoreWithEventsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BotScoreWithEventsResponse.from_dict(response.json())

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
) -> Response[BotScoreWithEventsResponse | HTTPValidationError]:
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
    org_id: UUID,
    recent_events_limit: int | Unset = 10,
    authorization: None | str | Unset = UNSET,
) -> Response[BotScoreWithEventsResponse | HTTPValidationError]:
    """Read Bot Score

     Get a bot's current score + recent N events.

    Args:
        bot_id (UUID):
        org_id (UUID): Organization scope
        recent_events_limit (int | Unset):  Default: 10.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotScoreWithEventsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        org_id=org_id,
        recent_events_limit=recent_events_limit,
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
    org_id: UUID,
    recent_events_limit: int | Unset = 10,
    authorization: None | str | Unset = UNSET,
) -> BotScoreWithEventsResponse | HTTPValidationError | None:
    """Read Bot Score

     Get a bot's current score + recent N events.

    Args:
        bot_id (UUID):
        org_id (UUID): Organization scope
        recent_events_limit (int | Unset):  Default: 10.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotScoreWithEventsResponse | HTTPValidationError
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        org_id=org_id,
        recent_events_limit=recent_events_limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    recent_events_limit: int | Unset = 10,
    authorization: None | str | Unset = UNSET,
) -> Response[BotScoreWithEventsResponse | HTTPValidationError]:
    """Read Bot Score

     Get a bot's current score + recent N events.

    Args:
        bot_id (UUID):
        org_id (UUID): Organization scope
        recent_events_limit (int | Unset):  Default: 10.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotScoreWithEventsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        org_id=org_id,
        recent_events_limit=recent_events_limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    recent_events_limit: int | Unset = 10,
    authorization: None | str | Unset = UNSET,
) -> BotScoreWithEventsResponse | HTTPValidationError | None:
    """Read Bot Score

     Get a bot's current score + recent N events.

    Args:
        bot_id (UUID):
        org_id (UUID): Organization scope
        recent_events_limit (int | Unset):  Default: 10.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotScoreWithEventsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            org_id=org_id,
            recent_events_limit=recent_events_limit,
            authorization=authorization,
        )
    ).parsed
