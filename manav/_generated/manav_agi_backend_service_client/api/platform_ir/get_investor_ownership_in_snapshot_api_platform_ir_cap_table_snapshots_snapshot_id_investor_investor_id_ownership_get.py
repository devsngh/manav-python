from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_investor_ownership_in_snapshot_api_platform_ir_cap_table_snapshots_snapshot_id_investor_investor_id_ownership_get_response_get_investor_ownership_in_snapshot_api_platform_ir_cap_table_snapshots_snapshot_id_investor_investor_id_ownership_get import (
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    snapshot_id: UUID,
    investor_id: UUID,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ir/cap-table/snapshots/{snapshot_id}/investor/{investor_id}/ownership".format(
            snapshot_id=quote(str(snapshot_id), safe=""),
            investor_id=quote(str(investor_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet.from_dict(
            response.json()
        )

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
) -> Response[
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    snapshot_id: UUID,
    investor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
]:
    """Get Investor Ownership In Snapshot

    Args:
        snapshot_id (UUID):
        investor_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        investor_id=investor_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    snapshot_id: UUID,
    investor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> (
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
    | None
):
    """Get Investor Ownership In Snapshot

    Args:
        snapshot_id (UUID):
        investor_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet | HTTPValidationError
    """

    return sync_detailed(
        snapshot_id=snapshot_id,
        investor_id=investor_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    snapshot_id: UUID,
    investor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
]:
    """Get Investor Ownership In Snapshot

    Args:
        snapshot_id (UUID):
        investor_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        snapshot_id=snapshot_id,
        investor_id=investor_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    snapshot_id: UUID,
    investor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> (
    GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet
    | HTTPValidationError
    | None
):
    """Get Investor Ownership In Snapshot

    Args:
        snapshot_id (UUID):
        investor_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGetResponseGetInvestorOwnershipInSnapshotApiPlatformIrCapTableSnapshotsSnapshotIdInvestorInvestorIdOwnershipGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            snapshot_id=snapshot_id,
            investor_id=investor_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
