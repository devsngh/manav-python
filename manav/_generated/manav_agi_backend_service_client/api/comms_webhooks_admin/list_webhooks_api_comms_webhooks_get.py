from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.webhook_registry_read import WebhookRegistryRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    org_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
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

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/comms/webhooks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[WebhookRegistryRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebhookRegistryRead.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[WebhookRegistryRead]]:
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
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    org_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[WebhookRegistryRead]]:
    """List Webhooks

    Args:
        category (None | str | Unset):
        provider (None | str | Unset):
        status (None | str | Unset):
        org_id (None | Unset | UUID): Super-admin org override; ignored for regular users
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[WebhookRegistryRead]]
    """

    kwargs = _get_kwargs(
        category=category,
        provider=provider,
        status=status,
        org_id=org_id,
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
    category: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    org_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[WebhookRegistryRead] | None:
    """List Webhooks

    Args:
        category (None | str | Unset):
        provider (None | str | Unset):
        status (None | str | Unset):
        org_id (None | Unset | UUID): Super-admin org override; ignored for regular users
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[WebhookRegistryRead]
    """

    return sync_detailed(
        client=client,
        category=category,
        provider=provider,
        status=status,
        org_id=org_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    org_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[WebhookRegistryRead]]:
    """List Webhooks

    Args:
        category (None | str | Unset):
        provider (None | str | Unset):
        status (None | str | Unset):
        org_id (None | Unset | UUID): Super-admin org override; ignored for regular users
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[WebhookRegistryRead]]
    """

    kwargs = _get_kwargs(
        category=category,
        provider=provider,
        status=status,
        org_id=org_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    org_id: None | Unset | UUID = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[WebhookRegistryRead] | None:
    """List Webhooks

    Args:
        category (None | str | Unset):
        provider (None | str | Unset):
        status (None | str | Unset):
        org_id (None | Unset | UUID): Super-admin org override; ignored for regular users
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[WebhookRegistryRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            provider=provider,
            status=status,
            org_id=org_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
