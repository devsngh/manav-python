from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deep_agent_list_response import DeepAgentListResponse
from ...models.deep_agent_status import DeepAgentStatus
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: DeepAgentStatus | None | Unset = UNSET,
    include_internal: bool | Unset = False,
    is_judge: bool | None | Unset = UNSET,
    is_ingestion: bool | None | Unset = UNSET,
    own_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, DeepAgentStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params["include_internal"] = include_internal

    json_is_judge: bool | None | Unset
    if isinstance(is_judge, Unset):
        json_is_judge = UNSET
    else:
        json_is_judge = is_judge
    params["is_judge"] = json_is_judge

    json_is_ingestion: bool | None | Unset
    if isinstance(is_ingestion, Unset):
        json_is_ingestion = UNSET
    else:
        json_is_ingestion = is_ingestion
    params["is_ingestion"] = json_is_ingestion

    params["own_only"] = own_only

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = DeepAgentListResponse.from_dict(response.json())

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
) -> Response[DeepAgentListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: DeepAgentStatus | None | Unset = UNSET,
    include_internal: bool | Unset = False,
    is_judge: bool | None | Unset = UNSET,
    is_ingestion: bool | None | Unset = UNSET,
    own_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentListResponse | HTTPValidationError]:
    """List Deepagents

     List DeepAgents.

    Plan user (non-admin) visibility:
      * own_only=false (default) — owned + assigned + rented (P2 union),
        with a `source` badge per row. Powers chat tray + playground.
      * own_only=true — owned only. Powers the registry page so table +
        metrics stay consistent on the user's own inventory.
    Internal/system agents stay hidden from plan users regardless.
    Platform admin sees all and may opt into internal via include_internal.

    Args:
        search (None | str | Unset):
        status (DeepAgentStatus | None | Unset):
        include_internal (bool | Unset): Include internal/system agents (super admin only)
            Default: False.
        is_judge (bool | None | Unset): Filter by judge flag (true = only judges)
        is_ingestion (bool | None | Unset): Filter by ingestion flag (true = only ingestion
            agents)
        own_only (bool | Unset): Plan users: skip the P2 assigned+rented union and return owned
            only. Default false keeps the chat tray / playground picker showing everything visible;
            the registry page passes true so its table + metrics stay consistent on the user's own
            inventory. Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        include_internal=include_internal,
        is_judge=is_judge,
        is_ingestion=is_ingestion,
        own_only=own_only,
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
    search: None | str | Unset = UNSET,
    status: DeepAgentStatus | None | Unset = UNSET,
    include_internal: bool | Unset = False,
    is_judge: bool | None | Unset = UNSET,
    is_ingestion: bool | None | Unset = UNSET,
    own_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentListResponse | HTTPValidationError | None:
    """List Deepagents

     List DeepAgents.

    Plan user (non-admin) visibility:
      * own_only=false (default) — owned + assigned + rented (P2 union),
        with a `source` badge per row. Powers chat tray + playground.
      * own_only=true — owned only. Powers the registry page so table +
        metrics stay consistent on the user's own inventory.
    Internal/system agents stay hidden from plan users regardless.
    Platform admin sees all and may opt into internal via include_internal.

    Args:
        search (None | str | Unset):
        status (DeepAgentStatus | None | Unset):
        include_internal (bool | Unset): Include internal/system agents (super admin only)
            Default: False.
        is_judge (bool | None | Unset): Filter by judge flag (true = only judges)
        is_ingestion (bool | None | Unset): Filter by ingestion flag (true = only ingestion
            agents)
        own_only (bool | Unset): Plan users: skip the P2 assigned+rented union and return owned
            only. Default false keeps the chat tray / playground picker showing everything visible;
            the registry page passes true so its table + metrics stay consistent on the user's own
            inventory. Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        include_internal=include_internal,
        is_judge=is_judge,
        is_ingestion=is_ingestion,
        own_only=own_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: DeepAgentStatus | None | Unset = UNSET,
    include_internal: bool | Unset = False,
    is_judge: bool | None | Unset = UNSET,
    is_ingestion: bool | None | Unset = UNSET,
    own_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentListResponse | HTTPValidationError]:
    """List Deepagents

     List DeepAgents.

    Plan user (non-admin) visibility:
      * own_only=false (default) — owned + assigned + rented (P2 union),
        with a `source` badge per row. Powers chat tray + playground.
      * own_only=true — owned only. Powers the registry page so table +
        metrics stay consistent on the user's own inventory.
    Internal/system agents stay hidden from plan users regardless.
    Platform admin sees all and may opt into internal via include_internal.

    Args:
        search (None | str | Unset):
        status (DeepAgentStatus | None | Unset):
        include_internal (bool | Unset): Include internal/system agents (super admin only)
            Default: False.
        is_judge (bool | None | Unset): Filter by judge flag (true = only judges)
        is_ingestion (bool | None | Unset): Filter by ingestion flag (true = only ingestion
            agents)
        own_only (bool | Unset): Plan users: skip the P2 assigned+rented union and return owned
            only. Default false keeps the chat tray / playground picker showing everything visible;
            the registry page passes true so its table + metrics stay consistent on the user's own
            inventory. Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        include_internal=include_internal,
        is_judge=is_judge,
        is_ingestion=is_ingestion,
        own_only=own_only,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: DeepAgentStatus | None | Unset = UNSET,
    include_internal: bool | Unset = False,
    is_judge: bool | None | Unset = UNSET,
    is_ingestion: bool | None | Unset = UNSET,
    own_only: bool | Unset = False,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentListResponse | HTTPValidationError | None:
    """List Deepagents

     List DeepAgents.

    Plan user (non-admin) visibility:
      * own_only=false (default) — owned + assigned + rented (P2 union),
        with a `source` badge per row. Powers chat tray + playground.
      * own_only=true — owned only. Powers the registry page so table +
        metrics stay consistent on the user's own inventory.
    Internal/system agents stay hidden from plan users regardless.
    Platform admin sees all and may opt into internal via include_internal.

    Args:
        search (None | str | Unset):
        status (DeepAgentStatus | None | Unset):
        include_internal (bool | Unset): Include internal/system agents (super admin only)
            Default: False.
        is_judge (bool | None | Unset): Filter by judge flag (true = only judges)
        is_ingestion (bool | None | Unset): Filter by ingestion flag (true = only ingestion
            agents)
        own_only (bool | Unset): Plan users: skip the P2 assigned+rented union and return owned
            only. Default false keeps the chat tray / playground picker showing everything visible;
            the registry page passes true so its table + metrics stay consistent on the user's own
            inventory. Default: False.
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            include_internal=include_internal,
            is_judge=is_judge,
            is_ingestion=is_ingestion,
            own_only=own_only,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
