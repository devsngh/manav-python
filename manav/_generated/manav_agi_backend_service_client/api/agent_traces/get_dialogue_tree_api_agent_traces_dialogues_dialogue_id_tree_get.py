from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dialogue_tree_response import DialogueTreeResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dialogue_id: UUID,
    *,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_bot_id, Unset):
        headers["X-Bot-Id"] = x_bot_id

    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent-traces/dialogues/{dialogue_id}/tree".format(
            dialogue_id=quote(str(dialogue_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DialogueTreeResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DialogueTreeResponse.from_dict(response.json())

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
) -> Response[DialogueTreeResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DialogueTreeResponse | HTTPValidationError]:
    """Get Dialogue Tree

     Pane-2: header + flat span list (client builds tree via parent_id).

    Args:
        dialogue_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DialogueTreeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dialogue_id=dialogue_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DialogueTreeResponse | HTTPValidationError | None:
    """Get Dialogue Tree

     Pane-2: header + flat span list (client builds tree via parent_id).

    Args:
        dialogue_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DialogueTreeResponse | HTTPValidationError
    """

    return sync_detailed(
        dialogue_id=dialogue_id,
        client=client,
        x_bot_id=x_bot_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DialogueTreeResponse | HTTPValidationError]:
    """Get Dialogue Tree

     Pane-2: header + flat span list (client builds tree via parent_id).

    Args:
        dialogue_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DialogueTreeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dialogue_id=dialogue_id,
        x_bot_id=x_bot_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_bot_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DialogueTreeResponse | HTTPValidationError | None:
    """Get Dialogue Tree

     Pane-2: header + flat span list (client builds tree via parent_id).

    Args:
        dialogue_id (UUID):
        x_bot_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DialogueTreeResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dialogue_id=dialogue_id,
            client=client,
            x_bot_id=x_bot_id,
            authorization=authorization,
        )
    ).parsed
