import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.transformation_followup_list_response import TransformationFollowupListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    proposal_id: None | Unset | UUID = UNSET,
    outcome: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
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

    json_proposal_id: None | str | Unset
    if isinstance(proposal_id, Unset):
        json_proposal_id = UNSET
    elif isinstance(proposal_id, UUID):
        json_proposal_id = str(proposal_id)
    else:
        json_proposal_id = proposal_id
    params["proposal_id"] = json_proposal_id

    json_outcome: None | str | Unset
    if isinstance(outcome, Unset):
        json_outcome = UNSET
    else:
        json_outcome = outcome
    params["outcome"] = json_outcome

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/transformations/followups",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TransformationFollowupListResponse | None:
    if response.status_code == 200:
        response_200 = TransformationFollowupListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TransformationFollowupListResponse]:
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
    proposal_id: None | Unset | UUID = UNSET,
    outcome: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TransformationFollowupListResponse]:
    """Search Followups

    Args:
        org_id (UUID):
        proposal_id (None | Unset | UUID):
        outcome (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TransformationFollowupListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        proposal_id=proposal_id,
        outcome=outcome,
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
    proposal_id: None | Unset | UUID = UNSET,
    outcome: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TransformationFollowupListResponse | None:
    """Search Followups

    Args:
        org_id (UUID):
        proposal_id (None | Unset | UUID):
        outcome (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TransformationFollowupListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        proposal_id=proposal_id,
        outcome=outcome,
        since=since,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    proposal_id: None | Unset | UUID = UNSET,
    outcome: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TransformationFollowupListResponse]:
    """Search Followups

    Args:
        org_id (UUID):
        proposal_id (None | Unset | UUID):
        outcome (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TransformationFollowupListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        proposal_id=proposal_id,
        outcome=outcome,
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
    proposal_id: None | Unset | UUID = UNSET,
    outcome: None | str | Unset = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TransformationFollowupListResponse | None:
    """Search Followups

    Args:
        org_id (UUID):
        proposal_id (None | Unset | UUID):
        outcome (None | str | Unset):
        since (datetime.datetime | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TransformationFollowupListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            proposal_id=proposal_id,
            outcome=outcome,
            since=since,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
