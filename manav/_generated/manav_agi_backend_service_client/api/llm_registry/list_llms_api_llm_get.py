from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.llm_list_response import LLMListResponse
from ...models.llm_status import LLMStatus
from ...models.model_category import ModelCategory
from ...models.model_type import ModelType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status_filter: LLMStatus | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_category: ModelCategory | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider

    json_status_filter: None | str | Unset
    if isinstance(status_filter, Unset):
        json_status_filter = UNSET
    elif isinstance(status_filter, LLMStatus):
        json_status_filter = status_filter.value
    else:
        json_status_filter = status_filter
    params["status_filter"] = json_status_filter

    json_model_type: None | str | Unset
    if isinstance(model_type, Unset):
        json_model_type = UNSET
    elif isinstance(model_type, ModelType):
        json_model_type = model_type.value
    else:
        json_model_type = model_type
    params["model_type"] = json_model_type

    json_model_category: None | str | Unset
    if isinstance(model_category, Unset):
        json_model_category = UNSET
    elif isinstance(model_category, ModelCategory):
        json_model_category = model_category.value
    else:
        json_model_category = model_category
    params["model_category"] = json_model_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/llm/",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LLMListResponse | None:
    if response.status_code == 200:
        response_200 = LLMListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LLMListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status_filter: LLMStatus | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_category: ModelCategory | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LLMListResponse]:
    """List Llms

     List LLMs with filters and pagination. Shared read-only catalog: everyone sees all.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        provider (None | str | Unset):
        status_filter (LLMStatus | None | Unset):
        model_type (ModelType | None | Unset):
        model_category (ModelCategory | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LLMListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        search=search,
        provider=provider,
        status_filter=status_filter,
        model_type=model_type,
        model_category=model_category,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status_filter: LLMStatus | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_category: ModelCategory | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LLMListResponse | None:
    """List Llms

     List LLMs with filters and pagination. Shared read-only catalog: everyone sees all.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        provider (None | str | Unset):
        status_filter (LLMStatus | None | Unset):
        model_type (ModelType | None | Unset):
        model_category (ModelCategory | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LLMListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        search=search,
        provider=provider,
        status_filter=status_filter,
        model_type=model_type,
        model_category=model_category,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status_filter: LLMStatus | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_category: ModelCategory | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LLMListResponse]:
    """List Llms

     List LLMs with filters and pagination. Shared read-only catalog: everyone sees all.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        provider (None | str | Unset):
        status_filter (LLMStatus | None | Unset):
        model_type (ModelType | None | Unset):
        model_category (ModelCategory | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LLMListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        search=search,
        provider=provider,
        status_filter=status_filter,
        model_type=model_type,
        model_category=model_category,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    search: None | str | Unset = UNSET,
    provider: None | str | Unset = UNSET,
    status_filter: LLMStatus | None | Unset = UNSET,
    model_type: ModelType | None | Unset = UNSET,
    model_category: ModelCategory | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LLMListResponse | None:
    """List Llms

     List LLMs with filters and pagination. Shared read-only catalog: everyone sees all.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        search (None | str | Unset):
        provider (None | str | Unset):
        status_filter (LLMStatus | None | Unset):
        model_type (ModelType | None | Unset):
        model_category (ModelCategory | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LLMListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            search=search,
            provider=provider,
            status_filter=status_filter,
            model_type=model_type,
            model_category=model_category,
            authorization=authorization,
        )
    ).parsed
