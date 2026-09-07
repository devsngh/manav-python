from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.content_response import ContentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    page: str,
    section_key: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/website/content/{page}/{section_key}".format(
            page=quote(str(page), safe=""),
            section_key=quote(str(section_key), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContentResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContentResponse.from_dict(response.json())

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
) -> Response[ContentResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    page: str,
    section_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ContentResponse | HTTPValidationError]:
    """Get Section Content

    Args:
        page (str):
        section_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        section_key=section_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    page: str,
    section_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ContentResponse | HTTPValidationError | None:
    """Get Section Content

    Args:
        page (str):
        section_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentResponse | HTTPValidationError
    """

    return sync_detailed(
        page=page,
        section_key=section_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    page: str,
    section_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ContentResponse | HTTPValidationError]:
    """Get Section Content

    Args:
        page (str):
        section_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        section_key=section_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    page: str,
    section_key: str,
    *,
    client: AuthenticatedClient | Client,
) -> ContentResponse | HTTPValidationError | None:
    """Get Section Content

    Args:
        page (str):
        section_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContentResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            page=page,
            section_key=section_key,
            client=client,
        )
    ).parsed
