from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.synthesis_insight_response import SynthesisInsightResponse
from ...models.synthesis_insight_update import SynthesisInsightUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    insight_id: UUID,
    *,
    body: SynthesisInsightUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/observability/insights/{insight_id}".format(
            insight_id=quote(str(insight_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SynthesisInsightResponse | None:
    if response.status_code == 200:
        response_200 = SynthesisInsightResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    insight_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    """Update Insight

    Args:
        insight_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightUpdate): Patch — status transitions, surfacing flags, retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SynthesisInsightResponse]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    insight_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SynthesisInsightResponse | None:
    """Update Insight

    Args:
        insight_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightUpdate): Patch — status transitions, surfacing flags, retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SynthesisInsightResponse
    """

    return sync_detailed(
        insight_id=insight_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    insight_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    """Update Insight

    Args:
        insight_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightUpdate): Patch — status transitions, surfacing flags, retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SynthesisInsightResponse]
    """

    kwargs = _get_kwargs(
        insight_id=insight_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    insight_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SynthesisInsightResponse | None:
    """Update Insight

    Args:
        insight_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightUpdate): Patch — status transitions, surfacing flags, retraction.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SynthesisInsightResponse
    """

    return (
        await asyncio_detailed(
            insight_id=insight_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
