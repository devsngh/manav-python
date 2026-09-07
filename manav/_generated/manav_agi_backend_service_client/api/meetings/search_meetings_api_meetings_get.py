from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_list_response import MeetingListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    meeting_type: None | str | Unset = UNSET,
    chair_id: None | Unset | UUID = UNSET,
    department_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    json_meeting_type: None | str | Unset
    if isinstance(meeting_type, Unset):
        json_meeting_type = UNSET
    else:
        json_meeting_type = meeting_type
    params["meeting_type"] = json_meeting_type

    json_chair_id: None | str | Unset
    if isinstance(chair_id, Unset):
        json_chair_id = UNSET
    elif isinstance(chair_id, UUID):
        json_chair_id = str(chair_id)
    else:
        json_chair_id = chair_id
    params["chair_id"] = json_chair_id

    json_department_id: None | str | Unset
    if isinstance(department_id, Unset):
        json_department_id = UNSET
    elif isinstance(department_id, UUID):
        json_department_id = str(department_id)
    else:
        json_department_id = department_id
    params["department_id"] = json_department_id

    json_is_active: bool | None | Unset
    if isinstance(is_active, Unset):
        json_is_active = UNSET
    else:
        json_is_active = is_active
    params["is_active"] = json_is_active

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/meetings",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MeetingListResponse | None:
    if response.status_code == 200:
        response_200 = MeetingListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MeetingListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    meeting_type: None | str | Unset = UNSET,
    chair_id: None | Unset | UUID = UNSET,
    department_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MeetingListResponse]:
    """Search Meetings

    Args:
        org_id (UUID):
        meeting_type (None | str | Unset):
        chair_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MeetingListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        meeting_type=meeting_type,
        chair_id=chair_id,
        department_id=department_id,
        is_active=is_active,
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
    org_id: UUID,
    meeting_type: None | str | Unset = UNSET,
    chair_id: None | Unset | UUID = UNSET,
    department_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MeetingListResponse | None:
    """Search Meetings

    Args:
        org_id (UUID):
        meeting_type (None | str | Unset):
        chair_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MeetingListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        meeting_type=meeting_type,
        chair_id=chair_id,
        department_id=department_id,
        is_active=is_active,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    meeting_type: None | str | Unset = UNSET,
    chair_id: None | Unset | UUID = UNSET,
    department_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MeetingListResponse]:
    """Search Meetings

    Args:
        org_id (UUID):
        meeting_type (None | str | Unset):
        chair_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MeetingListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        meeting_type=meeting_type,
        chair_id=chair_id,
        department_id=department_id,
        is_active=is_active,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    meeting_type: None | str | Unset = UNSET,
    chair_id: None | Unset | UUID = UNSET,
    department_id: None | Unset | UUID = UNSET,
    is_active: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MeetingListResponse | None:
    """Search Meetings

    Args:
        org_id (UUID):
        meeting_type (None | str | Unset):
        chair_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        is_active (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MeetingListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            meeting_type=meeting_type,
            chair_id=chair_id,
            department_id=department_id,
            is_active=is_active,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
