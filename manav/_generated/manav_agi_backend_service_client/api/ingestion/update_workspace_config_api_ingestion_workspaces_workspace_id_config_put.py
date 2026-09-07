from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ingestion_config_response import IngestionConfigResponse
from ...models.ingestion_config_update import IngestionConfigUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: str,
    *,
    body: IngestionConfigUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/ingestion/workspaces/{workspace_id}/config".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | IngestionConfigResponse | None:
    if response.status_code == 200:
        response_200 = IngestionConfigResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | IngestionConfigResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IngestionConfigUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IngestionConfigResponse]:
    """Update Workspace Config

     Update ingestion pipeline config for a workspace (PATCH semantics — only provided fields change).

    Args:
        workspace_id (str):
        authorization (None | str | Unset): Bearer token
        body (IngestionConfigUpdate): All fields optional — partial update (PATCH semantics via
            PUT).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IngestionConfigResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IngestionConfigUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | IngestionConfigResponse | None:
    """Update Workspace Config

     Update ingestion pipeline config for a workspace (PATCH semantics — only provided fields change).

    Args:
        workspace_id (str):
        authorization (None | str | Unset): Bearer token
        body (IngestionConfigUpdate): All fields optional — partial update (PATCH semantics via
            PUT).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IngestionConfigResponse
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IngestionConfigUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IngestionConfigResponse]:
    """Update Workspace Config

     Update ingestion pipeline config for a workspace (PATCH semantics — only provided fields change).

    Args:
        workspace_id (str):
        authorization (None | str | Unset): Bearer token
        body (IngestionConfigUpdate): All fields optional — partial update (PATCH semantics via
            PUT).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IngestionConfigResponse]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IngestionConfigUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | IngestionConfigResponse | None:
    """Update Workspace Config

     Update ingestion pipeline config for a workspace (PATCH semantics — only provided fields change).

    Args:
        workspace_id (str):
        authorization (None | str | Unset): Bearer token
        body (IngestionConfigUpdate): All fields optional — partial update (PATCH semantics via
            PUT).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IngestionConfigResponse
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
