from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.voice_session_read import VoiceSessionRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bridge_session_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/comms/voice/internal/sessions/{bridge_session_id}".format(
            bridge_session_id=quote(str(bridge_session_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | VoiceSessionRead | None:
    if response.status_code == 200:
        response_200 = VoiceSessionRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | VoiceSessionRead]:
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
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceSessionRead]:
    """Internal Read Session

     Bridge service fetches session context (system_prompt, voice_id,
    extra_context, etc.) on Twilio WS connect.

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceSessionRead]
    """

    kwargs = _get_kwargs(
        bridge_session_id=bridge_session_id,
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
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceSessionRead | None:
    """Internal Read Session

     Bridge service fetches session context (system_prompt, voice_id,
    extra_context, etc.) on Twilio WS connect.

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceSessionRead
    """

    return sync_detailed(
        bridge_session_id=bridge_session_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceSessionRead]:
    """Internal Read Session

     Bridge service fetches session context (system_prompt, voice_id,
    extra_context, etc.) on Twilio WS connect.

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceSessionRead]
    """

    kwargs = _get_kwargs(
        bridge_session_id=bridge_session_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bridge_session_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceSessionRead | None:
    """Internal Read Session

     Bridge service fetches session context (system_prompt, voice_id,
    extra_context, etc.) on Twilio WS connect.

    Args:
        bridge_session_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceSessionRead
    """

    return (
        await asyncio_detailed(
            bridge_session_id=bridge_session_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
