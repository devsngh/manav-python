from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_life_mode_request import AgentLifeModeRequest
from ...models.agent_life_mode_response import AgentLifeModeResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: AgentLifeModeRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/society/agents/{name}/life-mode".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentLifeModeResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentLifeModeResponse.from_dict(response.json())

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
) -> Response[AgentLifeModeResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentLifeModeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentLifeModeResponse | HTTPValidationError]:
    """Post Agent Life Mode

     Flip the per-agent life_mode_enabled flag.

    Returns 404 if the agent does not exist.
    Returns 409 if attempting to enable an agent whose eligibility='none'.

    Args:
        name (str):
        authorization (None | str | Unset): Bearer token
        body (AgentLifeModeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentLifeModeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentLifeModeRequest,
    authorization: None | str | Unset = UNSET,
) -> AgentLifeModeResponse | HTTPValidationError | None:
    """Post Agent Life Mode

     Flip the per-agent life_mode_enabled flag.

    Returns 404 if the agent does not exist.
    Returns 409 if attempting to enable an agent whose eligibility='none'.

    Args:
        name (str):
        authorization (None | str | Unset): Bearer token
        body (AgentLifeModeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentLifeModeResponse | HTTPValidationError
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentLifeModeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentLifeModeResponse | HTTPValidationError]:
    """Post Agent Life Mode

     Flip the per-agent life_mode_enabled flag.

    Returns 404 if the agent does not exist.
    Returns 409 if attempting to enable an agent whose eligibility='none'.

    Args:
        name (str):
        authorization (None | str | Unset): Bearer token
        body (AgentLifeModeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentLifeModeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: AgentLifeModeRequest,
    authorization: None | str | Unset = UNSET,
) -> AgentLifeModeResponse | HTTPValidationError | None:
    """Post Agent Life Mode

     Flip the per-agent life_mode_enabled flag.

    Returns 404 if the agent does not exist.
    Returns 409 if attempting to enable an agent whose eligibility='none'.

    Args:
        name (str):
        authorization (None | str | Unset): Bearer token
        body (AgentLifeModeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentLifeModeResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
