from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.prompt_list_response import PromptListResponse
from ...models.prompt_role import PromptRole
from ...models.prompt_status import PromptStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search: None | str | Unset = UNSET,
    status: None | PromptStatus | Unset = UNSET,
    category: None | str | Unset = UNSET,
    prompt_role: None | PromptRole | Unset = UNSET,
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
    elif isinstance(status, PromptStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_prompt_role: None | str | Unset
    if isinstance(prompt_role, Unset):
        json_prompt_role = UNSET
    elif isinstance(prompt_role, PromptRole):
        json_prompt_role = prompt_role.value
    else:
        json_prompt_role = prompt_role
    params["prompt_role"] = json_prompt_role

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/prompts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PromptListResponse | None:
    if response.status_code == 200:
        response_200 = PromptListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PromptListResponse]:
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
    status: None | PromptStatus | Unset = UNSET,
    category: None | str | Unset = UNSET,
    prompt_role: None | PromptRole | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PromptListResponse]:
    """List Prompts

     List prompts. Own-scoped: a plan user sees only prompts they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset):
        status (None | PromptStatus | Unset):
        category (None | str | Unset):
        prompt_role (None | PromptRole | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        category=category,
        prompt_role=prompt_role,
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
    status: None | PromptStatus | Unset = UNSET,
    category: None | str | Unset = UNSET,
    prompt_role: None | PromptRole | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PromptListResponse | None:
    """List Prompts

     List prompts. Own-scoped: a plan user sees only prompts they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset):
        status (None | PromptStatus | Unset):
        category (None | str | Unset):
        prompt_role (None | PromptRole | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptListResponse
    """

    return sync_detailed(
        client=client,
        search=search,
        status=status,
        category=category,
        prompt_role=prompt_role,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    search: None | str | Unset = UNSET,
    status: None | PromptStatus | Unset = UNSET,
    category: None | str | Unset = UNSET,
    prompt_role: None | PromptRole | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PromptListResponse]:
    """List Prompts

     List prompts. Own-scoped: a plan user sees only prompts they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset):
        status (None | PromptStatus | Unset):
        category (None | str | Unset):
        prompt_role (None | PromptRole | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PromptListResponse]
    """

    kwargs = _get_kwargs(
        search=search,
        status=status,
        category=category,
        prompt_role=prompt_role,
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
    status: None | PromptStatus | Unset = UNSET,
    category: None | str | Unset = UNSET,
    prompt_role: None | PromptRole | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PromptListResponse | None:
    """List Prompts

     List prompts. Own-scoped: a plan user sees only prompts they created;
    a platform admin sees all.

    Args:
        search (None | str | Unset):
        status (None | PromptStatus | Unset):
        category (None | str | Unset):
        prompt_role (None | PromptRole | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PromptListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            search=search,
            status=status,
            category=category,
            prompt_role=prompt_role,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
