from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.table_schema_response import TableSchemaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    profile_id: str,
    database_name: str,
    table_name: str,
    *,
    schema: str | Unset = "public",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["schema"] = schema

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/db-controller/profiles/{profile_id}/databases/{database_name}/tables/{table_name}/schema".format(
            profile_id=quote(str(profile_id), safe=""),
            database_name=quote(str(database_name), safe=""),
            table_name=quote(str(table_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TableSchemaResponse | None:
    if response.status_code == 200:
        response_200 = TableSchemaResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TableSchemaResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    profile_id: str,
    database_name: str,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    schema: str | Unset = "public",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TableSchemaResponse]:
    """Get Table Schema

     Get detailed table schema

    Args:
        profile_id (str):
        database_name (str):
        table_name (str):
        schema (str | Unset): Schema name for PostgreSQL Default: 'public'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TableSchemaResponse]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
        database_name=database_name,
        table_name=table_name,
        schema=schema,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    profile_id: str,
    database_name: str,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    schema: str | Unset = "public",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TableSchemaResponse | None:
    """Get Table Schema

     Get detailed table schema

    Args:
        profile_id (str):
        database_name (str):
        table_name (str):
        schema (str | Unset): Schema name for PostgreSQL Default: 'public'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TableSchemaResponse
    """

    return sync_detailed(
        profile_id=profile_id,
        database_name=database_name,
        table_name=table_name,
        client=client,
        schema=schema,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    profile_id: str,
    database_name: str,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    schema: str | Unset = "public",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TableSchemaResponse]:
    """Get Table Schema

     Get detailed table schema

    Args:
        profile_id (str):
        database_name (str):
        table_name (str):
        schema (str | Unset): Schema name for PostgreSQL Default: 'public'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TableSchemaResponse]
    """

    kwargs = _get_kwargs(
        profile_id=profile_id,
        database_name=database_name,
        table_name=table_name,
        schema=schema,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    profile_id: str,
    database_name: str,
    table_name: str,
    *,
    client: AuthenticatedClient | Client,
    schema: str | Unset = "public",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TableSchemaResponse | None:
    """Get Table Schema

     Get detailed table schema

    Args:
        profile_id (str):
        database_name (str):
        table_name (str):
        schema (str | Unset): Schema name for PostgreSQL Default: 'public'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TableSchemaResponse
    """

    return (
        await asyncio_detailed(
            profile_id=profile_id,
            database_name=database_name,
            table_name=table_name,
            client=client,
            schema=schema,
            authorization=authorization,
        )
    ).parsed
