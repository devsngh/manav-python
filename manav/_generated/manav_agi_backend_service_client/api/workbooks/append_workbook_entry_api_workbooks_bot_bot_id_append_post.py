from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.workbook_append_body import WorkbookAppendBody
from ...models.workbook_response import WorkbookResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_id: UUID,
    *,
    body: WorkbookAppendBody,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/workbooks/bot/{bot_id}/append".format(
            bot_id=quote(str(bot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    body: WorkbookAppendBody,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookResponse]:
    """Append Workbook Entry

     Append a dated entry to the bot's workbook (creates the workbook on
        first-ever append). Pratyaksha, Sangrahaka, Vishvakarma etc. call this
        at end-of-session to log the day's findings / curations / commits.

        Each call appends an `## <date> — <title>
    <entry>` block to the
        workbook's content field. Calling N times adds N entries; nothing is
        overwritten.

    Args:
        bot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (WorkbookAppendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
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
    body: WorkbookAppendBody,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookResponse | None:
    """Append Workbook Entry

     Append a dated entry to the bot's workbook (creates the workbook on
        first-ever append). Pratyaksha, Sangrahaka, Vishvakarma etc. call this
        at end-of-session to log the day's findings / curations / commits.

        Each call appends an `## <date> — <title>
    <entry>` block to the
        workbook's content field. Calling N times adds N entries; nothing is
        overwritten.

    Args:
        bot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (WorkbookAppendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WorkbookResponse
    """

    return sync_detailed(
        bot_id=bot_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: WorkbookAppendBody,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | WorkbookResponse]:
    """Append Workbook Entry

     Append a dated entry to the bot's workbook (creates the workbook on
        first-ever append). Pratyaksha, Sangrahaka, Vishvakarma etc. call this
        at end-of-session to log the day's findings / curations / commits.

        Each call appends an `## <date> — <title>
    <entry>` block to the
        workbook's content field. Calling N times adds N entries; nothing is
        overwritten.

    Args:
        bot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (WorkbookAppendBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WorkbookResponse]
    """

    kwargs = _get_kwargs(
        bot_id=bot_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: WorkbookAppendBody,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | WorkbookResponse | None:
    """Append Workbook Entry

     Append a dated entry to the bot's workbook (creates the workbook on
        first-ever append). Pratyaksha, Sangrahaka, Vishvakarma etc. call this
        at end-of-session to log the day's findings / curations / commits.

        Each call appends an `## <date> — <title>
    <entry>` block to the
        workbook's content field. Calling N times adds N entries; nothing is
        overwritten.

    Args:
        bot_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (WorkbookAppendBody):

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
            body=body,
            authorization=authorization,
        )
    ).parsed
