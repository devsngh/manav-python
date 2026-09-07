from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_description_response import AssetDescriptionResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.update_continuity_scores_request import UpdateContinuityScoresRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: UUID,
    *,
    body: UpdateContinuityScoresRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/assets/{asset_id}/description/scores".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetDescriptionResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AssetDescriptionResponse.from_dict(response.json())

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
) -> Response[AssetDescriptionResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateContinuityScoresRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetDescriptionResponse | HTTPValidationError]:
    """Update Continuity Scores

    Args:
        asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UpdateContinuityScoresRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDescriptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateContinuityScoresRequest,
    authorization: None | str | Unset = UNSET,
) -> AssetDescriptionResponse | HTTPValidationError | None:
    """Update Continuity Scores

    Args:
        asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UpdateContinuityScoresRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetDescriptionResponse | HTTPValidationError
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateContinuityScoresRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetDescriptionResponse | HTTPValidationError]:
    """Update Continuity Scores

    Args:
        asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UpdateContinuityScoresRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDescriptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateContinuityScoresRequest,
    authorization: None | str | Unset = UNSET,
) -> AssetDescriptionResponse | HTTPValidationError | None:
    """Update Continuity Scores

    Args:
        asset_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (UpdateContinuityScoresRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetDescriptionResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
