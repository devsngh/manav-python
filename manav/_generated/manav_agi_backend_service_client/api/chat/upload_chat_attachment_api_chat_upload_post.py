from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_chat_attachment_api_chat_upload_post import BodyUploadChatAttachmentApiChatUploadPost
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyUploadChatAttachmentApiChatUploadPost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/chat/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = response.json()
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
    body: BodyUploadChatAttachmentApiChatUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Upload Chat Attachment

     Upload a chat attachment.

    Accepted:
      - Text-extractable: PDF, DOCX, XLSX, PPTX, plus most code/config files
        (.py .js .ts .go .java .sql .yml .json .html .css .csv ...)
      - Images for native vision: PNG, JPG, GIF, WEBP

    Returns ``{url, filename, size, mime, kind}`` where ``kind`` is
    ``"text"`` (caller puts URL in DialogueCreate.file_urls — backend
    extracts text and prepends to the prompt) or ``"image"`` (caller puts
    URL in DialogueCreate.image_urls — backend base64-encodes and sends as
    a native vision block to the model).

    Limits:
      - 10 MiB max for text files
      - 5 MiB max per image (Anthropic vision cap)

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadChatAttachmentApiChatUploadPost):

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
    body: BodyUploadChatAttachmentApiChatUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Upload Chat Attachment

     Upload a chat attachment.

    Accepted:
      - Text-extractable: PDF, DOCX, XLSX, PPTX, plus most code/config files
        (.py .js .ts .go .java .sql .yml .json .html .css .csv ...)
      - Images for native vision: PNG, JPG, GIF, WEBP

    Returns ``{url, filename, size, mime, kind}`` where ``kind`` is
    ``"text"`` (caller puts URL in DialogueCreate.file_urls — backend
    extracts text and prepends to the prompt) or ``"image"`` (caller puts
    URL in DialogueCreate.image_urls — backend base64-encodes and sends as
    a native vision block to the model).

    Limits:
      - 10 MiB max for text files
      - 5 MiB max per image (Anthropic vision cap)

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadChatAttachmentApiChatUploadPost):

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
    body: BodyUploadChatAttachmentApiChatUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Upload Chat Attachment

     Upload a chat attachment.

    Accepted:
      - Text-extractable: PDF, DOCX, XLSX, PPTX, plus most code/config files
        (.py .js .ts .go .java .sql .yml .json .html .css .csv ...)
      - Images for native vision: PNG, JPG, GIF, WEBP

    Returns ``{url, filename, size, mime, kind}`` where ``kind`` is
    ``"text"`` (caller puts URL in DialogueCreate.file_urls — backend
    extracts text and prepends to the prompt) or ``"image"`` (caller puts
    URL in DialogueCreate.image_urls — backend base64-encodes and sends as
    a native vision block to the model).

    Limits:
      - 10 MiB max for text files
      - 5 MiB max per image (Anthropic vision cap)

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadChatAttachmentApiChatUploadPost):

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
    body: BodyUploadChatAttachmentApiChatUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Upload Chat Attachment

     Upload a chat attachment.

    Accepted:
      - Text-extractable: PDF, DOCX, XLSX, PPTX, plus most code/config files
        (.py .js .ts .go .java .sql .yml .json .html .css .csv ...)
      - Images for native vision: PNG, JPG, GIF, WEBP

    Returns ``{url, filename, size, mime, kind}`` where ``kind`` is
    ``"text"`` (caller puts URL in DialogueCreate.file_urls — backend
    extracts text and prepends to the prompt) or ``"image"`` (caller puts
    URL in DialogueCreate.image_urls — backend base64-encodes and sends as
    a native vision block to the model).

    Limits:
      - 10 MiB max for text files
      - 5 MiB max per image (Anthropic vision cap)

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadChatAttachmentApiChatUploadPost):

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
