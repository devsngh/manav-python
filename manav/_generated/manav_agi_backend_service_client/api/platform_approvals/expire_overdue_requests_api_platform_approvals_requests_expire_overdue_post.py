from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expire_overdue_response import ExpireOverdueResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hours_overdue: int | Unset = 24,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["hours_overdue"] = hours_overdue

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/approvals/requests/expire-overdue",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExpireOverdueResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExpireOverdueResponse.from_dict(response.json())

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
) -> Response[ExpireOverdueResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    hours_overdue: int | Unset = 24,
    authorization: None | str | Unset = UNSET,
) -> Response[ExpireOverdueResponse | HTTPValidationError]:
    """Expire Overdue Requests

     Auto-expire requests past SLA. Returns count expired.

    Args:
        hours_overdue (int | Unset):  Default: 24.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpireOverdueResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        hours_overdue=hours_overdue,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    hours_overdue: int | Unset = 24,
    authorization: None | str | Unset = UNSET,
) -> ExpireOverdueResponse | HTTPValidationError | None:
    """Expire Overdue Requests

     Auto-expire requests past SLA. Returns count expired.

    Args:
        hours_overdue (int | Unset):  Default: 24.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpireOverdueResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        hours_overdue=hours_overdue,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    hours_overdue: int | Unset = 24,
    authorization: None | str | Unset = UNSET,
) -> Response[ExpireOverdueResponse | HTTPValidationError]:
    """Expire Overdue Requests

     Auto-expire requests past SLA. Returns count expired.

    Args:
        hours_overdue (int | Unset):  Default: 24.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpireOverdueResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        hours_overdue=hours_overdue,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    hours_overdue: int | Unset = 24,
    authorization: None | str | Unset = UNSET,
) -> ExpireOverdueResponse | HTTPValidationError | None:
    """Expire Overdue Requests

     Auto-expire requests past SLA. Returns count expired.

    Args:
        hours_overdue (int | Unset):  Default: 24.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpireOverdueResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            hours_overdue=hours_overdue,
            authorization=authorization,
        )
    ).parsed
