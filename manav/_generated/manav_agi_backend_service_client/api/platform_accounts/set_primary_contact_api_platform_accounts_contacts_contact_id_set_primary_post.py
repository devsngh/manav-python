from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_response import ContactResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    contact_id: UUID,
    *,
    account_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_account_id = str(account_id)
    params["account_id"] = json_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/accounts/contacts/{contact_id}/set-primary".format(
            contact_id=quote(str(contact_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContactResponse.from_dict(response.json())

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
) -> Response[ContactResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[ContactResponse | HTTPValidationError]:
    """Set Primary Contact

    Args:
        contact_id (UUID):
        account_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        account_id=account_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> ContactResponse | HTTPValidationError | None:
    """Set Primary Contact

    Args:
        contact_id (UUID):
        account_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactResponse | HTTPValidationError
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        account_id=account_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    contact_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[ContactResponse | HTTPValidationError]:
    """Set Primary Contact

    Args:
        contact_id (UUID):
        account_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        account_id=account_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    account_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> ContactResponse | HTTPValidationError | None:
    """Set Primary Contact

    Args:
        contact_id (UUID):
        account_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            account_id=account_id,
            authorization=authorization,
        )
    ).parsed
