from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_description_response import AssetDescriptionResponse
from ...models.asset_description_upsert import AssetDescriptionUpsert
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: UUID,
    *,
    body: AssetDescriptionUpsert,
    generated_by: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_generated_by: None | str | Unset
    if isinstance(generated_by, Unset):
        json_generated_by = UNSET
    else:
        json_generated_by = generated_by
    params["generated_by"] = json_generated_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/platform/assets/{asset_id}/description".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
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
    body: AssetDescriptionUpsert,
    generated_by: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetDescriptionResponse | HTTPValidationError]:
    """Upsert Asset Description

     Insert or update the single description row for an asset (vision captioning output).

    Args:
        asset_id (UUID):
        generated_by (None | str | Unset): Model identifier (e.g. 'gpt-4o-vision')
        authorization (None | str | Unset): Bearer token
        body (AssetDescriptionUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDescriptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        generated_by=generated_by,
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
    body: AssetDescriptionUpsert,
    generated_by: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> AssetDescriptionResponse | HTTPValidationError | None:
    """Upsert Asset Description

     Insert or update the single description row for an asset (vision captioning output).

    Args:
        asset_id (UUID):
        generated_by (None | str | Unset): Model identifier (e.g. 'gpt-4o-vision')
        authorization (None | str | Unset): Bearer token
        body (AssetDescriptionUpsert):

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
        generated_by=generated_by,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetDescriptionUpsert,
    generated_by: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[AssetDescriptionResponse | HTTPValidationError]:
    """Upsert Asset Description

     Insert or update the single description row for an asset (vision captioning output).

    Args:
        asset_id (UUID):
        generated_by (None | str | Unset): Model identifier (e.g. 'gpt-4o-vision')
        authorization (None | str | Unset): Bearer token
        body (AssetDescriptionUpsert):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetDescriptionResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        generated_by=generated_by,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: AssetDescriptionUpsert,
    generated_by: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> AssetDescriptionResponse | HTTPValidationError | None:
    """Upsert Asset Description

     Insert or update the single description row for an asset (vision captioning output).

    Args:
        asset_id (UUID):
        generated_by (None | str | Unset): Model identifier (e.g. 'gpt-4o-vision')
        authorization (None | str | Unset): Bearer token
        body (AssetDescriptionUpsert):

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
            generated_by=generated_by,
            authorization=authorization,
        )
    ).parsed
