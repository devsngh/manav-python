from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.factory_response import FactoryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bot: str,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["bot"] = bot

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/factory/bot-health",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FactoryResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FactoryResponse.from_dict(response.json())

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
) -> Response[FactoryResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bot: str,
    authorization: None | str | Unset = UNSET,
) -> Response[FactoryResponse | HTTPValidationError]:
    """Bot Health

     Performance metrics for a single bot.

    Args:
        bot (str): Bot name, position, or bot_id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FactoryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot=bot,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bot: str,
    authorization: None | str | Unset = UNSET,
) -> FactoryResponse | HTTPValidationError | None:
    """Bot Health

     Performance metrics for a single bot.

    Args:
        bot (str): Bot name, position, or bot_id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FactoryResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        bot=bot,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bot: str,
    authorization: None | str | Unset = UNSET,
) -> Response[FactoryResponse | HTTPValidationError]:
    """Bot Health

     Performance metrics for a single bot.

    Args:
        bot (str): Bot name, position, or bot_id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FactoryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot=bot,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bot: str,
    authorization: None | str | Unset = UNSET,
) -> FactoryResponse | HTTPValidationError | None:
    """Bot Health

     Performance metrics for a single bot.

    Args:
        bot (str): Bot name, position, or bot_id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FactoryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            bot=bot,
            authorization=authorization,
        )
    ).parsed
