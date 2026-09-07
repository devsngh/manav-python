from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.tool_detail_response import ToolDetailResponse
from ...models.tool_update import ToolUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tool_id: str,
    *,
    body: ToolUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/tools/{tool_id}".format(
            tool_id=quote(str(tool_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ToolDetailResponse | None:
    if response.status_code == 200:
        response_200 = ToolDetailResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | ToolDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ToolDetailResponse]:
    """Update Tool

     Update tool (own-scoped: your own only; admin: any).

    Args:
        tool_id (str):
        authorization (None | str | Unset): Bearer token
        body (ToolUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolDetailResponse]
    """

    kwargs = _get_kwargs(
        tool_id=tool_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ToolDetailResponse | None:
    """Update Tool

     Update tool (own-scoped: your own only; admin: any).

    Args:
        tool_id (str):
        authorization (None | str | Unset): Bearer token
        body (ToolUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolDetailResponse
    """

    return sync_detailed(
        tool_id=tool_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ToolDetailResponse]:
    """Update Tool

     Update tool (own-scoped: your own only; admin: any).

    Args:
        tool_id (str):
        authorization (None | str | Unset): Bearer token
        body (ToolUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ToolDetailResponse]
    """

    kwargs = _get_kwargs(
        tool_id=tool_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tool_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | ToolDetailResponse | None:
    """Update Tool

     Update tool (own-scoped: your own only; admin: any).

    Args:
        tool_id (str):
        authorization (None | str | Unset): Bearer token
        body (ToolUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ToolDetailResponse
    """

    return (
        await asyncio_detailed(
            tool_id=tool_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
