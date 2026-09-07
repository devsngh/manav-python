from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.database_info import DatabaseInfo
from ...models.http_validation_error import HTTPValidationError
from ...models.select_databases_request import SelectDatabasesRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SelectDatabasesRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/db-controller/select-databases",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[DatabaseInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DatabaseInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[DatabaseInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SelectDatabasesRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[DatabaseInfo]]:
    """Select Databases

     Select databases (max 3) for a profile

    Args:
        authorization (None | str | Unset): Bearer token
        body (SelectDatabasesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[DatabaseInfo]]
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
    body: SelectDatabasesRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[DatabaseInfo] | None:
    """Select Databases

     Select databases (max 3) for a profile

    Args:
        authorization (None | str | Unset): Bearer token
        body (SelectDatabasesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[DatabaseInfo]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SelectDatabasesRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[DatabaseInfo]]:
    """Select Databases

     Select databases (max 3) for a profile

    Args:
        authorization (None | str | Unset): Bearer token
        body (SelectDatabasesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[DatabaseInfo]]
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
    body: SelectDatabasesRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[DatabaseInfo] | None:
    """Select Databases

     Select databases (max 3) for a profile

    Args:
        authorization (None | str | Unset): Bearer token
        body (SelectDatabasesRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[DatabaseInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
