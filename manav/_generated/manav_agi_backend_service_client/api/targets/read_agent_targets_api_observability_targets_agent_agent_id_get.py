from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_target_list_response import AgentTargetListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: UUID,
    *,
    org_id: UUID,
    status: None | str | Unset = UNSET,
    window: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_window: None | str | Unset
    if isinstance(window, Unset):
        json_window = UNSET
    else:
        json_window = window
    params["window"] = json_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/targets/agent/{agent_id}".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentTargetListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentTargetListResponse.from_dict(response.json())

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
) -> Response[AgentTargetListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    status: None | str | Unset = UNSET,
    window: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentTargetListResponse | HTTPValidationError]:
    """Read Agent Targets

     All targets for one agent (the canonical agent self-read).

    Args:
        agent_id (UUID):
        org_id (UUID):
        status (None | str | Unset):
        window (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTargetListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        org_id=org_id,
        status=status,
        window=window,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    status: None | str | Unset = UNSET,
    window: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> AgentTargetListResponse | HTTPValidationError | None:
    """Read Agent Targets

     All targets for one agent (the canonical agent self-read).

    Args:
        agent_id (UUID):
        org_id (UUID):
        status (None | str | Unset):
        window (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTargetListResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        org_id=org_id,
        status=status,
        window=window,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    status: None | str | Unset = UNSET,
    window: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentTargetListResponse | HTTPValidationError]:
    """Read Agent Targets

     All targets for one agent (the canonical agent self-read).

    Args:
        agent_id (UUID):
        org_id (UUID):
        status (None | str | Unset):
        window (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTargetListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        org_id=org_id,
        status=status,
        window=window,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    status: None | str | Unset = UNSET,
    window: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> AgentTargetListResponse | HTTPValidationError | None:
    """Read Agent Targets

     All targets for one agent (the canonical agent self-read).

    Args:
        agent_id (UUID):
        org_id (UUID):
        status (None | str | Unset):
        window (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTargetListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            org_id=org_id,
            status=status,
            window=window,
            authorization=authorization,
        )
    ).parsed
