from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.product_pricing_tier_create import ProductPricingTierCreate
from ...models.product_pricing_tier_response import ProductPricingTierResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: UUID,
    *,
    body: ProductPricingTierCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/products/{product_id}/pricing".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ProductPricingTierResponse | None:
    if response.status_code == 201:
        response_201 = ProductPricingTierResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ProductPricingTierResponse]:
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
    body: ProductPricingTierCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductPricingTierResponse]:
    """Create Pricing Tier

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductPricingTierCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductPricingTierResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
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
    body: ProductPricingTierCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductPricingTierResponse | None:
    """Create Pricing Tier

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductPricingTierCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductPricingTierResponse
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductPricingTierCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductPricingTierResponse]:
    """Create Pricing Tier

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductPricingTierCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductPricingTierResponse]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductPricingTierCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductPricingTierResponse | None:
    """Create Pricing Tier

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductPricingTierCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductPricingTierResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
