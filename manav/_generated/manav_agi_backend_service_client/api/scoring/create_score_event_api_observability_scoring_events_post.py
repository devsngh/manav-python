from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.score_event_create import ScoreEventCreate
from ...models.score_event_response import ScoreEventResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ScoreEventCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/observability/scoring/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ScoreEventResponse | None:
    if response.status_code == 201:
        response_201 = ScoreEventResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ScoreEventResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScoreEventCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ScoreEventResponse]:
    """Create Score Event

     Write a score event. Server-side validation:
    - role gate (granted_by_role ↔ event_type)
    - delta range (per event_type)
    - evidence_refs non-empty
    - granted_by_id != bot_id (DB CHECK is final firewall)
    - multi-party confirmation for catastrophic_incident

    On success, DB trigger updates bot_scores.current_score atomically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ScoreEventCreate): Request body for POST /api/observability/scoring/events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ScoreEventResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ScoreEventCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ScoreEventResponse | None:
    """Create Score Event

     Write a score event. Server-side validation:
    - role gate (granted_by_role ↔ event_type)
    - delta range (per event_type)
    - evidence_refs non-empty
    - granted_by_id != bot_id (DB CHECK is final firewall)
    - multi-party confirmation for catastrophic_incident

    On success, DB trigger updates bot_scores.current_score atomically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ScoreEventCreate): Request body for POST /api/observability/scoring/events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ScoreEventResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ScoreEventCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ScoreEventResponse]:
    """Create Score Event

     Write a score event. Server-side validation:
    - role gate (granted_by_role ↔ event_type)
    - delta range (per event_type)
    - evidence_refs non-empty
    - granted_by_id != bot_id (DB CHECK is final firewall)
    - multi-party confirmation for catastrophic_incident

    On success, DB trigger updates bot_scores.current_score atomically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ScoreEventCreate): Request body for POST /api/observability/scoring/events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ScoreEventResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ScoreEventCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ScoreEventResponse | None:
    """Create Score Event

     Write a score event. Server-side validation:
    - role gate (granted_by_role ↔ event_type)
    - delta range (per event_type)
    - evidence_refs non-empty
    - granted_by_id != bot_id (DB CHECK is final firewall)
    - multi-party confirmation for catastrophic_incident

    On success, DB trigger updates bot_scores.current_score atomically.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ScoreEventCreate): Request body for POST /api/observability/scoring/events.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ScoreEventResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
