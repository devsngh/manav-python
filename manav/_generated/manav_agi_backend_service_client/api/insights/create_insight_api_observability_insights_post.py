from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.synthesis_insight_create import SynthesisInsightCreate
from ...models.synthesis_insight_response import SynthesisInsightResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SynthesisInsightCreate,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/observability/insights",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SynthesisInsightResponse | None:
    if response.status_code == 201:
        response_201 = SynthesisInsightResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    """Create Insight

     Anveshana files a new meta-synthesis insight.

    Args:
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SynthesisInsightResponse]
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
    body: SynthesisInsightCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SynthesisInsightResponse | None:
    """Create Insight

     Anveshana files a new meta-synthesis insight.

    Args:
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SynthesisInsightResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SynthesisInsightCreate,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | SynthesisInsightResponse]:
    """Create Insight

     Anveshana files a new meta-synthesis insight.

    Args:
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SynthesisInsightResponse]
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
    body: SynthesisInsightCreate,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | SynthesisInsightResponse | None:
    """Create Insight

     Anveshana files a new meta-synthesis insight.

    Args:
        authorization (None | str | Unset): Bearer token
        body (SynthesisInsightCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SynthesisInsightResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
