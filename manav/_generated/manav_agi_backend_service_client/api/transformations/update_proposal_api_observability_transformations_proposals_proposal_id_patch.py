from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.transformation_proposal_response import TransformationProposalResponse
from ...models.transformation_proposal_update import TransformationProposalUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    proposal_id: UUID,
    *,
    body: TransformationProposalUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/observability/transformations/proposals/{proposal_id}".format(
            proposal_id=quote(str(proposal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TransformationProposalResponse | None:
    if response.status_code == 200:
        response_200 = TransformationProposalResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TransformationProposalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    proposal_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TransformationProposalUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TransformationProposalResponse]:
    """Update Proposal

    Args:
        proposal_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TransformationProposalUpdate): Patch — status transitions + lifecycle timestamps +
            actors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TransformationProposalResponse]
    """

    kwargs = _get_kwargs(
        proposal_id=proposal_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    proposal_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TransformationProposalUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TransformationProposalResponse | None:
    """Update Proposal

    Args:
        proposal_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TransformationProposalUpdate): Patch — status transitions + lifecycle timestamps +
            actors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TransformationProposalResponse
    """

    return sync_detailed(
        proposal_id=proposal_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    proposal_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TransformationProposalUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TransformationProposalResponse]:
    """Update Proposal

    Args:
        proposal_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TransformationProposalUpdate): Patch — status transitions + lifecycle timestamps +
            actors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TransformationProposalResponse]
    """

    kwargs = _get_kwargs(
        proposal_id=proposal_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    proposal_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TransformationProposalUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TransformationProposalResponse | None:
    """Update Proposal

    Args:
        proposal_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TransformationProposalUpdate): Patch — status transitions + lifecycle timestamps +
            actors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TransformationProposalResponse
    """

    return (
        await asyncio_detailed(
            proposal_id=proposal_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
