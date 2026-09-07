from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cabinet_reseed_response import CabinetReseedResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_name: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/cabinet/reseed/{agent_name}".format(
            agent_name=quote(str(agent_name), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CabinetReseedResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CabinetReseedResponse.from_dict(response.json())

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
) -> Response[CabinetReseedResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetReseedResponse | HTTPValidationError]:
    """Reseed Agent

     Force a cabinet re-seed for one agent — useful after editing
    templates so the change reaches a running agent without a full
    re-activation. Skipped for subagents.

    Args:
        agent_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetReseedResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_name=agent_name,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CabinetReseedResponse | HTTPValidationError | None:
    """Reseed Agent

     Force a cabinet re-seed for one agent — useful after editing
    templates so the change reaches a running agent without a full
    re-activation. Skipped for subagents.

    Args:
        agent_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetReseedResponse | HTTPValidationError
    """

    return sync_detailed(
        agent_name=agent_name,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetReseedResponse | HTTPValidationError]:
    """Reseed Agent

     Force a cabinet re-seed for one agent — useful after editing
    templates so the change reaches a running agent without a full
    re-activation. Skipped for subagents.

    Args:
        agent_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetReseedResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        agent_name=agent_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_name: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CabinetReseedResponse | HTTPValidationError | None:
    """Reseed Agent

     Force a cabinet re-seed for one agent — useful after editing
    templates so the change reaches a running agent without a full
    re-activation. Skipped for subagents.

    Args:
        agent_name (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetReseedResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            agent_name=agent_name,
            client=client,
            authorization=authorization,
        )
    ).parsed
