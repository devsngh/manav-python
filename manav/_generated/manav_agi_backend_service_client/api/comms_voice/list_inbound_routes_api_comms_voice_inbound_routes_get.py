from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.voice_inbound_route_read import VoiceInboundRouteRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    to_number: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_to_number: None | str | Unset
    if isinstance(to_number, Unset):
        json_to_number = UNSET
    else:
        json_to_number = to_number
    params["to_number"] = json_to_number

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    elif isinstance(agent_id, UUID):
        json_agent_id = str(agent_id)
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/comms/voice/inbound-routes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[VoiceInboundRouteRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = VoiceInboundRouteRead.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[VoiceInboundRouteRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    to_number: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[VoiceInboundRouteRead]]:
    """List Inbound Routes

    Args:
        to_number (None | str | Unset):
        is_active (bool | None | Unset):
        agent_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[VoiceInboundRouteRead]]
    """

    kwargs = _get_kwargs(
        to_number=to_number,
        is_active=is_active,
        agent_id=agent_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    to_number: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[VoiceInboundRouteRead] | None:
    """List Inbound Routes

    Args:
        to_number (None | str | Unset):
        is_active (bool | None | Unset):
        agent_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[VoiceInboundRouteRead]
    """

    return sync_detailed(
        client=client,
        to_number=to_number,
        is_active=is_active,
        agent_id=agent_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    to_number: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[VoiceInboundRouteRead]]:
    """List Inbound Routes

    Args:
        to_number (None | str | Unset):
        is_active (bool | None | Unset):
        agent_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[VoiceInboundRouteRead]]
    """

    kwargs = _get_kwargs(
        to_number=to_number,
        is_active=is_active,
        agent_id=agent_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    to_number: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    agent_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[VoiceInboundRouteRead] | None:
    """List Inbound Routes

    Args:
        to_number (None | str | Unset):
        is_active (bool | None | Unset):
        agent_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[VoiceInboundRouteRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            to_number=to_number,
            is_active=is_active,
            agent_id=agent_id,
            authorization=authorization,
        )
    ).parsed
