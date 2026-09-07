from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activate_body import ActivateBody
from ...models.activate_response import ActivateResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ActivateBody,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/agents/activate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivateResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ActivateResponse.from_dict(response.json())

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
) -> Response[ActivateResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateBody,
    authorization: None | str | Unset = UNSET,
) -> Response[ActivateResponse | HTTPValidationError]:
    """Activate Agent

     Activate or deactivate a deepagent.

    Authz (relaxed 2026-08-19): super admin can activate ANY agent.
    A regular user can activate an agent they OWN (owner_user_id matches).
    Platform-seeded agents (owner_user_id NULL — Orro, Manav, Cyra, etc.)
    require super admin. See module docstring for the full activation policy.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ActivateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateBody,
    authorization: None | str | Unset = UNSET,
) -> ActivateResponse | HTTPValidationError | None:
    """Activate Agent

     Activate or deactivate a deepagent.

    Authz (relaxed 2026-08-19): super admin can activate ANY agent.
    A regular user can activate an agent they OWN (owner_user_id matches).
    Platform-seeded agents (owner_user_id NULL — Orro, Manav, Cyra, etc.)
    require super admin. See module docstring for the full activation policy.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ActivateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateBody,
    authorization: None | str | Unset = UNSET,
) -> Response[ActivateResponse | HTTPValidationError]:
    """Activate Agent

     Activate or deactivate a deepagent.

    Authz (relaxed 2026-08-19): super admin can activate ANY agent.
    A regular user can activate an agent they OWN (owner_user_id matches).
    Platform-seeded agents (owner_user_id NULL — Orro, Manav, Cyra, etc.)
    require super admin. See module docstring for the full activation policy.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ActivateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivateResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ActivateBody,
    authorization: None | str | Unset = UNSET,
) -> ActivateResponse | HTTPValidationError | None:
    """Activate Agent

     Activate or deactivate a deepagent.

    Authz (relaxed 2026-08-19): super admin can activate ANY agent.
    A regular user can activate an agent they OWN (owner_user_id matches).
    Platform-seeded agents (owner_user_id NULL — Orro, Manav, Cyra, etc.)
    require super admin. See module docstring for the full activation policy.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ActivateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivateResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
