from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cabinet_sync_response import CabinetSyncResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_name: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/agents/cabinet/sync-to-workspace/{bot_name}".format(
            bot_name=quote(str(bot_name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CabinetSyncResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CabinetSyncResponse.from_dict(response.json())

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
) -> Response[CabinetSyncResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetSyncResponse | HTTPValidationError]:
    """Sync Cabinet To Workspace One

     Sync one bot's cabinet content from the LangGraph store into mem_<org>.

    Triggered automatically by the activation route on every activate call —
    this endpoint is for manual re-sync (e.g., after a cabinet content update
    that the activation hook didn't catch).

    Args:
        bot_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetSyncResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_name=bot_name,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CabinetSyncResponse | HTTPValidationError | None:
    """Sync Cabinet To Workspace One

     Sync one bot's cabinet content from the LangGraph store into mem_<org>.

    Triggered automatically by the activation route on every activate call —
    this endpoint is for manual re-sync (e.g., after a cabinet content update
    that the activation hook didn't catch).

    Args:
        bot_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetSyncResponse | HTTPValidationError
    """

    return sync_detailed(
        bot_name=bot_name,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetSyncResponse | HTTPValidationError]:
    """Sync Cabinet To Workspace One

     Sync one bot's cabinet content from the LangGraph store into mem_<org>.

    Triggered automatically by the activation route on every activate call —
    this endpoint is for manual re-sync (e.g., after a cabinet content update
    that the activation hook didn't catch).

    Args:
        bot_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetSyncResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        bot_name=bot_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CabinetSyncResponse | HTTPValidationError | None:
    """Sync Cabinet To Workspace One

     Sync one bot's cabinet content from the LangGraph store into mem_<org>.

    Triggered automatically by the activation route on every activate call —
    this endpoint is for manual re-sync (e.g., after a cabinet content update
    that the activation hook didn't catch).

    Args:
        bot_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetSyncResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            bot_name=bot_name,
            client=client,
            authorization=authorization,
        )
    ).parsed
