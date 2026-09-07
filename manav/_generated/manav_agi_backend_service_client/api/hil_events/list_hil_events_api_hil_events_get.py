from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hil_event_list_response import HILEventListResponse
from ...models.hil_event_status import HILEventStatus
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    thread_id: None | str | Unset = UNSET,
    status: HILEventStatus | None | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_thread_id: None | str | Unset
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, HILEventStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/hil-events",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HILEventListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = HILEventListResponse.from_dict(response.json())

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
) -> Response[HILEventListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    thread_id: None | str | Unset = UNSET,
    status: HILEventStatus | None | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HILEventListResponse | HTTPValidationError]:
    """List Hil Events

     List HIL events with optional filters. Non-admin callers are pinned
    to their own user_id server-side — a client-supplied `user_id` cannot
    widen visibility beyond the caller.

    Args:
        user_id (None | str | Unset):
        thread_id (None | str | Unset):
        status (HILEventStatus | None | Unset):
        bot_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILEventListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        thread_id=thread_id,
        status=status,
        bot_id=bot_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    thread_id: None | str | Unset = UNSET,
    status: HILEventStatus | None | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HILEventListResponse | HTTPValidationError | None:
    """List Hil Events

     List HIL events with optional filters. Non-admin callers are pinned
    to their own user_id server-side — a client-supplied `user_id` cannot
    widen visibility beyond the caller.

    Args:
        user_id (None | str | Unset):
        thread_id (None | str | Unset):
        status (HILEventStatus | None | Unset):
        bot_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILEventListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        thread_id=thread_id,
        status=status,
        bot_id=bot_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    thread_id: None | str | Unset = UNSET,
    status: HILEventStatus | None | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HILEventListResponse | HTTPValidationError]:
    """List Hil Events

     List HIL events with optional filters. Non-admin callers are pinned
    to their own user_id server-side — a client-supplied `user_id` cannot
    widen visibility beyond the caller.

    Args:
        user_id (None | str | Unset):
        thread_id (None | str | Unset):
        status (HILEventStatus | None | Unset):
        bot_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILEventListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        thread_id=thread_id,
        status=status,
        bot_id=bot_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    thread_id: None | str | Unset = UNSET,
    status: HILEventStatus | None | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HILEventListResponse | HTTPValidationError | None:
    """List Hil Events

     List HIL events with optional filters. Non-admin callers are pinned
    to their own user_id server-side — a client-supplied `user_id` cannot
    widen visibility beyond the caller.

    Args:
        user_id (None | str | Unset):
        thread_id (None | str | Unset):
        status (HILEventStatus | None | Unset):
        bot_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILEventListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            thread_id=thread_id,
            status=status,
            bot_id=bot_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
