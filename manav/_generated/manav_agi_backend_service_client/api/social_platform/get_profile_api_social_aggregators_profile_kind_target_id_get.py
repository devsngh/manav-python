from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.profile_response import ProfileResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    kind: str,
    target_id: UUID,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/social/aggregators/profile/{kind}/{target_id}".format(
            kind=quote(str(kind), safe=""),
            target_id=quote(str(target_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ProfileResponse | None:
    if response.status_code == 200:
        response_200 = ProfileResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ProfileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    kind: str,
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProfileResponse]:
    """Get Profile

     Unified user-or-bot profile lookup for the ProfileWindow.

    `kind` ∈ {'user', 'bot'}. Returns 404 if the target doesn't exist.

    Args:
        kind (str):
        target_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProfileResponse]
    """

    kwargs = _get_kwargs(
        kind=kind,
        target_id=target_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: str,
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProfileResponse | None:
    """Get Profile

     Unified user-or-bot profile lookup for the ProfileWindow.

    `kind` ∈ {'user', 'bot'}. Returns 404 if the target doesn't exist.

    Args:
        kind (str):
        target_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProfileResponse
    """

    return sync_detailed(
        kind=kind,
        target_id=target_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    kind: str,
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ProfileResponse]:
    """Get Profile

     Unified user-or-bot profile lookup for the ProfileWindow.

    `kind` ∈ {'user', 'bot'}. Returns 404 if the target doesn't exist.

    Args:
        kind (str):
        target_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ProfileResponse]
    """

    kwargs = _get_kwargs(
        kind=kind,
        target_id=target_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: str,
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ProfileResponse | None:
    """Get Profile

     Unified user-or-bot profile lookup for the ProfileWindow.

    `kind` ∈ {'user', 'bot'}. Returns 404 if the target doesn't exist.

    Args:
        kind (str):
        target_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ProfileResponse
    """

    return (
        await asyncio_detailed(
            kind=kind,
            target_id=target_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
