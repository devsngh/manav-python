from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.billing_plan_response import BillingPlanResponse
from ...models.billing_plan_update import BillingPlanUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plan_id: UUID,
    *,
    body: BillingPlanUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/billing/plans/{plan_id}".format(
            plan_id=quote(str(plan_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BillingPlanResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BillingPlanResponse.from_dict(response.json())

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
) -> Response[BillingPlanResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BillingPlanUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[BillingPlanResponse | HTTPValidationError]:
    """Update Plan

     billing_admin:update — update a plan.

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BillingPlanUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingPlanResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        plan_id=plan_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BillingPlanUpdate,
    authorization: None | str | Unset = UNSET,
) -> BillingPlanResponse | HTTPValidationError | None:
    """Update Plan

     billing_admin:update — update a plan.

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BillingPlanUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingPlanResponse | HTTPValidationError
    """

    return sync_detailed(
        plan_id=plan_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    plan_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BillingPlanUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[BillingPlanResponse | HTTPValidationError]:
    """Update Plan

     billing_admin:update — update a plan.

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BillingPlanUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BillingPlanResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        plan_id=plan_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: BillingPlanUpdate,
    authorization: None | str | Unset = UNSET,
) -> BillingPlanResponse | HTTPValidationError | None:
    """Update Plan

     billing_admin:update — update a plan.

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (BillingPlanUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BillingPlanResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            plan_id=plan_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
