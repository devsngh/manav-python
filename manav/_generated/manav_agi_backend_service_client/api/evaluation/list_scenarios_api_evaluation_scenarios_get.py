from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category: None | str | Unset = UNSET,
    bot_name: None | str | Unset = UNSET,
    tag: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_bot_name: None | str | Unset
    if isinstance(bot_name, Unset):
        json_bot_name = UNSET
    else:
        json_bot_name = bot_name
    params["bot_name"] = json_bot_name

    json_tag: None | str | Unset
    if isinstance(tag, Unset):
        json_tag = UNSET
    else:
        json_tag = tag
    params["tag"] = json_tag

    json_dataset_id: None | str | Unset
    if isinstance(dataset_id, Unset):
        json_dataset_id = UNSET
    else:
        json_dataset_id = dataset_id
    params["dataset_id"] = json_dataset_id

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/evaluation/scenarios",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    bot_name: None | str | Unset = UNSET,
    tag: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """List Scenarios

    Args:
        category (None | str | Unset):
        bot_name (None | str | Unset):
        tag (None | str | Unset):
        dataset_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        category=category,
        bot_name=bot_name,
        tag=tag,
        dataset_id=dataset_id,
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
    category: None | str | Unset = UNSET,
    bot_name: None | str | Unset = UNSET,
    tag: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """List Scenarios

    Args:
        category (None | str | Unset):
        bot_name (None | str | Unset):
        tag (None | str | Unset):
        dataset_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        category=category,
        bot_name=bot_name,
        tag=tag,
        dataset_id=dataset_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    bot_name: None | str | Unset = UNSET,
    tag: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """List Scenarios

    Args:
        category (None | str | Unset):
        bot_name (None | str | Unset):
        tag (None | str | Unset):
        dataset_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        category=category,
        bot_name=bot_name,
        tag=tag,
        dataset_id=dataset_id,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    category: None | str | Unset = UNSET,
    bot_name: None | str | Unset = UNSET,
    tag: None | str | Unset = UNSET,
    dataset_id: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """List Scenarios

    Args:
        category (None | str | Unset):
        bot_name (None | str | Unset):
        tag (None | str | Unset):
        dataset_id (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            bot_name=bot_name,
            tag=tag,
            dataset_id=dataset_id,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
