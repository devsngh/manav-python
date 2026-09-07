from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ast_request import AstRequest
from ...models.ast_response import AstResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AstRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/extract/ast",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AstResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AstResponse.from_dict(response.json())

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
) -> Response[AstResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AstRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AstResponse | HTTPValidationError]:
    """Extract With Ast

     Parse a code file with Python's `ast` module — function/class boundaries.

    Primitive: V1 supports Python only. Returns each top-level function +
    class as a structured unit with source slice + line range + docstring.
    Agent uses these as natural chunk boundaries instead of paragraph splits.

    For other languages, the agent should call sandbox_execute_python with
    tree-sitter or language-specific parsers. Future versions may add
    tree-sitter wrappers as separate primitives (extract_with_tree_sitter_js etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (AstRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AstResponse | HTTPValidationError]
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
    body: AstRequest,
    authorization: None | str | Unset = UNSET,
) -> AstResponse | HTTPValidationError | None:
    """Extract With Ast

     Parse a code file with Python's `ast` module — function/class boundaries.

    Primitive: V1 supports Python only. Returns each top-level function +
    class as a structured unit with source slice + line range + docstring.
    Agent uses these as natural chunk boundaries instead of paragraph splits.

    For other languages, the agent should call sandbox_execute_python with
    tree-sitter or language-specific parsers. Future versions may add
    tree-sitter wrappers as separate primitives (extract_with_tree_sitter_js etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (AstRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AstResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AstRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AstResponse | HTTPValidationError]:
    """Extract With Ast

     Parse a code file with Python's `ast` module — function/class boundaries.

    Primitive: V1 supports Python only. Returns each top-level function +
    class as a structured unit with source slice + line range + docstring.
    Agent uses these as natural chunk boundaries instead of paragraph splits.

    For other languages, the agent should call sandbox_execute_python with
    tree-sitter or language-specific parsers. Future versions may add
    tree-sitter wrappers as separate primitives (extract_with_tree_sitter_js etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (AstRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AstResponse | HTTPValidationError]
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
    body: AstRequest,
    authorization: None | str | Unset = UNSET,
) -> AstResponse | HTTPValidationError | None:
    """Extract With Ast

     Parse a code file with Python's `ast` module — function/class boundaries.

    Primitive: V1 supports Python only. Returns each top-level function +
    class as a structured unit with source slice + line range + docstring.
    Agent uses these as natural chunk boundaries instead of paragraph splits.

    For other languages, the agent should call sandbox_execute_python with
    tree-sitter or language-specific parsers. Future versions may add
    tree-sitter wrappers as separate primitives (extract_with_tree_sitter_js etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (AstRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AstResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
