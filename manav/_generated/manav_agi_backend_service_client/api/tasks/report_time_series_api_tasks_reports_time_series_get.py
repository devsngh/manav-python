from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_by: str | Unset = "week",
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["group_by"] = group_by

    json_date_from: None | str | Unset
    if isinstance(date_from, Unset):
        json_date_from = UNSET
    else:
        json_date_from = date_from
    params["date_from"] = json_date_from

    json_date_to: None | str | Unset
    if isinstance(date_to, Unset):
        json_date_to = UNSET
    else:
        json_date_to = date_to
    params["date_to"] = json_date_to

    json_period: None | str | Unset
    if isinstance(period, Unset):
        json_period = UNSET
    else:
        json_period = period
    params["period"] = json_period

    json_department_id: None | str | Unset
    if isinstance(department_id, Unset):
        json_department_id = UNSET
    elif isinstance(department_id, UUID):
        json_department_id = str(department_id)
    else:
        json_department_id = department_id
    params["department_id"] = json_department_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/reports/time-series",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = "week",
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Report Time Series

    Args:
        group_by (str | Unset):  Default: 'week'.
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        group_by=group_by,
        date_from=date_from,
        date_to=date_to,
        period=period,
        department_id=department_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = "week",
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Report Time Series

    Args:
        group_by (str | Unset):  Default: 'week'.
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        group_by=group_by,
        date_from=date_from,
        date_to=date_to,
        period=period,
        department_id=department_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = "week",
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Report Time Series

    Args:
        group_by (str | Unset):  Default: 'week'.
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        group_by=group_by,
        date_from=date_from,
        date_to=date_to,
        period=period,
        department_id=department_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_by: str | Unset = "week",
    date_from: None | str | Unset = UNSET,
    date_to: None | str | Unset = UNSET,
    period: None | str | Unset = UNSET,
    department_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Report Time Series

    Args:
        group_by (str | Unset):  Default: 'week'.
        date_from (None | str | Unset):
        date_to (None | str | Unset):
        period (None | str | Unset):
        department_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            group_by=group_by,
            date_from=date_from,
            date_to=date_to,
            period=period,
            department_id=department_id,
            authorization=authorization,
        )
    ).parsed
