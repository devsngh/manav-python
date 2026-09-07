import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contract_response import ContractResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    contract_id: UUID,
    *,
    effective_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_effective_date: None | str | Unset
    if isinstance(effective_date, Unset):
        json_effective_date = UNSET
    elif isinstance(effective_date, datetime.date):
        json_effective_date = effective_date.isoformat()
    else:
        json_effective_date = effective_date
    params["effective_date"] = json_effective_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/contracts/{contract_id}/activate".format(
            contract_id=quote(str(contract_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContractResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContractResponse.from_dict(response.json())

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
) -> Response[ContractResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contract_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    effective_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractResponse | HTTPValidationError]:
    """Activate Contract

    Args:
        contract_id (UUID):
        effective_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        effective_date=effective_date,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contract_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    effective_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ContractResponse | HTTPValidationError | None:
    """Activate Contract

    Args:
        contract_id (UUID):
        effective_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractResponse | HTTPValidationError
    """

    return sync_detailed(
        contract_id=contract_id,
        client=client,
        effective_date=effective_date,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    contract_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    effective_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractResponse | HTTPValidationError]:
    """Activate Contract

    Args:
        contract_id (UUID):
        effective_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contract_id=contract_id,
        effective_date=effective_date,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contract_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    effective_date: datetime.date | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ContractResponse | HTTPValidationError | None:
    """Activate Contract

    Args:
        contract_id (UUID):
        effective_date (datetime.date | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            contract_id=contract_id,
            client=client,
            effective_date=effective_date,
            authorization=authorization,
        )
    ).parsed
