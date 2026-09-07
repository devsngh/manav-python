from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.workbook_list_response import WorkbookListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bot_id: None | Unset | UUID = UNSET,
    workbook_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    elif isinstance(bot_id, UUID):
        json_bot_id = str(bot_id)
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_workbook_type: None | str | Unset
    if isinstance(workbook_type, Unset):
        json_workbook_type = UNSET
    else:
        json_workbook_type = workbook_type
    params["workbook_type"] = json_workbook_type

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/workbooks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WorkbookListResponse | None:
    if response.status_code == 200:
        response_200 = WorkbookListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WorkbookListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | Unset | UUID = UNSET,
    workbook_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookListResponse]:
    """List Workbooks

    Args:
        bot_id (None | Unset | UUID):
        workbook_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookListResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        workbook_type=workbook_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | Unset | UUID = UNSET,
    workbook_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookListResponse | None:
    """List Workbooks

    Args:
        bot_id (None | Unset | UUID):
        workbook_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkbookListResponse
    """

    return sync_detailed(
        client=client,
        bot_id=bot_id,
        workbook_type=workbook_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | Unset | UUID = UNSET,
    workbook_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookListResponse]:
    """List Workbooks

    Args:
        bot_id (None | Unset | UUID):
        workbook_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookListResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        workbook_type=workbook_type,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    bot_id: None | Unset | UUID = UNSET,
    workbook_type: None | str | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookListResponse | None:
    """List Workbooks

    Args:
        bot_id (None | Unset | UUID):
        workbook_type (None | str | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkbookListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            bot_id=bot_id,
            workbook_type=workbook_type,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
