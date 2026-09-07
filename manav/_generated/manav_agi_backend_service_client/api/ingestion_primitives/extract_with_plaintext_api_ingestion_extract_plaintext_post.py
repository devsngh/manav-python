from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.plaintext_request import PlaintextRequest
from ...models.plaintext_response import PlaintextResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PlaintextRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/extract/plaintext",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PlaintextResponse | None:
    if response.status_code == 200:
        response_200 = PlaintextResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PlaintextResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PlaintextRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlaintextResponse]:
    """Extract With Plaintext

     Read a plain-text file (or any text-like file: code, config, csv).

    Primitive: tries the requested encoding (or UTF-8 default) and falls back
    to latin-1 (which never fails on bytes). Reports which encoding actually
    succeeded.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PlaintextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlaintextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PlaintextRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlaintextResponse | None:
    """Extract With Plaintext

     Read a plain-text file (or any text-like file: code, config, csv).

    Primitive: tries the requested encoding (or UTF-8 default) and falls back
    to latin-1 (which never fails on bytes). Reports which encoding actually
    succeeded.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PlaintextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlaintextResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PlaintextRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | PlaintextResponse]:
    """Extract With Plaintext

     Read a plain-text file (or any text-like file: code, config, csv).

    Primitive: tries the requested encoding (or UTF-8 default) and falls back
    to latin-1 (which never fails on bytes). Reports which encoding actually
    succeeded.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PlaintextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlaintextResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PlaintextRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | PlaintextResponse | None:
    """Extract With Plaintext

     Read a plain-text file (or any text-like file: code, config, csv).

    Primitive: tries the requested encoding (or UTF-8 default) and falls back
    to latin-1 (which never fails on bytes). Reports which encoding actually
    succeeded.

    Args:
        authorization (None | str | Unset): Bearer token
        body (PlaintextRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlaintextResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
