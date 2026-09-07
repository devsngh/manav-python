from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.investor_commitment_response import InvestorCommitmentResponse
from ...models.record_term_sheet_request import RecordTermSheetRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    commitment_id: UUID,
    *,
    body: RecordTermSheetRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/ir/commitments/{commitment_id}/term-sheet".format(
            commitment_id=quote(str(commitment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    if response.status_code == 200:
        response_200 = InvestorCommitmentResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    commitment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordTermSheetRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
    """Record Commitment Term Sheet

    Args:
        commitment_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordTermSheetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorCommitmentResponse]
    """

    kwargs = _get_kwargs(
        commitment_id=commitment_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    commitment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordTermSheetRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    """Record Commitment Term Sheet

    Args:
        commitment_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordTermSheetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorCommitmentResponse
    """

    return sync_detailed(
        commitment_id=commitment_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    commitment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordTermSheetRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | InvestorCommitmentResponse]:
    """Record Commitment Term Sheet

    Args:
        commitment_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordTermSheetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | InvestorCommitmentResponse]
    """

    kwargs = _get_kwargs(
        commitment_id=commitment_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    commitment_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordTermSheetRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | InvestorCommitmentResponse | None:
    """Record Commitment Term Sheet

    Args:
        commitment_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordTermSheetRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | InvestorCommitmentResponse
    """

    return (
        await asyncio_detailed(
            commitment_id=commitment_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
