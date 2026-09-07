from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.legal_entity_response import LegalEntityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    query: str,
    *,
    limit: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/legal-entities/search/{query}".format(
            query=quote(str(query), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[LegalEntityResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LegalEntityResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[LegalEntityResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    query: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[LegalEntityResponse]]:
    """Search Legal Entities

    Args:
        query (str):
        limit (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LegalEntityResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[LegalEntityResponse] | None:
    """Search Legal Entities

    Args:
        query (str):
        limit (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LegalEntityResponse]
    """

    return sync_detailed(
        query=query,
        client=client,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    query: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[LegalEntityResponse]]:
    """Search Legal Entities

    Args:
        query (str):
        limit (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LegalEntityResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | list[LegalEntityResponse] | None:
    """Search Legal Entities

    Args:
        query (str):
        limit (int | Unset):  Default: 20.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LegalEntityResponse]
    """

    return (
        await asyncio_detailed(
            query=query,
            client=client,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
