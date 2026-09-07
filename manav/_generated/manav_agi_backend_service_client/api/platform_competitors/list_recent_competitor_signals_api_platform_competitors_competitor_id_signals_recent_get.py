from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.competitor_signal_response import CompetitorSignalResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    competitor_id: UUID,
    *,
    days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/competitors/{competitor_id}/signals/recent".format(
            competitor_id=quote(str(competitor_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CompetitorSignalResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CompetitorSignalResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[CompetitorSignalResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CompetitorSignalResponse]]:
    """List Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CompetitorSignalResponse]]
    """

    kwargs = _get_kwargs(
        competitor_id=competitor_id,
        days=days,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CompetitorSignalResponse] | None:
    """List Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CompetitorSignalResponse]
    """

    return sync_detailed(
        competitor_id=competitor_id,
        client=client,
        days=days,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CompetitorSignalResponse]]:
    """List Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CompetitorSignalResponse]]
    """

    kwargs = _get_kwargs(
        competitor_id=competitor_id,
        days=days,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    days: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CompetitorSignalResponse] | None:
    """List Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CompetitorSignalResponse]
    """

    return (
        await asyncio_detailed(
            competitor_id=competitor_id,
            client=client,
            days=days,
            authorization=authorization,
        )
    ).parsed
