from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.thread_list_response import ThreadListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    include_archived: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["include_archived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat/threads",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ThreadListResponse | None:
    if response.status_code == 200:
        response_200 = ThreadListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ThreadListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    include_archived: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ThreadListResponse]:
    """Get Threads

     Get paginated list of user's chat threads

    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 25, max: 100)
    - **include_archived**: Include archived threads (default: false)

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        include_archived (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ThreadListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_archived=include_archived,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    include_archived: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ThreadListResponse | None:
    """Get Threads

     Get paginated list of user's chat threads

    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 25, max: 100)
    - **include_archived**: Include archived threads (default: false)

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        include_archived (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ThreadListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        include_archived=include_archived,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    include_archived: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ThreadListResponse]:
    """Get Threads

     Get paginated list of user's chat threads

    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 25, max: 100)
    - **include_archived**: Include archived threads (default: false)

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        include_archived (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ThreadListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        include_archived=include_archived,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    include_archived: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ThreadListResponse | None:
    """Get Threads

     Get paginated list of user's chat threads

    - **page**: Page number (default: 1)
    - **page_size**: Items per page (default: 25, max: 100)
    - **include_archived**: Include archived threads (default: false)

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        include_archived (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ThreadListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            include_archived=include_archived,
            authorization=authorization,
        )
    ).parsed
