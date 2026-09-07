from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_register_request import BulkRegisterRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.ui_element_response import UIElementResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkRegisterRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ui-visibility/elements/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[UIElementResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UIElementResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[UIElementResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkRegisterRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UIElementResponse]]:
    """Bulk Register Elements

     Bulk register UI elements from frontend auto-registration.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UIElementResponse]]
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
    body: BulkRegisterRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UIElementResponse] | None:
    """Bulk Register Elements

     Bulk register UI elements from frontend auto-registration.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UIElementResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkRegisterRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UIElementResponse]]:
    """Bulk Register Elements

     Bulk register UI elements from frontend auto-registration.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UIElementResponse]]
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
    body: BulkRegisterRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UIElementResponse] | None:
    """Bulk Register Elements

     Bulk register UI elements from frontend auto-registration.

    Args:
        authorization (None | str | Unset): Bearer token
        body (BulkRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UIElementResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
