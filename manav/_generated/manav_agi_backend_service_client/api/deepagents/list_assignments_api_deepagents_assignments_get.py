from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assignment_target_type import AssignmentTargetType
from ...models.deep_agent_assign_list_response import DeepAgentAssignListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | str | Unset = UNSET,
    target_type: AssignmentTargetType | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_target_type: None | str | Unset
    if isinstance(target_type, Unset):
        json_target_type = UNSET
    elif isinstance(target_type, AssignmentTargetType):
        json_target_type = target_type.value
    else:
        json_target_type = target_type
    params["target_type"] = json_target_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents/assignments",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentAssignListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeepAgentAssignListResponse.from_dict(response.json())

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
) -> Response[DeepAgentAssignListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    target_type: AssignmentTargetType | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentAssignListResponse | HTTPValidationError]:
    """List Assignments

     List all active assignments, optionally filtered by DeepAgent or target type

    Args:
        agent_id (None | str | Unset):
        target_type (AssignmentTargetType | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentAssignListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        target_type=target_type,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    target_type: AssignmentTargetType | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentAssignListResponse | HTTPValidationError | None:
    """List Assignments

     List all active assignments, optionally filtered by DeepAgent or target type

    Args:
        agent_id (None | str | Unset):
        target_type (AssignmentTargetType | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentAssignListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        target_type=target_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    target_type: AssignmentTargetType | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentAssignListResponse | HTTPValidationError]:
    """List Assignments

     List all active assignments, optionally filtered by DeepAgent or target type

    Args:
        agent_id (None | str | Unset):
        target_type (AssignmentTargetType | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentAssignListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        target_type=target_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | str | Unset = UNSET,
    target_type: AssignmentTargetType | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentAssignListResponse | HTTPValidationError | None:
    """List Assignments

     List all active assignments, optionally filtered by DeepAgent or target type

    Args:
        agent_id (None | str | Unset):
        target_type (AssignmentTargetType | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentAssignListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            target_type=target_type,
            authorization=authorization,
        )
    ).parsed
