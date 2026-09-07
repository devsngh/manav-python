from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.world_sync_response import WorldSyncResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/agents/world/sync-to-workspace",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WorldSyncResponse | None:
    if response.status_code == 200:
        response_200 = WorldSyncResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WorldSyncResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorldSyncResponse]:
    """Sync World To Workspace

     Sync world_db reference data (countries + cities + industries) into the
    world_global Vespa workspace.

    Reads structured rows from world_db, builds NL descriptions, UPSERTs
    ingestion_documents + ingestion_entities in the world_global workspace.
    Idempotent — safe to re-run after world_db is refreshed.

    Run sequence at fresh-bootstrap time:
      1. master_seed (loads YAMLs into world_db via world_data cluster)
      2. POST /api/agents/world/sync-to-workspace (this endpoint)
      3. World data is now retrievable via the world_global workspace

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorldSyncResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorldSyncResponse | None:
    """Sync World To Workspace

     Sync world_db reference data (countries + cities + industries) into the
    world_global Vespa workspace.

    Reads structured rows from world_db, builds NL descriptions, UPSERTs
    ingestion_documents + ingestion_entities in the world_global workspace.
    Idempotent — safe to re-run after world_db is refreshed.

    Run sequence at fresh-bootstrap time:
      1. master_seed (loads YAMLs into world_db via world_data cluster)
      2. POST /api/agents/world/sync-to-workspace (this endpoint)
      3. World data is now retrievable via the world_global workspace

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorldSyncResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorldSyncResponse]:
    """Sync World To Workspace

     Sync world_db reference data (countries + cities + industries) into the
    world_global Vespa workspace.

    Reads structured rows from world_db, builds NL descriptions, UPSERTs
    ingestion_documents + ingestion_entities in the world_global workspace.
    Idempotent — safe to re-run after world_db is refreshed.

    Run sequence at fresh-bootstrap time:
      1. master_seed (loads YAMLs into world_db via world_data cluster)
      2. POST /api/agents/world/sync-to-workspace (this endpoint)
      3. World data is now retrievable via the world_global workspace

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorldSyncResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorldSyncResponse | None:
    """Sync World To Workspace

     Sync world_db reference data (countries + cities + industries) into the
    world_global Vespa workspace.

    Reads structured rows from world_db, builds NL descriptions, UPSERTs
    ingestion_documents + ingestion_entities in the world_global workspace.
    Idempotent — safe to re-run after world_db is refreshed.

    Run sequence at fresh-bootstrap time:
      1. master_seed (loads YAMLs into world_db via world_data cluster)
      2. POST /api/agents/world/sync-to-workspace (this endpoint)
      3. World data is now retrievable via the world_global workspace

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorldSyncResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
