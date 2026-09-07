from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agents_md_version_list_response import AgentsMdVersionListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents/{agent_id}/agents-md/versions".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentsMdVersionListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentsMdVersionListResponse.from_dict(response.json())

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
) -> Response[AgentsMdVersionListResponse | HTTPValidationError]:
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
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentsMdVersionListResponse | HTTPValidationError]:
    """List Agents Md Versions

     List version history of AGENTS.md for a DeepAgent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsMdVersionListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        page_size=page_size,
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
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> AgentsMdVersionListResponse | HTTPValidationError | None:
    """List Agents Md Versions

     List version history of AGENTS.md for a DeepAgent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsMdVersionListResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentsMdVersionListResponse | HTTPValidationError]:
    """List Agents Md Versions

     List version history of AGENTS.md for a DeepAgent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentsMdVersionListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> AgentsMdVersionListResponse | HTTPValidationError | None:
    """List Agents Md Versions

     List version history of AGENTS.md for a DeepAgent (own-scoped: your own only; admin: any).

    Args:
        agent_id (str):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentsMdVersionListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
