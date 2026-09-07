from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect_request import ConnectRequest
from ...models.connection_response import ConnectionResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    datasource_id: str,
    *,
    body: ConnectRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/datasources/{datasource_id}/connect".format(
            datasource_id=quote(str(datasource_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectionResponse | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = ConnectionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ConnectionResponse | HTTPValidationError]:
    """Connect To Datasource

     Connect user to datasource with credentials + optional per-channel config.

    For platform-scope datasources the service branches into
    DatasourceConfigParameter storage and requires super_admin — we pass
    the flag through so the service can enforce it.

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (ConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequest,
    authorization: None | str | Unset = UNSET,
) -> ConnectionResponse | HTTPValidationError | None:
    """Connect To Datasource

     Connect user to datasource with credentials + optional per-channel config.

    For platform-scope datasources the service branches into
    DatasourceConfigParameter storage and requires super_admin — we pass
    the flag through so the service can enforce it.

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (ConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionResponse | HTTPValidationError
    """

    return sync_detailed(
        datasource_id=datasource_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ConnectionResponse | HTTPValidationError]:
    """Connect To Datasource

     Connect user to datasource with credentials + optional per-channel config.

    For platform-scope datasources the service branches into
    DatasourceConfigParameter storage and requires super_admin — we pass
    the flag through so the service can enforce it.

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (ConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datasource_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConnectRequest,
    authorization: None | str | Unset = UNSET,
) -> ConnectionResponse | HTTPValidationError | None:
    """Connect To Datasource

     Connect user to datasource with credentials + optional per-channel config.

    For platform-scope datasources the service branches into
    DatasourceConfigParameter storage and requires super_admin — we pass
    the flag through so the service can enforce it.

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (ConnectRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            datasource_id=datasource_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
