from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.city_read import CityRead
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country_iso: None | str | Unset = UNSET,
    tier_global: None | str | Unset = UNSET,
    tier_local: None | str | Unset = UNSET,
    is_capital: bool | None | Unset = UNSET,
    is_financial_hub: bool | None | Unset = UNSET,
    is_tech_hub: bool | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_country_iso: None | str | Unset
    if isinstance(country_iso, Unset):
        json_country_iso = UNSET
    else:
        json_country_iso = country_iso
    params["country_iso"] = json_country_iso

    json_tier_global: None | str | Unset
    if isinstance(tier_global, Unset):
        json_tier_global = UNSET
    else:
        json_tier_global = tier_global
    params["tier_global"] = json_tier_global

    json_tier_local: None | str | Unset
    if isinstance(tier_local, Unset):
        json_tier_local = UNSET
    else:
        json_tier_local = tier_local
    params["tier_local"] = json_tier_local

    json_is_capital: bool | None | Unset
    if isinstance(is_capital, Unset):
        json_is_capital = UNSET
    else:
        json_is_capital = is_capital
    params["is_capital"] = json_is_capital

    json_is_financial_hub: bool | None | Unset
    if isinstance(is_financial_hub, Unset):
        json_is_financial_hub = UNSET
    else:
        json_is_financial_hub = is_financial_hub
    params["is_financial_hub"] = json_is_financial_hub

    json_is_tech_hub: bool | None | Unset
    if isinstance(is_tech_hub, Unset):
        json_is_tech_hub = UNSET
    else:
        json_is_tech_hub = is_tech_hub
    params["is_tech_hub"] = json_is_tech_hub

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/world/cities",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CityRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CityRead.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[CityRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    country_iso: None | str | Unset = UNSET,
    tier_global: None | str | Unset = UNSET,
    tier_local: None | str | Unset = UNSET,
    is_capital: bool | None | Unset = UNSET,
    is_financial_hub: bool | None | Unset = UNSET,
    is_tech_hub: bool | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CityRead]]:
    """List Cities

    Args:
        country_iso (None | str | Unset):
        tier_global (None | str | Unset):
        tier_local (None | str | Unset):
        is_capital (bool | None | Unset):
        is_financial_hub (bool | None | Unset):
        is_tech_hub (bool | None | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CityRead]]
    """

    kwargs = _get_kwargs(
        country_iso=country_iso,
        tier_global=tier_global,
        tier_local=tier_local,
        is_capital=is_capital,
        is_financial_hub=is_financial_hub,
        is_tech_hub=is_tech_hub,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    country_iso: None | str | Unset = UNSET,
    tier_global: None | str | Unset = UNSET,
    tier_local: None | str | Unset = UNSET,
    is_capital: bool | None | Unset = UNSET,
    is_financial_hub: bool | None | Unset = UNSET,
    is_tech_hub: bool | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CityRead] | None:
    """List Cities

    Args:
        country_iso (None | str | Unset):
        tier_global (None | str | Unset):
        tier_local (None | str | Unset):
        is_capital (bool | None | Unset):
        is_financial_hub (bool | None | Unset):
        is_tech_hub (bool | None | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CityRead]
    """

    return sync_detailed(
        client=client,
        country_iso=country_iso,
        tier_global=tier_global,
        tier_local=tier_local,
        is_capital=is_capital,
        is_financial_hub=is_financial_hub,
        is_tech_hub=is_tech_hub,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    country_iso: None | str | Unset = UNSET,
    tier_global: None | str | Unset = UNSET,
    tier_local: None | str | Unset = UNSET,
    is_capital: bool | None | Unset = UNSET,
    is_financial_hub: bool | None | Unset = UNSET,
    is_tech_hub: bool | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CityRead]]:
    """List Cities

    Args:
        country_iso (None | str | Unset):
        tier_global (None | str | Unset):
        tier_local (None | str | Unset):
        is_capital (bool | None | Unset):
        is_financial_hub (bool | None | Unset):
        is_tech_hub (bool | None | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CityRead]]
    """

    kwargs = _get_kwargs(
        country_iso=country_iso,
        tier_global=tier_global,
        tier_local=tier_local,
        is_capital=is_capital,
        is_financial_hub=is_financial_hub,
        is_tech_hub=is_tech_hub,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    country_iso: None | str | Unset = UNSET,
    tier_global: None | str | Unset = UNSET,
    tier_local: None | str | Unset = UNSET,
    is_capital: bool | None | Unset = UNSET,
    is_financial_hub: bool | None | Unset = UNSET,
    is_tech_hub: bool | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CityRead] | None:
    """List Cities

    Args:
        country_iso (None | str | Unset):
        tier_global (None | str | Unset):
        tier_local (None | str | Unset):
        is_capital (bool | None | Unset):
        is_financial_hub (bool | None | Unset):
        is_tech_hub (bool | None | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CityRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            country_iso=country_iso,
            tier_global=tier_global,
            tier_local=tier_local,
            is_capital=is_capital,
            is_financial_hub=is_financial_hub,
            is_tech_hub=is_tech_hub,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
