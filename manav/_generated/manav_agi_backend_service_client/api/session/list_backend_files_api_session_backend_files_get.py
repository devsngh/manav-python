from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bot_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    path_prefix: str | Unset = "/",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    params["path_prefix"] = path_prefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/backend-files",
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
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    path_prefix: str | Unset = "/",
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """List Backend Files

     List persistent files stored by a bot's CompositeBackend.
    Reads from the LangGraph store (StoreBackend) to show what's in
    /memories/, /skills/, /artifacts/ for a specific user/bot.

    Args:
        bot_id (None | str | Unset): Bot UUID to inspect
        user_id (None | str | Unset): User UUID (owner of the files)
        path_prefix (str | Unset): Path prefix to list (e.g., /memories/, /skills/, /artifacts/)
            Default: '/'.
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        user_id=user_id,
        path_prefix=path_prefix,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    path_prefix: str | Unset = "/",
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """List Backend Files

     List persistent files stored by a bot's CompositeBackend.
    Reads from the LangGraph store (StoreBackend) to show what's in
    /memories/, /skills/, /artifacts/ for a specific user/bot.

    Args:
        bot_id (None | str | Unset): Bot UUID to inspect
        user_id (None | str | Unset): User UUID (owner of the files)
        path_prefix (str | Unset): Path prefix to list (e.g., /memories/, /skills/, /artifacts/)
            Default: '/'.
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        bot_id=bot_id,
        user_id=user_id,
        path_prefix=path_prefix,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    path_prefix: str | Unset = "/",
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """List Backend Files

     List persistent files stored by a bot's CompositeBackend.
    Reads from the LangGraph store (StoreBackend) to show what's in
    /memories/, /skills/, /artifacts/ for a specific user/bot.

    Args:
        bot_id (None | str | Unset): Bot UUID to inspect
        user_id (None | str | Unset): User UUID (owner of the files)
        path_prefix (str | Unset): Path prefix to list (e.g., /memories/, /skills/, /artifacts/)
            Default: '/'.
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        user_id=user_id,
        path_prefix=path_prefix,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | str | Unset = UNSET,
    user_id: None | str | Unset = UNSET,
    path_prefix: str | Unset = "/",
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """List Backend Files

     List persistent files stored by a bot's CompositeBackend.
    Reads from the LangGraph store (StoreBackend) to show what's in
    /memories/, /skills/, /artifacts/ for a specific user/bot.

    Args:
        bot_id (None | str | Unset): Bot UUID to inspect
        user_id (None | str | Unset): User UUID (owner of the files)
        path_prefix (str | Unset): Path prefix to list (e.g., /memories/, /skills/, /artifacts/)
            Default: '/'.
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            bot_id=bot_id,
            user_id=user_id,
            path_prefix=path_prefix,
            authorization=authorization,
        )
    ).parsed
