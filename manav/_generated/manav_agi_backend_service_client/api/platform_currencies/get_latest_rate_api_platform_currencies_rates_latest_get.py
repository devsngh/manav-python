import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exchange_rate_response import ExchangeRateResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_currency_id: UUID,
    to_currency_id: UUID,
    rate_type_id: UUID,
    as_of: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_from_currency_id = str(from_currency_id)
    params["from_currency_id"] = json_from_currency_id

    json_to_currency_id = str(to_currency_id)
    params["to_currency_id"] = json_to_currency_id

    json_rate_type_id = str(rate_type_id)
    params["rate_type_id"] = json_rate_type_id

    json_as_of: None | str | Unset
    if isinstance(as_of, Unset):
        json_as_of = UNSET
    elif isinstance(as_of, datetime.date):
        json_as_of = as_of.isoformat()
    else:
        json_as_of = as_of
    params["as_of"] = json_as_of

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/currencies/rates/latest",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExchangeRateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExchangeRateResponse.from_dict(response.json())

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
) -> Response[ExchangeRateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: UUID,
    to_currency_id: UUID,
    rate_type_id: UUID,
    as_of: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ExchangeRateResponse | HTTPValidationError]:
    """Get Latest Rate

     Most recent rate effective on or before `as_of` (default today).

    Args:
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        as_of (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: UUID,
    to_currency_id: UUID,
    rate_type_id: UUID,
    as_of: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ExchangeRateResponse | HTTPValidationError | None:
    """Get Latest Rate

     Most recent rate effective on or before `as_of` (default today).

    Args:
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        as_of (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRateResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: UUID,
    to_currency_id: UUID,
    rate_type_id: UUID,
    as_of: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ExchangeRateResponse | HTTPValidationError]:
    """Get Latest Rate

     Most recent rate effective on or before `as_of` (default today).

    Args:
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        as_of (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExchangeRateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        from_currency_id=from_currency_id,
        to_currency_id=to_currency_id,
        rate_type_id=rate_type_id,
        as_of=as_of,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_currency_id: UUID,
    to_currency_id: UUID,
    rate_type_id: UUID,
    as_of: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ExchangeRateResponse | HTTPValidationError | None:
    """Get Latest Rate

     Most recent rate effective on or before `as_of` (default today).

    Args:
        from_currency_id (UUID):
        to_currency_id (UUID):
        rate_type_id (UUID):
        as_of (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExchangeRateResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            from_currency_id=from_currency_id,
            to_currency_id=to_currency_id,
            rate_type_id=rate_type_id,
            as_of=as_of,
            authorization=authorization,
        )
    ).parsed
