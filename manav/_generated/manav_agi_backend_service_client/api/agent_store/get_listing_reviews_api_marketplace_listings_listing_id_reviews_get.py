from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.review_response import ReviewResponse
from ...types import Response


def _get_kwargs(
    listing_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/marketplace/listings/{listing_id}/reviews".format(
            listing_id=quote(str(listing_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ReviewResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ReviewResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[ReviewResponse]]:
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
) -> Response[HTTPValidationError | list[ReviewResponse]]:
    """Get Listing Reviews

     Public — anyone can read reviews. Writing a review still requires auth.

    Args:
        listing_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ReviewResponse]]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[ReviewResponse] | None:
    """Get Listing Reviews

     Public — anyone can read reviews. Writing a review still requires auth.

    Args:
        listing_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ReviewResponse]
    """

    return sync_detailed(
        listing_id=listing_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[ReviewResponse]]:
    """Get Listing Reviews

     Public — anyone can read reviews. Writing a review still requires auth.

    Args:
        listing_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ReviewResponse]]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[ReviewResponse] | None:
    """Get Listing Reviews

     Public — anyone can read reviews. Writing a review still requires auth.

    Args:
        listing_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ReviewResponse]
    """

    return (
        await asyncio_detailed(
            listing_id=listing_id,
            client=client,
        )
    ).parsed
