from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_message_read import ExternalMessageRead
from ...models.http_validation_error import HTTPValidationError
from ...models.list_messages_api_comms_email_messages_get_direction_type_0 import (
    ListMessagesApiCommsEmailMessagesGetDirectionType0,
)
from ...models.list_messages_api_comms_email_messages_get_status_type_0 import (
    ListMessagesApiCommsEmailMessagesGetStatusType0,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    direction: ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset = UNSET,
    thread_id: None | Unset | UUID = UNSET,
    campaign_id: None | Unset | UUID = UNSET,
    sender_agent_id: None | Unset | UUID = UNSET,
    status: ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_direction: None | str | Unset
    if isinstance(direction, Unset):
        json_direction = UNSET
    elif isinstance(direction, ListMessagesApiCommsEmailMessagesGetDirectionType0):
        json_direction = direction.value
    else:
        json_direction = direction
    params["direction"] = json_direction

    json_thread_id: None | str | Unset
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    elif isinstance(thread_id, UUID):
        json_thread_id = str(thread_id)
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_campaign_id: None | str | Unset
    if isinstance(campaign_id, Unset):
        json_campaign_id = UNSET
    elif isinstance(campaign_id, UUID):
        json_campaign_id = str(campaign_id)
    else:
        json_campaign_id = campaign_id
    params["campaign_id"] = json_campaign_id

    json_sender_agent_id: None | str | Unset
    if isinstance(sender_agent_id, Unset):
        json_sender_agent_id = UNSET
    elif isinstance(sender_agent_id, UUID):
        json_sender_agent_id = str(sender_agent_id)
    else:
        json_sender_agent_id = sender_agent_id
    params["sender_agent_id"] = json_sender_agent_id

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListMessagesApiCommsEmailMessagesGetStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/comms/email/messages",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ExternalMessageRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExternalMessageRead.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[ExternalMessageRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    direction: ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset = UNSET,
    thread_id: None | Unset | UUID = UNSET,
    campaign_id: None | Unset | UUID = UNSET,
    sender_agent_id: None | Unset | UUID = UNSET,
    status: ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ExternalMessageRead]]:
    """List Messages

    Args:
        direction (ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset):
        thread_id (None | Unset | UUID):
        campaign_id (None | Unset | UUID):
        sender_agent_id (None | Unset | UUID):
        status (ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ExternalMessageRead]]
    """

    kwargs = _get_kwargs(
        direction=direction,
        thread_id=thread_id,
        campaign_id=campaign_id,
        sender_agent_id=sender_agent_id,
        status=status,
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
    direction: ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset = UNSET,
    thread_id: None | Unset | UUID = UNSET,
    campaign_id: None | Unset | UUID = UNSET,
    sender_agent_id: None | Unset | UUID = UNSET,
    status: ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ExternalMessageRead] | None:
    """List Messages

    Args:
        direction (ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset):
        thread_id (None | Unset | UUID):
        campaign_id (None | Unset | UUID):
        sender_agent_id (None | Unset | UUID):
        status (ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ExternalMessageRead]
    """

    return sync_detailed(
        client=client,
        direction=direction,
        thread_id=thread_id,
        campaign_id=campaign_id,
        sender_agent_id=sender_agent_id,
        status=status,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    direction: ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset = UNSET,
    thread_id: None | Unset | UUID = UNSET,
    campaign_id: None | Unset | UUID = UNSET,
    sender_agent_id: None | Unset | UUID = UNSET,
    status: ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ExternalMessageRead]]:
    """List Messages

    Args:
        direction (ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset):
        thread_id (None | Unset | UUID):
        campaign_id (None | Unset | UUID):
        sender_agent_id (None | Unset | UUID):
        status (ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ExternalMessageRead]]
    """

    kwargs = _get_kwargs(
        direction=direction,
        thread_id=thread_id,
        campaign_id=campaign_id,
        sender_agent_id=sender_agent_id,
        status=status,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    direction: ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset = UNSET,
    thread_id: None | Unset | UUID = UNSET,
    campaign_id: None | Unset | UUID = UNSET,
    sender_agent_id: None | Unset | UUID = UNSET,
    status: ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ExternalMessageRead] | None:
    """List Messages

    Args:
        direction (ListMessagesApiCommsEmailMessagesGetDirectionType0 | None | Unset):
        thread_id (None | Unset | UUID):
        campaign_id (None | Unset | UUID):
        sender_agent_id (None | Unset | UUID):
        status (ListMessagesApiCommsEmailMessagesGetStatusType0 | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ExternalMessageRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            direction=direction,
            thread_id=thread_id,
            campaign_id=campaign_id,
            sender_agent_id=sender_agent_id,
            status=status,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
