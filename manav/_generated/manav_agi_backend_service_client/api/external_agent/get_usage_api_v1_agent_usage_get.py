from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.usage_response import UsageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    headers["X-API-Key"] = x_api_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agent/usage",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UsageResponse | None:
    if response.status_code == 200:
        response_200 = UsageResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UsageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> Response[HTTPValidationError | UsageResponse]:
    """Get Usage

     Get usage stats for the current API key.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> HTTPValidationError | UsageResponse | None:
    """Get Usage

     Get usage stats for the current API key.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageResponse
    """

    return sync_detailed(
        client=client,
        authorization=authorization,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> Response[HTTPValidationError | UsageResponse]:
    """Get Usage

     Get usage stats for the current API key.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageResponse]
    """

    kwargs = _get_kwargs(
        authorization=authorization,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
    x_api_key: str,
) -> HTTPValidationError | UsageResponse | None:
    """Get Usage

     Get usage stats for the current API key.

    Args:
        authorization (None | str | Unset): Bearer token
        x_api_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            authorization=authorization,
            x_api_key=x_api_key,
        )
    ).parsed
