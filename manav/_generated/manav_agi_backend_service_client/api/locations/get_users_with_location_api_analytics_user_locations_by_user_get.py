from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.users_with_location_response import UsersWithLocationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/analytics/user-locations/by-user",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UsersWithLocationResponse | None:
    if response.status_code == 200:
        response_200 = UsersWithLocationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UsersWithLocationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UsersWithLocationResponse]:
    """Get Users With Location

     One row per user: their current (most recent) login location +
    total login count + full history array. Powers the user-centric
    table where each row is expandable to reveal that user's history
    without a second network call.

    Args:
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsersWithLocationResponse]
    """

    kwargs = _get_kwargs(
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
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UsersWithLocationResponse | None:
    """Get Users With Location

     One row per user: their current (most recent) login location +
    total login count + full history array. Powers the user-centric
    table where each row is expandable to reveal that user's history
    without a second network call.

    Args:
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsersWithLocationResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UsersWithLocationResponse]:
    """Get Users With Location

     One row per user: their current (most recent) login location +
    total login count + full history array. Powers the user-centric
    table where each row is expandable to reveal that user's history
    without a second network call.

    Args:
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsersWithLocationResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 200,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UsersWithLocationResponse | None:
    """Get Users With Location

     One row per user: their current (most recent) login location +
    total login count + full history array. Powers the user-centric
    table where each row is expandable to reveal that user's history
    without a second network call.

    Args:
        limit (int | Unset):  Default: 200.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsersWithLocationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
