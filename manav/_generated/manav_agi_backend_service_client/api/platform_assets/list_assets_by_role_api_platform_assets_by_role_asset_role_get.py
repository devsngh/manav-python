from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_response import AssetResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_role: str,
    *,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/assets/by-role/{asset_role}".format(
            asset_role=quote(str(asset_role), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[AssetResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AssetResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[AssetResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_role: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[AssetResponse]]:
    """List Assets By Role

    Args:
        asset_role (str):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AssetResponse]]
    """

    kwargs = _get_kwargs(
        asset_role=asset_role,
        status=status,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_role: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[AssetResponse] | None:
    """List Assets By Role

    Args:
        asset_role (str):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AssetResponse]
    """

    return sync_detailed(
        asset_role=asset_role,
        client=client,
        status=status,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    asset_role: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[AssetResponse]]:
    """List Assets By Role

    Args:
        asset_role (str):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[AssetResponse]]
    """

    kwargs = _get_kwargs(
        asset_role=asset_role,
        status=status,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_role: str,
    *,
    client: AuthenticatedClient | Client,
    status: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[AssetResponse] | None:
    """List Assets By Role

    Args:
        asset_role (str):
        status (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[AssetResponse]
    """

    return (
        await asyncio_detailed(
            asset_role=asset_role,
            client=client,
            status=status,
            authorization=authorization,
        )
    ).parsed
