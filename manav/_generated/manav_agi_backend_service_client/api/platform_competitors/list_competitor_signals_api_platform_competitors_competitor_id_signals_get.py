import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.competitor_signal_list_response import CompetitorSignalListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    competitor_id: UUID,
    *,
    signal_type: None | str | Unset = UNSET,
    detected_in_dept: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_signal_type: None | str | Unset
    if isinstance(signal_type, Unset):
        json_signal_type = UNSET
    else:
        json_signal_type = signal_type
    params["signal_type"] = json_signal_type

    json_detected_in_dept: None | str | Unset
    if isinstance(detected_in_dept, Unset):
        json_detected_in_dept = UNSET
    else:
        json_detected_in_dept = detected_in_dept
    params["detected_in_dept"] = json_detected_in_dept

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/competitors/{competitor_id}/signals".format(
            competitor_id=quote(str(competitor_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompetitorSignalListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CompetitorSignalListResponse.from_dict(response.json())

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
) -> Response[CompetitorSignalListResponse | HTTPValidationError]:
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
    signal_type: None | str | Unset = UNSET,
    detected_in_dept: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CompetitorSignalListResponse | HTTPValidationError]:
    """List Competitor Signals

    Args:
        competitor_id (UUID):
        signal_type (None | str | Unset):
        detected_in_dept (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitorSignalListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        competitor_id=competitor_id,
        signal_type=signal_type,
        detected_in_dept=detected_in_dept,
        since=since,
        page=page,
        page_size=page_size,
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
    signal_type: None | str | Unset = UNSET,
    detected_in_dept: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CompetitorSignalListResponse | HTTPValidationError | None:
    """List Competitor Signals

    Args:
        competitor_id (UUID):
        signal_type (None | str | Unset):
        detected_in_dept (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitorSignalListResponse | HTTPValidationError
    """

    return sync_detailed(
        competitor_id=competitor_id,
        client=client,
        signal_type=signal_type,
        detected_in_dept=detected_in_dept,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    signal_type: None | str | Unset = UNSET,
    detected_in_dept: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CompetitorSignalListResponse | HTTPValidationError]:
    """List Competitor Signals

    Args:
        competitor_id (UUID):
        signal_type (None | str | Unset):
        detected_in_dept (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitorSignalListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        competitor_id=competitor_id,
        signal_type=signal_type,
        detected_in_dept=detected_in_dept,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    competitor_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    signal_type: None | str | Unset = UNSET,
    detected_in_dept: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CompetitorSignalListResponse | HTTPValidationError | None:
    """List Competitor Signals

    Args:
        competitor_id (UUID):
        signal_type (None | str | Unset):
        detected_in_dept (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitorSignalListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            competitor_id=competitor_id,
            client=client,
            signal_type=signal_type,
            detected_in_dept=detected_in_dept,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
