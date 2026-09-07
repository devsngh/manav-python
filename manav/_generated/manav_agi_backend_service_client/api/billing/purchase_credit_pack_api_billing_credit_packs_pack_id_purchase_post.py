from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkout_session_response import CheckoutSessionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pack_id: UUID,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/billing/credit-packs/{pack_id}/purchase".format(
            pack_id=quote(str(pack_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckoutSessionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CheckoutSessionResponse.from_dict(response.json())

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
) -> Response[CheckoutSessionResponse | HTTPValidationError]:
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
    authorization: None | str | Unset = UNSET,
) -> Response[CheckoutSessionResponse | HTTPValidationError]:
    """Purchase Credit Pack

     Create Stripe checkout session for credit pack purchase.

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutSessionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
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
    authorization: None | str | Unset = UNSET,
) -> CheckoutSessionResponse | HTTPValidationError | None:
    """Purchase Credit Pack

     Create Stripe checkout session for credit pack purchase.

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutSessionResponse | HTTPValidationError
    """

    return sync_detailed(
        pack_id=pack_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CheckoutSessionResponse | HTTPValidationError]:
    """Purchase Credit Pack

     Create Stripe checkout session for credit pack purchase.

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckoutSessionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        pack_id=pack_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pack_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CheckoutSessionResponse | HTTPValidationError | None:
    """Purchase Credit Pack

     Create Stripe checkout session for credit pack purchase.

    Args:
        pack_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckoutSessionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            pack_id=pack_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
