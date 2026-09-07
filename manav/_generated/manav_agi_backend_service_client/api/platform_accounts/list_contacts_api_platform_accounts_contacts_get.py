from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_list_response import ContactListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: None | Unset | UUID = UNSET,
    persona_id: None | Unset | UUID = UNSET,
    seniority: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_account_id: None | str | Unset
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    elif isinstance(account_id, UUID):
        json_account_id = str(account_id)
    else:
        json_account_id = account_id
    params["account_id"] = json_account_id

    json_persona_id: None | str | Unset
    if isinstance(persona_id, Unset):
        json_persona_id = UNSET
    elif isinstance(persona_id, UUID):
        json_persona_id = str(persona_id)
    else:
        json_persona_id = persona_id
    params["persona_id"] = json_persona_id

    json_seniority: None | str | Unset
    if isinstance(seniority, Unset):
        json_seniority = UNSET
    else:
        json_seniority = seniority
    params["seniority"] = json_seniority

    json_buying_committee_role: None | str | Unset
    if isinstance(buying_committee_role, Unset):
        json_buying_committee_role = UNSET
    else:
        json_buying_committee_role = buying_committee_role
    params["buying_committee_role"] = json_buying_committee_role

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/accounts/contacts/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContactListResponse.from_dict(response.json())

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
) -> Response[ContactListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | Unset | UUID = UNSET,
    persona_id: None | Unset | UUID = UNSET,
    seniority: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ContactListResponse | HTTPValidationError]:
    """List Contacts

    Args:
        account_id (None | Unset | UUID):
        persona_id (None | Unset | UUID):
        seniority (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        persona_id=persona_id,
        seniority=seniority,
        buying_committee_role=buying_committee_role,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | Unset | UUID = UNSET,
    persona_id: None | Unset | UUID = UNSET,
    seniority: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ContactListResponse | HTTPValidationError | None:
    """List Contacts

    Args:
        account_id (None | Unset | UUID):
        persona_id (None | Unset | UUID):
        seniority (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        persona_id=persona_id,
        seniority=seniority,
        buying_committee_role=buying_committee_role,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | Unset | UUID = UNSET,
    persona_id: None | Unset | UUID = UNSET,
    seniority: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ContactListResponse | HTTPValidationError]:
    """List Contacts

    Args:
        account_id (None | Unset | UUID):
        persona_id (None | Unset | UUID):
        seniority (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        persona_id=persona_id,
        seniority=seniority,
        buying_committee_role=buying_committee_role,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: None | Unset | UUID = UNSET,
    persona_id: None | Unset | UUID = UNSET,
    seniority: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ContactListResponse | HTTPValidationError | None:
    """List Contacts

    Args:
        account_id (None | Unset | UUID):
        persona_id (None | Unset | UUID):
        seniority (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            persona_id=persona_id,
            seniority=seniority,
            buying_committee_role=buying_committee_role,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
