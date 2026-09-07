from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    webhook_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/webhooks/{webhook_id}".format(
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 202:
        response_202 = response.json()
        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    """Receive Webhook

     Generic webhook dispatcher.

    Steps:
      1. Look up webhook_registry by webhook_id (must exist + status=active)
      2. Verify HMAC signature
      3. Enforce max payload size + rate limits (best-effort)
      4. Resolve handler from HANDLERS registry by category
      5. Dispatch — handler returns a status dict
      6. Update counters, return 202 with the handler result

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    """Receive Webhook

     Generic webhook dispatcher.

    Steps:
      1. Look up webhook_registry by webhook_id (must exist + status=active)
      2. Verify HMAC signature
      3. Enforce max payload size + rate limits (best-effort)
      4. Resolve handler from HANDLERS registry by category
      5. Dispatch — handler returns a status dict
      6. Update counters, return 202 with the handler result

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | HTTPValidationError]:
    """Receive Webhook

     Generic webhook dispatcher.

    Steps:
      1. Look up webhook_registry by webhook_id (must exist + status=active)
      2. Verify HMAC signature
      3. Enforce max payload size + rate limits (best-effort)
      4. Resolve handler from HANDLERS registry by category
      5. Dispatch — handler returns a status dict
      6. Update counters, return 202 with the handler result

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    webhook_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Any | HTTPValidationError | None:
    """Receive Webhook

     Generic webhook dispatcher.

    Steps:
      1. Look up webhook_registry by webhook_id (must exist + status=active)
      2. Verify HMAC signature
      3. Enforce max payload size + rate limits (best-effort)
      4. Resolve handler from HANDLERS registry by category
      5. Dispatch — handler returns a status dict
      6. Update counters, return 202 with the handler result

    Args:
        webhook_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
