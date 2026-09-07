from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.currency_response import CurrencyResponse
from ...models.currency_update import CurrencyUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    currency_id: UUID,
    *,
    body: CurrencyUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/platform/currencies/{currency_id}".format(
            currency_id=quote(str(currency_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CurrencyResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CurrencyResponse.from_dict(response.json())

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
) -> Response[CurrencyResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    currency_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CurrencyUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CurrencyResponse | HTTPValidationError]:
    """Update Currency

     Update currency fields.

    Args:
        currency_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CurrencyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrencyResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        currency_id=currency_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    currency_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CurrencyUpdate,
    authorization: None | str | Unset = UNSET,
) -> CurrencyResponse | HTTPValidationError | None:
    """Update Currency

     Update currency fields.

    Args:
        currency_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CurrencyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrencyResponse | HTTPValidationError
    """

    return sync_detailed(
        currency_id=currency_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    currency_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CurrencyUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CurrencyResponse | HTTPValidationError]:
    """Update Currency

     Update currency fields.

    Args:
        currency_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CurrencyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CurrencyResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        currency_id=currency_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    currency_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CurrencyUpdate,
    authorization: None | str | Unset = UNSET,
) -> CurrencyResponse | HTTPValidationError | None:
    """Update Currency

     Update currency fields.

    Args:
        currency_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CurrencyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CurrencyResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            currency_id=currency_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
