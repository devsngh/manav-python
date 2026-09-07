from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.task_response import TaskResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    threshold_minutes: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["threshold_minutes"] = threshold_minutes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/tasks/stale",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[TaskResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TaskResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[TaskResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    threshold_minutes: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[TaskResponse]]:
    """Stale Tasks

    Args:
        threshold_minutes (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[TaskResponse]]
    """

    kwargs = _get_kwargs(
        threshold_minutes=threshold_minutes,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    threshold_minutes: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[TaskResponse] | None:
    """Stale Tasks

    Args:
        threshold_minutes (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[TaskResponse]
    """

    return sync_detailed(
        client=client,
        threshold_minutes=threshold_minutes,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    threshold_minutes: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[TaskResponse]]:
    """Stale Tasks

    Args:
        threshold_minutes (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[TaskResponse]]
    """

    kwargs = _get_kwargs(
        threshold_minutes=threshold_minutes,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    threshold_minutes: int | Unset = 30,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[TaskResponse] | None:
    """Stale Tasks

    Args:
        threshold_minutes (int | Unset):  Default: 30.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[TaskResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            threshold_minutes=threshold_minutes,
            authorization=authorization,
        )
    ).parsed
