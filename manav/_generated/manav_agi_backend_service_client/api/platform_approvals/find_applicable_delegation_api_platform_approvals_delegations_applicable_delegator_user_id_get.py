from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delegation_rule_response import DelegationRuleResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    delegator_user_id: UUID,
    *,
    resource_type: None | str | Unset = UNSET,
    amount: float | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_resource_type: None | str | Unset
    if isinstance(resource_type, Unset):
        json_resource_type = UNSET
    else:
        json_resource_type = resource_type
    params["resource_type"] = json_resource_type

    json_amount: float | None | Unset
    if isinstance(amount, Unset):
        json_amount = UNSET
    else:
        json_amount = amount
    params["amount"] = json_amount

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/approvals/delegations/applicable/{delegator_user_id}".format(
            delegator_user_id=quote(str(delegator_user_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DelegationRuleResponse | None | HTTPValidationError | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> DelegationRuleResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DelegationRuleResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DelegationRuleResponse | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[DelegationRuleResponse | None | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    delegator_user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | str | Unset = UNSET,
    amount: float | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DelegationRuleResponse | None | HTTPValidationError]:
    """Find Applicable Delegation

    Args:
        delegator_user_id (UUID):
        resource_type (None | str | Unset):
        amount (float | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegationRuleResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        delegator_user_id=delegator_user_id,
        resource_type=resource_type,
        amount=amount,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delegator_user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | str | Unset = UNSET,
    amount: float | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DelegationRuleResponse | None | HTTPValidationError | None:
    """Find Applicable Delegation

    Args:
        delegator_user_id (UUID):
        resource_type (None | str | Unset):
        amount (float | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegationRuleResponse | None | HTTPValidationError
    """

    return sync_detailed(
        delegator_user_id=delegator_user_id,
        client=client,
        resource_type=resource_type,
        amount=amount,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    delegator_user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | str | Unset = UNSET,
    amount: float | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DelegationRuleResponse | None | HTTPValidationError]:
    """Find Applicable Delegation

    Args:
        delegator_user_id (UUID):
        resource_type (None | str | Unset):
        amount (float | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DelegationRuleResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        delegator_user_id=delegator_user_id,
        resource_type=resource_type,
        amount=amount,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    delegator_user_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    resource_type: None | str | Unset = UNSET,
    amount: float | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DelegationRuleResponse | None | HTTPValidationError | None:
    """Find Applicable Delegation

    Args:
        delegator_user_id (UUID):
        resource_type (None | str | Unset):
        amount (float | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DelegationRuleResponse | None | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            delegator_user_id=delegator_user_id,
            client=client,
            resource_type=resource_type,
            amount=amount,
            authorization=authorization,
        )
    ).parsed
