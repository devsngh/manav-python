from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: None | str | Unset = UNSET,
    for_user_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_for_user_id: None | str | Unset
    if isinstance(for_user_id, Unset):
        json_for_user_id = UNSET
    else:
        json_for_user_id = for_user_id
    params["for_user_id"] = json_for_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/directory",
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
    org_id: None | str | Unset = UNSET,
    for_user_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Org Directory

     Return a compact org directory for context injection into agent system prompts.
    Includes departments, bots, positions — everything the agent needs to resolve
    identities without making multiple tool calls.

    Called once at session start by the orchestrator's context_builder. When
    `for_user_id` is set, the response's `bots` list is expanded to include
    bots for agents the user has ACCESS to (assigned or rented) beyond just
    their org — so a rented agent shows up as a colleague of the renter's
    other bots, and vice-versa.

    Args:
        org_id (None | str | Unset):
        for_user_id (None | str | Unset): When set, directory is scoped to this user's world —
            includes the user's org bots PLUS bots for agents they have assigned or rented (cross-org
            access). Beta agent-architecture P2. When absent, behavior is unchanged (org-only).
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        for_user_id=for_user_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | str | Unset = UNSET,
    for_user_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Org Directory

     Return a compact org directory for context injection into agent system prompts.
    Includes departments, bots, positions — everything the agent needs to resolve
    identities without making multiple tool calls.

    Called once at session start by the orchestrator's context_builder. When
    `for_user_id` is set, the response's `bots` list is expanded to include
    bots for agents the user has ACCESS to (assigned or rented) beyond just
    their org — so a rented agent shows up as a colleague of the renter's
    other bots, and vice-versa.

    Args:
        org_id (None | str | Unset):
        for_user_id (None | str | Unset): When set, directory is scoped to this user's world —
            includes the user's org bots PLUS bots for agents they have assigned or rented (cross-org
            access). Beta agent-architecture P2. When absent, behavior is unchanged (org-only).
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        for_user_id=for_user_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | str | Unset = UNSET,
    for_user_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Org Directory

     Return a compact org directory for context injection into agent system prompts.
    Includes departments, bots, positions — everything the agent needs to resolve
    identities without making multiple tool calls.

    Called once at session start by the orchestrator's context_builder. When
    `for_user_id` is set, the response's `bots` list is expanded to include
    bots for agents the user has ACCESS to (assigned or rented) beyond just
    their org — so a rented agent shows up as a colleague of the renter's
    other bots, and vice-versa.

    Args:
        org_id (None | str | Unset):
        for_user_id (None | str | Unset): When set, directory is scoped to this user's world —
            includes the user's org bots PLUS bots for agents they have assigned or rented (cross-org
            access). Beta agent-architecture P2. When absent, behavior is unchanged (org-only).
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        for_user_id=for_user_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | str | Unset = UNSET,
    for_user_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Org Directory

     Return a compact org directory for context injection into agent system prompts.
    Includes departments, bots, positions — everything the agent needs to resolve
    identities without making multiple tool calls.

    Called once at session start by the orchestrator's context_builder. When
    `for_user_id` is set, the response's `bots` list is expanded to include
    bots for agents the user has ACCESS to (assigned or rented) beyond just
    their org — so a rented agent shows up as a colleague of the renter's
    other bots, and vice-versa.

    Args:
        org_id (None | str | Unset):
        for_user_id (None | str | Unset): When set, directory is scoped to this user's world —
            includes the user's org bots PLUS bots for agents they have assigned or rented (cross-org
            access). Beta agent-architecture P2. When absent, behavior is unchanged (org-only).
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            for_user_id=for_user_id,
            authorization=authorization,
        )
    ).parsed
