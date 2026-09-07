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
    direction: str | Unset = "outgoing",
    depth: int | Unset = 1,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["direction"] = direction

    params["depth"] = depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/retriever/tools/get-neighbors/{node_type}/{node_id}".format(
            node_type=quote(str(node_type), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
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
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    direction: str | Unset = "outgoing",
    depth: int | Unset = 1,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Tool Get Neighbors

     Graph traversal — same validation rules as get-node.

    Args:
        node_type (str):
        node_id (str):
        direction (str | Unset):  Default: 'outgoing'.
        depth (int | Unset):  Default: 1.
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
        direction=direction,
        depth=depth,
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
    direction: str | Unset = "outgoing",
    depth: int | Unset = 1,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Tool Get Neighbors

     Graph traversal — same validation rules as get-node.

    Args:
        node_type (str):
        node_id (str):
        direction (str | Unset):  Default: 'outgoing'.
        depth (int | Unset):  Default: 1.
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
        direction=direction,
        depth=depth,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    direction: str | Unset = "outgoing",
    depth: int | Unset = 1,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Tool Get Neighbors

     Graph traversal — same validation rules as get-node.

    Args:
        node_type (str):
        node_id (str):
        direction (str | Unset):  Default: 'outgoing'.
        depth (int | Unset):  Default: 1.
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
        direction=direction,
        depth=depth,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_type: str,
    node_id: str,
    *,
    client: AuthenticatedClient | Client,
    direction: str | Unset = "outgoing",
    depth: int | Unset = 1,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Tool Get Neighbors

     Graph traversal — same validation rules as get-node.

    Args:
        node_type (str):
        node_id (str):
        direction (str | Unset):  Default: 'outgoing'.
        depth (int | Unset):  Default: 1.
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
            direction=direction,
            depth=depth,
            authorization=authorization,
        )
    ).parsed
