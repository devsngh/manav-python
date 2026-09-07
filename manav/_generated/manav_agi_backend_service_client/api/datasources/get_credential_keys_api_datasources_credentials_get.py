from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_keys_response import CredentialKeysResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    datasource_id: None | str | Unset = UNSET,
    datasource_name: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_datasource_id: None | str | Unset
    if isinstance(datasource_id, Unset):
        json_datasource_id = UNSET
    else:
        json_datasource_id = datasource_id
    params["datasource_id"] = json_datasource_id

    json_datasource_name: None | str | Unset
    if isinstance(datasource_name, Unset):
        json_datasource_name = UNSET
    else:
        json_datasource_name = datasource_name
    params["datasource_name"] = json_datasource_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasources/credentials",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CredentialKeysResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CredentialKeysResponse.from_dict(response.json())

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
) -> Response[CredentialKeysResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    datasource_id: None | str | Unset = UNSET,
    datasource_name: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[CredentialKeysResponse | HTTPValidationError]:
    """Get Credential Keys

     Get credential field definitions for a datasource
    Provide either datasource_id or datasource_name

    Args:
        datasource_id (None | str | Unset):
        datasource_name (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialKeysResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        datasource_name=datasource_name,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    datasource_id: None | str | Unset = UNSET,
    datasource_name: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> CredentialKeysResponse | HTTPValidationError | None:
    """Get Credential Keys

     Get credential field definitions for a datasource
    Provide either datasource_id or datasource_name

    Args:
        datasource_id (None | str | Unset):
        datasource_name (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialKeysResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        datasource_id=datasource_id,
        datasource_name=datasource_name,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    datasource_id: None | str | Unset = UNSET,
    datasource_name: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[CredentialKeysResponse | HTTPValidationError]:
    """Get Credential Keys

     Get credential field definitions for a datasource
    Provide either datasource_id or datasource_name

    Args:
        datasource_id (None | str | Unset):
        datasource_name (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialKeysResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        datasource_id=datasource_id,
        datasource_name=datasource_name,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    datasource_id: None | str | Unset = UNSET,
    datasource_name: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> CredentialKeysResponse | HTTPValidationError | None:
    """Get Credential Keys

     Get credential field definitions for a datasource
    Provide either datasource_id or datasource_name

    Args:
        datasource_id (None | str | Unset):
        datasource_name (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialKeysResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            datasource_id=datasource_id,
            datasource_name=datasource_name,
            authorization=authorization,
        )
    ).parsed
