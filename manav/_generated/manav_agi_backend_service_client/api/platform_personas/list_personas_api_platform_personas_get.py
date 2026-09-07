from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.persona_list_response import PersonaListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tier: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_tier: None | str | Unset
    if isinstance(tier, Unset):
        json_tier = UNSET
    else:
        json_tier = tier
    params["tier"] = json_tier

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_buying_committee_role: None | str | Unset
    if isinstance(buying_committee_role, Unset):
        json_buying_committee_role = UNSET
    else:
        json_buying_committee_role = buying_committee_role
    params["buying_committee_role"] = json_buying_committee_role

    params["include_deleted"] = include_deleted

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/personas",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PersonaListResponse | None:
    if response.status_code == 200:
        response_200 = PersonaListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PersonaListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    tier: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PersonaListResponse]:
    """List Personas

    Args:
        tier (None | str | Unset):
        status (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PersonaListResponse]
    """

    kwargs = _get_kwargs(
        tier=tier,
        status=status,
        buying_committee_role=buying_committee_role,
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
    tier: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PersonaListResponse | None:
    """List Personas

    Args:
        tier (None | str | Unset):
        status (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PersonaListResponse
    """

    return sync_detailed(
        client=client,
        tier=tier,
        status=status,
        buying_committee_role=buying_committee_role,
        include_deleted=include_deleted,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    tier: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PersonaListResponse]:
    """List Personas

    Args:
        tier (None | str | Unset):
        status (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PersonaListResponse]
    """

    kwargs = _get_kwargs(
        tier=tier,
        status=status,
        buying_committee_role=buying_committee_role,
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
    tier: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    buying_committee_role: None | str | Unset = UNSET,
    include_deleted: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PersonaListResponse | None:
    """List Personas

    Args:
        tier (None | str | Unset):
        status (None | str | Unset):
        buying_committee_role (None | str | Unset):
        include_deleted (bool | Unset):  Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PersonaListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            tier=tier,
            status=status,
            buying_committee_role=buying_committee_role,
            include_deleted=include_deleted,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
