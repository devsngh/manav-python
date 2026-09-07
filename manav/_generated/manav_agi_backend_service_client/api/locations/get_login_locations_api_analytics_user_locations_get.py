import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location_list_response import LocationListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    elif isinstance(start_date, datetime.date):
        json_start_date = start_date.isoformat()
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    elif isinstance(end_date, datetime.date):
        json_end_date = end_date.isoformat()
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/analytics/user-locations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LocationListResponse | None:
    if response.status_code == 200:
        response_200 = LocationListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LocationListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LocationListResponse]:
    """Get Login Locations

     Return recent login-location markers (newest first).

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationListResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LocationListResponse | None:
    """Get Login Locations

     Return recent login-location markers (newest first).

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationListResponse
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LocationListResponse]:
    """Get Login Locations

     Return recent login-location markers (newest first).

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationListResponse]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LocationListResponse | None:
    """Get Login Locations

     Return recent login-location markers (newest first).

    Args:
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
