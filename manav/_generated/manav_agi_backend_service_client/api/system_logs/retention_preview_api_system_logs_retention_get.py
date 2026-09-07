from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.retention_preview_response import RetentionPreviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    retention_days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["retention_days"] = retention_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/system-logs/retention",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RetentionPreviewResponse | None:
    if response.status_code == 200:
        response_200 = RetentionPreviewResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | RetentionPreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    retention_days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RetentionPreviewResponse]:
    """Retention Preview

     Preview: how many logs would be purged at given retention period.

    Args:
        retention_days (int | Unset): Retention period in days Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RetentionPreviewResponse]
    """

    kwargs = _get_kwargs(
        retention_days=retention_days,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    retention_days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RetentionPreviewResponse | None:
    """Retention Preview

     Preview: how many logs would be purged at given retention period.

    Args:
        retention_days (int | Unset): Retention period in days Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RetentionPreviewResponse
    """

    return sync_detailed(
        client=client,
        retention_days=retention_days,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    retention_days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RetentionPreviewResponse]:
    """Retention Preview

     Preview: how many logs would be purged at given retention period.

    Args:
        retention_days (int | Unset): Retention period in days Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RetentionPreviewResponse]
    """

    kwargs = _get_kwargs(
        retention_days=retention_days,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    retention_days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RetentionPreviewResponse | None:
    """Retention Preview

     Preview: how many logs would be purged at given retention period.

    Args:
        retention_days (int | Unset): Retention period in days Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RetentionPreviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            retention_days=retention_days,
            authorization=authorization,
        )
    ).parsed
