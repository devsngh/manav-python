from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credit_pack_response import CreditPackResponse
from ...models.credit_pack_update import CreditPackUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pack_id: UUID,
    *,
    body: CreditPackUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/billing/credit-packs/{pack_id}".format(
            pack_id=quote(str(pack_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreditPackResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CreditPackResponse.from_dict(response.json())

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
) -> Response[CreditPackResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditPackUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CreditPackResponse | HTTPValidationError]:
    """Update Credit Pack

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditPackUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreditPackResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditPackUpdate,
    authorization: None | str | Unset = UNSET,
) -> CreditPackResponse | HTTPValidationError | None:
    """Update Credit Pack

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditPackUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreditPackResponse | HTTPValidationError
    """

    return sync_detailed(
        pack_id=pack_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditPackUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CreditPackResponse | HTTPValidationError]:
    """Update Credit Pack

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditPackUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreditPackResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditPackUpdate,
    authorization: None | str | Unset = UNSET,
) -> CreditPackResponse | HTTPValidationError | None:
    """Update Credit Pack

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditPackUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreditPackResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            pack_id=pack_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
