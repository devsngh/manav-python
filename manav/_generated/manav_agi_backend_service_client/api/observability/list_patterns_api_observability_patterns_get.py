from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pattern_list_response import PatternListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: None | Unset | UUID = UNSET,
    status: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    pattern_type: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_severity: None | str | Unset
    if isinstance(severity, Unset):
        json_severity = UNSET
    else:
        json_severity = severity
    params["severity"] = json_severity

    json_pattern_type: None | str | Unset
    if isinstance(pattern_type, Unset):
        json_pattern_type = UNSET
    else:
        json_pattern_type = pattern_type
    params["pattern_type"] = json_pattern_type

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/patterns",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PatternListResponse | None:
    if response.status_code == 200:
        response_200 = PatternListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PatternListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    status: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    pattern_type: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PatternListResponse]:
    """List Patterns

     List patterns, most recently active first.

    Args:
        org_id (None | Unset | UUID): Filter by org (defaults to all visible)
        status (None | str | Unset): active | dismissed | resolved
        severity (None | str | Unset): info | ok | warn | danger
        pattern_type (None | str | Unset):
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatternListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        status=status,
        severity=severity,
        pattern_type=pattern_type,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    status: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    pattern_type: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PatternListResponse | None:
    """List Patterns

     List patterns, most recently active first.

    Args:
        org_id (None | Unset | UUID): Filter by org (defaults to all visible)
        status (None | str | Unset): active | dismissed | resolved
        severity (None | str | Unset): info | ok | warn | danger
        pattern_type (None | str | Unset):
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatternListResponse
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        status=status,
        severity=severity,
        pattern_type=pattern_type,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    status: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    pattern_type: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PatternListResponse]:
    """List Patterns

     List patterns, most recently active first.

    Args:
        org_id (None | Unset | UUID): Filter by org (defaults to all visible)
        status (None | str | Unset): active | dismissed | resolved
        severity (None | str | Unset): info | ok | warn | danger
        pattern_type (None | str | Unset):
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PatternListResponse]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        status=status,
        severity=severity,
        pattern_type=pattern_type,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    status: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    pattern_type: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PatternListResponse | None:
    """List Patterns

     List patterns, most recently active first.

    Args:
        org_id (None | Unset | UUID): Filter by org (defaults to all visible)
        status (None | str | Unset): active | dismissed | resolved
        severity (None | str | Unset): info | ok | warn | danger
        pattern_type (None | str | Unset):
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PatternListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            status=status,
            severity=severity,
            pattern_type=pattern_type,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
