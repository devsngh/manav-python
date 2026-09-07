from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agents_md_version_response import AgentsMdVersionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    version_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents/{agent_id}/agents-md/versions/{version_id}".format(
            agent_id=quote(str(agent_id), safe=""),
            version_id=quote(str(version_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentsMdVersionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentsMdVersionResponse.from_dict(response.json())

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
) -> Response[AgentsMdVersionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentsMdVersionResponse | HTTPValidationError]:
    """Get Agents Md Version

     Get a specific AGENTS.md version snapshot (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        version_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsMdVersionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        version_id=version_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> AgentsMdVersionResponse | HTTPValidationError | None:
    """Get Agents Md Version

     Get a specific AGENTS.md version snapshot (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        version_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsMdVersionResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        version_id=version_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentsMdVersionResponse | HTTPValidationError]:
    """Get Agents Md Version

     Get a specific AGENTS.md version snapshot (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        version_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsMdVersionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        version_id=version_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    version_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> AgentsMdVersionResponse | HTTPValidationError | None:
    """Get Agents Md Version

     Get a specific AGENTS.md version snapshot (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        version_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsMdVersionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            version_id=version_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
