from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.country_read import CountryRead
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: None | str | Unset = UNSET,
    continent: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_region: None | str | Unset
    if isinstance(region, Unset):
        json_region = UNSET
    else:
        json_region = region
    params["region"] = json_region

    json_continent: None | str | Unset
    if isinstance(continent, Unset):
        json_continent = UNSET
    else:
        json_continent = continent
    params["continent"] = json_continent

    json_tier: None | str | Unset
    if isinstance(tier, Unset):
        json_tier = UNSET
    else:
        json_tier = tier
    params["tier"] = json_tier

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/world/countries",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CountryRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CountryRead.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[CountryRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    region: None | str | Unset = UNSET,
    continent: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CountryRead]]:
    """List Countries

    Args:
        region (None | str | Unset):
        continent (None | str | Unset):
        tier (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CountryRead]]
    """

    kwargs = _get_kwargs(
        region=region,
        continent=continent,
        tier=tier,
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
    region: None | str | Unset = UNSET,
    continent: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CountryRead] | None:
    """List Countries

    Args:
        region (None | str | Unset):
        continent (None | str | Unset):
        tier (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CountryRead]
    """

    return sync_detailed(
        client=client,
        region=region,
        continent=continent,
        tier=tier,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    region: None | str | Unset = UNSET,
    continent: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CountryRead]]:
    """List Countries

    Args:
        region (None | str | Unset):
        continent (None | str | Unset):
        tier (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CountryRead]]
    """

    kwargs = _get_kwargs(
        region=region,
        continent=continent,
        tier=tier,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    region: None | str | Unset = UNSET,
    continent: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CountryRead] | None:
    """List Countries

    Args:
        region (None | str | Unset):
        continent (None | str | Unset):
        tier (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CountryRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            continent=continent,
            tier=tier,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
