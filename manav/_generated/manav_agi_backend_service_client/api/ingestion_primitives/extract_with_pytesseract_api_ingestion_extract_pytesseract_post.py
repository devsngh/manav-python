from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_ocr_request import ExtractOcrRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.ocr_response import OcrResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExtractOcrRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/extract/pytesseract",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | OcrResponse | None:
    if response.status_code == 200:
        response_200 = OcrResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | OcrResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExtractOcrRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OcrResponse]:
    """Extract With Pytesseract

     OCR an image with pytesseract. Configurable language.

    Primitive: no preprocessing decision (caller can request specific mode via
    future param), no confidence threshold filtering. Returns text + the
    average word-level confidence Tesseract reports.

    `lang` examples: 'eng', 'hin', 'eng+hin', 'fra', 'jpn'. Default 'eng'.
    Multiple languages joined with '+'.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractOcrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OcrResponse]
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
    body: ExtractOcrRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | OcrResponse | None:
    """Extract With Pytesseract

     OCR an image with pytesseract. Configurable language.

    Primitive: no preprocessing decision (caller can request specific mode via
    future param), no confidence threshold filtering. Returns text + the
    average word-level confidence Tesseract reports.

    `lang` examples: 'eng', 'hin', 'eng+hin', 'fra', 'jpn'. Default 'eng'.
    Multiple languages joined with '+'.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractOcrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OcrResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExtractOcrRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | OcrResponse]:
    """Extract With Pytesseract

     OCR an image with pytesseract. Configurable language.

    Primitive: no preprocessing decision (caller can request specific mode via
    future param), no confidence threshold filtering. Returns text + the
    average word-level confidence Tesseract reports.

    `lang` examples: 'eng', 'hin', 'eng+hin', 'fra', 'jpn'. Default 'eng'.
    Multiple languages joined with '+'.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractOcrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | OcrResponse]
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
    body: ExtractOcrRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | OcrResponse | None:
    """Extract With Pytesseract

     OCR an image with pytesseract. Configurable language.

    Primitive: no preprocessing decision (caller can request specific mode via
    future param), no confidence threshold filtering. Returns text + the
    average word-level confidence Tesseract reports.

    `lang` examples: 'eng', 'hin', 'eng+hin', 'fra', 'jpn'. Default 'eng'.
    Multiple languages joined with '+'.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractOcrRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | OcrResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
