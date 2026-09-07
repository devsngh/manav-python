from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pattern_dismiss_request import PatternDismissRequest
from ...models.pattern_read import PatternRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pattern_id: UUID,
    *,
    body: PatternDismissRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/observability/patterns/{pattern_id}/dismiss".format(
            pattern_id=quote(str(pattern_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PatternRead | None:
    if response.status_code == 200:
        response_200 = PatternRead.from_dict(response.json())

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
) -> Response[HTTPValidationError | PatternRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pattern_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatternDismissRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PatternRead]:
    """Dismiss Pattern

     Mark a pattern as dismissed. Preserves occurrence_count/last_seen_at
    so a re-detection shows up in the audit trail without reopening the row.

    Args:
        pattern_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PatternDismissRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatternRead]
    """

    kwargs = _get_kwargs(
        pattern_id=pattern_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pattern_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatternDismissRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PatternRead | None:
    """Dismiss Pattern

     Mark a pattern as dismissed. Preserves occurrence_count/last_seen_at
    so a re-detection shows up in the audit trail without reopening the row.

    Args:
        pattern_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PatternDismissRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatternRead
    """

    return sync_detailed(
        pattern_id=pattern_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    pattern_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatternDismissRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PatternRead]:
    """Dismiss Pattern

     Mark a pattern as dismissed. Preserves occurrence_count/last_seen_at
    so a re-detection shows up in the audit trail without reopening the row.

    Args:
        pattern_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PatternDismissRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatternRead]
    """

    kwargs = _get_kwargs(
        pattern_id=pattern_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pattern_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PatternDismissRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PatternRead | None:
    """Dismiss Pattern

     Mark a pattern as dismissed. Preserves occurrence_count/last_seen_at
    so a re-detection shows up in the audit trail without reopening the row.

    Args:
        pattern_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PatternDismissRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatternRead
    """

    return (
        await asyncio_detailed(
            pattern_id=pattern_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
