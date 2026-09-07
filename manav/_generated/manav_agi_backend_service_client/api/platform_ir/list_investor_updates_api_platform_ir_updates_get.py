import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.investor_update_list_response import InvestorUpdateListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    period_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_period_type: None | str | Unset
    if isinstance(period_type, Unset):
        json_period_type = UNSET
    else:
        json_period_type = period_type
    params["period_type"] = json_period_type

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.date):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ir/updates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InvestorUpdateListResponse | None:
    if response.status_code == 200:
        response_200 = InvestorUpdateListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | InvestorUpdateListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorUpdateListResponse]:
    """List Investor Updates

    Args:
        period_type (None | str | Unset):
        status (None | str | Unset):
        since (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorUpdateListResponse]
    """

    kwargs = _get_kwargs(
        period_type=period_type,
        status=status,
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
    *,
    client: AuthenticatedClient | Client,
    period_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorUpdateListResponse | None:
    """List Investor Updates

    Args:
        period_type (None | str | Unset):
        status (None | str | Unset):
        since (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorUpdateListResponse
    """

    return sync_detailed(
        client=client,
        period_type=period_type,
        status=status,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    period_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorUpdateListResponse]:
    """List Investor Updates

    Args:
        period_type (None | str | Unset):
        status (None | str | Unset):
        since (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorUpdateListResponse]
    """

    kwargs = _get_kwargs(
        period_type=period_type,
        status=status,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    period_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorUpdateListResponse | None:
    """List Investor Updates

    Args:
        period_type (None | str | Unset):
        status (None | str | Unset):
        since (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorUpdateListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            period_type=period_type,
            status=status,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
