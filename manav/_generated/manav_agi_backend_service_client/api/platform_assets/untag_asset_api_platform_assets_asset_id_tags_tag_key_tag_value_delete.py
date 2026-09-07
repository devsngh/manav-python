from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.untag_asset_api_platform_assets_asset_id_tags_tag_key_tag_value_delete_response_untag_asset_api_platform_assets_asset_id_tags_tag_key_tag_value_delete import (
    UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: UUID,
    tag_key: str,
    tag_value: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/platform/assets/{asset_id}/tags/{tag_key}/{tag_value}".format(
            asset_id=quote(str(asset_id), safe=""),
            tag_key=quote(str(tag_key), safe=""),
            tag_value=quote(str(tag_value), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
    | None
):
    if response.status_code == 200:
        response_200 = UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete.from_dict(
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
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: UUID,
    tag_key: str,
    tag_value: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
]:
    """Untag Asset

    Args:
        asset_id (UUID):
        tag_key (str):
        tag_value (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        tag_key=tag_key,
        tag_value=tag_value,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: UUID,
    tag_key: str,
    tag_value: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
    | None
):
    """Untag Asset

    Args:
        asset_id (UUID):
        tag_key (str):
        tag_value (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
    """

    return sync_detailed(
        asset_id=asset_id,
        tag_key=tag_key,
        tag_value=tag_value,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    asset_id: UUID,
    tag_key: str,
    tag_value: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
]:
    """Untag Asset

    Args:
        asset_id (UUID):
        tag_key (str):
        tag_value (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        tag_key=tag_key,
        tag_value=tag_value,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: UUID,
    tag_key: str,
    tag_value: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> (
    HTTPValidationError
    | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
    | None
):
    """Untag Asset

    Args:
        asset_id (UUID):
        tag_key (str):
        tag_value (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDeleteResponseUntagAssetApiPlatformAssetsAssetIdTagsTagKeyTagValueDelete
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            tag_key=tag_key,
            tag_value=tag_value,
            client=client,
            authorization=authorization,
        )
    ).parsed
