from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: UUID,
    *,
    q: str,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["q"] = q

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/channel/{channel_id}/messages/search".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Search Channel Messages

     Case-insensitive substring search inside a main channel. Same
    auth guard as `get_messages` (require_social_read).

    Args:
        channel_id (UUID):
        q (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Search Channel Messages

     Case-insensitive substring search inside a main channel. Same
    auth guard as `get_messages` (require_social_read).

    Args:
        channel_id (UUID):
        q (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        q=q,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    channel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Search Channel Messages

     Case-insensitive substring search inside a main channel. Same
    auth guard as `get_messages` (require_social_read).

    Args:
        channel_id (UUID):
        q (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        q=q,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    q: str,
    page: int | Unset = 1,
    page_size: int | Unset = 25,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Search Channel Messages

     Case-insensitive substring search inside a main channel. Same
    auth guard as `get_messages` (require_social_read).

    Args:
        channel_id (UUID):
        q (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 25.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            q=q,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
