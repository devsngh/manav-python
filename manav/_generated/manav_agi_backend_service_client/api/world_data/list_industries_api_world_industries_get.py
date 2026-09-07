from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.industry_read import IndustryRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    parent_code: None | str | Unset = UNSET,
    typical_cycle: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_parent_code: None | str | Unset
    if isinstance(parent_code, Unset):
        json_parent_code = UNSET
    else:
        json_parent_code = parent_code
    params["parent_code"] = json_parent_code

    json_typical_cycle: None | str | Unset
    if isinstance(typical_cycle, Unset):
        json_typical_cycle = UNSET
    else:
        json_typical_cycle = typical_cycle
    params["typical_cycle"] = json_typical_cycle

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/world/industries",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[IndustryRead] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IndustryRead.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[IndustryRead]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_code: None | str | Unset = UNSET,
    typical_cycle: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[IndustryRead]]:
    """List Industries

    Args:
        parent_code (None | str | Unset):
        typical_cycle (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[IndustryRead]]
    """

    kwargs = _get_kwargs(
        parent_code=parent_code,
        typical_cycle=typical_cycle,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    parent_code: None | str | Unset = UNSET,
    typical_cycle: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[IndustryRead] | None:
    """List Industries

    Args:
        parent_code (None | str | Unset):
        typical_cycle (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[IndustryRead]
    """

    return sync_detailed(
        client=client,
        parent_code=parent_code,
        typical_cycle=typical_cycle,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    parent_code: None | str | Unset = UNSET,
    typical_cycle: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[IndustryRead]]:
    """List Industries

    Args:
        parent_code (None | str | Unset):
        typical_cycle (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[IndustryRead]]
    """

    kwargs = _get_kwargs(
        parent_code=parent_code,
        typical_cycle=typical_cycle,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    parent_code: None | str | Unset = UNSET,
    typical_cycle: None | str | Unset = UNSET,
    limit: int | Unset = 500,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[IndustryRead] | None:
    """List Industries

    Args:
        parent_code (None | str | Unset):
        typical_cycle (None | str | Unset):
        limit (int | Unset):  Default: 500.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[IndustryRead]
    """

    return (
        await asyncio_detailed(
            client=client,
            parent_code=parent_code,
            typical_cycle=typical_cycle,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
