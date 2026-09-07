import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_rate_list_response import ExchangeRateListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_currency_id: None | Unset | UUID = UNSET,
    to_currency_id: None | Unset | UUID = UNSET,
    rate_type_id: None | Unset | UUID = UNSET,
    as_of: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_from_currency_id: None | str | Unset
    if isinstance(from_currency_id, Unset):
        json_from_currency_id = UNSET
    elif isinstance(from_currency_id, UUID):
        json_from_currency_id = str(from_currency_id)
    else:
        json_from_currency_id = from_currency_id
    params["from_currency_id"] = json_from_currency_id

    json_to_currency_id: None | str | Unset
    if isinstance(to_currency_id, Unset):
        json_to_currency_id = UNSET
    elif isinstance(to_currency_id, UUID):
        json_to_currency_id = str(to_currency_id)
    else:
        json_to_currency_id = to_currency_id
    params["to_currency_id"] = json_to_currency_id

    json_rate_type_id: None | str | Unset
    if isinstance(rate_type_id, Unset):
        json_rate_type_id = UNSET
    elif isinstance(rate_type_id, UUID):
        json_rate_type_id = str(rate_type_id)
    else:
        json_rate_type_id = rate_type_id
    params["rate_type_id"] = json_rate_type_id

    json_as_of: None | str | Unset
    if isinstance(as_of, Unset):
        json_as_of = UNSET
    elif isinstance(as_of, datetime.date):
        json_as_of = as_of.isoformat()
    else:
        json_as_of = as_of
    params["as_of"] = json_as_of

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/currencies/rates/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExchangeRateListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExchangeRateListResponse.from_dict(response.json())

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
) -> Response[ExchangeRateListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: None | Unset | UUID = UNSET,
    to_currency_id: None | Unset | UUID = UNSET,
    rate_type_id: None | Unset | UUID = UNSET,
    as_of: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ExchangeRateListResponse | HTTPValidationError]:
    """List Exchange Rates

     List rates with optional currency-pair + rate-type + date filtering.

    Args:
        from_currency_id (None | Unset | UUID):
        to_currency_id (None | Unset | UUID):
        rate_type_id (None | Unset | UUID):
        as_of (datetime.date | None | Unset): On or before this date
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRateListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
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
    from_currency_id: None | Unset | UUID = UNSET,
    to_currency_id: None | Unset | UUID = UNSET,
    rate_type_id: None | Unset | UUID = UNSET,
    as_of: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ExchangeRateListResponse | HTTPValidationError | None:
    """List Exchange Rates

     List rates with optional currency-pair + rate-type + date filtering.

    Args:
        from_currency_id (None | Unset | UUID):
        to_currency_id (None | Unset | UUID):
        rate_type_id (None | Unset | UUID):
        as_of (datetime.date | None | Unset): On or before this date
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRateListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: None | Unset | UUID = UNSET,
    to_currency_id: None | Unset | UUID = UNSET,
    rate_type_id: None | Unset | UUID = UNSET,
    as_of: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ExchangeRateListResponse | HTTPValidationError]:
    """List Exchange Rates

     List rates with optional currency-pair + rate-type + date filtering.

    Args:
        from_currency_id (None | Unset | UUID):
        to_currency_id (None | Unset | UUID):
        rate_type_id (None | Unset | UUID):
        as_of (datetime.date | None | Unset): On or before this date
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRateListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: None | Unset | UUID = UNSET,
    to_currency_id: None | Unset | UUID = UNSET,
    rate_type_id: None | Unset | UUID = UNSET,
    as_of: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ExchangeRateListResponse | HTTPValidationError | None:
    """List Exchange Rates

     List rates with optional currency-pair + rate-type + date filtering.

    Args:
        from_currency_id (None | Unset | UUID):
        to_currency_id (None | Unset | UUID):
        rate_type_id (None | Unset | UUID):
        as_of (datetime.date | None | Unset): On or before this date
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRateListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            from_currency_id=from_currency_id,
            to_currency_id=to_currency_id,
            rate_type_id=rate_type_id,
            as_of=as_of,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
