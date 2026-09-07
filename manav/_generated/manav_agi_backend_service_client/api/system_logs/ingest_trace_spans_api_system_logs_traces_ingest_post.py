from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.span_ingest_request import SpanIngestRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SpanIngestRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/system-logs/traces/ingest",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SpanIngestRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Ingest Trace Spans

     Ingest orchestrator spans into trace_spans table. Called by orchestrator after execution.

    Accepts either a user JWT (frontend) OR X-Internal-Service-Token
    (orchestrator). Previously required a JWT, so internal orchestrator
    calls without a forwarded user JWT (e.g. background jobs, anonymous
    runs back when those were allowed) silently 401'd and lost their
    traces. Fixed 2026-06-03 (Obs #4).

    RBAC dep removed 2026-07-27: the endpoint had `system_logs:create:org`
    but no role granted it, so every non-super-admin bot 403'd when the
    orchestrator forwarded their JWT for trace ingest. Bots writing
    traces about their OWN runs shouldn't need a special grant — identity
    is already verified by require_service_or_user. Follow-up: enforce
    that trace.user_id matches auth identity (data-integrity check).

    Args:
        authorization (None | str | Unset):
        body (SpanIngestRequest): Request to ingest orchestrator spans into trace_spans table.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: SpanIngestRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Ingest Trace Spans

     Ingest orchestrator spans into trace_spans table. Called by orchestrator after execution.

    Accepts either a user JWT (frontend) OR X-Internal-Service-Token
    (orchestrator). Previously required a JWT, so internal orchestrator
    calls without a forwarded user JWT (e.g. background jobs, anonymous
    runs back when those were allowed) silently 401'd and lost their
    traces. Fixed 2026-06-03 (Obs #4).

    RBAC dep removed 2026-07-27: the endpoint had `system_logs:create:org`
    but no role granted it, so every non-super-admin bot 403'd when the
    orchestrator forwarded their JWT for trace ingest. Bots writing
    traces about their OWN runs shouldn't need a special grant — identity
    is already verified by require_service_or_user. Follow-up: enforce
    that trace.user_id matches auth identity (data-integrity check).

    Args:
        authorization (None | str | Unset):
        body (SpanIngestRequest): Request to ingest orchestrator spans into trace_spans table.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SpanIngestRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Ingest Trace Spans

     Ingest orchestrator spans into trace_spans table. Called by orchestrator after execution.

    Accepts either a user JWT (frontend) OR X-Internal-Service-Token
    (orchestrator). Previously required a JWT, so internal orchestrator
    calls without a forwarded user JWT (e.g. background jobs, anonymous
    runs back when those were allowed) silently 401'd and lost their
    traces. Fixed 2026-06-03 (Obs #4).

    RBAC dep removed 2026-07-27: the endpoint had `system_logs:create:org`
    but no role granted it, so every non-super-admin bot 403'd when the
    orchestrator forwarded their JWT for trace ingest. Bots writing
    traces about their OWN runs shouldn't need a special grant — identity
    is already verified by require_service_or_user. Follow-up: enforce
    that trace.user_id matches auth identity (data-integrity check).

    Args:
        authorization (None | str | Unset):
        body (SpanIngestRequest): Request to ingest orchestrator spans into trace_spans table.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: SpanIngestRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Ingest Trace Spans

     Ingest orchestrator spans into trace_spans table. Called by orchestrator after execution.

    Accepts either a user JWT (frontend) OR X-Internal-Service-Token
    (orchestrator). Previously required a JWT, so internal orchestrator
    calls without a forwarded user JWT (e.g. background jobs, anonymous
    runs back when those were allowed) silently 401'd and lost their
    traces. Fixed 2026-06-03 (Obs #4).

    RBAC dep removed 2026-07-27: the endpoint had `system_logs:create:org`
    but no role granted it, so every non-super-admin bot 403'd when the
    orchestrator forwarded their JWT for trace ingest. Bots writing
    traces about their OWN runs shouldn't need a special grant — identity
    is already verified by require_service_or_user. Follow-up: enforce
    that trace.user_id matches auth identity (data-integrity check).

    Args:
        authorization (None | str | Unset):
        body (SpanIngestRequest): Request to ingest orchestrator spans into trace_spans table.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
