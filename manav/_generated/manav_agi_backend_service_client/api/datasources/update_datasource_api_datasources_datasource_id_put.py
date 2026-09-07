from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_update_datasource_api_datasources_datasource_id_put import (
    BodyUpdateDatasourceApiDatasourcesDatasourceIdPut,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    datasource_id: str,
    *,
    body: BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/datasources/{datasource_id}".format(
            datasource_id=quote(str(datasource_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> HTTPValidationError | None:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[HTTPValidationError]:
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
    body: BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """Update Datasource

     Update datasource (own-scoped: your own only; admin: any).

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
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
    body: BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """Update Datasource

     Update datasource (own-scoped: your own only; admin: any).

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
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
    body: BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError]:
    """Update Datasource

     Update datasource (own-scoped: your own only; admin: any).

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
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
    body: BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | None:
    """Update Datasource

     Update datasource (own-scoped: your own only; admin: any).

    Args:
        datasource_id (str):
        authorization (None | str | Unset): Bearer token
        body (BodyUpdateDatasourceApiDatasourcesDatasourceIdPut | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            datasource_id=datasource_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
