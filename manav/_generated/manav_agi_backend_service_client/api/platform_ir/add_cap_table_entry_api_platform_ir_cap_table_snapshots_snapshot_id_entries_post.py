from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cap_table_entry_create import CapTableEntryCreate
from ...models.cap_table_entry_response import CapTableEntryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    snapshot_id: UUID,
    *,
    body: CapTableEntryCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/ir/cap-table/snapshots/{snapshot_id}/entries".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CapTableEntryResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = CapTableEntryResponse.from_dict(response.json())

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
) -> Response[CapTableEntryResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CapTableEntryCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[CapTableEntryResponse | HTTPValidationError]:
    """Add Cap Table Entry

    Args:
        snapshot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CapTableEntryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CapTableEntryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CapTableEntryCreate,
    authorization: None | str | Unset = UNSET,
) -> CapTableEntryResponse | HTTPValidationError | None:
    """Add Cap Table Entry

    Args:
        snapshot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CapTableEntryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CapTableEntryResponse | HTTPValidationError
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CapTableEntryCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[CapTableEntryResponse | HTTPValidationError]:
    """Add Cap Table Entry

    Args:
        snapshot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CapTableEntryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CapTableEntryResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CapTableEntryCreate,
    authorization: None | str | Unset = UNSET,
) -> CapTableEntryResponse | HTTPValidationError | None:
    """Add Cap Table Entry

    Args:
        snapshot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CapTableEntryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CapTableEntryResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
