from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.investor_commitment_response import InvestorCommitmentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    round_id: UUID,
    *,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ir/rounds/{round_id}/commitments".format(
            round_id=quote(str(round_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[InvestorCommitmentResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = InvestorCommitmentResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[InvestorCommitmentResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[InvestorCommitmentResponse]]:
    """List Commitments For Round

    Args:
        round_id (UUID):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[InvestorCommitmentResponse]]
    """

    kwargs = _get_kwargs(
        round_id=round_id,
        status=status,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[InvestorCommitmentResponse] | None:
    """List Commitments For Round

    Args:
        round_id (UUID):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[InvestorCommitmentResponse]
    """

    return sync_detailed(
        round_id=round_id,
        client=client,
        status=status,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[InvestorCommitmentResponse]]:
    """List Commitments For Round

    Args:
        round_id (UUID):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[InvestorCommitmentResponse]]
    """

    kwargs = _get_kwargs(
        round_id=round_id,
        status=status,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[InvestorCommitmentResponse] | None:
    """List Commitments For Round

    Args:
        round_id (UUID):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[InvestorCommitmentResponse]
    """

    return (
        await asyncio_detailed(
            round_id=round_id,
            client=client,
            status=status,
            authorization=authorization,
        )
    ).parsed
