from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sub_agent_response import SubAgentResponse
from ...models.sub_agent_update import SubAgentUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: SubAgentUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/subagents/{agent_id}".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SubAgentResponse | None:
    if response.status_code == 200:
        response_200 = SubAgentResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SubAgentResponse]:
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
    body: SubAgentUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SubAgentResponse]:
    """Update Subagent

     Update a subagent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (SubAgentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentResponse]
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
    body: SubAgentUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SubAgentResponse | None:
    """Update Subagent

     Update a subagent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (SubAgentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentResponse
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
    body: SubAgentUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SubAgentResponse]:
    """Update Subagent

     Update a subagent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (SubAgentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SubAgentResponse]
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
    body: SubAgentUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SubAgentResponse | None:
    """Update Subagent

     Update a subagent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        authorization (None | str | Unset): Bearer token
        body (SubAgentUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SubAgentResponse
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
