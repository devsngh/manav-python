from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.child_trace_list_response import ChildTraceListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_span_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_parent_span_id = str(parent_span_id)
    params["parent_span_id"] = json_parent_span_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat-traces/child-traces",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ChildTraceListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ChildTraceListResponse.from_dict(response.json())

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
) -> Response[ChildTraceListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_span_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[ChildTraceListResponse | HTTPValidationError]:
    """Child Traces

     Panel 3 subagent drill-down — child agent traces reachable from
    a delegate event. Each item points at another thread the frontend
    can open in a NEW AgentTracesTower window.

    Resolution: triggered_span_ids (Wave A7.1) → caused_by_span_id
    backlinks → parent_id children with different bot_id. Ship 0
    graceful-empty when data isn't populated yet — Ship 1 PR 3 will
    make this rich.

    Auth-only gate. The child thread's own summary/events endpoints
    apply the full visible_bots + beta whitelist checks, so a caller
    can't reach a child trace they wouldn't otherwise be allowed to
    see — the response gives them the target coordinates, but the
    downstream endpoints reject the actual data pull.

    Args:
        parent_span_id (UUID): Delegate/subagent span id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChildTraceListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        parent_span_id=parent_span_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_span_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> ChildTraceListResponse | HTTPValidationError | None:
    """Child Traces

     Panel 3 subagent drill-down — child agent traces reachable from
    a delegate event. Each item points at another thread the frontend
    can open in a NEW AgentTracesTower window.

    Resolution: triggered_span_ids (Wave A7.1) → caused_by_span_id
    backlinks → parent_id children with different bot_id. Ship 0
    graceful-empty when data isn't populated yet — Ship 1 PR 3 will
    make this rich.

    Auth-only gate. The child thread's own summary/events endpoints
    apply the full visible_bots + beta whitelist checks, so a caller
    can't reach a child trace they wouldn't otherwise be allowed to
    see — the response gives them the target coordinates, but the
    downstream endpoints reject the actual data pull.

    Args:
        parent_span_id (UUID): Delegate/subagent span id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChildTraceListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        parent_span_id=parent_span_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_span_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[ChildTraceListResponse | HTTPValidationError]:
    """Child Traces

     Panel 3 subagent drill-down — child agent traces reachable from
    a delegate event. Each item points at another thread the frontend
    can open in a NEW AgentTracesTower window.

    Resolution: triggered_span_ids (Wave A7.1) → caused_by_span_id
    backlinks → parent_id children with different bot_id. Ship 0
    graceful-empty when data isn't populated yet — Ship 1 PR 3 will
    make this rich.

    Auth-only gate. The child thread's own summary/events endpoints
    apply the full visible_bots + beta whitelist checks, so a caller
    can't reach a child trace they wouldn't otherwise be allowed to
    see — the response gives them the target coordinates, but the
    downstream endpoints reject the actual data pull.

    Args:
        parent_span_id (UUID): Delegate/subagent span id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChildTraceListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        parent_span_id=parent_span_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_span_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> ChildTraceListResponse | HTTPValidationError | None:
    """Child Traces

     Panel 3 subagent drill-down — child agent traces reachable from
    a delegate event. Each item points at another thread the frontend
    can open in a NEW AgentTracesTower window.

    Resolution: triggered_span_ids (Wave A7.1) → caused_by_span_id
    backlinks → parent_id children with different bot_id. Ship 0
    graceful-empty when data isn't populated yet — Ship 1 PR 3 will
    make this rich.

    Auth-only gate. The child thread's own summary/events endpoints
    apply the full visible_bots + beta whitelist checks, so a caller
    can't reach a child trace they wouldn't otherwise be allowed to
    see — the response gives them the target coordinates, but the
    downstream endpoints reject the actual data pull.

    Args:
        parent_span_id (UUID): Delegate/subagent span id
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChildTraceListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_span_id=parent_span_id,
            authorization=authorization,
        )
    ).parsed
