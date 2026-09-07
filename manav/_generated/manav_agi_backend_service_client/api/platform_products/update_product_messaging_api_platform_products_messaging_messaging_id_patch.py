from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.product_messaging_response import ProductMessagingResponse
from ...models.product_messaging_update import ProductMessagingUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    messaging_id: UUID,
    *,
    body: ProductMessagingUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/platform/products/messaging/{messaging_id}".format(
            messaging_id=quote(str(messaging_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ProductMessagingResponse | None:
    if response.status_code == 200:
        response_200 = ProductMessagingResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProductMessagingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    messaging_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductMessagingUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductMessagingResponse]:
    """Update Product Messaging

    Args:
        messaging_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductMessagingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductMessagingResponse]
    """

    kwargs = _get_kwargs(
        messaging_id=messaging_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    messaging_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductMessagingUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductMessagingResponse | None:
    """Update Product Messaging

    Args:
        messaging_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductMessagingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductMessagingResponse
    """

    return sync_detailed(
        messaging_id=messaging_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    messaging_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductMessagingUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProductMessagingResponse]:
    """Update Product Messaging

    Args:
        messaging_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductMessagingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProductMessagingResponse]
    """

    kwargs = _get_kwargs(
        messaging_id=messaging_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    messaging_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ProductMessagingUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProductMessagingResponse | None:
    """Update Product Messaging

    Args:
        messaging_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (ProductMessagingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProductMessagingResponse
    """

    return (
        await asyncio_detailed(
            messaging_id=messaging_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
