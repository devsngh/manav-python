from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.investor_commitment_create import InvestorCommitmentCreate
from ...models.investor_commitment_response import InvestorCommitmentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    round_id: UUID,
    *,
    body: InvestorCommitmentCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/ir/rounds/{round_id}/commitments".format(
            round_id=quote(str(round_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    if response.status_code == 201:
        response_201 = InvestorCommitmentResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
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
    body: InvestorCommitmentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
    """Create Commitment

    Args:
        round_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (InvestorCommitmentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorCommitmentResponse]
    """

    kwargs = _get_kwargs(
        round_id=round_id,
        body=body,
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
    body: InvestorCommitmentCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    """Create Commitment

    Args:
        round_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (InvestorCommitmentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorCommitmentResponse
    """

    return sync_detailed(
        round_id=round_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: InvestorCommitmentCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
    """Create Commitment

    Args:
        round_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (InvestorCommitmentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorCommitmentResponse]
    """

    kwargs = _get_kwargs(
        round_id=round_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    round_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: InvestorCommitmentCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    """Create Commitment

    Args:
        round_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (InvestorCommitmentCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorCommitmentResponse
    """

    return (
        await asyncio_detailed(
            round_id=round_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
