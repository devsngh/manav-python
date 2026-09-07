from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.debate_event_list import DebateEventList
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    debate_id: str,
    *,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/debates/{debate_id}/events".format(
            debate_id=quote(str(debate_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DebateEventList | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DebateEventList.from_dict(response.json())

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
) -> Response[DebateEventList | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[DebateEventList | HTTPValidationError]:
    """List Debate Events

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebateEventList | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        debate_id=debate_id,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> DebateEventList | HTTPValidationError | None:
    """List Debate Events

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebateEventList | HTTPValidationError
    """

    return sync_detailed(
        debate_id=debate_id,
        client=client,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[DebateEventList | HTTPValidationError]:
    """List Debate Events

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebateEventList | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        debate_id=debate_id,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> DebateEventList | HTTPValidationError | None:
    """List Debate Events

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebateEventList | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            debate_id=debate_id,
            client=client,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
