from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deep_agent_user_extension_response import DeepAgentUserExtensionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents/{agent_id}/my-extensions".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentUserExtensionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeepAgentUserExtensionResponse.from_dict(response.json())

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
) -> Response[DeepAgentUserExtensionResponse | HTTPValidationError]:
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
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentUserExtensionResponse | HTTPValidationError]:
    """Get My Extension

     Get the caller's extension overlay for this agent.

    Returns an all-empty response (not 404) when the user has no
    extensions yet — the frontend treats absence and empty identically.

    Visibility: caller must be able to see the agent via any P2 path
    (owned, assigned, or rented). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentUserExtensionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
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
    authorization: None | str | Unset = UNSET,
) -> DeepAgentUserExtensionResponse | HTTPValidationError | None:
    """Get My Extension

     Get the caller's extension overlay for this agent.

    Returns an all-empty response (not 404) when the user has no
    extensions yet — the frontend treats absence and empty identically.

    Visibility: caller must be able to see the agent via any P2 path
    (owned, assigned, or rented). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentUserExtensionResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentUserExtensionResponse | HTTPValidationError]:
    """Get My Extension

     Get the caller's extension overlay for this agent.

    Returns an all-empty response (not 404) when the user has no
    extensions yet — the frontend treats absence and empty identically.

    Visibility: caller must be able to see the agent via any P2 path
    (owned, assigned, or rented). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentUserExtensionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentUserExtensionResponse | HTTPValidationError | None:
    """Get My Extension

     Get the caller's extension overlay for this agent.

    Returns an all-empty response (not 404) when the user has no
    extensions yet — the frontend treats absence and empty identically.

    Visibility: caller must be able to see the agent via any P2 path
    (owned, assigned, or rented). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentUserExtensionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
