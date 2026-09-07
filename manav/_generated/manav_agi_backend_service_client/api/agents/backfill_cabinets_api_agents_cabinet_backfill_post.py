from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backfill_response import BackfillResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/agents/cabinet/backfill",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackfillResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BackfillResponse.from_dict(response.json())

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
) -> Response[BackfillResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[BackfillResponse | HTTPValidationError]:
    """Backfill Cabinets

     One-shot endpoint to seed V2 cabinets for every deepagent_config.

    Useful right after a fresh `master_seed.py` run so all agents have
    their `_first_boot.md` + role/master cabinet drafts + org constitution
    + library/library.md staged in the LangGraph store before any of them
    is woken. /team_knowledge/ is skipped (dept_id resolution is per-agent;
    caller may extend later).

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackfillResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> BackfillResponse | HTTPValidationError | None:
    """Backfill Cabinets

     One-shot endpoint to seed V2 cabinets for every deepagent_config.

    Useful right after a fresh `master_seed.py` run so all agents have
    their `_first_boot.md` + role/master cabinet drafts + org constitution
    + library/library.md staged in the LangGraph store before any of them
    is woken. /team_knowledge/ is skipped (dept_id resolution is per-agent;
    caller may extend later).

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackfillResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[BackfillResponse | HTTPValidationError]:
    """Backfill Cabinets

     One-shot endpoint to seed V2 cabinets for every deepagent_config.

    Useful right after a fresh `master_seed.py` run so all agents have
    their `_first_boot.md` + role/master cabinet drafts + org constitution
    + library/library.md staged in the LangGraph store before any of them
    is woken. /team_knowledge/ is skipped (dept_id resolution is per-agent;
    caller may extend later).

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackfillResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> BackfillResponse | HTTPValidationError | None:
    """Backfill Cabinets

     One-shot endpoint to seed V2 cabinets for every deepagent_config.

    Useful right after a fresh `master_seed.py` run so all agents have
    their `_first_boot.md` + role/master cabinet drafts + org constitution
    + library/library.md staged in the LangGraph store before any of them
    is woken. /team_knowledge/ is skipped (dept_id resolution is per-agent;
    caller may extend later).

    Args:
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackfillResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
        )
    ).parsed
