from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.social_platform_response import SocialPlatformResponse
from ...models.social_platform_update import SocialPlatformUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    platform_id: UUID,
    *,
    body: SocialPlatformUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/platform/social-platforms/{platform_id}".format(
            platform_id=quote(str(platform_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SocialPlatformResponse | None:
    if response.status_code == 200:
        response_200 = SocialPlatformResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SocialPlatformResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    platform_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SocialPlatformUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialPlatformResponse]:
    """Update Social Platform

    Args:
        platform_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SocialPlatformUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialPlatformResponse]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    platform_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SocialPlatformUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialPlatformResponse | None:
    """Update Social Platform

    Args:
        platform_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SocialPlatformUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialPlatformResponse
    """

    return sync_detailed(
        platform_id=platform_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    platform_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SocialPlatformUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SocialPlatformResponse]:
    """Update Social Platform

    Args:
        platform_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SocialPlatformUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SocialPlatformResponse]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    platform_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SocialPlatformUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SocialPlatformResponse | None:
    """Update Social Platform

    Args:
        platform_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SocialPlatformUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SocialPlatformResponse
    """

    return (
        await asyncio_detailed(
            platform_id=platform_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
