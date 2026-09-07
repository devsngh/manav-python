from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cabinet_template_create import CabinetTemplateCreate
from ...models.cabinet_template_full import CabinetTemplateFull
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CabinetTemplateCreate,
    source: str | Unset = "ui",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["source"] = source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/cabinet/templates",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CabinetTemplateFull | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = CabinetTemplateFull.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CabinetTemplateFull | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CabinetTemplateCreate,
    source: str | Unset = "ui",
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetTemplateFull | HTTPValidationError]:
    """Create Template

    Args:
        source (str | Unset): Provenance tag — 'ui' (human) or 'agent' (MCP writer) Default: 'ui'.
        authorization (None | str | Unset): Bearer token
        body (CabinetTemplateCreate): Body for `POST /api/cabinet/templates`.

            The route fills in `created_by_user_id` from the auth dependency and
            sets `source='ui'` (UI authoring) or `source='agent'` (when called via
            `cabinet_writer_mcp` — that path uses a different internal entrypoint).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetTemplateFull | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        source=source,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CabinetTemplateCreate,
    source: str | Unset = "ui",
    authorization: None | str | Unset = UNSET,
) -> CabinetTemplateFull | HTTPValidationError | None:
    """Create Template

    Args:
        source (str | Unset): Provenance tag — 'ui' (human) or 'agent' (MCP writer) Default: 'ui'.
        authorization (None | str | Unset): Bearer token
        body (CabinetTemplateCreate): Body for `POST /api/cabinet/templates`.

            The route fills in `created_by_user_id` from the auth dependency and
            sets `source='ui'` (UI authoring) or `source='agent'` (when called via
            `cabinet_writer_mcp` — that path uses a different internal entrypoint).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetTemplateFull | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        source=source,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CabinetTemplateCreate,
    source: str | Unset = "ui",
    authorization: None | str | Unset = UNSET,
) -> Response[CabinetTemplateFull | HTTPValidationError]:
    """Create Template

    Args:
        source (str | Unset): Provenance tag — 'ui' (human) or 'agent' (MCP writer) Default: 'ui'.
        authorization (None | str | Unset): Bearer token
        body (CabinetTemplateCreate): Body for `POST /api/cabinet/templates`.

            The route fills in `created_by_user_id` from the auth dependency and
            sets `source='ui'` (UI authoring) or `source='agent'` (when called via
            `cabinet_writer_mcp` — that path uses a different internal entrypoint).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CabinetTemplateFull | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        source=source,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CabinetTemplateCreate,
    source: str | Unset = "ui",
    authorization: None | str | Unset = UNSET,
) -> CabinetTemplateFull | HTTPValidationError | None:
    """Create Template

    Args:
        source (str | Unset): Provenance tag — 'ui' (human) or 'agent' (MCP writer) Default: 'ui'.
        authorization (None | str | Unset): Bearer token
        body (CabinetTemplateCreate): Body for `POST /api/cabinet/templates`.

            The route fills in `created_by_user_id` from the auth dependency and
            sets `source='ui'` (UI authoring) or `source='agent'` (when called via
            `cabinet_writer_mcp` — that path uses a different internal entrypoint).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CabinetTemplateFull | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            source=source,
            authorization=authorization,
        )
    ).parsed
