import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.token_usage_time_series_response import TokenUsageTimeSeriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: None | Unset | UUID = UNSET,
    model_id: None | str | Unset = UNSET,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_model_id: None | str | Unset
    if isinstance(model_id, Unset):
        json_model_id = UNSET
    else:
        json_model_id = model_id
    params["model_id"] = json_model_id

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/analytics/token-usage",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TokenUsageTimeSeriesResponse | None:
    if response.status_code == 200:
        response_200 = TokenUsageTimeSeriesResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TokenUsageTimeSeriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    model_id: None | str | Unset = UNSET,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TokenUsageTimeSeriesResponse]:
    """Get Token Usage

     Time series: daily tokens (filterable by org, model, date range).

    Args:
        org_id (None | Unset | UUID):
        model_id (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenUsageTimeSeriesResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        model_id=model_id,
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    model_id: None | str | Unset = UNSET,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TokenUsageTimeSeriesResponse | None:
    """Get Token Usage

     Time series: daily tokens (filterable by org, model, date range).

    Args:
        org_id (None | Unset | UUID):
        model_id (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenUsageTimeSeriesResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        model_id=model_id,
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    model_id: None | str | Unset = UNSET,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TokenUsageTimeSeriesResponse]:
    """Get Token Usage

     Time series: daily tokens (filterable by org, model, date range).

    Args:
        org_id (None | Unset | UUID):
        model_id (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TokenUsageTimeSeriesResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        model_id=model_id,
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    model_id: None | str | Unset = UNSET,
    start_date: datetime.date | None | Unset = UNSET,
    end_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TokenUsageTimeSeriesResponse | None:
    """Get Token Usage

     Time series: daily tokens (filterable by org, model, date range).

    Args:
        org_id (None | Unset | UUID):
        model_id (None | str | Unset):
        start_date (datetime.date | None | Unset):
        end_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TokenUsageTimeSeriesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            model_id=model_id,
            start_date=start_date,
            end_date=end_date,
            authorization=authorization,
        )
    ).parsed
