from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_instance_response import MeetingInstanceResponse
from ...models.meeting_instance_update import MeetingInstanceUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    instance_id: UUID,
    *,
    body: MeetingInstanceUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/meetings/instances/{instance_id}".format(
            instance_id=quote(str(instance_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MeetingInstanceResponse | None:
    if response.status_code == 200:
        response_200 = MeetingInstanceResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MeetingInstanceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instance_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MeetingInstanceUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MeetingInstanceResponse]:
    """Update Meeting Instance

    Args:
        instance_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MeetingInstanceUpdate): Patch — set any subset of fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MeetingInstanceResponse]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    instance_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MeetingInstanceUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MeetingInstanceResponse | None:
    """Update Meeting Instance

    Args:
        instance_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MeetingInstanceUpdate): Patch — set any subset of fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MeetingInstanceResponse
    """

    return sync_detailed(
        instance_id=instance_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    instance_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MeetingInstanceUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MeetingInstanceResponse]:
    """Update Meeting Instance

    Args:
        instance_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MeetingInstanceUpdate): Patch — set any subset of fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MeetingInstanceResponse]
    """

    kwargs = _get_kwargs(
        instance_id=instance_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    instance_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: MeetingInstanceUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MeetingInstanceResponse | None:
    """Update Meeting Instance

    Args:
        instance_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (MeetingInstanceUpdate): Patch — set any subset of fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MeetingInstanceResponse
    """

    return (
        await asyncio_detailed(
            instance_id=instance_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
