from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contract_list_response import ContractListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contract_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    related_account_id: None | Unset | UUID = UNSET,
    related_supplier_id: None | Unset | UUID = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    auto_renew: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_contract_type: None | str | Unset
    if isinstance(contract_type, Unset):
        json_contract_type = UNSET
    else:
        json_contract_type = contract_type
    params["contract_type"] = json_contract_type

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_legal_entity_id: None | str | Unset
    if isinstance(legal_entity_id, Unset):
        json_legal_entity_id = UNSET
    elif isinstance(legal_entity_id, UUID):
        json_legal_entity_id = str(legal_entity_id)
    else:
        json_legal_entity_id = legal_entity_id
    params["legal_entity_id"] = json_legal_entity_id

    json_related_account_id: None | str | Unset
    if isinstance(related_account_id, Unset):
        json_related_account_id = UNSET
    elif isinstance(related_account_id, UUID):
        json_related_account_id = str(related_account_id)
    else:
        json_related_account_id = related_account_id
    params["related_account_id"] = json_related_account_id

    json_related_supplier_id: None | str | Unset
    if isinstance(related_supplier_id, Unset):
        json_related_supplier_id = UNSET
    elif isinstance(related_supplier_id, UUID):
        json_related_supplier_id = str(related_supplier_id)
    else:
        json_related_supplier_id = related_supplier_id
    params["related_supplier_id"] = json_related_supplier_id

    json_related_product_id: None | str | Unset
    if isinstance(related_product_id, Unset):
        json_related_product_id = UNSET
    elif isinstance(related_product_id, UUID):
        json_related_product_id = str(related_product_id)
    else:
        json_related_product_id = related_product_id
    params["related_product_id"] = json_related_product_id

    json_owner_user_id: None | str | Unset
    if isinstance(owner_user_id, Unset):
        json_owner_user_id = UNSET
    elif isinstance(owner_user_id, UUID):
        json_owner_user_id = str(owner_user_id)
    else:
        json_owner_user_id = owner_user_id
    params["owner_user_id"] = json_owner_user_id

    json_owner_bot_id: None | str | Unset
    if isinstance(owner_bot_id, Unset):
        json_owner_bot_id = UNSET
    elif isinstance(owner_bot_id, UUID):
        json_owner_bot_id = str(owner_bot_id)
    else:
        json_owner_bot_id = owner_bot_id
    params["owner_bot_id"] = json_owner_bot_id

    json_auto_renew: bool | None | Unset
    if isinstance(auto_renew, Unset):
        json_auto_renew = UNSET
    else:
        json_auto_renew = auto_renew
    params["auto_renew"] = json_auto_renew

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/contracts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContractListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ContractListResponse.from_dict(response.json())

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
) -> Response[ContractListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    contract_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    related_account_id: None | Unset | UUID = UNSET,
    related_supplier_id: None | Unset | UUID = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    auto_renew: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractListResponse | HTTPValidationError]:
    """List Contracts

    Args:
        contract_type (None | str | Unset):
        status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        related_account_id (None | Unset | UUID):
        related_supplier_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_bot_id (None | Unset | UUID):
        auto_renew (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contract_type=contract_type,
        status=status,
        legal_entity_id=legal_entity_id,
        related_account_id=related_account_id,
        related_supplier_id=related_supplier_id,
        related_product_id=related_product_id,
        owner_user_id=owner_user_id,
        owner_bot_id=owner_bot_id,
        auto_renew=auto_renew,
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
    contract_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    related_account_id: None | Unset | UUID = UNSET,
    related_supplier_id: None | Unset | UUID = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    auto_renew: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ContractListResponse | HTTPValidationError | None:
    """List Contracts

    Args:
        contract_type (None | str | Unset):
        status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        related_account_id (None | Unset | UUID):
        related_supplier_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_bot_id (None | Unset | UUID):
        auto_renew (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        contract_type=contract_type,
        status=status,
        legal_entity_id=legal_entity_id,
        related_account_id=related_account_id,
        related_supplier_id=related_supplier_id,
        related_product_id=related_product_id,
        owner_user_id=owner_user_id,
        owner_bot_id=owner_bot_id,
        auto_renew=auto_renew,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    contract_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    related_account_id: None | Unset | UUID = UNSET,
    related_supplier_id: None | Unset | UUID = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    auto_renew: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[ContractListResponse | HTTPValidationError]:
    """List Contracts

    Args:
        contract_type (None | str | Unset):
        status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        related_account_id (None | Unset | UUID):
        related_supplier_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_bot_id (None | Unset | UUID):
        auto_renew (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContractListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        contract_type=contract_type,
        status=status,
        legal_entity_id=legal_entity_id,
        related_account_id=related_account_id,
        related_supplier_id=related_supplier_id,
        related_product_id=related_product_id,
        owner_user_id=owner_user_id,
        owner_bot_id=owner_bot_id,
        auto_renew=auto_renew,
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
    contract_type: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    related_account_id: None | Unset | UUID = UNSET,
    related_supplier_id: None | Unset | UUID = UNSET,
    related_product_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    auto_renew: bool | None | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> ContractListResponse | HTTPValidationError | None:
    """List Contracts

    Args:
        contract_type (None | str | Unset):
        status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        related_account_id (None | Unset | UUID):
        related_supplier_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_bot_id (None | Unset | UUID):
        auto_renew (bool | None | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContractListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            contract_type=contract_type,
            status=status,
            legal_entity_id=legal_entity_id,
            related_account_id=related_account_id,
            related_supplier_id=related_supplier_id,
            related_product_id=related_product_id,
            owner_user_id=owner_user_id,
            owner_bot_id=owner_bot_id,
            auto_renew=auto_renew,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
