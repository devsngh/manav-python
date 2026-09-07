from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contract_party_response import ContractPartyResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.record_signature_request import RecordSignatureRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    party_id: UUID,
    *,
    body: RecordSignatureRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/contracts/parties/{party_id}/sign".format(
            party_id=quote(str(party_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContractPartyResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContractPartyResponse.from_dict(response.json())

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
) -> Response[ContractPartyResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    party_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSignatureRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractPartyResponse | HTTPValidationError]:
    """Record Party Signature

    Args:
        party_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordSignatureRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractPartyResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        party_id=party_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    party_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSignatureRequest,
    authorization: None | str | Unset = UNSET,
) -> ContractPartyResponse | HTTPValidationError | None:
    """Record Party Signature

    Args:
        party_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordSignatureRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractPartyResponse | HTTPValidationError
    """

    return sync_detailed(
        party_id=party_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    party_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSignatureRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractPartyResponse | HTTPValidationError]:
    """Record Party Signature

    Args:
        party_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordSignatureRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractPartyResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        party_id=party_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    party_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RecordSignatureRequest,
    authorization: None | str | Unset = UNSET,
) -> ContractPartyResponse | HTTPValidationError | None:
    """Record Party Signature

    Args:
        party_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (RecordSignatureRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractPartyResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            party_id=party_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
