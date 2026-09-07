from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.social_platform_list_response import SocialPlatformListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    api_available: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    json_api_available: bool | None | Unset
    if isinstance(api_available, Unset):
        json_api_available = UNSET
    else:
        json_api_available = api_available
    params["api_available"] = json_api_available

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/social-platforms",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SocialPlatformListResponse | None:
    if response.status_code == 200:
        response_200 = SocialPlatformListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SocialPlatformListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    api_available: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialPlatformListResponse]:
    """List Social Platforms

     Open to any authenticated user — agents need this to validate posts.

    Args:
        category (None | str | Unset):
        is_active (bool | None | Unset):
        api_available (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialPlatformListResponse]
    """

    kwargs = _get_kwargs(
        category=category,
        is_active=is_active,
        api_available=api_available,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    api_available: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialPlatformListResponse | None:
    """List Social Platforms

     Open to any authenticated user — agents need this to validate posts.

    Args:
        category (None | str | Unset):
        is_active (bool | None | Unset):
        api_available (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialPlatformListResponse
    """

    return sync_detailed(
        client=client,
        category=category,
        is_active=is_active,
        api_available=api_available,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    api_available: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialPlatformListResponse]:
    """List Social Platforms

     Open to any authenticated user — agents need this to validate posts.

    Args:
        category (None | str | Unset):
        is_active (bool | None | Unset):
        api_available (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialPlatformListResponse]
    """

    kwargs = _get_kwargs(
        category=category,
        is_active=is_active,
        api_available=api_available,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    is_active: bool | None | Unset = UNSET,
    api_available: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialPlatformListResponse | None:
    """List Social Platforms

     Open to any authenticated user — agents need this to validate posts.

    Args:
        category (None | str | Unset):
        is_active (bool | None | Unset):
        api_available (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialPlatformListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            is_active=is_active,
            api_available=api_available,
            authorization=authorization,
        )
    ).parsed
