from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.count_recent_competitor_signals_api_platform_competitors_competitor_id_signals_count_get_response_count_recent_competitor_signals_api_platform_competitors_competitor_id_signals_count_get import (
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet,
)
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
        "url": "/api/platform/competitors/{competitor_id}/signals/count".format(
            competitor_id=quote(str(competitor_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
    | None
):
    if response.status_code == 200:
        response_200 = CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet.from_dict(
            response.json()
        )

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
) -> Response[
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
]:
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
) -> Response[
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
]:
    """Count Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet | HTTPValidationError]
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
) -> (
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
    | None
):
    """Count Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet | HTTPValidationError
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
) -> Response[
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
]:
    """Count Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet | HTTPValidationError]
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
) -> (
    CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet
    | HTTPValidationError
    | None
):
    """Count Recent Competitor Signals

    Args:
        competitor_id (UUID):
        days (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGetResponseCountRecentCompetitorSignalsApiPlatformCompetitorsCompetitorIdSignalsCountGet | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            competitor_id=competitor_id,
            client=client,
            days=days,
            authorization=authorization,
        )
    ).parsed
