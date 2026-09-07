from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blog_post_list_response import BlogPostListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/website/blog/posts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BlogPostListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BlogPostListResponse.from_dict(response.json())

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
) -> Response[BlogPostListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BlogPostListResponse | HTTPValidationError]:
    """Public List Posts

    Args:
        type_ (None | str | Unset): blog | newsletter
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlogPostListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        type_=type_,
        search=search,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BlogPostListResponse | HTTPValidationError | None:
    """Public List Posts

    Args:
        type_ (None | str | Unset): blog | newsletter
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlogPostListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        type_=type_,
        search=search,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> Response[BlogPostListResponse | HTTPValidationError]:
    """Public List Posts

    Args:
        type_ (None | str | Unset): blog | newsletter
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BlogPostListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        type_=type_,
        search=search,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: None | str | Unset = UNSET,
    search: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
) -> BlogPostListResponse | HTTPValidationError | None:
    """Public List Posts

    Args:
        type_ (None | str | Unset): blog | newsletter
        search (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BlogPostListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
            search=search,
            page=page,
            page_size=page_size,
        )
    ).parsed
