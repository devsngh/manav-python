from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sub_agent_user_extension_response import SubAgentUserExtensionResponse
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
        "url": "/api/subagents/{agent_id}/my-extensions".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SubAgentUserExtensionResponse | None:
    if response.status_code == 200:
        response_200 = SubAgentUserExtensionResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SubAgentUserExtensionResponse]:
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
) -> Response[HTTPValidationError | SubAgentUserExtensionResponse]:
    """Get My Subagent Extension

     Get the caller's model override for this subagent. Returns an empty
    row (not 404) when the user hasn't set one — frontend treats absence
    and empty identically. Visibility: caller must be able to see the
    subagent (own or shared). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentUserExtensionResponse]
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
) -> HTTPValidationError | SubAgentUserExtensionResponse | None:
    """Get My Subagent Extension

     Get the caller's model override for this subagent. Returns an empty
    row (not 404) when the user hasn't set one — frontend treats absence
    and empty identically. Visibility: caller must be able to see the
    subagent (own or shared). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentUserExtensionResponse
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
) -> Response[HTTPValidationError | SubAgentUserExtensionResponse]:
    """Get My Subagent Extension

     Get the caller's model override for this subagent. Returns an empty
    row (not 404) when the user hasn't set one — frontend treats absence
    and empty identically. Visibility: caller must be able to see the
    subagent (own or shared). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentUserExtensionResponse]
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
) -> HTTPValidationError | SubAgentUserExtensionResponse | None:
    """Get My Subagent Extension

     Get the caller's model override for this subagent. Returns an empty
    row (not 404) when the user hasn't set one — frontend treats absence
    and empty identically. Visibility: caller must be able to see the
    subagent (own or shared). Otherwise 404 (probe-safe).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentUserExtensionResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
