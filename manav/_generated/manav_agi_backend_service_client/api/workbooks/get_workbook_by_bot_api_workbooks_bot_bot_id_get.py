from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.workbook_response import WorkbookResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    workbook_type: str | Unset = "personal",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["workbook_type"] = workbook_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/workbooks/bot/{bot_id}".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WorkbookResponse | None:
    if response.status_code == 200:
        response_200 = WorkbookResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WorkbookResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workbook_type: str | Unset = "personal",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookResponse]:
    """Get Workbook By Bot

    Args:
        bot_id (UUID):
        workbook_type (str | Unset):  Default: 'personal'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        workbook_type=workbook_type,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workbook_type: str | Unset = "personal",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookResponse | None:
    """Get Workbook By Bot

    Args:
        bot_id (UUID):
        workbook_type (str | Unset):  Default: 'personal'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkbookResponse
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        workbook_type=workbook_type,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workbook_type: str | Unset = "personal",
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookResponse]:
    """Get Workbook By Bot

    Args:
        bot_id (UUID):
        workbook_type (str | Unset):  Default: 'personal'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        workbook_type=workbook_type,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    workbook_type: str | Unset = "personal",
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookResponse | None:
    """Get Workbook By Bot

    Args:
        bot_id (UUID):
        workbook_type (str | Unset):  Default: 'personal'.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkbookResponse
    """

    return (
        await asyncio_detailed(
            bot_id=bot_id,
            client=client,
            workbook_type=workbook_type,
            authorization=authorization,
        )
    ).parsed
