from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.waah_response import WaahResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    weeks: int | Unset = 12,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["weeks"] = weeks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/analytics/waah",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WaahResponse | None:
    if response.status_code == 200:
        response_200 = WaahResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WaahResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    weeks: int | Unset = 12,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WaahResponse]:
    """Get Waah

     Weekly Active Agent-Hours — sum of completed-task durations, weekly buckets.

    Args:
        weeks (int | Unset):  Default: 12.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WaahResponse]
    """

    kwargs = _get_kwargs(
        weeks=weeks,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    weeks: int | Unset = 12,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WaahResponse | None:
    """Get Waah

     Weekly Active Agent-Hours — sum of completed-task durations, weekly buckets.

    Args:
        weeks (int | Unset):  Default: 12.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WaahResponse
    """

    return sync_detailed(
        client=client,
        weeks=weeks,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    weeks: int | Unset = 12,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WaahResponse]:
    """Get Waah

     Weekly Active Agent-Hours — sum of completed-task durations, weekly buckets.

    Args:
        weeks (int | Unset):  Default: 12.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WaahResponse]
    """

    kwargs = _get_kwargs(
        weeks=weeks,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    weeks: int | Unset = 12,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WaahResponse | None:
    """Get Waah

     Weekly Active Agent-Hours — sum of completed-task durations, weekly buckets.

    Args:
        weeks (int | Unset):  Default: 12.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WaahResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            weeks=weeks,
            authorization=authorization,
        )
    ).parsed
