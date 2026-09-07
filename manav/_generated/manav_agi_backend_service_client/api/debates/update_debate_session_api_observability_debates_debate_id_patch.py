from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.debate_session_response import DebateSessionResponse
from ...models.debate_session_update import DebateSessionUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    debate_id: str,
    *,
    body: DebateSessionUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/observability/debates/{debate_id}".format(
            debate_id=quote(str(debate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DebateSessionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DebateSessionResponse.from_dict(response.json())

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
) -> Response[DebateSessionResponse | HTTPValidationError]:
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
    body: DebateSessionUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[DebateSessionResponse | HTTPValidationError]:
    """Update Debate Session

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        authorization (None | str | Unset): Bearer token
        body (DebateSessionUpdate): Patch — phase advance, speaker swap, positions/rebuttals
            append, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebateSessionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        debate_id=debate_id,
        body=body,
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
    body: DebateSessionUpdate,
    authorization: None | str | Unset = UNSET,
) -> DebateSessionResponse | HTTPValidationError | None:
    """Update Debate Session

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        authorization (None | str | Unset): Bearer token
        body (DebateSessionUpdate): Patch — phase advance, speaker swap, positions/rebuttals
            append, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebateSessionResponse | HTTPValidationError
    """

    return sync_detailed(
        debate_id=debate_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DebateSessionUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[DebateSessionResponse | HTTPValidationError]:
    """Update Debate Session

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        authorization (None | str | Unset): Bearer token
        body (DebateSessionUpdate): Patch — phase advance, speaker swap, positions/rebuttals
            append, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DebateSessionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        debate_id=debate_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    debate_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DebateSessionUpdate,
    authorization: None | str | Unset = UNSET,
) -> DebateSessionResponse | HTTPValidationError | None:
    """Update Debate Session

    Args:
        debate_id (str): Full UUID or unique hex prefix >=8 chars
        authorization (None | str | Unset): Bearer token
        body (DebateSessionUpdate): Patch — phase advance, speaker swap, positions/rebuttals
            append, etc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DebateSessionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            debate_id=debate_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
