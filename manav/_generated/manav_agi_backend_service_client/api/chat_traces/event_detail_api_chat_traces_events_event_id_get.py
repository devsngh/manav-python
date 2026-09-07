from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_detail import EventDetail
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/chat-traces/events/{event_id}".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventDetail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EventDetail.from_dict(response.json())

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
) -> Response[EventDetail | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[EventDetail | HTTPValidationError]:
    """Event Detail

     Panel 3 — full detail for one event.

    Event ID shapes are namespaced (same as activation tower):
      <span_id>                        — raw trace_spans row
      write:<prefix>:<key>             — cabinet write
      milestone:<prefix>:<key>         — cabinet write flagged as milestone
      activation_done:<prefix>:<key>   — boot-complete sentinel
      activation_begin:<agent_id>      — synthesized boot-start marker
      checkpoint:<thread_id>:<cid>     — LangGraph state snapshot

    Compliance: for span event ids (raw UUID), fetch the (bot_id,
    source_type, source_id) off the span and enforce the same per-
    source_type ownership check the thread endpoints use. For non-span
    ids (write / milestone / checkpoint) the source is derivable from
    the id itself; we enforce there too when we can, otherwise
    fall back to auth-only (defense in depth via the parent thread
    endpoint that would have gated the event's discoverability).

    Args:
        event_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> EventDetail | HTTPValidationError | None:
    """Event Detail

     Panel 3 — full detail for one event.

    Event ID shapes are namespaced (same as activation tower):
      <span_id>                        — raw trace_spans row
      write:<prefix>:<key>             — cabinet write
      milestone:<prefix>:<key>         — cabinet write flagged as milestone
      activation_done:<prefix>:<key>   — boot-complete sentinel
      activation_begin:<agent_id>      — synthesized boot-start marker
      checkpoint:<thread_id>:<cid>     — LangGraph state snapshot

    Compliance: for span event ids (raw UUID), fetch the (bot_id,
    source_type, source_id) off the span and enforce the same per-
    source_type ownership check the thread endpoints use. For non-span
    ids (write / milestone / checkpoint) the source is derivable from
    the id itself; we enforce there too when we can, otherwise
    fall back to auth-only (defense in depth via the parent thread
    endpoint that would have gated the event's discoverability).

    Args:
        event_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventDetail | HTTPValidationError
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[EventDetail | HTTPValidationError]:
    """Event Detail

     Panel 3 — full detail for one event.

    Event ID shapes are namespaced (same as activation tower):
      <span_id>                        — raw trace_spans row
      write:<prefix>:<key>             — cabinet write
      milestone:<prefix>:<key>         — cabinet write flagged as milestone
      activation_done:<prefix>:<key>   — boot-complete sentinel
      activation_begin:<agent_id>      — synthesized boot-start marker
      checkpoint:<thread_id>:<cid>     — LangGraph state snapshot

    Compliance: for span event ids (raw UUID), fetch the (bot_id,
    source_type, source_id) off the span and enforce the same per-
    source_type ownership check the thread endpoints use. For non-span
    ids (write / milestone / checkpoint) the source is derivable from
    the id itself; we enforce there too when we can, otherwise
    fall back to auth-only (defense in depth via the parent thread
    endpoint that would have gated the event's discoverability).

    Args:
        event_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> EventDetail | HTTPValidationError | None:
    """Event Detail

     Panel 3 — full detail for one event.

    Event ID shapes are namespaced (same as activation tower):
      <span_id>                        — raw trace_spans row
      write:<prefix>:<key>             — cabinet write
      milestone:<prefix>:<key>         — cabinet write flagged as milestone
      activation_done:<prefix>:<key>   — boot-complete sentinel
      activation_begin:<agent_id>      — synthesized boot-start marker
      checkpoint:<thread_id>:<cid>     — LangGraph state snapshot

    Compliance: for span event ids (raw UUID), fetch the (bot_id,
    source_type, source_id) off the span and enforce the same per-
    source_type ownership check the thread endpoints use. For non-span
    ids (write / milestone / checkpoint) the source is derivable from
    the id itself; we enforce there too when we can, otherwise
    fall back to auth-only (defense in depth via the parent thread
    endpoint that would have gated the event's discoverability).

    Args:
        event_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventDetail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
