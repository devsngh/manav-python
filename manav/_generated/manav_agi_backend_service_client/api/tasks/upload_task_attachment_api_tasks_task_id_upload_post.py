from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_task_attachment_api_tasks_task_id_upload_post import (
    BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: UUID,
    *,
    body: BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/{task_id}/upload".format(
            task_id=quote(str(task_id), safe=""),
        ),
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
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Upload Task Attachment

     Upload attachment to a task (images, files). Uses multipart form data.

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadTaskAttachmentApiTasksTaskIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Upload Task Attachment

     Upload attachment to a task (images, files). Uses multipart form data.

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadTaskAttachmentApiTasksTaskIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Upload Task Attachment

     Upload attachment to a task (images, files). Uses multipart form data.

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadTaskAttachmentApiTasksTaskIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyUploadTaskAttachmentApiTasksTaskIdUploadPost,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Upload Task Attachment

     Upload attachment to a task (images, files). Uses multipart form data.

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyUploadTaskAttachmentApiTasksTaskIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
