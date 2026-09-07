from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegation_rule_list_response import DelegationRuleListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    delegator_user_id: None | Unset | UUID = UNSET,
    delegate_user_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_delegator_user_id: None | str | Unset
    if isinstance(delegator_user_id, Unset):
        json_delegator_user_id = UNSET
    elif isinstance(delegator_user_id, UUID):
        json_delegator_user_id = str(delegator_user_id)
    else:
        json_delegator_user_id = delegator_user_id
    params["delegator_user_id"] = json_delegator_user_id

    json_delegate_user_id: None | str | Unset
    if isinstance(delegate_user_id, Unset):
        json_delegate_user_id = UNSET
    elif isinstance(delegate_user_id, UUID):
        json_delegate_user_id = str(delegate_user_id)
    else:
        json_delegate_user_id = delegate_user_id
    params["delegate_user_id"] = json_delegate_user_id

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/approvals/delegations",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DelegationRuleListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DelegationRuleListResponse.from_dict(response.json())

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
) -> Response[DelegationRuleListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    delegator_user_id: None | Unset | UUID = UNSET,
    delegate_user_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[DelegationRuleListResponse | HTTPValidationError]:
    """List Delegations

    Args:
        delegator_user_id (None | Unset | UUID):
        delegate_user_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegationRuleListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        delegator_user_id=delegator_user_id,
        delegate_user_id=delegate_user_id,
        is_active=is_active,
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
    delegator_user_id: None | Unset | UUID = UNSET,
    delegate_user_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> DelegationRuleListResponse | HTTPValidationError | None:
    """List Delegations

    Args:
        delegator_user_id (None | Unset | UUID):
        delegate_user_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegationRuleListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        delegator_user_id=delegator_user_id,
        delegate_user_id=delegate_user_id,
        is_active=is_active,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    delegator_user_id: None | Unset | UUID = UNSET,
    delegate_user_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[DelegationRuleListResponse | HTTPValidationError]:
    """List Delegations

    Args:
        delegator_user_id (None | Unset | UUID):
        delegate_user_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegationRuleListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        delegator_user_id=delegator_user_id,
        delegate_user_id=delegate_user_id,
        is_active=is_active,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    delegator_user_id: None | Unset | UUID = UNSET,
    delegate_user_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> DelegationRuleListResponse | HTTPValidationError | None:
    """List Delegations

    Args:
        delegator_user_id (None | Unset | UUID):
        delegate_user_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegationRuleListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            delegator_user_id=delegator_user_id,
            delegate_user_id=delegate_user_id,
            is_active=is_active,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
