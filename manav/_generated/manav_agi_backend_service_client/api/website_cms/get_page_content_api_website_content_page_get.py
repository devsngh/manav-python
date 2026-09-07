from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.page_content_response import PageContentResponse
from ...types import Response


def _get_kwargs(
    page: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/website/content/{page}".format(
            page=quote(str(page), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PageContentResponse | None:
    if response.status_code == 200:
        response_200 = PageContentResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PageContentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    page: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | PageContentResponse]:
    """Get Page Content

    Args:
        page (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PageContentResponse]
    """

    kwargs = _get_kwargs(
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    page: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | PageContentResponse | None:
    """Get Page Content

    Args:
        page (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PageContentResponse
    """

    return sync_detailed(
        page=page,
        client=client,
    ).parsed


async def asyncio_detailed(
    page: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | PageContentResponse]:
    """Get Page Content

    Args:
        page (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PageContentResponse]
    """

    kwargs = _get_kwargs(
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    page: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | PageContentResponse | None:
    """Get Page Content

    Args:
        page (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PageContentResponse
    """

    return (
        await asyncio_detailed(
            page=page,
            client=client,
        )
    ).parsed
