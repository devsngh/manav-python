from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.banner_response import BannerResponse
from ...models.body_admin_upload_banner_image_api_marketplace_admin_banners_banner_id_image_post import (
    BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    banner_id: UUID,
    *,
    body: BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/marketplace/admin/banners/{banner_id}/image".format(
            banner_id=quote(str(banner_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BannerResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BannerResponse.from_dict(response.json())

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
) -> Response[BannerResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    banner_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
    authorization: None | str | Unset = UNSET,
) -> Response[BannerResponse | HTTPValidationError]:
    """Admin Upload Banner Image

    Args:
        banner_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BannerResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        banner_id=banner_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    banner_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
    authorization: None | str | Unset = UNSET,
) -> BannerResponse | HTTPValidationError | None:
    """Admin Upload Banner Image

    Args:
        banner_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BannerResponse | HTTPValidationError
    """

    return sync_detailed(
        banner_id=banner_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    banner_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
    authorization: None | str | Unset = UNSET,
) -> Response[BannerResponse | HTTPValidationError]:
    """Admin Upload Banner Image

    Args:
        banner_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BannerResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        banner_id=banner_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    banner_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost,
    authorization: None | str | Unset = UNSET,
) -> BannerResponse | HTTPValidationError | None:
    """Admin Upload Banner Image

    Args:
        banner_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BodyAdminUploadBannerImageApiMarketplaceAdminBannersBannerIdImagePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BannerResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            banner_id=banner_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
