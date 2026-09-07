from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.debate_session_response import DebateSessionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_group_id: None | str | Unset
    if isinstance(group_id, Unset):
        json_group_id = UNSET
    elif isinstance(group_id, UUID):
        json_group_id = str(group_id)
    else:
        json_group_id = group_id
    params["group_id"] = json_group_id

    params["active_only"] = active_only

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/debates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[DebateSessionResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DebateSessionResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[DebateSessionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[DebateSessionResponse]]:
    """List Debate Sessions

    Args:
        group_id (None | Unset | UUID): Filter to debates for this user_bot_group
        active_only (bool | Unset): Exclude concluded debates Default: False.
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[DebateSessionResponse]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        active_only=active_only,
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
    group_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[DebateSessionResponse] | None:
    """List Debate Sessions

    Args:
        group_id (None | Unset | UUID): Filter to debates for this user_bot_group
        active_only (bool | Unset): Exclude concluded debates Default: False.
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[DebateSessionResponse]
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        active_only=active_only,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    group_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[DebateSessionResponse]]:
    """List Debate Sessions

    Args:
        group_id (None | Unset | UUID): Filter to debates for this user_bot_group
        active_only (bool | Unset): Exclude concluded debates Default: False.
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[DebateSessionResponse]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        active_only=active_only,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    group_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = False,
    limit: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[DebateSessionResponse] | None:
    """List Debate Sessions

    Args:
        group_id (None | Unset | UUID): Filter to debates for this user_bot_group
        active_only (bool | Unset): Exclude concluded debates Default: False.
        limit (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[DebateSessionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            active_only=active_only,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
