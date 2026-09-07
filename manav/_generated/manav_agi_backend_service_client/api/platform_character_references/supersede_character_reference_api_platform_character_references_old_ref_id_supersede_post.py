from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.character_reference_response import CharacterReferenceResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.supersede_request import SupersedeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    old_ref_id: UUID,
    *,
    body: SupersedeRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/character-references/{old_ref_id}/supersede".format(
            old_ref_id=quote(str(old_ref_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CharacterReferenceResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = CharacterReferenceResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CharacterReferenceResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    old_ref_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SupersedeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[CharacterReferenceResponse | HTTPValidationError]:
    """Supersede Character Reference

     Create a new version that supersedes an existing one.

    Deactivates the old, creates the new with parent_reference_id pointing back.

    Args:
        old_ref_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SupersedeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharacterReferenceResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        old_ref_id=old_ref_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    old_ref_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SupersedeRequest,
    authorization: None | str | Unset = UNSET,
) -> CharacterReferenceResponse | HTTPValidationError | None:
    """Supersede Character Reference

     Create a new version that supersedes an existing one.

    Deactivates the old, creates the new with parent_reference_id pointing back.

    Args:
        old_ref_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SupersedeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharacterReferenceResponse | HTTPValidationError
    """

    return sync_detailed(
        old_ref_id=old_ref_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    old_ref_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SupersedeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[CharacterReferenceResponse | HTTPValidationError]:
    """Supersede Character Reference

     Create a new version that supersedes an existing one.

    Deactivates the old, creates the new with parent_reference_id pointing back.

    Args:
        old_ref_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SupersedeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharacterReferenceResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        old_ref_id=old_ref_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    old_ref_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: SupersedeRequest,
    authorization: None | str | Unset = UNSET,
) -> CharacterReferenceResponse | HTTPValidationError | None:
    """Supersede Character Reference

     Create a new version that supersedes an existing one.

    Deactivates the old, creates the new with parent_reference_id pointing back.

    Args:
        old_ref_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (SupersedeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharacterReferenceResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            old_ref_id=old_ref_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
