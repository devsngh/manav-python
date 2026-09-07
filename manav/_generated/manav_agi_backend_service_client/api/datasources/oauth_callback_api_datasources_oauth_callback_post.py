from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connection_response import ConnectionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.o_auth_callback_request import OAuthCallbackRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OAuthCallbackRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/datasources/oauth/callback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConnectionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = ConnectionResponse.from_dict(response.json())

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
) -> Response[ConnectionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OAuthCallbackRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ConnectionResponse | HTTPValidationError]:
    """Oauth Callback

     Handle OAuth callback and create connection

    Args:
        authorization (None | str | Unset): Bearer token
        body (OAuthCallbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionResponse | HTTPValidationError]
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
    body: OAuthCallbackRequest,
    authorization: None | str | Unset = UNSET,
) -> ConnectionResponse | HTTPValidationError | None:
    """Oauth Callback

     Handle OAuth callback and create connection

    Args:
        authorization (None | str | Unset): Bearer token
        body (OAuthCallbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OAuthCallbackRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ConnectionResponse | HTTPValidationError]:
    """Oauth Callback

     Handle OAuth callback and create connection

    Args:
        authorization (None | str | Unset): Bearer token
        body (OAuthCallbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionResponse | HTTPValidationError]
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
    body: OAuthCallbackRequest,
    authorization: None | str | Unset = UNSET,
) -> ConnectionResponse | HTTPValidationError | None:
    """Oauth Callback

     Handle OAuth callback and create connection

    Args:
        authorization (None | str | Unset): Bearer token
        body (OAuthCallbackRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
