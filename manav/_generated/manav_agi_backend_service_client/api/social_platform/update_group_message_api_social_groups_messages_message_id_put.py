from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_group_message_response import UserGroupMessageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    message_id: UUID,
    *,
    content: str,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["content"] = content

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/social/groups/messages/{message_id}".format(
            message_id=quote(str(message_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UserGroupMessageResponse | None:
    if response.status_code == 200:
        response_200 = UserGroupMessageResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UserGroupMessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    content: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserGroupMessageResponse]:
    """Update Group Message

     Edit a group message

    Args:
        message_id (UUID):
        content (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupMessageResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        content=content,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    content: str,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserGroupMessageResponse | None:
    """Update Group Message

     Edit a group message

    Args:
        message_id (UUID):
        content (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupMessageResponse
    """

    return sync_detailed(
        message_id=message_id,
        client=client,
        content=content,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    content: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UserGroupMessageResponse]:
    """Update Group Message

     Edit a group message

    Args:
        message_id (UUID):
        content (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UserGroupMessageResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        content=content,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    content: str,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UserGroupMessageResponse | None:
    """Update Group Message

     Edit a group message

    Args:
        message_id (UUID):
        content (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UserGroupMessageResponse
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            client=client,
            content=content,
            authorization=authorization,
        )
    ).parsed
