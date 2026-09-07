from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.public_persona_list_response import PublicPersonaListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    subject_type: None | str | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
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

    json_is_public: bool | None | Unset
    if isinstance(is_public, Unset):
        json_is_public = UNSET
    else:
        json_is_public = is_public
    params["is_public"] = json_is_public

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/public-personas",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PublicPersonaListResponse | None:
    if response.status_code == 200:
        response_200 = PublicPersonaListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PublicPersonaListResponse]:
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
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PublicPersonaListResponse]:
    """List Public Personas

    Args:
        subject_type (None | str | Unset): bot / human
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PublicPersonaListResponse]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        is_public=is_public,
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
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PublicPersonaListResponse | None:
    """List Public Personas

    Args:
        subject_type (None | str | Unset): bot / human
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PublicPersonaListResponse
    """

    return sync_detailed(
        client=client,
        subject_type=subject_type,
        is_public=is_public,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    subject_type: None | str | Unset = UNSET,
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PublicPersonaListResponse]:
    """List Public Personas

    Args:
        subject_type (None | str | Unset): bot / human
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PublicPersonaListResponse]
    """

    kwargs = _get_kwargs(
        subject_type=subject_type,
        is_public=is_public,
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
    is_public: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PublicPersonaListResponse | None:
    """List Public Personas

    Args:
        subject_type (None | str | Unset): bot / human
        is_public (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PublicPersonaListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            subject_type=subject_type,
            is_public=is_public,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
