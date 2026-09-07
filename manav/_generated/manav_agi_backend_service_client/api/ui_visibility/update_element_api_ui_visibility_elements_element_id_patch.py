from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ui_element_response import UIElementResponse
from ...models.ui_element_update import UIElementUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    element_id: UUID,
    *,
    body: UIElementUpdate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/ui-visibility/elements/{element_id}".format(
            element_id=quote(str(element_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UIElementResponse | None:
    if response.status_code == 200:
        response_200 = UIElementResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UIElementResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    element_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UIElementUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UIElementResponse]:
    """Update Element

     Update a UI element (label, category, active toggle).

    Args:
        element_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UIElementUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UIElementResponse]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    element_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UIElementUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UIElementResponse | None:
    """Update Element

     Update a UI element (label, category, active toggle).

    Args:
        element_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UIElementUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UIElementResponse
    """

    return sync_detailed(
        element_id=element_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    element_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UIElementUpdate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UIElementResponse]:
    """Update Element

     Update a UI element (label, category, active toggle).

    Args:
        element_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UIElementUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UIElementResponse]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    element_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UIElementUpdate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UIElementResponse | None:
    """Update Element

     Update a UI element (label, category, active toggle).

    Args:
        element_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UIElementUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UIElementResponse
    """

    return (
        await asyncio_detailed(
            element_id=element_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
