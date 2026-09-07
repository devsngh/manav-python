from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hil_rule_list_response import HILRuleListResponse
from ...models.hil_rule_status import HILRuleStatus
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: HILRuleStatus | None | Unset = UNSET,
    tool_name: None | str | Unset = UNSET,
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
    elif isinstance(status, HILRuleStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_tool_name: None | str | Unset
    if isinstance(tool_name, Unset):
        json_tool_name = UNSET
    else:
        json_tool_name = tool_name
    params["tool_name"] = json_tool_name

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/hil-rules",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HILRuleListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = HILRuleListResponse.from_dict(response.json())

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
) -> Response[HILRuleListResponse | HTTPValidationError]:
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
    status: HILRuleStatus | None | Unset = UNSET,
    tool_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HILRuleListResponse | HTTPValidationError]:
    """List Hil Rules

     List HIL rules. Non-admin callers see only the rules THEY created —
    the seeded platform-wide policy rules are hidden. Platform admins see
    every rule.

    Args:
        search (None | str | Unset):
        status (HILRuleStatus | None | Unset):
        tool_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILRuleListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        tool_name=tool_name,
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
    status: HILRuleStatus | None | Unset = UNSET,
    tool_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HILRuleListResponse | HTTPValidationError | None:
    """List Hil Rules

     List HIL rules. Non-admin callers see only the rules THEY created —
    the seeded platform-wide policy rules are hidden. Platform admins see
    every rule.

    Args:
        search (None | str | Unset):
        status (HILRuleStatus | None | Unset):
        tool_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILRuleListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        tool_name=tool_name,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: HILRuleStatus | None | Unset = UNSET,
    tool_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HILRuleListResponse | HTTPValidationError]:
    """List Hil Rules

     List HIL rules. Non-admin callers see only the rules THEY created —
    the seeded platform-wide policy rules are hidden. Platform admins see
    every rule.

    Args:
        search (None | str | Unset):
        status (HILRuleStatus | None | Unset):
        tool_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HILRuleListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        tool_name=tool_name,
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
    status: HILRuleStatus | None | Unset = UNSET,
    tool_name: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HILRuleListResponse | HTTPValidationError | None:
    """List Hil Rules

     List HIL rules. Non-admin callers see only the rules THEY created —
    the seeded platform-wide policy rules are hidden. Platform admins see
    every rule.

    Args:
        search (None | str | Unset):
        status (HILRuleStatus | None | Unset):
        tool_name (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HILRuleListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            tool_name=tool_name,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
