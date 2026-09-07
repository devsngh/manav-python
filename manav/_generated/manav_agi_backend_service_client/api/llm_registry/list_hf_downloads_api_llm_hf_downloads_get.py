from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_status import DownloadStatus
from ...models.hf_download_list_response import HFDownloadListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    status_filter: DownloadStatus | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_status_filter: None | str | Unset
    if isinstance(status_filter, Unset):
        json_status_filter = UNSET
    elif isinstance(status_filter, DownloadStatus):
        json_status_filter = status_filter.value
    else:
        json_status_filter = status_filter
    params["status_filter"] = json_status_filter

    json_is_registered: bool | None | Unset
    if isinstance(is_registered, Unset):
        json_is_registered = UNSET
    else:
        json_is_registered = is_registered
    params["is_registered"] = json_is_registered

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/llm/hf/downloads",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HFDownloadListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = HFDownloadListResponse.from_dict(response.json())

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
) -> Response[HFDownloadListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    status_filter: DownloadStatus | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HFDownloadListResponse | HTTPValidationError]:
    """List Hf Downloads

     List HuggingFace downloads

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status_filter (DownloadStatus | None | Unset):
        is_registered (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HFDownloadListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        status_filter=status_filter,
        is_registered=is_registered,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    status_filter: DownloadStatus | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HFDownloadListResponse | HTTPValidationError | None:
    """List Hf Downloads

     List HuggingFace downloads

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status_filter (DownloadStatus | None | Unset):
        is_registered (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HFDownloadListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
        status_filter=status_filter,
        is_registered=is_registered,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    status_filter: DownloadStatus | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[HFDownloadListResponse | HTTPValidationError]:
    """List Hf Downloads

     List HuggingFace downloads

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status_filter (DownloadStatus | None | Unset):
        is_registered (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HFDownloadListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
        status_filter=status_filter,
        is_registered=is_registered,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
    status_filter: DownloadStatus | None | Unset = UNSET,
    is_registered: bool | None | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> HFDownloadListResponse | HTTPValidationError | None:
    """List Hf Downloads

     List HuggingFace downloads

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.
        status_filter (DownloadStatus | None | Unset):
        is_registered (bool | None | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HFDownloadListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
            status_filter=status_filter,
            is_registered=is_registered,
            authorization=authorization,
        )
    ).parsed
