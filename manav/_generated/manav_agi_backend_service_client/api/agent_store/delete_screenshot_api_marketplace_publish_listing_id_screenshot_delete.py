from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.listing_response import ListingResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    listing_id: UUID,
    *,
    url_query: str,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["url"] = url_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/marketplace/publish/{listing_id}/screenshot".format(
            listing_id=quote(str(listing_id), safe=""),
        ),
        "params": params,
    }

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
    url_query: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListingResponse]:
    """Delete Screenshot

    Args:
        listing_id (UUID):
        url_query (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListingResponse]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
        url_query=url_query,
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
    url_query: str,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ListingResponse | None:
    """Delete Screenshot

    Args:
        listing_id (UUID):
        url_query (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListingResponse
    """

    return sync_detailed(
        listing_id=listing_id,
        client=client,
        url_query=url_query,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListingResponse]:
    """Delete Screenshot

    Args:
        listing_id (UUID):
        url_query (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListingResponse]
    """

    kwargs = _get_kwargs(
        listing_id=listing_id,
        url_query=url_query,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    listing_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    url_query: str,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ListingResponse | None:
    """Delete Screenshot

    Args:
        listing_id (UUID):
        url_query (str):
        authorization (None | str | Unset): Bearer token

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
            url_query=url_query,
            authorization=authorization,
        )
    ).parsed
