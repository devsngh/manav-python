from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dialogue_edit import DialogueEdit
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dialogue_id: UUID,
    *,
    body: DialogueEdit,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/chat/dialogues/{dialogue_id}/edit-and-stream".format(
            dialogue_id=quote(str(dialogue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DialogueEdit,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Edit And Stream Dialogue

     Edit the LAST dialogue in a thread and stream a fresh response.

    Replaces the B14 stub (which just echoed the query back). Guards enforced
    server-side (also enforced by the frontend but repeated here as
    defence-in-depth):
      * dialogue must be the last non-deleted row in its thread
      * no other dialogue in the thread may currently be streaming
      * a pending HIL interrupt on this dialogue must be resolved first

    Preserves the dialogue_id — the new agent response REPLACES the
    prior one on the same row. Traces, cost rollups, and execution
    steps re-run under the same key.

    Body identical to DialogueCreate (query + optional file_urls +
    image_urls) so users can re-attach files when editing.

    Args:
        dialogue_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (DialogueEdit): Schema for editing and resending a query.

            Used by two endpoints:
              * PUT  /api/chat/dialogues/{id}                  — legacy stub
              * POST /api/chat/dialogues/{id}/edit-and-stream  — wires to
                orchestrator; body accepts file/image attachments identical
                to DialogueCreate so the edited turn can re-attach files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dialogue_id=dialogue_id,
        body=body,
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
    body: DialogueEdit,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Edit And Stream Dialogue

     Edit the LAST dialogue in a thread and stream a fresh response.

    Replaces the B14 stub (which just echoed the query back). Guards enforced
    server-side (also enforced by the frontend but repeated here as
    defence-in-depth):
      * dialogue must be the last non-deleted row in its thread
      * no other dialogue in the thread may currently be streaming
      * a pending HIL interrupt on this dialogue must be resolved first

    Preserves the dialogue_id — the new agent response REPLACES the
    prior one on the same row. Traces, cost rollups, and execution
    steps re-run under the same key.

    Body identical to DialogueCreate (query + optional file_urls +
    image_urls) so users can re-attach files when editing.

    Args:
        dialogue_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (DialogueEdit): Schema for editing and resending a query.

            Used by two endpoints:
              * PUT  /api/chat/dialogues/{id}                  — legacy stub
              * POST /api/chat/dialogues/{id}/edit-and-stream  — wires to
                orchestrator; body accepts file/image attachments identical
                to DialogueCreate so the edited turn can re-attach files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        dialogue_id=dialogue_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DialogueEdit,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Edit And Stream Dialogue

     Edit the LAST dialogue in a thread and stream a fresh response.

    Replaces the B14 stub (which just echoed the query back). Guards enforced
    server-side (also enforced by the frontend but repeated here as
    defence-in-depth):
      * dialogue must be the last non-deleted row in its thread
      * no other dialogue in the thread may currently be streaming
      * a pending HIL interrupt on this dialogue must be resolved first

    Preserves the dialogue_id — the new agent response REPLACES the
    prior one on the same row. Traces, cost rollups, and execution
    steps re-run under the same key.

    Body identical to DialogueCreate (query + optional file_urls +
    image_urls) so users can re-attach files when editing.

    Args:
        dialogue_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (DialogueEdit): Schema for editing and resending a query.

            Used by two endpoints:
              * PUT  /api/chat/dialogues/{id}                  — legacy stub
              * POST /api/chat/dialogues/{id}/edit-and-stream  — wires to
                orchestrator; body accepts file/image attachments identical
                to DialogueCreate so the edited turn can re-attach files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        dialogue_id=dialogue_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dialogue_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: DialogueEdit,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Edit And Stream Dialogue

     Edit the LAST dialogue in a thread and stream a fresh response.

    Replaces the B14 stub (which just echoed the query back). Guards enforced
    server-side (also enforced by the frontend but repeated here as
    defence-in-depth):
      * dialogue must be the last non-deleted row in its thread
      * no other dialogue in the thread may currently be streaming
      * a pending HIL interrupt on this dialogue must be resolved first

    Preserves the dialogue_id — the new agent response REPLACES the
    prior one on the same row. Traces, cost rollups, and execution
    steps re-run under the same key.

    Body identical to DialogueCreate (query + optional file_urls +
    image_urls) so users can re-attach files when editing.

    Args:
        dialogue_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (DialogueEdit): Schema for editing and resending a query.

            Used by two endpoints:
              * PUT  /api/chat/dialogues/{id}                  — legacy stub
              * POST /api/chat/dialogues/{id}/edit-and-stream  — wires to
                orchestrator; body accepts file/image attachments identical
                to DialogueCreate so the edited turn can re-attach files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            dialogue_id=dialogue_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
