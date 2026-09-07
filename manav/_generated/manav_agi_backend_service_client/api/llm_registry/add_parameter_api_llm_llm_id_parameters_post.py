from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.llm_parameter_create import LLMParameterCreate
from ...models.llm_parameter_response import LLMParameterResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    llm_id: UUID,
    *,
    body: LLMParameterCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/llm/{llm_id}/parameters".format(
            llm_id=quote(str(llm_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LLMParameterResponse | None:
    if response.status_code == 200:
        response_200 = LLMParameterResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LLMParameterResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    llm_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LLMParameterCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LLMParameterResponse]:
    """Add Parameter

     Add parameter to LLM

    Args:
        llm_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (LLMParameterCreate): Create LLM parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LLMParameterResponse]
    """

    kwargs = _get_kwargs(
        llm_id=llm_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    llm_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LLMParameterCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LLMParameterResponse | None:
    """Add Parameter

     Add parameter to LLM

    Args:
        llm_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (LLMParameterCreate): Create LLM parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LLMParameterResponse
    """

    return sync_detailed(
        llm_id=llm_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    llm_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LLMParameterCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LLMParameterResponse]:
    """Add Parameter

     Add parameter to LLM

    Args:
        llm_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (LLMParameterCreate): Create LLM parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LLMParameterResponse]
    """

    kwargs = _get_kwargs(
        llm_id=llm_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    llm_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: LLMParameterCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LLMParameterResponse | None:
    """Add Parameter

     Add parameter to LLM

    Args:
        llm_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (LLMParameterCreate): Create LLM parameter

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LLMParameterResponse
    """

    return (
        await asyncio_detailed(
            llm_id=llm_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
