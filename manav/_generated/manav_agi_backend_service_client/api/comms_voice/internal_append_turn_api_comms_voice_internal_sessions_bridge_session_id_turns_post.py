from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.voice_turn_create import VoiceTurnCreate
from ...models.voice_turn_read import VoiceTurnRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bridge_session_id: str,
    *,
    body: VoiceTurnCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/comms/voice/internal/sessions/{bridge_session_id}/turns".format(
            bridge_session_id=quote(str(bridge_session_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | VoiceTurnRead | None:
    if response.status_code == 201:
        response_201 = VoiceTurnRead.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | VoiceTurnRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VoiceTurnCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceTurnRead]:
    """Internal Append Turn

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):
        body (VoiceTurnCreate): Body sent by voice_bridge_service when persisting a new turn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceTurnRead]
    """

    kwargs = _get_kwargs(
        bridge_session_id=bridge_session_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VoiceTurnCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceTurnRead | None:
    """Internal Append Turn

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):
        body (VoiceTurnCreate): Body sent by voice_bridge_service when persisting a new turn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceTurnRead
    """

    return sync_detailed(
        bridge_session_id=bridge_session_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VoiceTurnCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceTurnRead]:
    """Internal Append Turn

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):
        body (VoiceTurnCreate): Body sent by voice_bridge_service when persisting a new turn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceTurnRead]
    """

    kwargs = _get_kwargs(
        bridge_session_id=bridge_session_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VoiceTurnCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceTurnRead | None:
    """Internal Append Turn

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):
        body (VoiceTurnCreate): Body sent by voice_bridge_service when persisting a new turn.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceTurnRead
    """

    return (
        await asyncio_detailed(
            bridge_session_id=bridge_session_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
