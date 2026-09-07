from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.master_switch_request import MasterSwitchRequest
from ...models.master_switch_response import MasterSwitchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MasterSwitchRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/admin/society/master-switch",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MasterSwitchResponse | None:
    if response.status_code == 200:
        response_200 = MasterSwitchResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | MasterSwitchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MasterSwitchRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MasterSwitchResponse]:
    """Post Master Switch

     Flip the platform-wide master switch. Logs the flipping user.

    Args:
        authorization (None | str | Unset): Bearer token
        body (MasterSwitchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MasterSwitchResponse]
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
    body: MasterSwitchRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MasterSwitchResponse | None:
    """Post Master Switch

     Flip the platform-wide master switch. Logs the flipping user.

    Args:
        authorization (None | str | Unset): Bearer token
        body (MasterSwitchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MasterSwitchResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MasterSwitchRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | MasterSwitchResponse]:
    """Post Master Switch

     Flip the platform-wide master switch. Logs the flipping user.

    Args:
        authorization (None | str | Unset): Bearer token
        body (MasterSwitchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MasterSwitchResponse]
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
    body: MasterSwitchRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | MasterSwitchResponse | None:
    """Post Master Switch

     Flip the platform-wide master switch. Logs the flipping user.

    Args:
        authorization (None | str | Unset): Bearer token
        body (MasterSwitchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MasterSwitchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
