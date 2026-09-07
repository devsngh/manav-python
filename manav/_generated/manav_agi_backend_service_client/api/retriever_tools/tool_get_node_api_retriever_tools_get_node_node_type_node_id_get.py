from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_type: str,
    node_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/retriever/tools/get-node/{node_type}/{node_id}".format(
            node_type=quote(str(node_type), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
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
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Tool Get Node

     Look up a graph node by label + id.

    `node_type` MUST be a valid Neo4j identifier (alphanumeric + underscore).
    Invalid types are rejected with 400 — both to give callers (agents) a
    clean error message AND to prevent Cypher injection.

    Args:
        node_type (str):
        node_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        node_type=node_type,
        node_id=node_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Tool Get Node

     Look up a graph node by label + id.

    `node_type` MUST be a valid Neo4j identifier (alphanumeric + underscore).
    Invalid types are rejected with 400 — both to give callers (agents) a
    clean error message AND to prevent Cypher injection.

    Args:
        node_type (str):
        node_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        node_type=node_type,
        node_id=node_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Tool Get Node

     Look up a graph node by label + id.

    `node_type` MUST be a valid Neo4j identifier (alphanumeric + underscore).
    Invalid types are rejected with 400 — both to give callers (agents) a
    clean error message AND to prevent Cypher injection.

    Args:
        node_type (str):
        node_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        node_type=node_type,
        node_id=node_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Tool Get Node

     Look up a graph node by label + id.

    `node_type` MUST be a valid Neo4j identifier (alphanumeric + underscore).
    Invalid types are rejected with 400 — both to give callers (agents) a
    clean error message AND to prevent Cypher injection.

    Args:
        node_type (str):
        node_id (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            node_type=node_type,
            node_id=node_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
