from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hil_event_escalate import HILEventEscalate
from ...models.hil_event_response import HILEventResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    body: HILEventEscalate,
    user_id: str,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["user_id"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/hil-events/{event_id}/escalate".format(
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HILEventResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = HILEventResponse.from_dict(response.json())

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
) -> Response[HILEventResponse | HTTPValidationError]:
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
    body: HILEventEscalate,
    user_id: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HILEventResponse | HTTPValidationError]:
    """Escalate Hil Event

     Escalate a pending HIL event one position-level up the org chart.

    Resolution walks positions.reports_to_position_id (+ position_reporting
    sidecar for global agents); falls back to Organization.created_by_user_id
    if top-of-chain. Returns the newly created CHILD HIL event; the parent's
    status flips to 'escalated'.

    Args:
        event_id (str):
        user_id (str): User UUID escalating the event
        authorization (None | str | Unset): Bearer token
        body (HILEventEscalate): Body for POST /hil-events/{id}/escalate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILEventResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
        user_id=user_id,
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
    body: HILEventEscalate,
    user_id: str,
    authorization: None | str | Unset = UNSET,
) -> HILEventResponse | HTTPValidationError | None:
    """Escalate Hil Event

     Escalate a pending HIL event one position-level up the org chart.

    Resolution walks positions.reports_to_position_id (+ position_reporting
    sidecar for global agents); falls back to Organization.created_by_user_id
    if top-of-chain. Returns the newly created CHILD HIL event; the parent's
    status flips to 'escalated'.

    Args:
        event_id (str):
        user_id (str): User UUID escalating the event
        authorization (None | str | Unset): Bearer token
        body (HILEventEscalate): Body for POST /hil-events/{id}/escalate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILEventResponse | HTTPValidationError
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
        user_id=user_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HILEventEscalate,
    user_id: str,
    authorization: None | str | Unset = UNSET,
) -> Response[HILEventResponse | HTTPValidationError]:
    """Escalate Hil Event

     Escalate a pending HIL event one position-level up the org chart.

    Resolution walks positions.reports_to_position_id (+ position_reporting
    sidecar for global agents); falls back to Organization.created_by_user_id
    if top-of-chain. Returns the newly created CHILD HIL event; the parent's
    status flips to 'escalated'.

    Args:
        event_id (str):
        user_id (str): User UUID escalating the event
        authorization (None | str | Unset): Bearer token
        body (HILEventEscalate): Body for POST /hil-events/{id}/escalate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILEventResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
        user_id=user_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: HILEventEscalate,
    user_id: str,
    authorization: None | str | Unset = UNSET,
) -> HILEventResponse | HTTPValidationError | None:
    """Escalate Hil Event

     Escalate a pending HIL event one position-level up the org chart.

    Resolution walks positions.reports_to_position_id (+ position_reporting
    sidecar for global agents); falls back to Organization.created_by_user_id
    if top-of-chain. Returns the newly created CHILD HIL event; the parent's
    status flips to 'escalated'.

    Args:
        event_id (str):
        user_id (str): User UUID escalating the event
        authorization (None | str | Unset): Bearer token
        body (HILEventEscalate): Body for POST /hil-events/{id}/escalate.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILEventResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
            user_id=user_id,
            authorization=authorization,
        )
    ).parsed
