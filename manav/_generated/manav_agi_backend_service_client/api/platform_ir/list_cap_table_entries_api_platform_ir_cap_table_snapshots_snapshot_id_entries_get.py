from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cap_table_entry_response import CapTableEntryResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    snapshot_id: UUID,
    *,
    shareholder_type: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_shareholder_type: None | str | Unset
    if isinstance(shareholder_type, Unset):
        json_shareholder_type = UNSET
    else:
        json_shareholder_type = shareholder_type
    params["shareholder_type"] = json_shareholder_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ir/cap-table/snapshots/{snapshot_id}/entries".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CapTableEntryResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CapTableEntryResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[CapTableEntryResponse]]:
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
    shareholder_type: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CapTableEntryResponse]]:
    """List Cap Table Entries

     The actual cap table — entries for one snapshot, ordered by ownership_pct.

    Args:
        snapshot_id (UUID):
        shareholder_type (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CapTableEntryResponse]]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        shareholder_type=shareholder_type,
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
    shareholder_type: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CapTableEntryResponse] | None:
    """List Cap Table Entries

     The actual cap table — entries for one snapshot, ordered by ownership_pct.

    Args:
        snapshot_id (UUID):
        shareholder_type (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CapTableEntryResponse]
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        client=client,
        shareholder_type=shareholder_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    shareholder_type: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CapTableEntryResponse]]:
    """List Cap Table Entries

     The actual cap table — entries for one snapshot, ordered by ownership_pct.

    Args:
        snapshot_id (UUID):
        shareholder_type (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CapTableEntryResponse]]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        shareholder_type=shareholder_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    shareholder_type: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CapTableEntryResponse] | None:
    """List Cap Table Entries

     The actual cap table — entries for one snapshot, ordered by ownership_pct.

    Args:
        snapshot_id (UUID):
        shareholder_type (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CapTableEntryResponse]
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            client=client,
            shareholder_type=shareholder_type,
            authorization=authorization,
        )
    ).parsed
