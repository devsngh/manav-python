from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.ui_visibility_rule_list_response import UIVisibilityRuleListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    element_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_element_id: None | str | Unset
    if isinstance(element_id, Unset):
        json_element_id = UNSET
    elif isinstance(element_id, UUID):
        json_element_id = str(element_id)
    else:
        json_element_id = element_id
    params["element_id"] = json_element_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/ui-visibility/rules",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UIVisibilityRuleListResponse | None:
    if response.status_code == 200:
        response_200 = UIVisibilityRuleListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UIVisibilityRuleListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    element_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UIVisibilityRuleListResponse]:
    """List Rules

     List all visibility rules, optionally filtered by element.

    Args:
        element_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UIVisibilityRuleListResponse]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    element_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UIVisibilityRuleListResponse | None:
    """List Rules

     List all visibility rules, optionally filtered by element.

    Args:
        element_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UIVisibilityRuleListResponse
    """

    return sync_detailed(
        client=client,
        element_id=element_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    element_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UIVisibilityRuleListResponse]:
    """List Rules

     List all visibility rules, optionally filtered by element.

    Args:
        element_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UIVisibilityRuleListResponse]
    """

    kwargs = _get_kwargs(
        element_id=element_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    element_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | UIVisibilityRuleListResponse | None:
    """List Rules

     List all visibility rules, optionally filtered by element.

    Args:
        element_id (None | Unset | UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UIVisibilityRuleListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            element_id=element_id,
            authorization=authorization,
        )
    ).parsed
