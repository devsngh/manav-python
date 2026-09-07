from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.plan_feature_response import PlanFeatureResponse
from ...models.plan_feature_update import PlanFeatureUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    plan_id: UUID,
    feature_id: UUID,
    *,
    body: PlanFeatureUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/billing/plans/{plan_id}/features/{feature_id}".format(
            plan_id=quote(str(plan_id), safe=""),
            feature_id=quote(str(feature_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PlanFeatureResponse | None:
    if response.status_code == 200:
        response_200 = PlanFeatureResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PlanFeatureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plan_id: UUID,
    feature_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PlanFeatureUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlanFeatureResponse]:
    """Update Plan Feature

    Args:
        plan_id (UUID):
        feature_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanFeatureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlanFeatureResponse]
    """

    kwargs = _get_kwargs(
        plan_id=plan_id,
        feature_id=feature_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plan_id: UUID,
    feature_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PlanFeatureUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlanFeatureResponse | None:
    """Update Plan Feature

    Args:
        plan_id (UUID):
        feature_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanFeatureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlanFeatureResponse
    """

    return sync_detailed(
        plan_id=plan_id,
        feature_id=feature_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    plan_id: UUID,
    feature_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PlanFeatureUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlanFeatureResponse]:
    """Update Plan Feature

    Args:
        plan_id (UUID):
        feature_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanFeatureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlanFeatureResponse]
    """

    kwargs = _get_kwargs(
        plan_id=plan_id,
        feature_id=feature_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plan_id: UUID,
    feature_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PlanFeatureUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlanFeatureResponse | None:
    """Update Plan Feature

    Args:
        plan_id (UUID):
        feature_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PlanFeatureUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlanFeatureResponse
    """

    return (
        await asyncio_detailed(
            plan_id=plan_id,
            feature_id=feature_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
