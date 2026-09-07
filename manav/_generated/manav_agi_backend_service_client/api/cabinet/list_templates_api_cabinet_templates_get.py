from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cabinet_template_summary import CabinetTemplateSummary
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bucket: None | str | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    role: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_bucket: None | str | Unset
    if isinstance(bucket, Unset):
        json_bucket = UNSET
    else:
        json_bucket = bucket
    params["bucket"] = json_bucket

    json_agent_name: None | str | Unset
    if isinstance(agent_name, Unset):
        json_agent_name = UNSET
    else:
        json_agent_name = agent_name
    params["agent_name"] = json_agent_name

    json_role: None | str | Unset
    if isinstance(role, Unset):
        json_role = UNSET
    else:
        json_role = role
    params["role"] = json_role

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    params["active_only"] = active_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cabinet/templates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CabinetTemplateSummary] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CabinetTemplateSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[CabinetTemplateSummary]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bucket: None | str | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    role: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CabinetTemplateSummary]]:
    """List Templates

     List templates with optional filters. No content body — use the
    single-template endpoint to fetch full YAML.

    Args:
        bucket (None | str | Unset): Filter to one bucket
        agent_name (None | str | Unset): Per-agent override filter
        role (None | str | Unset): Archetype role filter
        org_id (None | str | Unset): Scope filter. Special values: 'platform' → only platform
            defaults (org_id IS NULL); UUID → that org's overrides only. Omitted → return both scopes
            together.
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CabinetTemplateSummary]]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        agent_name=agent_name,
        role=role,
        org_id=org_id,
        active_only=active_only,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bucket: None | str | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    role: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CabinetTemplateSummary] | None:
    """List Templates

     List templates with optional filters. No content body — use the
    single-template endpoint to fetch full YAML.

    Args:
        bucket (None | str | Unset): Filter to one bucket
        agent_name (None | str | Unset): Per-agent override filter
        role (None | str | Unset): Archetype role filter
        org_id (None | str | Unset): Scope filter. Special values: 'platform' → only platform
            defaults (org_id IS NULL); UUID → that org's overrides only. Omitted → return both scopes
            together.
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CabinetTemplateSummary]
    """

    return sync_detailed(
        client=client,
        bucket=bucket,
        agent_name=agent_name,
        role=role,
        org_id=org_id,
        active_only=active_only,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bucket: None | str | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    role: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[CabinetTemplateSummary]]:
    """List Templates

     List templates with optional filters. No content body — use the
    single-template endpoint to fetch full YAML.

    Args:
        bucket (None | str | Unset): Filter to one bucket
        agent_name (None | str | Unset): Per-agent override filter
        role (None | str | Unset): Archetype role filter
        org_id (None | str | Unset): Scope filter. Special values: 'platform' → only platform
            defaults (org_id IS NULL); UUID → that org's overrides only. Omitted → return both scopes
            together.
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CabinetTemplateSummary]]
    """

    kwargs = _get_kwargs(
        bucket=bucket,
        agent_name=agent_name,
        role=role,
        org_id=org_id,
        active_only=active_only,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bucket: None | str | Unset = UNSET,
    agent_name: None | str | Unset = UNSET,
    role: None | str | Unset = UNSET,
    org_id: None | str | Unset = UNSET,
    active_only: bool | Unset = True,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[CabinetTemplateSummary] | None:
    """List Templates

     List templates with optional filters. No content body — use the
    single-template endpoint to fetch full YAML.

    Args:
        bucket (None | str | Unset): Filter to one bucket
        agent_name (None | str | Unset): Per-agent override filter
        role (None | str | Unset): Archetype role filter
        org_id (None | str | Unset): Scope filter. Special values: 'platform' → only platform
            defaults (org_id IS NULL); UUID → that org's overrides only. Omitted → return both scopes
            together.
        active_only (bool | Unset):  Default: True.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CabinetTemplateSummary]
    """

    return (
        await asyncio_detailed(
            client=client,
            bucket=bucket,
            agent_name=agent_name,
            role=role,
            org_id=org_id,
            active_only=active_only,
            authorization=authorization,
        )
    ).parsed
