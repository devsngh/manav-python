from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execution_config_response import ExecutionConfigResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    model_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["model_id"] = model_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/llm/internal/resolve-by-model-id",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecutionConfigResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ExecutionConfigResponse.from_dict(response.json())

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
) -> Response[ExecutionConfigResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_id: str,
) -> Response[ExecutionConfigResponse | HTTPValidationError]:
    """Internal Resolve By Model Id

    Args:
        model_id (str): The model_id string, e.g. 'gpt-image-1'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionConfigResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    model_id: str,
) -> ExecutionConfigResponse | HTTPValidationError | None:
    """Internal Resolve By Model Id

    Args:
        model_id (str): The model_id string, e.g. 'gpt-image-1'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionConfigResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        model_id=model_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    model_id: str,
) -> Response[ExecutionConfigResponse | HTTPValidationError]:
    """Internal Resolve By Model Id

    Args:
        model_id (str): The model_id string, e.g. 'gpt-image-1'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecutionConfigResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        model_id=model_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    model_id: str,
) -> ExecutionConfigResponse | HTTPValidationError | None:
    """Internal Resolve By Model Id

    Args:
        model_id (str): The model_id string, e.g. 'gpt-image-1'

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecutionConfigResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            model_id=model_id,
        )
    ).parsed
