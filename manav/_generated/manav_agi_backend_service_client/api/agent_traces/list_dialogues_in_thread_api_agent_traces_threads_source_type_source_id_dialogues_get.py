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
    source_type: str,
    source_id: UUID,
    *,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_bot_id, Unset):
        headers["X-Bot-Id"] = x_bot_id

    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent-traces/threads/{source_type}/{source_id}/dialogues".format(
            source_type=quote(str(source_type), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Dialogues In Thread

     Pane-1 expand: dialogues / turns inside a thread, newest first.

    Args:
        source_type (str):
        source_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        source_id=source_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Dialogues In Thread

     Pane-1 expand: dialogues / turns inside a thread, newest first.

    Args:
        source_type (str):
        source_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        source_type=source_type,
        source_id=source_id,
        client=client,
        x_bot_id=x_bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """List Dialogues In Thread

     Pane-1 expand: dialogues / turns inside a thread, newest first.

    Args:
        source_type (str):
        source_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        source_type=source_type,
        source_id=source_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source_type: str,
    source_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """List Dialogues In Thread

     Pane-1 expand: dialogues / turns inside a thread, newest first.

    Args:
        source_type (str):
        source_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            source_type=source_type,
            source_id=source_id,
            client=client,
            x_bot_id=x_bot_id,
            authorization=authorization,
        )
    ).parsed
