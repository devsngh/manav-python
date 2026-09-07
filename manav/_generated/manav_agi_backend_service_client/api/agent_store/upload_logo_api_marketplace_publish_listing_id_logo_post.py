from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_logo_api_marketplace_publish_listing_id_logo_post import (
    BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.listing_response import ListingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    listing_id: UUID,
    *,
    body: BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace/publish/{listing_id}/logo".format(
            listing_id=quote(str(listing_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListingResponse | None:
    if response.status_code == 200:
        response_200 = ListingResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ListingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListingResponse]:
    """Upload Logo

    Args:
        listing_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadLogoApiMarketplacePublishListingIdLogoPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListingResponse]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ListingResponse | None:
    """Upload Logo

    Args:
        listing_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadLogoApiMarketplacePublishListingIdLogoPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListingResponse
    """

    return sync_detailed(
        listing_id=listing_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListingResponse]:
    """Upload Logo

    Args:
        listing_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadLogoApiMarketplacePublishListingIdLogoPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListingResponse]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadLogoApiMarketplacePublishListingIdLogoPost,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ListingResponse | None:
    """Upload Logo

    Args:
        listing_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadLogoApiMarketplacePublishListingIdLogoPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListingResponse
    """

    return (
        await asyncio_detailed(
            listing_id=listing_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
