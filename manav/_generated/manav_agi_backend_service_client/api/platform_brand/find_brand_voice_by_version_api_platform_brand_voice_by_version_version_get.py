from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.brand_voice_guidelines_response import BrandVoiceGuidelinesResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/brand/voice/by-version/{version}".format(
            version=quote(str(version), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BrandVoiceGuidelinesResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = BrandVoiceGuidelinesResponse.from_dict(response.json())

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
) -> Response[BrandVoiceGuidelinesResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandVoiceGuidelinesResponse | HTTPValidationError]:
    """Find Brand Voice By Version

    Args:
        version (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandVoiceGuidelinesResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        version=version,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> BrandVoiceGuidelinesResponse | HTTPValidationError | None:
    """Find Brand Voice By Version

    Args:
        version (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandVoiceGuidelinesResponse | HTTPValidationError
    """

    return sync_detailed(
        version=version,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    version: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[BrandVoiceGuidelinesResponse | HTTPValidationError]:
    """Find Brand Voice By Version

    Args:
        version (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BrandVoiceGuidelinesResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        version=version,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> BrandVoiceGuidelinesResponse | HTTPValidationError | None:
    """Find Brand Voice By Version

    Args:
        version (str):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BrandVoiceGuidelinesResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            version=version,
            client=client,
            authorization=authorization,
        )
    ).parsed
