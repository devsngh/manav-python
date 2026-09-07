from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.stats_response import StatsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source_type: list[str] | None | Unset = UNSET,
    bot_id: list[UUID] | None | Unset = UNSET,
    time_range: None | str | Unset = "24h",
    errors_only: bool | Unset = False,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_bot_id, Unset):
        headers["X-Bot-Id"] = x_bot_id

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

    json_bot_id: list[str] | None | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    elif isinstance(bot_id, list):
        json_bot_id = []
        for bot_id_type_0_item_data in bot_id:
            bot_id_type_0_item = str(bot_id_type_0_item_data)
            json_bot_id.append(bot_id_type_0_item)

    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_time_range: None | str | Unset
    if isinstance(time_range, Unset):
        json_time_range = UNSET
    else:
        json_time_range = time_range
    params["time_range"] = json_time_range

    params["errors_only"] = errors_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent-traces/stats",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | StatsResponse | None:
    if response.status_code == 200:
        response_200 = StatsResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | StatsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    bot_id: list[UUID] | None | Unset = UNSET,
    time_range: None | str | Unset = "24h",
    errors_only: bool | Unset = False,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StatsResponse]:
    """Get Stats

     Top-of-page aggregate pills scoped to the current filter.

    Args:
        source_type (list[str] | None | Unset):
        bot_id (list[UUID] | None | Unset):
        time_range (None | str | Unset):  Default: '24h'.
        errors_only (bool | Unset):  Default: False.
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StatsResponse]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        bot_id=bot_id,
        time_range=time_range,
        errors_only=errors_only,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    bot_id: list[UUID] | None | Unset = UNSET,
    time_range: None | str | Unset = "24h",
    errors_only: bool | Unset = False,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | StatsResponse | None:
    """Get Stats

     Top-of-page aggregate pills scoped to the current filter.

    Args:
        source_type (list[str] | None | Unset):
        bot_id (list[UUID] | None | Unset):
        time_range (None | str | Unset):  Default: '24h'.
        errors_only (bool | Unset):  Default: False.
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StatsResponse
    """

    return sync_detailed(
        client=client,
        source_type=source_type,
        bot_id=bot_id,
        time_range=time_range,
        errors_only=errors_only,
        x_bot_id=x_bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    bot_id: list[UUID] | None | Unset = UNSET,
    time_range: None | str | Unset = "24h",
    errors_only: bool | Unset = False,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | StatsResponse]:
    """Get Stats

     Top-of-page aggregate pills scoped to the current filter.

    Args:
        source_type (list[str] | None | Unset):
        bot_id (list[UUID] | None | Unset):
        time_range (None | str | Unset):  Default: '24h'.
        errors_only (bool | Unset):  Default: False.
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | StatsResponse]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        bot_id=bot_id,
        time_range=time_range,
        errors_only=errors_only,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    source_type: list[str] | None | Unset = UNSET,
    bot_id: list[UUID] | None | Unset = UNSET,
    time_range: None | str | Unset = "24h",
    errors_only: bool | Unset = False,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | StatsResponse | None:
    """Get Stats

     Top-of-page aggregate pills scoped to the current filter.

    Args:
        source_type (list[str] | None | Unset):
        bot_id (list[UUID] | None | Unset):
        time_range (None | str | Unset):  Default: '24h'.
        errors_only (bool | Unset):  Default: False.
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | StatsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            source_type=source_type,
            bot_id=bot_id,
            time_range=time_range,
            errors_only=errors_only,
            x_bot_id=x_bot_id,
            authorization=authorization,
        )
    ).parsed
