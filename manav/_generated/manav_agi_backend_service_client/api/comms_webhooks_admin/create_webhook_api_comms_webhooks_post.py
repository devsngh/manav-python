from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.webhook_registry_create import WebhookRegistryCreate
from ...models.webhook_secret_reveal import WebhookSecretReveal
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WebhookRegistryCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/comms/webhooks",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WebhookSecretReveal | None:
    if response.status_code == 201:
        response_201 = WebhookSecretReveal.from_dict(response.json())

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
) -> Response[HTTPValidationError | WebhookSecretReveal]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookRegistryCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WebhookSecretReveal]:
    """Create Webhook

     Create a new webhook + return the secret PLAINTEXT (shown once).

    Org resolution: super-admins (whose `user.org_id` is NULL) must pass
    `org_id` in the request body. Regular users: route uses `user.org_id`
    and ignores any `org_id` in the body (prevents cross-org spoofing).

    Args:
        authorization (None | str | Unset): Bearer token
        body (WebhookRegistryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WebhookSecretReveal]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookRegistryCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WebhookSecretReveal | None:
    """Create Webhook

     Create a new webhook + return the secret PLAINTEXT (shown once).

    Org resolution: super-admins (whose `user.org_id` is NULL) must pass
    `org_id` in the request body. Regular users: route uses `user.org_id`
    and ignores any `org_id` in the body (prevents cross-org spoofing).

    Args:
        authorization (None | str | Unset): Bearer token
        body (WebhookRegistryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WebhookSecretReveal
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookRegistryCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WebhookSecretReveal]:
    """Create Webhook

     Create a new webhook + return the secret PLAINTEXT (shown once).

    Org resolution: super-admins (whose `user.org_id` is NULL) must pass
    `org_id` in the request body. Regular users: route uses `user.org_id`
    and ignores any `org_id` in the body (prevents cross-org spoofing).

    Args:
        authorization (None | str | Unset): Bearer token
        body (WebhookRegistryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WebhookSecretReveal]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: WebhookRegistryCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WebhookSecretReveal | None:
    """Create Webhook

     Create a new webhook + return the secret PLAINTEXT (shown once).

    Org resolution: super-admins (whose `user.org_id` is NULL) must pass
    `org_id` in the request body. Regular users: route uses `user.org_id`
    and ignores any `org_id` in the body (prevents cross-org spoofing).

    Args:
        authorization (None | str | Unset): Bearer token
        body (WebhookRegistryCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WebhookSecretReveal
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
