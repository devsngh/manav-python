from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deep_agent_assign_response import DeepAgentAssignResponse
from ...models.deep_agent_assign_update import DeepAgentAssignUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    assignment_id: str,
    *,
    body: DeepAgentAssignUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/deepagents/assignments/{assignment_id}".format(
            assignment_id=quote(str(assignment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentAssignResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeepAgentAssignResponse.from_dict(response.json())

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
) -> Response[DeepAgentAssignResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assignment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeepAgentAssignUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentAssignResponse | HTTPValidationError]:
    """Update Assignment

     Update fields of an existing assignment (agent, target_type,
    target_id, target_label). Any subset can be sent.

    Args:
        assignment_id (str):
        authorization (None | str | Unset): Bearer token
        body (DeepAgentAssignUpdate): PATCH — any subset. deepagent_id lets you re-point the
            assignment
            at a different catalog agent without deleting + recreating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentAssignResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assignment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeepAgentAssignUpdate,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentAssignResponse | HTTPValidationError | None:
    """Update Assignment

     Update fields of an existing assignment (agent, target_type,
    target_id, target_label). Any subset can be sent.

    Args:
        assignment_id (str):
        authorization (None | str | Unset): Bearer token
        body (DeepAgentAssignUpdate): PATCH — any subset. deepagent_id lets you re-point the
            assignment
            at a different catalog agent without deleting + recreating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentAssignResponse | HTTPValidationError
    """

    return sync_detailed(
        assignment_id=assignment_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    assignment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeepAgentAssignUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentAssignResponse | HTTPValidationError]:
    """Update Assignment

     Update fields of an existing assignment (agent, target_type,
    target_id, target_label). Any subset can be sent.

    Args:
        assignment_id (str):
        authorization (None | str | Unset): Bearer token
        body (DeepAgentAssignUpdate): PATCH — any subset. deepagent_id lets you re-point the
            assignment
            at a different catalog agent without deleting + recreating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentAssignResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        assignment_id=assignment_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assignment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DeepAgentAssignUpdate,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentAssignResponse | HTTPValidationError | None:
    """Update Assignment

     Update fields of an existing assignment (agent, target_type,
    target_id, target_label). Any subset can be sent.

    Args:
        assignment_id (str):
        authorization (None | str | Unset): Bearer token
        body (DeepAgentAssignUpdate): PATCH — any subset. deepagent_id lets you re-point the
            assignment
            at a different catalog agent without deleting + recreating.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentAssignResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            assignment_id=assignment_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
