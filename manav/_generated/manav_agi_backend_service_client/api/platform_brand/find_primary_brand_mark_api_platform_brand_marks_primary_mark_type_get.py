from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.brand_mark_response import BrandMarkResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    mark_type: str,
    *,
    variant: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_variant: None | str | Unset
    if isinstance(variant, Unset):
        json_variant = UNSET
    else:
        json_variant = variant
    params["variant"] = json_variant

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/brand/marks/primary/{mark_type}".format(
            mark_type=quote(str(mark_type), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrandMarkResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BrandMarkResponse.from_dict(response.json())

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
) -> Response[BrandMarkResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    mark_type: str,
    *,
    client: AuthenticatedClient | Client,
    variant: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandMarkResponse | HTTPValidationError]:
    """Find Primary Brand Mark

     Find the designated primary mark of a type (and optional variant).

    Args:
        mark_type (str):
        variant (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandMarkResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        mark_type=mark_type,
        variant=variant,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    mark_type: str,
    *,
    client: AuthenticatedClient | Client,
    variant: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> BrandMarkResponse | HTTPValidationError | None:
    """Find Primary Brand Mark

     Find the designated primary mark of a type (and optional variant).

    Args:
        mark_type (str):
        variant (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandMarkResponse | HTTPValidationError
    """

    return sync_detailed(
        mark_type=mark_type,
        client=client,
        variant=variant,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    mark_type: str,
    *,
    client: AuthenticatedClient | Client,
    variant: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandMarkResponse | HTTPValidationError]:
    """Find Primary Brand Mark

     Find the designated primary mark of a type (and optional variant).

    Args:
        mark_type (str):
        variant (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandMarkResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        mark_type=mark_type,
        variant=variant,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    mark_type: str,
    *,
    client: AuthenticatedClient | Client,
    variant: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> BrandMarkResponse | HTTPValidationError | None:
    """Find Primary Brand Mark

     Find the designated primary mark of a type (and optional variant).

    Args:
        mark_type (str):
        variant (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandMarkResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            mark_type=mark_type,
            client=client,
            variant=variant,
            authorization=authorization,
        )
    ).parsed
