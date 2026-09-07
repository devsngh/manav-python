from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_message_read import ExternalMessageRead
from ...models.http_validation_error import HTTPValidationError
from ...models.sms_send_request import SmsSendRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SmsSendRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/comms/sms/send",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExternalMessageRead | HTTPValidationError | None:
    if response.status_code == 202:
        response_202 = ExternalMessageRead.from_dict(response.json())

        return response_202

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExternalMessageRead | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SmsSendRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ExternalMessageRead | HTTPValidationError]:
    """Send Sms

     Send an outbound SMS through the org's active SMS datasource (Twilio etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (SmsSendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalMessageRead | HTTPValidationError]
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
    body: SmsSendRequest,
    authorization: None | str | Unset = UNSET,
) -> ExternalMessageRead | HTTPValidationError | None:
    """Send Sms

     Send an outbound SMS through the org's active SMS datasource (Twilio etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (SmsSendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalMessageRead | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SmsSendRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[ExternalMessageRead | HTTPValidationError]:
    """Send Sms

     Send an outbound SMS through the org's active SMS datasource (Twilio etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (SmsSendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalMessageRead | HTTPValidationError]
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
    body: SmsSendRequest,
    authorization: None | str | Unset = UNSET,
) -> ExternalMessageRead | HTTPValidationError | None:
    """Send Sms

     Send an outbound SMS through the org's active SMS datasource (Twilio etc.).

    Args:
        authorization (None | str | Unset): Bearer token
        body (SmsSendRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalMessageRead | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
