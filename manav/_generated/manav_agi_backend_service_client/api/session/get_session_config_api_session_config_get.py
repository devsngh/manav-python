from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.session_config import SessionConfig
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    prefer_bot_id: None | str | Unset = UNSET,
    deepagent_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_role_id: None | str | Unset
    if isinstance(role_id, Unset):
        json_role_id = UNSET
    else:
        json_role_id = role_id
    params["role_id"] = json_role_id

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_prefer_bot_id: None | str | Unset
    if isinstance(prefer_bot_id, Unset):
        json_prefer_bot_id = UNSET
    else:
        json_prefer_bot_id = prefer_bot_id
    params["prefer_bot_id"] = json_prefer_bot_id

    json_deepagent_id: None | str | Unset
    if isinstance(deepagent_id, Unset):
        json_deepagent_id = UNSET
    else:
        json_deepagent_id = deepagent_id
    params["deepagent_id"] = json_deepagent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/config",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SessionConfig | None:
    if response.status_code == 200:
        response_200 = SessionConfig.from_dict(response.json())

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
) -> Response[HTTPValidationError | SessionConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    prefer_bot_id: None | str | Unset = UNSET,
    deepagent_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SessionConfig]:
    """Get Session Config

     Build and return a complete session configuration for an agent session.

    Resolves the active DeepAgent for the given user/role context,
    then hydrates all referenced IDs into full objects:
    - system_prompt: compiled prompt text
    - tools: tool metadata + datasource info (including mcp_path)
    - hil_rules: HIL rule details
    - subagents: subagent configs available for spawning
    - skills: resolved skill definitions for SKILL.md generation

    Called by the orchestrator at chat session / thread start.
    Priority: deepagent_id > prefer_bot_id > user > role > default

    Args:
        user_id (None | str | Unset): User UUID — resolves user or role/default assignment
        org_id (None | str | Unset): Organisation UUID — used for org-scoped tool filtering
        role_id (None | str | Unset): Role UUID — resolves role or default assignment
        bot_id (None | str | Unset): Bot UUID — for credential resolution
        prefer_bot_id (None | str | Unset): Bot UUID to resolve architecture from (overrides user
            assignment)
        deepagent_id (None | str | Unset): DeepAgentConfig UUID — directly resolve this config,
            bypassing assignment chain
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionConfig]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        org_id=org_id,
        role_id=role_id,
        bot_id=bot_id,
        prefer_bot_id=prefer_bot_id,
        deepagent_id=deepagent_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    prefer_bot_id: None | str | Unset = UNSET,
    deepagent_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SessionConfig | None:
    """Get Session Config

     Build and return a complete session configuration for an agent session.

    Resolves the active DeepAgent for the given user/role context,
    then hydrates all referenced IDs into full objects:
    - system_prompt: compiled prompt text
    - tools: tool metadata + datasource info (including mcp_path)
    - hil_rules: HIL rule details
    - subagents: subagent configs available for spawning
    - skills: resolved skill definitions for SKILL.md generation

    Called by the orchestrator at chat session / thread start.
    Priority: deepagent_id > prefer_bot_id > user > role > default

    Args:
        user_id (None | str | Unset): User UUID — resolves user or role/default assignment
        org_id (None | str | Unset): Organisation UUID — used for org-scoped tool filtering
        role_id (None | str | Unset): Role UUID — resolves role or default assignment
        bot_id (None | str | Unset): Bot UUID — for credential resolution
        prefer_bot_id (None | str | Unset): Bot UUID to resolve architecture from (overrides user
            assignment)
        deepagent_id (None | str | Unset): DeepAgentConfig UUID — directly resolve this config,
            bypassing assignment chain
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionConfig
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        org_id=org_id,
        role_id=role_id,
        bot_id=bot_id,
        prefer_bot_id=prefer_bot_id,
        deepagent_id=deepagent_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    prefer_bot_id: None | str | Unset = UNSET,
    deepagent_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SessionConfig]:
    """Get Session Config

     Build and return a complete session configuration for an agent session.

    Resolves the active DeepAgent for the given user/role context,
    then hydrates all referenced IDs into full objects:
    - system_prompt: compiled prompt text
    - tools: tool metadata + datasource info (including mcp_path)
    - hil_rules: HIL rule details
    - subagents: subagent configs available for spawning
    - skills: resolved skill definitions for SKILL.md generation

    Called by the orchestrator at chat session / thread start.
    Priority: deepagent_id > prefer_bot_id > user > role > default

    Args:
        user_id (None | str | Unset): User UUID — resolves user or role/default assignment
        org_id (None | str | Unset): Organisation UUID — used for org-scoped tool filtering
        role_id (None | str | Unset): Role UUID — resolves role or default assignment
        bot_id (None | str | Unset): Bot UUID — for credential resolution
        prefer_bot_id (None | str | Unset): Bot UUID to resolve architecture from (overrides user
            assignment)
        deepagent_id (None | str | Unset): DeepAgentConfig UUID — directly resolve this config,
            bypassing assignment chain
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SessionConfig]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        org_id=org_id,
        role_id=role_id,
        bot_id=bot_id,
        prefer_bot_id=prefer_bot_id,
        deepagent_id=deepagent_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    prefer_bot_id: None | str | Unset = UNSET,
    deepagent_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SessionConfig | None:
    """Get Session Config

     Build and return a complete session configuration for an agent session.

    Resolves the active DeepAgent for the given user/role context,
    then hydrates all referenced IDs into full objects:
    - system_prompt: compiled prompt text
    - tools: tool metadata + datasource info (including mcp_path)
    - hil_rules: HIL rule details
    - subagents: subagent configs available for spawning
    - skills: resolved skill definitions for SKILL.md generation

    Called by the orchestrator at chat session / thread start.
    Priority: deepagent_id > prefer_bot_id > user > role > default

    Args:
        user_id (None | str | Unset): User UUID — resolves user or role/default assignment
        org_id (None | str | Unset): Organisation UUID — used for org-scoped tool filtering
        role_id (None | str | Unset): Role UUID — resolves role or default assignment
        bot_id (None | str | Unset): Bot UUID — for credential resolution
        prefer_bot_id (None | str | Unset): Bot UUID to resolve architecture from (overrides user
            assignment)
        deepagent_id (None | str | Unset): DeepAgentConfig UUID — directly resolve this config,
            bypassing assignment chain
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SessionConfig
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            org_id=org_id,
            role_id=role_id,
            bot_id=bot_id,
            prefer_bot_id=prefer_bot_id,
            deepagent_id=deepagent_id,
            authorization=authorization,
        )
    ).parsed
