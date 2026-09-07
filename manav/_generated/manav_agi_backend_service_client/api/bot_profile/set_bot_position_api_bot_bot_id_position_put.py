from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_set_bot_position_request import AdminSetBotPositionRequest
from ...models.bot_response import BotResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: str,
    *,
    body: AdminSetBotPositionRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/bot/{bot_id}/position".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BotResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BotResponse.from_dict(response.json())

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
) -> Response[BotResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminSetBotPositionRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[BotResponse | HTTPValidationError]:
    """Set Bot Position

     Admin endpoint: Set position for a bot.
    Only SUPER_ADMIN can set bot positions.
    Position field will only be visible to users if it has been set.

    Args:
        bot_id (str):
        authorization (None | str | Unset): Bearer token
        body (AdminSetBotPositionRequest): Admin can set bot position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminSetBotPositionRequest,
    authorization: None | str | Unset = UNSET,
) -> BotResponse | HTTPValidationError | None:
    """Set Bot Position

     Admin endpoint: Set position for a bot.
    Only SUPER_ADMIN can set bot positions.
    Position field will only be visible to users if it has been set.

    Args:
        bot_id (str):
        authorization (None | str | Unset): Bearer token
        body (AdminSetBotPositionRequest): Admin can set bot position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotResponse | HTTPValidationError
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminSetBotPositionRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[BotResponse | HTTPValidationError]:
    """Set Bot Position

     Admin endpoint: Set position for a bot.
    Only SUPER_ADMIN can set bot positions.
    Position field will only be visible to users if it has been set.

    Args:
        bot_id (str):
        authorization (None | str | Unset): Bearer token
        body (AdminSetBotPositionRequest): Admin can set bot position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AdminSetBotPositionRequest,
    authorization: None | str | Unset = UNSET,
) -> BotResponse | HTTPValidationError | None:
    """Set Bot Position

     Admin endpoint: Set position for a bot.
    Only SUPER_ADMIN can set bot positions.
    Position field will only be visible to users if it has been set.

    Args:
        bot_id (str):
        authorization (None | str | Unset): Bearer token
        body (AdminSetBotPositionRequest): Admin can set bot position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
