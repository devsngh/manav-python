from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cap_table_snapshot_response import CapTableSnapshotResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    legal_entity_id: UUID,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/ir/cap-table/legal-entity/{legal_entity_id}/latest".format(
            legal_entity_id=quote(str(legal_entity_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CapTableSnapshotResponse | None | HTTPValidationError | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> CapTableSnapshotResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CapTableSnapshotResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableSnapshotResponse | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[CapTableSnapshotResponse | None | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    legal_entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CapTableSnapshotResponse | None | HTTPValidationError]:
    """Get Latest Cap Table

     Most recent 'current' snapshot for the legal entity.

    Args:
        legal_entity_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CapTableSnapshotResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        legal_entity_id=legal_entity_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    legal_entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CapTableSnapshotResponse | None | HTTPValidationError | None:
    """Get Latest Cap Table

     Most recent 'current' snapshot for the legal entity.

    Args:
        legal_entity_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CapTableSnapshotResponse | None | HTTPValidationError
    """

    return sync_detailed(
        legal_entity_id=legal_entity_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    legal_entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[CapTableSnapshotResponse | None | HTTPValidationError]:
    """Get Latest Cap Table

     Most recent 'current' snapshot for the legal entity.

    Args:
        legal_entity_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CapTableSnapshotResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        legal_entity_id=legal_entity_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    legal_entity_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> CapTableSnapshotResponse | None | HTTPValidationError | None:
    """Get Latest Cap Table

     Most recent 'current' snapshot for the legal entity.

    Args:
        legal_entity_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CapTableSnapshotResponse | None | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            legal_entity_id=legal_entity_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
