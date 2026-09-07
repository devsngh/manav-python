from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.social_account_list_response import SocialAccountListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    platform: None | str | Unset = UNSET,
    account_purpose: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_platform: None | str | Unset
    if isinstance(platform, Unset):
        json_platform = UNSET
    else:
        json_platform = platform
    params["platform"] = json_platform

    json_account_purpose: None | str | Unset
    if isinstance(account_purpose, Unset):
        json_account_purpose = UNSET
    else:
        json_account_purpose = account_purpose
    params["account_purpose"] = json_account_purpose

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    json_is_verified: bool | None | Unset
    if isinstance(is_verified, Unset):
        json_is_verified = UNSET
    else:
        json_is_verified = is_verified
    params["is_verified"] = json_is_verified

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/social-accounts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SocialAccountListResponse | None:
    if response.status_code == 200:
        response_200 = SocialAccountListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SocialAccountListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: None | str | Unset = UNSET,
    account_purpose: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialAccountListResponse]:
    """List Social Accounts

    Args:
        platform (None | str | Unset):
        account_purpose (None | str | Unset):
        is_active (bool | None | Unset):
        is_verified (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialAccountListResponse]
    """

    kwargs = _get_kwargs(
        platform=platform,
        account_purpose=account_purpose,
        is_active=is_active,
        is_verified=is_verified,
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
    platform: None | str | Unset = UNSET,
    account_purpose: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialAccountListResponse | None:
    """List Social Accounts

    Args:
        platform (None | str | Unset):
        account_purpose (None | str | Unset):
        is_active (bool | None | Unset):
        is_verified (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialAccountListResponse
    """

    return sync_detailed(
        client=client,
        platform=platform,
        account_purpose=account_purpose,
        is_active=is_active,
        is_verified=is_verified,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: None | str | Unset = UNSET,
    account_purpose: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialAccountListResponse]:
    """List Social Accounts

    Args:
        platform (None | str | Unset):
        account_purpose (None | str | Unset):
        is_active (bool | None | Unset):
        is_verified (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialAccountListResponse]
    """

    kwargs = _get_kwargs(
        platform=platform,
        account_purpose=account_purpose,
        is_active=is_active,
        is_verified=is_verified,
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
    platform: None | str | Unset = UNSET,
    account_purpose: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    is_verified: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialAccountListResponse | None:
    """List Social Accounts

    Args:
        platform (None | str | Unset):
        account_purpose (None | str | Unset):
        is_active (bool | None | Unset):
        is_verified (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialAccountListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            platform=platform,
            account_purpose=account_purpose,
            is_active=is_active,
            is_verified=is_verified,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
