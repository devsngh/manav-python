from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_list_response import AssetListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_type: None | str | Unset = UNSET,
    asset_role: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    visibility: None | str | Unset = UNSET,
    created_by_bot_id: None | Unset | UUID = UNSET,
    created_by_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_asset_type: None | str | Unset
    if isinstance(asset_type, Unset):
        json_asset_type = UNSET
    else:
        json_asset_type = asset_type
    params["asset_type"] = json_asset_type

    json_asset_role: None | str | Unset
    if isinstance(asset_role, Unset):
        json_asset_role = UNSET
    else:
        json_asset_role = asset_role
    params["asset_role"] = json_asset_role

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    else:
        json_source = source
    params["source"] = json_source

    json_visibility: None | str | Unset
    if isinstance(visibility, Unset):
        json_visibility = UNSET
    else:
        json_visibility = visibility
    params["visibility"] = json_visibility

    json_created_by_bot_id: None | str | Unset
    if isinstance(created_by_bot_id, Unset):
        json_created_by_bot_id = UNSET
    elif isinstance(created_by_bot_id, UUID):
        json_created_by_bot_id = str(created_by_bot_id)
    else:
        json_created_by_bot_id = created_by_bot_id
    params["created_by_bot_id"] = json_created_by_bot_id

    json_created_by_user_id: None | str | Unset
    if isinstance(created_by_user_id, Unset):
        json_created_by_user_id = UNSET
    elif isinstance(created_by_user_id, UUID):
        json_created_by_user_id = str(created_by_user_id)
    else:
        json_created_by_user_id = created_by_user_id
    params["created_by_user_id"] = json_created_by_user_id

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/assets",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssetListResponse.from_dict(response.json())

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
) -> Response[AssetListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_type: None | str | Unset = UNSET,
    asset_role: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    visibility: None | str | Unset = UNSET,
    created_by_bot_id: None | Unset | UUID = UNSET,
    created_by_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetListResponse | HTTPValidationError]:
    """List Assets

    Args:
        asset_type (None | str | Unset):
        asset_role (None | str | Unset):
        status (None | str | Unset):
        source (None | str | Unset):
        visibility (None | str | Unset):
        created_by_bot_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        asset_role=asset_role,
        status=status,
        source=source,
        visibility=visibility,
        created_by_bot_id=created_by_bot_id,
        created_by_user_id=created_by_user_id,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    asset_type: None | str | Unset = UNSET,
    asset_role: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    visibility: None | str | Unset = UNSET,
    created_by_bot_id: None | Unset | UUID = UNSET,
    created_by_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AssetListResponse | HTTPValidationError | None:
    """List Assets

    Args:
        asset_type (None | str | Unset):
        asset_role (None | str | Unset):
        status (None | str | Unset):
        source (None | str | Unset):
        visibility (None | str | Unset):
        created_by_bot_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        asset_type=asset_type,
        asset_role=asset_role,
        status=status,
        source=source,
        visibility=visibility,
        created_by_bot_id=created_by_bot_id,
        created_by_user_id=created_by_user_id,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    asset_type: None | str | Unset = UNSET,
    asset_role: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    visibility: None | str | Unset = UNSET,
    created_by_bot_id: None | Unset | UUID = UNSET,
    created_by_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetListResponse | HTTPValidationError]:
    """List Assets

    Args:
        asset_type (None | str | Unset):
        asset_role (None | str | Unset):
        status (None | str | Unset):
        source (None | str | Unset):
        visibility (None | str | Unset):
        created_by_bot_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        asset_role=asset_role,
        status=status,
        source=source,
        visibility=visibility,
        created_by_bot_id=created_by_bot_id,
        created_by_user_id=created_by_user_id,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    asset_type: None | str | Unset = UNSET,
    asset_role: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    visibility: None | str | Unset = UNSET,
    created_by_bot_id: None | Unset | UUID = UNSET,
    created_by_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AssetListResponse | HTTPValidationError | None:
    """List Assets

    Args:
        asset_type (None | str | Unset):
        asset_role (None | str | Unset):
        status (None | str | Unset):
        source (None | str | Unset):
        visibility (None | str | Unset):
        created_by_bot_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type=asset_type,
            asset_role=asset_role,
            status=status,
            source=source,
            visibility=visibility,
            created_by_bot_id=created_by_bot_id,
            created_by_user_id=created_by_user_id,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
