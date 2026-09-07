from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.character_reference_list_response import CharacterReferenceListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subject_type: None | str | Unset = UNSET,
    subject_bot_id: None | Unset | UUID = UNSET,
    subject_user_id: None | Unset | UUID = UNSET,
    subject_persona_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = True,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_subject_type: None | str | Unset
    if isinstance(subject_type, Unset):
        json_subject_type = UNSET
    else:
        json_subject_type = subject_type
    params["subject_type"] = json_subject_type

    json_subject_bot_id: None | str | Unset
    if isinstance(subject_bot_id, Unset):
        json_subject_bot_id = UNSET
    elif isinstance(subject_bot_id, UUID):
        json_subject_bot_id = str(subject_bot_id)
    else:
        json_subject_bot_id = subject_bot_id
    params["subject_bot_id"] = json_subject_bot_id

    json_subject_user_id: None | str | Unset
    if isinstance(subject_user_id, Unset):
        json_subject_user_id = UNSET
    elif isinstance(subject_user_id, UUID):
        json_subject_user_id = str(subject_user_id)
    else:
        json_subject_user_id = subject_user_id
    params["subject_user_id"] = json_subject_user_id

    json_subject_persona_id: None | str | Unset
    if isinstance(subject_persona_id, Unset):
        json_subject_persona_id = UNSET
    elif isinstance(subject_persona_id, UUID):
        json_subject_persona_id = str(subject_persona_id)
    else:
        json_subject_persona_id = subject_persona_id
    params["subject_persona_id"] = json_subject_persona_id

    params["active_only"] = active_only

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/character-references",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CharacterReferenceListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CharacterReferenceListResponse.from_dict(response.json())

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
) -> Response[CharacterReferenceListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: None | str | Unset = UNSET,
    subject_bot_id: None | Unset | UUID = UNSET,
    subject_user_id: None | Unset | UUID = UNSET,
    subject_persona_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = True,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CharacterReferenceListResponse | HTTPValidationError]:
    """List Character References

    Args:
        subject_type (None | str | Unset):
        subject_bot_id (None | Unset | UUID):
        subject_user_id (None | Unset | UUID):
        subject_persona_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: True.
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharacterReferenceListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_bot_id=subject_bot_id,
        subject_user_id=subject_user_id,
        subject_persona_id=subject_persona_id,
        active_only=active_only,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    subject_type: None | str | Unset = UNSET,
    subject_bot_id: None | Unset | UUID = UNSET,
    subject_user_id: None | Unset | UUID = UNSET,
    subject_persona_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = True,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CharacterReferenceListResponse | HTTPValidationError | None:
    """List Character References

    Args:
        subject_type (None | str | Unset):
        subject_bot_id (None | Unset | UUID):
        subject_user_id (None | Unset | UUID):
        subject_persona_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: True.
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharacterReferenceListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        subject_type=subject_type,
        subject_bot_id=subject_bot_id,
        subject_user_id=subject_user_id,
        subject_persona_id=subject_persona_id,
        active_only=active_only,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: None | str | Unset = UNSET,
    subject_bot_id: None | Unset | UUID = UNSET,
    subject_user_id: None | Unset | UUID = UNSET,
    subject_persona_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = True,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CharacterReferenceListResponse | HTTPValidationError]:
    """List Character References

    Args:
        subject_type (None | str | Unset):
        subject_bot_id (None | Unset | UUID):
        subject_user_id (None | Unset | UUID):
        subject_persona_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: True.
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CharacterReferenceListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        subject_bot_id=subject_bot_id,
        subject_user_id=subject_user_id,
        subject_persona_id=subject_persona_id,
        active_only=active_only,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    subject_type: None | str | Unset = UNSET,
    subject_bot_id: None | Unset | UUID = UNSET,
    subject_user_id: None | Unset | UUID = UNSET,
    subject_persona_id: None | Unset | UUID = UNSET,
    active_only: bool | Unset = True,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CharacterReferenceListResponse | HTTPValidationError | None:
    """List Character References

    Args:
        subject_type (None | str | Unset):
        subject_bot_id (None | Unset | UUID):
        subject_user_id (None | Unset | UUID):
        subject_persona_id (None | Unset | UUID):
        active_only (bool | Unset):  Default: True.
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CharacterReferenceListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            subject_type=subject_type,
            subject_bot_id=subject_bot_id,
            subject_user_id=subject_user_id,
            subject_persona_id=subject_persona_id,
            active_only=active_only,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
