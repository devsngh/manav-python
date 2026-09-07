from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.rubric_assignment_list_response import RubricAssignmentListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent_id: None | Unset | UUID = UNSET,
    rubric_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_agent_id: None | str | Unset
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    elif isinstance(agent_id, UUID):
        json_agent_id = str(agent_id)
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_rubric_id: None | str | Unset
    if isinstance(rubric_id, Unset):
        json_rubric_id = UNSET
    elif isinstance(rubric_id, UUID):
        json_rubric_id = str(rubric_id)
    else:
        json_rubric_id = rubric_id
    params["rubric_id"] = json_rubric_id

    params["active_only"] = active_only

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/rubric-assignments",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | RubricAssignmentListResponse | None:
    if response.status_code == 200:
        response_200 = RubricAssignmentListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | RubricAssignmentListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    rubric_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RubricAssignmentListResponse]:
    """List Assignments

    Args:
        agent_id (None | Unset | UUID):
        rubric_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RubricAssignmentListResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        rubric_id=rubric_id,
        active_only=active_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    rubric_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RubricAssignmentListResponse | None:
    """List Assignments

    Args:
        agent_id (None | Unset | UUID):
        rubric_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RubricAssignmentListResponse
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        rubric_id=rubric_id,
        active_only=active_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    rubric_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | RubricAssignmentListResponse]:
    """List Assignments

    Args:
        agent_id (None | Unset | UUID):
        rubric_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | RubricAssignmentListResponse]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        rubric_id=rubric_id,
        active_only=active_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    agent_id: None | Unset | UUID = UNSET,
    rubric_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | RubricAssignmentListResponse | None:
    """List Assignments

    Args:
        agent_id (None | Unset | UUID):
        rubric_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | RubricAssignmentListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            rubric_id=rubric_id,
            active_only=active_only,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
