import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.subject_type import SubjectType
from ...models.timeline_response import TimelineResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subject_type: SubjectType,
    subject_id: UUID,
    window_start: datetime.datetime,
    window_end: datetime.datetime,
    kinds: list[str] | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_subject_type = subject_type.value
    params["subject_type"] = json_subject_type

    json_subject_id = str(subject_id)
    params["subject_id"] = json_subject_id

    json_window_start = window_start.isoformat()
    params["window_start"] = json_window_start

    json_window_end = window_end.isoformat()
    params["window_end"] = json_window_end

    json_kinds: list[str] | None | Unset
    if isinstance(kinds, Unset):
        json_kinds = UNSET
    elif isinstance(kinds, list):
        json_kinds = kinds

    else:
        json_kinds = kinds
    params["kinds"] = json_kinds

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/timeline",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TimelineResponse | None:
    if response.status_code == 200:
        response_200 = TimelineResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TimelineResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: SubjectType,
    subject_id: UUID,
    window_start: datetime.datetime,
    window_end: datetime.datetime,
    kinds: list[str] | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TimelineResponse]:
    """Get Timeline

     Merged timeline for a subject in a window.

    Unions trace_spans (Track A) + domain event tables (Track C) into
    one time-ordered canonical event stream. Track B (LangGraph
    checkpoints) integration is a follow-up.

    Example:
        GET /api/observability/timeline
            ?subject_type=agent
            &subject_id=da65d449-...
            &window_start=2026-08-10T00:00:00Z
            &window_end=2026-08-10T23:59:59Z
            &kinds=llm.call&kinds=tool.call&kinds=hil.raised
            &limit=500

    Args:
        subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
        subject_id (UUID): ID of the entity
        window_start (datetime.datetime): Timeline window start (ISO 8601)
        window_end (datetime.datetime): Timeline window end (ISO 8601)
        kinds (list[str] | None | Unset): Filter to these canonical kinds (empty = all)
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TimelineResponse]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
        window_start=window_start,
        window_end=window_end,
        kinds=kinds,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    subject_type: SubjectType,
    subject_id: UUID,
    window_start: datetime.datetime,
    window_end: datetime.datetime,
    kinds: list[str] | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TimelineResponse | None:
    """Get Timeline

     Merged timeline for a subject in a window.

    Unions trace_spans (Track A) + domain event tables (Track C) into
    one time-ordered canonical event stream. Track B (LangGraph
    checkpoints) integration is a follow-up.

    Example:
        GET /api/observability/timeline
            ?subject_type=agent
            &subject_id=da65d449-...
            &window_start=2026-08-10T00:00:00Z
            &window_end=2026-08-10T23:59:59Z
            &kinds=llm.call&kinds=tool.call&kinds=hil.raised
            &limit=500

    Args:
        subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
        subject_id (UUID): ID of the entity
        window_start (datetime.datetime): Timeline window start (ISO 8601)
        window_end (datetime.datetime): Timeline window end (ISO 8601)
        kinds (list[str] | None | Unset): Filter to these canonical kinds (empty = all)
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TimelineResponse
    """

    return sync_detailed(
        client=client,
        subject_type=subject_type,
        subject_id=subject_id,
        window_start=window_start,
        window_end=window_end,
        kinds=kinds,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: SubjectType,
    subject_id: UUID,
    window_start: datetime.datetime,
    window_end: datetime.datetime,
    kinds: list[str] | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TimelineResponse]:
    """Get Timeline

     Merged timeline for a subject in a window.

    Unions trace_spans (Track A) + domain event tables (Track C) into
    one time-ordered canonical event stream. Track B (LangGraph
    checkpoints) integration is a follow-up.

    Example:
        GET /api/observability/timeline
            ?subject_type=agent
            &subject_id=da65d449-...
            &window_start=2026-08-10T00:00:00Z
            &window_end=2026-08-10T23:59:59Z
            &kinds=llm.call&kinds=tool.call&kinds=hil.raised
            &limit=500

    Args:
        subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
        subject_id (UUID): ID of the entity
        window_start (datetime.datetime): Timeline window start (ISO 8601)
        window_end (datetime.datetime): Timeline window end (ISO 8601)
        kinds (list[str] | None | Unset): Filter to these canonical kinds (empty = all)
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TimelineResponse]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_id=subject_id,
        window_start=window_start,
        window_end=window_end,
        kinds=kinds,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    subject_type: SubjectType,
    subject_id: UUID,
    window_start: datetime.datetime,
    window_end: datetime.datetime,
    kinds: list[str] | None | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TimelineResponse | None:
    """Get Timeline

     Merged timeline for a subject in a window.

    Unions trace_spans (Track A) + domain event tables (Track C) into
    one time-ordered canonical event stream. Track B (LangGraph
    checkpoints) integration is a follow-up.

    Example:
        GET /api/observability/timeline
            ?subject_type=agent
            &subject_id=da65d449-...
            &window_start=2026-08-10T00:00:00Z
            &window_end=2026-08-10T23:59:59Z
            &kinds=llm.call&kinds=tool.call&kinds=hil.raised
            &limit=500

    Args:
        subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
        subject_id (UUID): ID of the entity
        window_start (datetime.datetime): Timeline window start (ISO 8601)
        window_end (datetime.datetime): Timeline window end (ISO 8601)
        kinds (list[str] | None | Unset): Filter to these canonical kinds (empty = all)
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TimelineResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            subject_type=subject_type,
            subject_id=subject_id,
            window_start=window_start,
            window_end=window_end,
            kinds=kinds,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
