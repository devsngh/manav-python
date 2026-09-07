from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_register import AssetRegister
from ...models.asset_response import AssetResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    parent_asset_id: UUID,
    *,
    body: AssetRegister,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/assets/{parent_asset_id}/derive".format(
            parent_asset_id=quote(str(parent_asset_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = AssetResponse.from_dict(response.json())

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
) -> Response[AssetResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    parent_asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetRegister,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetResponse | HTTPValidationError]:
    """Create Asset Derivative

     Create a new asset derived from an existing one (parent + version+1).

    Args:
        parent_asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (AssetRegister):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        parent_asset_id=parent_asset_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    parent_asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetRegister,
    authorization: None | str | Unset = UNSET,
) -> AssetResponse | HTTPValidationError | None:
    """Create Asset Derivative

     Create a new asset derived from an existing one (parent + version+1).

    Args:
        parent_asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (AssetRegister):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetResponse | HTTPValidationError
    """

    return sync_detailed(
        parent_asset_id=parent_asset_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    parent_asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetRegister,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetResponse | HTTPValidationError]:
    """Create Asset Derivative

     Create a new asset derived from an existing one (parent + version+1).

    Args:
        parent_asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (AssetRegister):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        parent_asset_id=parent_asset_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    parent_asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetRegister,
    authorization: None | str | Unset = UNSET,
) -> AssetResponse | HTTPValidationError | None:
    """Create Asset Derivative

     Create a new asset derived from an existing one (parent + version+1).

    Args:
        parent_asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (AssetRegister):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            parent_asset_id=parent_asset_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
