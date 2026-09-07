from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.voice_session_start_request import VoiceSessionStartRequest
from ...models.voice_session_start_response import VoiceSessionStartResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VoiceSessionStartRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/comms/voice/sessions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | VoiceSessionStartResponse | None:
    if response.status_code == 202:
        response_202 = VoiceSessionStartResponse.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | VoiceSessionStartResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceSessionStartRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceSessionStartResponse]:
    """Start Voice Session

     Start a voice session.

    For mode='live_realtime': the call is dialed and on answer the call is
    bridged to OpenAI Realtime via the voice_bridge_service. The agent stays
    on the call until either side hangs up or max_duration_seconds elapses.

    For mode='prerendered_dtmf': use POST /api/comms/voice/call instead —
    that endpoint is the existing make_call path which pre-renders TTS and
    plays via TwiML.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceSessionStartRequest): Body for POST /api/comms/voice/sessions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceSessionStartResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceSessionStartRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceSessionStartResponse | None:
    """Start Voice Session

     Start a voice session.

    For mode='live_realtime': the call is dialed and on answer the call is
    bridged to OpenAI Realtime via the voice_bridge_service. The agent stays
    on the call until either side hangs up or max_duration_seconds elapses.

    For mode='prerendered_dtmf': use POST /api/comms/voice/call instead —
    that endpoint is the existing make_call path which pre-renders TTS and
    plays via TwiML.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceSessionStartRequest): Body for POST /api/comms/voice/sessions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceSessionStartResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceSessionStartRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceSessionStartResponse]:
    """Start Voice Session

     Start a voice session.

    For mode='live_realtime': the call is dialed and on answer the call is
    bridged to OpenAI Realtime via the voice_bridge_service. The agent stays
    on the call until either side hangs up or max_duration_seconds elapses.

    For mode='prerendered_dtmf': use POST /api/comms/voice/call instead —
    that endpoint is the existing make_call path which pre-renders TTS and
    plays via TwiML.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceSessionStartRequest): Body for POST /api/comms/voice/sessions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceSessionStartResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceSessionStartRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceSessionStartResponse | None:
    """Start Voice Session

     Start a voice session.

    For mode='live_realtime': the call is dialed and on answer the call is
    bridged to OpenAI Realtime via the voice_bridge_service. The agent stays
    on the call until either side hangs up or max_duration_seconds elapses.

    For mode='prerendered_dtmf': use POST /api/comms/voice/call instead —
    that endpoint is the existing make_call path which pre-renders TTS and
    plays via TwiML.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceSessionStartRequest): Body for POST /api/comms/voice/sessions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceSessionStartResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
