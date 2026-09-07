from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.treasury_alert_response import TreasuryAlertResponse
from ...models.treasury_alert_update import TreasuryAlertUpdate
from ...types import Response


def _get_kwargs(
    alert_id: UUID,
    *,
    body: TreasuryAlertUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/billing/treasury-alerts/{alert_id}".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TreasuryAlertResponse | None:
    if response.status_code == 200:
        response_200 = TreasuryAlertResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TreasuryAlertResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TreasuryAlertUpdate,
) -> Response[HTTPValidationError | TreasuryAlertResponse]:
    """Update Treasury Alert

    Args:
        alert_id (UUID):
        body (TreasuryAlertUpdate): Patch — lifecycle transitions + retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TreasuryAlertResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TreasuryAlertUpdate,
) -> HTTPValidationError | TreasuryAlertResponse | None:
    """Update Treasury Alert

    Args:
        alert_id (UUID):
        body (TreasuryAlertUpdate): Patch — lifecycle transitions + retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TreasuryAlertResponse
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    alert_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TreasuryAlertUpdate,
) -> Response[HTTPValidationError | TreasuryAlertResponse]:
    """Update Treasury Alert

    Args:
        alert_id (UUID):
        body (TreasuryAlertUpdate): Patch — lifecycle transitions + retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TreasuryAlertResponse]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TreasuryAlertUpdate,
) -> HTTPValidationError | TreasuryAlertResponse | None:
    """Update Treasury Alert

    Args:
        alert_id (UUID):
        body (TreasuryAlertUpdate): Patch — lifecycle transitions + retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TreasuryAlertResponse
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
            body=body,
        )
    ).parsed
