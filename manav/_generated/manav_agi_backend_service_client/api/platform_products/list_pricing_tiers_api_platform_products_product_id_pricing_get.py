from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.product_pricing_tier_response import ProductPricingTierResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: UUID,
    *,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["active_only"] = active_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/products/{product_id}/pricing".format(
            product_id=quote(str(product_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ProductPricingTierResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProductPricingTierResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[ProductPricingTierResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ProductPricingTierResponse]]:
    """List Pricing Tiers

    Args:
        product_id (UUID):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProductPricingTierResponse]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        active_only=active_only,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ProductPricingTierResponse] | None:
    """List Pricing Tiers

    Args:
        product_id (UUID):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProductPricingTierResponse]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        active_only=active_only,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ProductPricingTierResponse]]:
    """List Pricing Tiers

    Args:
        product_id (UUID):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ProductPricingTierResponse]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        active_only=active_only,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ProductPricingTierResponse] | None:
    """List Pricing Tiers

    Args:
        product_id (UUID):
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ProductPricingTierResponse]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            active_only=active_only,
            authorization=authorization,
        )
    ).parsed
