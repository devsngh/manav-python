from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.score_event_list_response import ScoreEventListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    bot_id: None | Unset | UUID = UNSET,
    event_type: None | str | Unset = UNSET,
    granted_by_role: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    elif isinstance(bot_id, UUID):
        json_bot_id = str(bot_id)
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_event_type: None | str | Unset
    if isinstance(event_type, Unset):
        json_event_type = UNSET
    else:
        json_event_type = event_type
    params["event_type"] = json_event_type

    json_granted_by_role: None | str | Unset
    if isinstance(granted_by_role, Unset):
        json_granted_by_role = UNSET
    else:
        json_granted_by_role = granted_by_role
    params["granted_by_role"] = json_granted_by_role

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/scoring/events",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ScoreEventListResponse | None:
    if response.status_code == 200:
        response_200 = ScoreEventListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ScoreEventListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    bot_id: None | Unset | UUID = UNSET,
    event_type: None | str | Unset = UNSET,
    granted_by_role: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ScoreEventListResponse]:
    """Search Score Events

     Paginated event search with filters.

    Args:
        org_id (UUID): Organization scope
        bot_id (None | Unset | UUID):
        event_type (None | str | Unset):
        granted_by_role (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ScoreEventListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        bot_id=bot_id,
        event_type=event_type,
        granted_by_role=granted_by_role,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    bot_id: None | Unset | UUID = UNSET,
    event_type: None | str | Unset = UNSET,
    granted_by_role: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ScoreEventListResponse | None:
    """Search Score Events

     Paginated event search with filters.

    Args:
        org_id (UUID): Organization scope
        bot_id (None | Unset | UUID):
        event_type (None | str | Unset):
        granted_by_role (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ScoreEventListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        bot_id=bot_id,
        event_type=event_type,
        granted_by_role=granted_by_role,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    bot_id: None | Unset | UUID = UNSET,
    event_type: None | str | Unset = UNSET,
    granted_by_role: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ScoreEventListResponse]:
    """Search Score Events

     Paginated event search with filters.

    Args:
        org_id (UUID): Organization scope
        bot_id (None | Unset | UUID):
        event_type (None | str | Unset):
        granted_by_role (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ScoreEventListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        bot_id=bot_id,
        event_type=event_type,
        granted_by_role=granted_by_role,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    bot_id: None | Unset | UUID = UNSET,
    event_type: None | str | Unset = UNSET,
    granted_by_role: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ScoreEventListResponse | None:
    """Search Score Events

     Paginated event search with filters.

    Args:
        org_id (UUID): Organization scope
        bot_id (None | Unset | UUID):
        event_type (None | str | Unset):
        granted_by_role (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ScoreEventListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            bot_id=bot_id,
            event_type=event_type,
            granted_by_role=granted_by_role,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
