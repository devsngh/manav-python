from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    doc_id: str,
    *,
    limit: int | Unset = 100,
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
        "url": "/api/retriever/documents/{doc_id}/chunks".format(
            doc_id=quote(str(doc_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """User Get Chunks

    Args:
        doc_id (str):
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        limit=limit,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """User Get Chunks

    Args:
        doc_id (str):
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        doc_id=doc_id,
        client=client,
        limit=limit,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """User Get Chunks

    Args:
        doc_id (str):
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        doc_id=doc_id,
        limit=limit,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    doc_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """User Get Chunks

    Args:
        doc_id (str):
        limit (int | Unset):  Default: 100.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            doc_id=doc_id,
            client=client,
            limit=limit,
            authorization=authorization,
        )
    ).parsed
