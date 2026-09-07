from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_definition_response import ComponentDefinitionResponse
from ...models.component_type import ComponentType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    component_type: ComponentType | None | Unset = UNSET,
    include_inactive: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_component_type: None | str | Unset
    if isinstance(component_type, Unset):
        json_component_type = UNSET
    elif isinstance(component_type, ComponentType):
        json_component_type = component_type.value
    else:
        json_component_type = component_type
    params["component_type"] = json_component_type

    params["include_inactive"] = include_inactive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/prompts/components/definitions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ComponentDefinitionResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ComponentDefinitionResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[ComponentDefinitionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    component_type: ComponentType | None | Unset = UNSET,
    include_inactive: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ComponentDefinitionResponse]]:
    """List Component Definitions

     List all component definitions

    Args:
        component_type (ComponentType | None | Unset):
        include_inactive (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ComponentDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        component_type=component_type,
        include_inactive=include_inactive,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    component_type: ComponentType | None | Unset = UNSET,
    include_inactive: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ComponentDefinitionResponse] | None:
    """List Component Definitions

     List all component definitions

    Args:
        component_type (ComponentType | None | Unset):
        include_inactive (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ComponentDefinitionResponse]
    """

    return sync_detailed(
        client=client,
        component_type=component_type,
        include_inactive=include_inactive,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    component_type: ComponentType | None | Unset = UNSET,
    include_inactive: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[ComponentDefinitionResponse]]:
    """List Component Definitions

     List all component definitions

    Args:
        component_type (ComponentType | None | Unset):
        include_inactive (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ComponentDefinitionResponse]]
    """

    kwargs = _get_kwargs(
        component_type=component_type,
        include_inactive=include_inactive,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    component_type: ComponentType | None | Unset = UNSET,
    include_inactive: bool | Unset = False,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[ComponentDefinitionResponse] | None:
    """List Component Definitions

     List all component definitions

    Args:
        component_type (ComponentType | None | Unset):
        include_inactive (bool | Unset):  Default: False.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ComponentDefinitionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            component_type=component_type,
            include_inactive=include_inactive,
            authorization=authorization,
        )
    ).parsed
