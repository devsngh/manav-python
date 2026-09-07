from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    org_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/bots/{bot_id}/unread-summary".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Unread Summary

     Aggregate unread message counts for one bot across all conversation
    surfaces. Used by every metabot's wake-up routine to know what to act on.

    Args:
        bot_id (UUID):
        org_id (None | Unset | UUID): Optional org-scope filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Unread Summary

     Aggregate unread message counts for one bot across all conversation
    surfaces. Used by every metabot's wake-up routine to know what to act on.

    Args:
        bot_id (UUID):
        org_id (None | Unset | UUID): Optional org-scope filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        org_id=org_id,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Unread Summary

     Aggregate unread message counts for one bot across all conversation
    surfaces. Used by every metabot's wake-up routine to know what to act on.

    Args:
        bot_id (UUID):
        org_id (None | Unset | UUID): Optional org-scope filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Unread Summary

     Aggregate unread message counts for one bot across all conversation
    surfaces. Used by every metabot's wake-up routine to know what to act on.

    Args:
        bot_id (UUID):
        org_id (None | Unset | UUID): Optional org-scope filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            org_id=org_id,
        )
    ).parsed
