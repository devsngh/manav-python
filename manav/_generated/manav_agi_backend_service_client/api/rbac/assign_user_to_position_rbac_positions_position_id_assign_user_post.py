from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.position_assign_request import PositionAssignRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    position_id: UUID,
    *,
    body: PositionAssignRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rbac/positions/{position_id}/assign-user".format(
            position_id=quote(str(position_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    position_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PositionAssignRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Assign User To Position

     Assign a user to this position

    Args:
        position_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PositionAssignRequest): Assign a user to a position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        position_id=position_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    position_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PositionAssignRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Assign User To Position

     Assign a user to this position

    Args:
        position_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PositionAssignRequest): Assign a user to a position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        position_id=position_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    position_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PositionAssignRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Assign User To Position

     Assign a user to this position

    Args:
        position_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PositionAssignRequest): Assign a user to a position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        position_id=position_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    position_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: PositionAssignRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Assign User To Position

     Assign a user to this position

    Args:
        position_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (PositionAssignRequest): Assign a user to a position

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            position_id=position_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
