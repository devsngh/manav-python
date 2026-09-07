from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_voice_stream_api_voice_stream_post import BodyVoiceStreamApiVoiceStreamPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyVoiceStreamApiVoiceStreamPost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/voice/stream",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

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
    body: BodyVoiceStreamApiVoiceStreamPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Voice Stream

     Full voice chat flow via SSE:
    1. Receive audio from microphone
    2. STT → convert to text
    3. Send text to orchestrator (same as text chat)
    4. Stream text response events
    5. On done → TTS → stream audio as base64
    6. Save dialogue to thread

    SSE events:
      - stt: {"type": "stt", "text": "transcribed text"}
      - token: {"type": "token", "text": "response token"}
      - step: {"type": "step", ...}
      - tts: {"type": "tts", "audio": "base64...", "content_type": "audio/mp3"}
      - done: {"type": "done", "response": "full text", ...}
      - error: {"type": "error", "message": "..."}

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyVoiceStreamApiVoiceStreamPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BodyVoiceStreamApiVoiceStreamPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Voice Stream

     Full voice chat flow via SSE:
    1. Receive audio from microphone
    2. STT → convert to text
    3. Send text to orchestrator (same as text chat)
    4. Stream text response events
    5. On done → TTS → stream audio as base64
    6. Save dialogue to thread

    SSE events:
      - stt: {"type": "stt", "text": "transcribed text"}
      - token: {"type": "token", "text": "response token"}
      - step: {"type": "step", ...}
      - tts: {"type": "tts", "audio": "base64...", "content_type": "audio/mp3"}
      - done: {"type": "done", "response": "full text", ...}
      - error: {"type": "error", "message": "..."}

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyVoiceStreamApiVoiceStreamPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyVoiceStreamApiVoiceStreamPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Voice Stream

     Full voice chat flow via SSE:
    1. Receive audio from microphone
    2. STT → convert to text
    3. Send text to orchestrator (same as text chat)
    4. Stream text response events
    5. On done → TTS → stream audio as base64
    6. Save dialogue to thread

    SSE events:
      - stt: {"type": "stt", "text": "transcribed text"}
      - token: {"type": "token", "text": "response token"}
      - step: {"type": "step", ...}
      - tts: {"type": "tts", "audio": "base64...", "content_type": "audio/mp3"}
      - done: {"type": "done", "response": "full text", ...}
      - error: {"type": "error", "message": "..."}

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyVoiceStreamApiVoiceStreamPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: BodyVoiceStreamApiVoiceStreamPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Voice Stream

     Full voice chat flow via SSE:
    1. Receive audio from microphone
    2. STT → convert to text
    3. Send text to orchestrator (same as text chat)
    4. Stream text response events
    5. On done → TTS → stream audio as base64
    6. Save dialogue to thread

    SSE events:
      - stt: {"type": "stt", "text": "transcribed text"}
      - token: {"type": "token", "text": "response token"}
      - step: {"type": "step", ...}
      - tts: {"type": "tts", "audio": "base64...", "content_type": "audio/mp3"}
      - done: {"type": "done", "response": "full text", ...}
      - error: {"type": "error", "message": "..."}

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyVoiceStreamApiVoiceStreamPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
