from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_stats_response import ExecutionStatsResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_start_date: None | str | Unset
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: None | str | Unset
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent-executions/stats",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecutionStatsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExecutionStatsResponse.from_dict(response.json())

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
) -> Response[ExecutionStatsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ExecutionStatsResponse | HTTPValidationError]:
    """Get Execution Stats

     Get aggregate execution statistics.

    Args:
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionStatsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ExecutionStatsResponse | HTTPValidationError | None:
    """Get Execution Stats

     Get aggregate execution statistics.

    Args:
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionStatsResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[ExecutionStatsResponse | HTTPValidationError]:
    """Get Execution Stats

     Get aggregate execution statistics.

    Args:
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionStatsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    start_date: None | str | Unset = UNSET,
    end_date: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> ExecutionStatsResponse | HTTPValidationError | None:
    """Get Execution Stats

     Get aggregate execution statistics.

    Args:
        start_date (None | str | Unset):
        end_date (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionStatsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            authorization=authorization,
        )
    ).parsed
