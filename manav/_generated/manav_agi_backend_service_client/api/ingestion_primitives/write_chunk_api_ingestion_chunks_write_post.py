from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.write_chunk_request import WriteChunkRequest
from ...models.write_chunk_response import WriteChunkResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WriteChunkRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/chunks/write",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WriteChunkResponse | None:
    if response.status_code == 200:
        response_200 = WriteChunkResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WriteChunkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WriteChunkRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WriteChunkResponse]:
    """Write Chunk

     Insert a single chunk row into ingestion_chunks.

    The document_id resolves workspace_id + source_id automatically (chunks
    inherit those from their parent document). Caller passes the chunk's
    raw_text + index + (optionally) pre-computed embedding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (WriteChunkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WriteChunkResponse]
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
    body: WriteChunkRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WriteChunkResponse | None:
    """Write Chunk

     Insert a single chunk row into ingestion_chunks.

    The document_id resolves workspace_id + source_id automatically (chunks
    inherit those from their parent document). Caller passes the chunk's
    raw_text + index + (optionally) pre-computed embedding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (WriteChunkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WriteChunkResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WriteChunkRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WriteChunkResponse]:
    """Write Chunk

     Insert a single chunk row into ingestion_chunks.

    The document_id resolves workspace_id + source_id automatically (chunks
    inherit those from their parent document). Caller passes the chunk's
    raw_text + index + (optionally) pre-computed embedding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (WriteChunkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WriteChunkResponse]
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
    body: WriteChunkRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WriteChunkResponse | None:
    """Write Chunk

     Insert a single chunk row into ingestion_chunks.

    The document_id resolves workspace_id + source_id automatically (chunks
    inherit those from their parent document). Caller passes the chunk's
    raw_text + index + (optionally) pre-computed embedding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (WriteChunkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WriteChunkResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
