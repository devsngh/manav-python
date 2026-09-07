from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.plan_quota_create import PlanQuotaCreate
from ...models.plan_quota_response import PlanQuotaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plan_id: UUID,
    *,
    body: PlanQuotaCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/billing/plans/{plan_id}/quotas".format(
            plan_id=quote(str(plan_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PlanQuotaResponse | None:
    if response.status_code == 201:
        response_201 = PlanQuotaResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | PlanQuotaResponse]:
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
    body: PlanQuotaCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlanQuotaResponse]:
    """Create Plan Quota

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanQuotaCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlanQuotaResponse]
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
    body: PlanQuotaCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlanQuotaResponse | None:
    """Create Plan Quota

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanQuotaCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlanQuotaResponse
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
    body: PlanQuotaCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlanQuotaResponse]:
    """Create Plan Quota

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanQuotaCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlanQuotaResponse]
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
    body: PlanQuotaCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlanQuotaResponse | None:
    """Create Plan Quota

    Args:
        plan_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanQuotaCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlanQuotaResponse
    """

    return (
        await asyncio_detailed(
            plan_id=plan_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
