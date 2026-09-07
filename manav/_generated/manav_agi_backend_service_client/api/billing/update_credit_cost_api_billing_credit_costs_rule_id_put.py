from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credit_cost_rule_response import CreditCostRuleResponse
from ...models.credit_cost_rule_update import CreditCostRuleUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    rule_id: UUID,
    *,
    body: CreditCostRuleUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/billing/credit-costs/{rule_id}".format(
            rule_id=quote(str(rule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreditCostRuleResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CreditCostRuleResponse.from_dict(response.json())

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
) -> Response[CreditCostRuleResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditCostRuleUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CreditCostRuleResponse | HTTPValidationError]:
    """Update Credit Cost

    Args:
        rule_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditCostRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreditCostRuleResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditCostRuleUpdate,
    authorization: None | str | Unset = UNSET,
) -> CreditCostRuleResponse | HTTPValidationError | None:
    """Update Credit Cost

    Args:
        rule_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditCostRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreditCostRuleResponse | HTTPValidationError
    """

    return sync_detailed(
        rule_id=rule_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditCostRuleUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[CreditCostRuleResponse | HTTPValidationError]:
    """Update Credit Cost

    Args:
        rule_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditCostRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreditCostRuleResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        rule_id=rule_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    rule_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreditCostRuleUpdate,
    authorization: None | str | Unset = UNSET,
) -> CreditCostRuleResponse | HTTPValidationError | None:
    """Update Credit Cost

    Args:
        rule_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (CreditCostRuleUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreditCostRuleResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            rule_id=rule_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
