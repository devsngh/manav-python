from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.message_response import MessageResponse
from ...models.user_signup import UserSignup
from ...types import Response


def _get_kwargs(
    *,
    body: UserSignup,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/signup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MessageResponse | None:
    if response.status_code == 201:
        response_201 = MessageResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | MessageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserSignup,
) -> Response[HTTPValidationError | MessageResponse]:
    """Signup

     Register new user with email and password.
    Default role: USER

    The frontend signup compliance gate is expected to send
    `legal_consents` (Terms + Privacy at minimum) and `marketing_opt_in`
    in the request body. We record those alongside the new user — one
    row per accepted document, plus a marketing opt-in/out row.

    Model B auto-assigns the user's plan-default agent pack at signup so
    the inbox shows a real assigned default immediately (no fallback path).

    Args:
        body (UserSignup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MessageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UserSignup,
) -> HTTPValidationError | MessageResponse | None:
    """Signup

     Register new user with email and password.
    Default role: USER

    The frontend signup compliance gate is expected to send
    `legal_consents` (Terms + Privacy at minimum) and `marketing_opt_in`
    in the request body. We record those alongside the new user — one
    row per accepted document, plus a marketing opt-in/out row.

    Model B auto-assigns the user's plan-default agent pack at signup so
    the inbox shows a real assigned default immediately (no fallback path).

    Args:
        body (UserSignup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MessageResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserSignup,
) -> Response[HTTPValidationError | MessageResponse]:
    """Signup

     Register new user with email and password.
    Default role: USER

    The frontend signup compliance gate is expected to send
    `legal_consents` (Terms + Privacy at minimum) and `marketing_opt_in`
    in the request body. We record those alongside the new user — one
    row per accepted document, plus a marketing opt-in/out row.

    Model B auto-assigns the user's plan-default agent pack at signup so
    the inbox shows a real assigned default immediately (no fallback path).

    Args:
        body (UserSignup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MessageResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserSignup,
) -> HTTPValidationError | MessageResponse | None:
    """Signup

     Register new user with email and password.
    Default role: USER

    The frontend signup compliance gate is expected to send
    `legal_consents` (Terms + Privacy at minimum) and `marketing_opt_in`
    in the request body. We record those alongside the new user — one
    row per accepted document, plus a marketing opt-in/out row.

    Model B auto-assigns the user's plan-default agent pack at signup so
    the inbox shows a real assigned default immediately (no fallback path).

    Args:
        body (UserSignup):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MessageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
