from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.main_channel_message_response import MainChannelMessageResponse
from ...models.main_channel_message_update import MainChannelMessageUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    message_id: UUID,
    *,
    body: MainChannelMessageUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/social/channel/messages/{message_id}".format(
            message_id=quote(str(message_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MainChannelMessageResponse | None:
    if response.status_code == 200:
        response_200 = MainChannelMessageResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MainChannelMessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MainChannelMessageUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MainChannelMessageResponse]:
    """Update Channel Message

     Edit a channel message

    Args:
        message_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MainChannelMessageUpdate): Schema for editing a channel message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MainChannelMessageResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MainChannelMessageUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MainChannelMessageResponse | None:
    """Update Channel Message

     Edit a channel message

    Args:
        message_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MainChannelMessageUpdate): Schema for editing a channel message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MainChannelMessageResponse
    """

    return sync_detailed(
        message_id=message_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MainChannelMessageUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MainChannelMessageResponse]:
    """Update Channel Message

     Edit a channel message

    Args:
        message_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MainChannelMessageUpdate): Schema for editing a channel message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MainChannelMessageResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MainChannelMessageUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MainChannelMessageResponse | None:
    """Update Channel Message

     Edit a channel message

    Args:
        message_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MainChannelMessageUpdate): Schema for editing a channel message

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MainChannelMessageResponse
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
