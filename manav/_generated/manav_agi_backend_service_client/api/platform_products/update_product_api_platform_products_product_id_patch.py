from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.product_response import ProductResponse
from ...models.product_update import ProductUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: UUID,
    *,
    body: ProductUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/platform/products/{product_id}".format(
            product_id=quote(str(product_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ProductResponse | None:
    if response.status_code == 200:
        response_200 = ProductResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProductResponse]:
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
    body: ProductUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductResponse]:
    """Update Product

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductResponse]
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
    body: ProductUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductResponse | None:
    """Update Product

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductResponse
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
    body: ProductUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductResponse]:
    """Update Product

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductResponse]
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
    body: ProductUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductResponse | None:
    """Update Product

    Args:
        product_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductResponse
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
