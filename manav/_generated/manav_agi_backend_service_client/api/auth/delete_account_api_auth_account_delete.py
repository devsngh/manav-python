from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.message_response import MessageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/auth/account",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MessageResponse | None:
    if response.status_code == 200:
        response_200 = MessageResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MessageResponse]:
    """Delete Account

     Hard-delete the caller's account with cascade across DBs.

    Was soft-delete (just `is_active = false`). Now:
    - Reassigns marketplace listings to a fixed "[deleted user]" placeholder
      so buyers / active rentals aren't broken.
    - Cascades user-owned rows across core_db (via PG ON DELETE CASCADE for
      the 9 owned tables + explicit DELETE for the others) and operations_db
      loose-ref tables (chat threads, audit logs, tasks, etc).
    - Deletes solo org + its subscription + wallet.
    - Frees the email address for reuse.
    - Sends a courtesy 'account deleted' email BEFORE nuking (best-effort).

    Rejects if user has an active PAID subscription — cancel first.

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MessageResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MessageResponse | None:
    """Delete Account

     Hard-delete the caller's account with cascade across DBs.

    Was soft-delete (just `is_active = false`). Now:
    - Reassigns marketplace listings to a fixed "[deleted user]" placeholder
      so buyers / active rentals aren't broken.
    - Cascades user-owned rows across core_db (via PG ON DELETE CASCADE for
      the 9 owned tables + explicit DELETE for the others) and operations_db
      loose-ref tables (chat threads, audit logs, tasks, etc).
    - Deletes solo org + its subscription + wallet.
    - Frees the email address for reuse.
    - Sends a courtesy 'account deleted' email BEFORE nuking (best-effort).

    Rejects if user has an active PAID subscription — cancel first.

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MessageResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MessageResponse]:
    """Delete Account

     Hard-delete the caller's account with cascade across DBs.

    Was soft-delete (just `is_active = false`). Now:
    - Reassigns marketplace listings to a fixed "[deleted user]" placeholder
      so buyers / active rentals aren't broken.
    - Cascades user-owned rows across core_db (via PG ON DELETE CASCADE for
      the 9 owned tables + explicit DELETE for the others) and operations_db
      loose-ref tables (chat threads, audit logs, tasks, etc).
    - Deletes solo org + its subscription + wallet.
    - Frees the email address for reuse.
    - Sends a courtesy 'account deleted' email BEFORE nuking (best-effort).

    Rejects if user has an active PAID subscription — cancel first.

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MessageResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MessageResponse | None:
    """Delete Account

     Hard-delete the caller's account with cascade across DBs.

    Was soft-delete (just `is_active = false`). Now:
    - Reassigns marketplace listings to a fixed "[deleted user]" placeholder
      so buyers / active rentals aren't broken.
    - Cascades user-owned rows across core_db (via PG ON DELETE CASCADE for
      the 9 owned tables + explicit DELETE for the others) and operations_db
      loose-ref tables (chat threads, audit logs, tasks, etc).
    - Deletes solo org + its subscription + wallet.
    - Frees the email address for reuse.
    - Sends a courtesy 'account deleted' email BEFORE nuking (best-effort).

    Rejects if user has an active PAID subscription — cancel first.

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MessageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
