from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.competitor_list_response import CompetitorListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    threat_level: None | str | Unset = UNSET,
    primary_category: None | str | Unset = UNSET,
    public_or_private: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_threat_level: None | str | Unset
    if isinstance(threat_level, Unset):
        json_threat_level = UNSET
    else:
        json_threat_level = threat_level
    params["threat_level"] = json_threat_level

    json_primary_category: None | str | Unset
    if isinstance(primary_category, Unset):
        json_primary_category = UNSET
    else:
        json_primary_category = primary_category
    params["primary_category"] = json_primary_category

    json_public_or_private: None | str | Unset
    if isinstance(public_or_private, Unset):
        json_public_or_private = UNSET
    else:
        json_public_or_private = public_or_private
    params["public_or_private"] = json_public_or_private

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/competitors",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompetitorListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CompetitorListResponse.from_dict(response.json())

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
) -> Response[CompetitorListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    threat_level: None | str | Unset = UNSET,
    primary_category: None | str | Unset = UNSET,
    public_or_private: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CompetitorListResponse | HTTPValidationError]:
    """List Competitors

    Args:
        status (None | str | Unset):
        threat_level (None | str | Unset):
        primary_category (None | str | Unset):
        public_or_private (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitorListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        status=status,
        threat_level=threat_level,
        primary_category=primary_category,
        public_or_private=public_or_private,
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
    status: None | str | Unset = UNSET,
    threat_level: None | str | Unset = UNSET,
    primary_category: None | str | Unset = UNSET,
    public_or_private: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CompetitorListResponse | HTTPValidationError | None:
    """List Competitors

    Args:
        status (None | str | Unset):
        threat_level (None | str | Unset):
        primary_category (None | str | Unset):
        public_or_private (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitorListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        status=status,
        threat_level=threat_level,
        primary_category=primary_category,
        public_or_private=public_or_private,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    threat_level: None | str | Unset = UNSET,
    primary_category: None | str | Unset = UNSET,
    public_or_private: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[CompetitorListResponse | HTTPValidationError]:
    """List Competitors

    Args:
        status (None | str | Unset):
        threat_level (None | str | Unset):
        primary_category (None | str | Unset):
        public_or_private (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitorListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        status=status,
        threat_level=threat_level,
        primary_category=primary_category,
        public_or_private=public_or_private,
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
    status: None | str | Unset = UNSET,
    threat_level: None | str | Unset = UNSET,
    primary_category: None | str | Unset = UNSET,
    public_or_private: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> CompetitorListResponse | HTTPValidationError | None:
    """List Competitors

    Args:
        status (None | str | Unset):
        threat_level (None | str | Unset):
        primary_category (None | str | Unset):
        public_or_private (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitorListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            threat_level=threat_level,
            primary_category=primary_category,
            public_or_private=public_or_private,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
