from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_document_api_ingestion_upload_post import BodyUploadDocumentApiIngestionUploadPost
from ...models.http_validation_error import HTTPValidationError
from ...models.upload_response import UploadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BodyUploadDocumentApiIngestionUploadPost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/upload",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UploadResponse | None:
    if response.status_code == 202:
        response_202 = UploadResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadDocumentApiIngestionUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UploadResponse]:
    """Upload Document

     Upload a file → save to S3 → queue Celery task → return job_id.
    If source_id not provided, a new 'upload' source is created automatically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadDocumentApiIngestionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadResponse]
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
    body: BodyUploadDocumentApiIngestionUploadPost,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UploadResponse | None:
    """Upload Document

     Upload a file → save to S3 → queue Celery task → return job_id.
    If source_id not provided, a new 'upload' source is created automatically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadDocumentApiIngestionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadDocumentApiIngestionUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UploadResponse]:
    """Upload Document

     Upload a file → save to S3 → queue Celery task → return job_id.
    If source_id not provided, a new 'upload' source is created automatically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadDocumentApiIngestionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UploadResponse]
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
    body: BodyUploadDocumentApiIngestionUploadPost,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UploadResponse | None:
    """Upload Document

     Upload a file → save to S3 → queue Celery task → return job_id.
    If source_id not provided, a new 'upload' source is created automatically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BodyUploadDocumentApiIngestionUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UploadResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
