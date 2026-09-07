from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    window_minutes: int | Unset = 15,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["window_minutes"] = window_minutes

    json_focus_user_id: None | str | Unset
    if isinstance(focus_user_id, Unset):
        json_focus_user_id = UNSET
    else:
        json_focus_user_id = focus_user_id
    params["focus_user_id"] = json_focus_user_id

    json_focus_bot_id: None | str | Unset
    if isinstance(focus_bot_id, Unset):
        json_focus_bot_id = UNSET
    else:
        json_focus_bot_id = focus_bot_id
    params["focus_bot_id"] = json_focus_bot_id

    json_focus_org_id: None | str | Unset
    if isinstance(focus_org_id, Unset):
        json_focus_org_id = UNSET
    else:
        json_focus_org_id = focus_org_id
    params["focus_org_id"] = json_focus_org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/system-logs/traces/whiteboard",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
    window_minutes: int | Unset = 15,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Trace Whiteboard

     Trace Explorer "Now" mode — narrative-first landing view.

    Returns a single payload answering "is anything broken right now?":
    per-category health, unresolved errors, slow endpoints, traffic
    sparkline + baseline comparison. Probes are excluded from the health
    aggregate (else 40k healthy probes drown out real errors).

    Args:
        window_minutes (int | Unset): Window in minutes (1-1440) Default: 15.
        focus_user_id (None | str | Unset): Filter to one user
        focus_bot_id (None | str | Unset): Filter to one bot
        focus_org_id (None | str | Unset): Filter to one org
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        window_minutes=window_minutes,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    window_minutes: int | Unset = 15,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Trace Whiteboard

     Trace Explorer "Now" mode — narrative-first landing view.

    Returns a single payload answering "is anything broken right now?":
    per-category health, unresolved errors, slow endpoints, traffic
    sparkline + baseline comparison. Probes are excluded from the health
    aggregate (else 40k healthy probes drown out real errors).

    Args:
        window_minutes (int | Unset): Window in minutes (1-1440) Default: 15.
        focus_user_id (None | str | Unset): Filter to one user
        focus_bot_id (None | str | Unset): Filter to one bot
        focus_org_id (None | str | Unset): Filter to one org
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        window_minutes=window_minutes,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    window_minutes: int | Unset = 15,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Trace Whiteboard

     Trace Explorer "Now" mode — narrative-first landing view.

    Returns a single payload answering "is anything broken right now?":
    per-category health, unresolved errors, slow endpoints, traffic
    sparkline + baseline comparison. Probes are excluded from the health
    aggregate (else 40k healthy probes drown out real errors).

    Args:
        window_minutes (int | Unset): Window in minutes (1-1440) Default: 15.
        focus_user_id (None | str | Unset): Filter to one user
        focus_bot_id (None | str | Unset): Filter to one bot
        focus_org_id (None | str | Unset): Filter to one org
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        window_minutes=window_minutes,
        focus_user_id=focus_user_id,
        focus_bot_id=focus_bot_id,
        focus_org_id=focus_org_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    window_minutes: int | Unset = 15,
    focus_user_id: None | str | Unset = UNSET,
    focus_bot_id: None | str | Unset = UNSET,
    focus_org_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Trace Whiteboard

     Trace Explorer "Now" mode — narrative-first landing view.

    Returns a single payload answering "is anything broken right now?":
    per-category health, unresolved errors, slow endpoints, traffic
    sparkline + baseline comparison. Probes are excluded from the health
    aggregate (else 40k healthy probes drown out real errors).

    Args:
        window_minutes (int | Unset): Window in minutes (1-1440) Default: 15.
        focus_user_id (None | str | Unset): Filter to one user
        focus_bot_id (None | str | Unset): Filter to one bot
        focus_org_id (None | str | Unset): Filter to one org
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            window_minutes=window_minutes,
            focus_user_id=focus_user_id,
            focus_bot_id=focus_bot_id,
            focus_org_id=focus_org_id,
            authorization=authorization,
        )
    ).parsed
