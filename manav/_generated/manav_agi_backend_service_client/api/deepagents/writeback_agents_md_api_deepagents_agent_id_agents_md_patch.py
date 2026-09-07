from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agents_md_write_back import AgentsMdWriteBack
from ...models.deep_agent_response import DeepAgentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: AgentsMdWriteBack,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/deepagents/{agent_id}/agents-md".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeepAgentResponse.from_dict(response.json())

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
) -> Response[DeepAgentResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsMdWriteBack,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentResponse | HTTPValidationError]:
    """Writeback Agents Md

     Update agents.md content for a DeepAgent.

    Two auth paths (orchestrator service vs. user/agent flow):

      (a) Service path — orchestrator writes back after execution.
          Caller MUST present a matching ``X-Internal-API-Key`` header AND
          ``INTERNAL_API_KEY`` must be configured server-side. Bypasses the
          owner check (service trust boundary).

      (b) User path — agent / human updates its own memory.
          Caller MUST present a valid JWT (``Authorization: Bearer ...``) AND
          own the DeepAgent. Super-admins may update any DeepAgent.

    If neither auth path is satisfied, returns 401. This closes the previous
    fail-open gap: when ``INTERNAL_API_KEY`` was unset in dev, the route used
    to skip the key check and fall through to a 404 lookup, which let anyone
    enumerate or rewrite agents whose UUID they could guess.

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (AgentsMdWriteBack):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsMdWriteBack,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentResponse | HTTPValidationError | None:
    """Writeback Agents Md

     Update agents.md content for a DeepAgent.

    Two auth paths (orchestrator service vs. user/agent flow):

      (a) Service path — orchestrator writes back after execution.
          Caller MUST present a matching ``X-Internal-API-Key`` header AND
          ``INTERNAL_API_KEY`` must be configured server-side. Bypasses the
          owner check (service trust boundary).

      (b) User path — agent / human updates its own memory.
          Caller MUST present a valid JWT (``Authorization: Bearer ...``) AND
          own the DeepAgent. Super-admins may update any DeepAgent.

    If neither auth path is satisfied, returns 401. This closes the previous
    fail-open gap: when ``INTERNAL_API_KEY`` was unset in dev, the route used
    to skip the key check and fall through to a 404 lookup, which let anyone
    enumerate or rewrite agents whose UUID they could guess.

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (AgentsMdWriteBack):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsMdWriteBack,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentResponse | HTTPValidationError]:
    """Writeback Agents Md

     Update agents.md content for a DeepAgent.

    Two auth paths (orchestrator service vs. user/agent flow):

      (a) Service path — orchestrator writes back after execution.
          Caller MUST present a matching ``X-Internal-API-Key`` header AND
          ``INTERNAL_API_KEY`` must be configured server-side. Bypasses the
          owner check (service trust boundary).

      (b) User path — agent / human updates its own memory.
          Caller MUST present a valid JWT (``Authorization: Bearer ...``) AND
          own the DeepAgent. Super-admins may update any DeepAgent.

    If neither auth path is satisfied, returns 401. This closes the previous
    fail-open gap: when ``INTERNAL_API_KEY`` was unset in dev, the route used
    to skip the key check and fall through to a 404 lookup, which let anyone
    enumerate or rewrite agents whose UUID they could guess.

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (AgentsMdWriteBack):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentsMdWriteBack,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentResponse | HTTPValidationError | None:
    """Writeback Agents Md

     Update agents.md content for a DeepAgent.

    Two auth paths (orchestrator service vs. user/agent flow):

      (a) Service path — orchestrator writes back after execution.
          Caller MUST present a matching ``X-Internal-API-Key`` header AND
          ``INTERNAL_API_KEY`` must be configured server-side. Bypasses the
          owner check (service trust boundary).

      (b) User path — agent / human updates its own memory.
          Caller MUST present a valid JWT (``Authorization: Bearer ...``) AND
          own the DeepAgent. Super-admins may update any DeepAgent.

    If neither auth path is satisfied, returns 401. This closes the previous
    fail-open gap: when ``INTERNAL_API_KEY`` was unset in dev, the route used
    to skip the key check and fall through to a 404 lookup, which let anyone
    enumerate or rewrite agents whose UUID they could guess.

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (AgentsMdWriteBack):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
