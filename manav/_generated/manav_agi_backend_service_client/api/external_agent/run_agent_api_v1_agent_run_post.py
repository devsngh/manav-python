from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_run_request import AgentRunRequest
from ...models.agent_run_response import AgentRunResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AgentRunRequest,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    headers["X-API-Key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/agent/run",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentRunResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentRunResponse.from_dict(response.json())

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
) -> Response[AgentRunResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Run Agent

     Execute an agent via API key.
    Resolves the user/org/agent from the key, calls the orchestrator, returns the response.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> AgentRunResponse | HTTPValidationError | None:
    """Run Agent

     Execute an agent via API key.
    Resolves the user/org/agent from the key, calls the orchestrator, returns the response.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> Response[AgentRunResponse | HTTPValidationError]:
    """Run Agent

     Execute an agent via API key.
    Resolves the user/org/agent from the key, calls the orchestrator, returns the response.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRunResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AgentRunRequest,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> AgentRunResponse | HTTPValidationError | None:
    """Run Agent

     Execute an agent via API key.
    Resolves the user/org/agent from the key, calls the orchestrator, returns the response.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):
        body (AgentRunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRunResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
            x_api_key=x_api_key,
        )
    ).parsed
