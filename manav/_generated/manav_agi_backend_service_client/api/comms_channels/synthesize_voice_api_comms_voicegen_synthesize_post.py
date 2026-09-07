from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.voice_gen_request import VoiceGenRequest
from ...models.voice_gen_response import VoiceGenResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VoiceGenRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/comms/voicegen/synthesize",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | VoiceGenResponse | None:
    if response.status_code == 201:
        response_201 = VoiceGenResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | VoiceGenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceGenRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceGenResponse]:
    """Synthesize Voice

     Generate a voice-asset audio file via the org's voicegen datasource
    (ElevenLabs etc.). Output is uploaded to S3 + a platform.assets row is
    created; the response carries asset_id + signed URL.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceGenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceGenResponse]
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
    body: VoiceGenRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceGenResponse | None:
    """Synthesize Voice

     Generate a voice-asset audio file via the org's voicegen datasource
    (ElevenLabs etc.). Output is uploaded to S3 + a platform.assets row is
    created; the response carries asset_id + signed URL.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceGenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceGenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VoiceGenRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | VoiceGenResponse]:
    """Synthesize Voice

     Generate a voice-asset audio file via the org's voicegen datasource
    (ElevenLabs etc.). Output is uploaded to S3 + a platform.assets row is
    created; the response carries asset_id + signed URL.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceGenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | VoiceGenResponse]
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
    body: VoiceGenRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | VoiceGenResponse | None:
    """Synthesize Voice

     Generate a voice-asset audio file via the org's voicegen datasource
    (ElevenLabs etc.). Output is uploaded to S3 + a platform.assets row is
    created; the response carries asset_id + signed URL.

    Args:
        authorization (None | str | Unset): Bearer token
        body (VoiceGenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | VoiceGenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
