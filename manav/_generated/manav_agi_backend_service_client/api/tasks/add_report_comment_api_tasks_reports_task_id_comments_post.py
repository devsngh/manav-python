from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.task_comment_create import TaskCommentCreate
from ...models.task_comment_response import TaskCommentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: UUID,
    *,
    body: TaskCommentCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/reports/{task_id}/comments".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TaskCommentResponse | None:
    if response.status_code == 201:
        response_201 = TaskCommentResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TaskCommentResponse]:
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
    body: TaskCommentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskCommentResponse]:
    """Add Report Comment

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TaskCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskCommentResponse]
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
    body: TaskCommentCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskCommentResponse | None:
    """Add Report Comment

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TaskCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskCommentResponse
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
    body: TaskCommentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TaskCommentResponse]:
    """Add Report Comment

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TaskCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TaskCommentResponse]
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
    body: TaskCommentCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TaskCommentResponse | None:
    """Add Report Comment

    Args:
        task_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TaskCommentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TaskCommentResponse
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
