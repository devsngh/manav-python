from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feedback_list_response import FeedbackListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    target_entity_type: None | str | Unset = UNSET,
    target_entity_id: None | Unset | UUID = UNSET,
    kind: None | str | Unset = UNSET,
    apply_status: None | str | Unset = UNSET,
    author_id: None | Unset | UUID = UNSET,
    author_role: None | str | Unset = UNSET,
    source_channel: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
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

    json_target_entity_type: None | str | Unset
    if isinstance(target_entity_type, Unset):
        json_target_entity_type = UNSET
    else:
        json_target_entity_type = target_entity_type
    params["target_entity_type"] = json_target_entity_type

    json_target_entity_id: None | str | Unset
    if isinstance(target_entity_id, Unset):
        json_target_entity_id = UNSET
    elif isinstance(target_entity_id, UUID):
        json_target_entity_id = str(target_entity_id)
    else:
        json_target_entity_id = target_entity_id
    params["target_entity_id"] = json_target_entity_id

    json_kind: None | str | Unset
    if isinstance(kind, Unset):
        json_kind = UNSET
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_apply_status: None | str | Unset
    if isinstance(apply_status, Unset):
        json_apply_status = UNSET
    else:
        json_apply_status = apply_status
    params["apply_status"] = json_apply_status

    json_author_id: None | str | Unset
    if isinstance(author_id, Unset):
        json_author_id = UNSET
    elif isinstance(author_id, UUID):
        json_author_id = str(author_id)
    else:
        json_author_id = author_id
    params["author_id"] = json_author_id

    json_author_role: None | str | Unset
    if isinstance(author_role, Unset):
        json_author_role = UNSET
    else:
        json_author_role = author_role
    params["author_role"] = json_author_role

    json_source_channel: None | str | Unset
    if isinstance(source_channel, Unset):
        json_source_channel = UNSET
    else:
        json_source_channel = source_channel
    params["source_channel"] = json_source_channel

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/feedback",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FeedbackListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FeedbackListResponse.from_dict(response.json())

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
) -> Response[FeedbackListResponse | HTTPValidationError]:
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
    target_entity_type: None | str | Unset = UNSET,
    target_entity_id: None | Unset | UUID = UNSET,
    kind: None | str | Unset = UNSET,
    apply_status: None | str | Unset = UNSET,
    author_id: None | Unset | UUID = UNSET,
    author_role: None | str | Unset = UNSET,
    source_channel: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[FeedbackListResponse | HTTPValidationError]:
    """Search Feedback

    Args:
        org_id (UUID):
        target_entity_type (None | str | Unset):
        target_entity_id (None | Unset | UUID):
        kind (None | str | Unset):
        apply_status (None | str | Unset):
        author_id (None | Unset | UUID):
        author_role (None | str | Unset):
        source_channel (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedbackListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        target_entity_type=target_entity_type,
        target_entity_id=target_entity_id,
        kind=kind,
        apply_status=apply_status,
        author_id=author_id,
        author_role=author_role,
        source_channel=source_channel,
        since=since,
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
    target_entity_type: None | str | Unset = UNSET,
    target_entity_id: None | Unset | UUID = UNSET,
    kind: None | str | Unset = UNSET,
    apply_status: None | str | Unset = UNSET,
    author_id: None | Unset | UUID = UNSET,
    author_role: None | str | Unset = UNSET,
    source_channel: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> FeedbackListResponse | HTTPValidationError | None:
    """Search Feedback

    Args:
        org_id (UUID):
        target_entity_type (None | str | Unset):
        target_entity_id (None | Unset | UUID):
        kind (None | str | Unset):
        apply_status (None | str | Unset):
        author_id (None | Unset | UUID):
        author_role (None | str | Unset):
        source_channel (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedbackListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        target_entity_type=target_entity_type,
        target_entity_id=target_entity_id,
        kind=kind,
        apply_status=apply_status,
        author_id=author_id,
        author_role=author_role,
        source_channel=source_channel,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    target_entity_type: None | str | Unset = UNSET,
    target_entity_id: None | Unset | UUID = UNSET,
    kind: None | str | Unset = UNSET,
    apply_status: None | str | Unset = UNSET,
    author_id: None | Unset | UUID = UNSET,
    author_role: None | str | Unset = UNSET,
    source_channel: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[FeedbackListResponse | HTTPValidationError]:
    """Search Feedback

    Args:
        org_id (UUID):
        target_entity_type (None | str | Unset):
        target_entity_id (None | Unset | UUID):
        kind (None | str | Unset):
        apply_status (None | str | Unset):
        author_id (None | Unset | UUID):
        author_role (None | str | Unset):
        source_channel (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedbackListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        target_entity_type=target_entity_type,
        target_entity_id=target_entity_id,
        kind=kind,
        apply_status=apply_status,
        author_id=author_id,
        author_role=author_role,
        source_channel=source_channel,
        since=since,
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
    target_entity_type: None | str | Unset = UNSET,
    target_entity_id: None | Unset | UUID = UNSET,
    kind: None | str | Unset = UNSET,
    apply_status: None | str | Unset = UNSET,
    author_id: None | Unset | UUID = UNSET,
    author_role: None | str | Unset = UNSET,
    source_channel: None | str | Unset = UNSET,
    since: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> FeedbackListResponse | HTTPValidationError | None:
    """Search Feedback

    Args:
        org_id (UUID):
        target_entity_type (None | str | Unset):
        target_entity_id (None | Unset | UUID):
        kind (None | str | Unset):
        apply_status (None | str | Unset):
        author_id (None | Unset | UUID):
        author_role (None | str | Unset):
        source_channel (None | str | Unset):
        since (None | str | Unset): ISO datetime
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedbackListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            target_entity_type=target_entity_type,
            target_entity_id=target_entity_id,
            kind=kind,
            apply_status=apply_status,
            author_id=author_id,
            author_role=author_role,
            source_channel=source_channel,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
