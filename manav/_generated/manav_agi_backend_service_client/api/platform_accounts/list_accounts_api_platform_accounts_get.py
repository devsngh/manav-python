from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_list_response import AccountListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_type: None | str | Unset = UNSET,
    industry: None | str | Unset = UNSET,
    size_segment: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_account_type: None | str | Unset
    if isinstance(account_type, Unset):
        json_account_type = UNSET
    else:
        json_account_type = account_type
    params["account_type"] = json_account_type

    json_industry: None | str | Unset
    if isinstance(industry, Unset):
        json_industry = UNSET
    else:
        json_industry = industry
    params["industry"] = json_industry

    json_size_segment: None | str | Unset
    if isinstance(size_segment, Unset):
        json_size_segment = UNSET
    else:
        json_size_segment = size_segment
    params["size_segment"] = json_size_segment

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_tier: None | str | Unset
    if isinstance(tier, Unset):
        json_tier = UNSET
    else:
        json_tier = tier
    params["tier"] = json_tier

    json_owner_bot_id: None | str | Unset
    if isinstance(owner_bot_id, Unset):
        json_owner_bot_id = UNSET
    elif isinstance(owner_bot_id, UUID):
        json_owner_bot_id = str(owner_bot_id)
    else:
        json_owner_bot_id = owner_bot_id
    params["owner_bot_id"] = json_owner_bot_id

    json_owner_user_id: None | str | Unset
    if isinstance(owner_user_id, Unset):
        json_owner_user_id = UNSET
    elif isinstance(owner_user_id, UUID):
        json_owner_user_id = str(owner_user_id)
    else:
        json_owner_user_id = owner_user_id
    params["owner_user_id"] = json_owner_user_id

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/accounts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AccountListResponse.from_dict(response.json())

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
) -> Response[AccountListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_type: None | str | Unset = UNSET,
    industry: None | str | Unset = UNSET,
    size_segment: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AccountListResponse | HTTPValidationError]:
    """List Accounts

    Args:
        account_type (None | str | Unset):
        industry (None | str | Unset):
        size_segment (None | str | Unset):
        status (None | str | Unset):
        tier (None | str | Unset):
        owner_bot_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        account_type=account_type,
        industry=industry,
        size_segment=size_segment,
        status=status,
        tier=tier,
        owner_bot_id=owner_bot_id,
        owner_user_id=owner_user_id,
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
    account_type: None | str | Unset = UNSET,
    industry: None | str | Unset = UNSET,
    size_segment: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AccountListResponse | HTTPValidationError | None:
    """List Accounts

    Args:
        account_type (None | str | Unset):
        industry (None | str | Unset):
        size_segment (None | str | Unset):
        status (None | str | Unset):
        tier (None | str | Unset):
        owner_bot_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        account_type=account_type,
        industry=industry,
        size_segment=size_segment,
        status=status,
        tier=tier,
        owner_bot_id=owner_bot_id,
        owner_user_id=owner_user_id,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_type: None | str | Unset = UNSET,
    industry: None | str | Unset = UNSET,
    size_segment: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[AccountListResponse | HTTPValidationError]:
    """List Accounts

    Args:
        account_type (None | str | Unset):
        industry (None | str | Unset):
        size_segment (None | str | Unset):
        status (None | str | Unset):
        tier (None | str | Unset):
        owner_bot_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        account_type=account_type,
        industry=industry,
        size_segment=size_segment,
        status=status,
        tier=tier,
        owner_bot_id=owner_bot_id,
        owner_user_id=owner_user_id,
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
    account_type: None | str | Unset = UNSET,
    industry: None | str | Unset = UNSET,
    size_segment: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    tier: None | str | Unset = UNSET,
    owner_bot_id: None | Unset | UUID = UNSET,
    owner_user_id: None | Unset | UUID = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> AccountListResponse | HTTPValidationError | None:
    """List Accounts

    Args:
        account_type (None | str | Unset):
        industry (None | str | Unset):
        size_segment (None | str | Unset):
        status (None | str | Unset):
        tier (None | str | Unset):
        owner_bot_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            account_type=account_type,
            industry=industry,
            size_segment=size_segment,
            status=status,
            tier=tier,
            owner_bot_id=owner_bot_id,
            owner_user_id=owner_user_id,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
