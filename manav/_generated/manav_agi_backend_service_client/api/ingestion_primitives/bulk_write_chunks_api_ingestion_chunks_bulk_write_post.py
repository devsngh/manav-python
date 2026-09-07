from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_write_chunks_request import BulkWriteChunksRequest
from ...models.bulk_write_chunks_response import BulkWriteChunksResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkWriteChunksRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/chunks/bulk-write",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkWriteChunksResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BulkWriteChunksResponse.from_dict(response.json())

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
) -> Response[BulkWriteChunksResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkWriteChunksRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[BulkWriteChunksResponse | HTTPValidationError]:
    """Bulk Write Chunks

     Bulk insert chunks for one document in a single transaction.

    All chunks must have unique chunk_index. total_chunks on each row defaults
    to len(chunks) but can be overridden via the request's total_chunks.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkWriteChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkWriteChunksResponse | HTTPValidationError]
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
    body: BulkWriteChunksRequest,
    authorization: None | str | Unset = UNSET,
) -> BulkWriteChunksResponse | HTTPValidationError | None:
    """Bulk Write Chunks

     Bulk insert chunks for one document in a single transaction.

    All chunks must have unique chunk_index. total_chunks on each row defaults
    to len(chunks) but can be overridden via the request's total_chunks.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkWriteChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkWriteChunksResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkWriteChunksRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[BulkWriteChunksResponse | HTTPValidationError]:
    """Bulk Write Chunks

     Bulk insert chunks for one document in a single transaction.

    All chunks must have unique chunk_index. total_chunks on each row defaults
    to len(chunks) but can be overridden via the request's total_chunks.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkWriteChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkWriteChunksResponse | HTTPValidationError]
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
    body: BulkWriteChunksRequest,
    authorization: None | str | Unset = UNSET,
) -> BulkWriteChunksResponse | HTTPValidationError | None:
    """Bulk Write Chunks

     Bulk insert chunks for one document in a single transaction.

    All chunks must have unique chunk_index. total_chunks on each row defaults
    to len(chunks) but can be overridden via the request's total_chunks.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkWriteChunksRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkWriteChunksResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
