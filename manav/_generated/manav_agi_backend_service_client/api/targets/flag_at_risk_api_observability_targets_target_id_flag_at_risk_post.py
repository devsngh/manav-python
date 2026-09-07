from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_target_response import AgentTargetResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.target_flag_at_risk import TargetFlagAtRisk
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_id: UUID,
    *,
    body: TargetFlagAtRisk,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/observability/targets/{target_id}/flag-at-risk".format(
            target_id=quote(str(target_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentTargetResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AgentTargetResponse.from_dict(response.json())

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
) -> Response[AgentTargetResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TargetFlagAtRisk,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentTargetResponse | HTTPValidationError]:
    """Flag At Risk

     Agent self-flags target before timeout. Appends to evidence_refs.

    Args:
        target_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TargetFlagAtRisk): POST .../flag-at-risk — agent self-flags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTargetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TargetFlagAtRisk,
    authorization: None | str | Unset = UNSET,
) -> AgentTargetResponse | HTTPValidationError | None:
    """Flag At Risk

     Agent self-flags target before timeout. Appends to evidence_refs.

    Args:
        target_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TargetFlagAtRisk): POST .../flag-at-risk — agent self-flags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTargetResponse | HTTPValidationError
    """

    return sync_detailed(
        target_id=target_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TargetFlagAtRisk,
    authorization: None | str | Unset = UNSET,
) -> Response[AgentTargetResponse | HTTPValidationError]:
    """Flag At Risk

     Agent self-flags target before timeout. Appends to evidence_refs.

    Args:
        target_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TargetFlagAtRisk): POST .../flag-at-risk — agent self-flags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentTargetResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TargetFlagAtRisk,
    authorization: None | str | Unset = UNSET,
) -> AgentTargetResponse | HTTPValidationError | None:
    """Flag At Risk

     Agent self-flags target before timeout. Appends to evidence_refs.

    Args:
        target_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TargetFlagAtRisk): POST .../flag-at-risk — agent self-flags.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentTargetResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            target_id=target_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
