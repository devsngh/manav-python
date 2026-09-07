from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/session/hil-events/{event_id}/resume".format(
            event_id=quote(str(event_id), safe=""),
        ),
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
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Resume Hil Event

     After a user resolves a HIL event, build a resume payload.
    The frontend uses this payload to call the orchestrator's /run/resume endpoint,
    or a future iteration can proxy the call directly.

    DB note: hil_events lives in observability_db, NOT core_db. Using
    get_operations_db here (not get_db) so the SELECT for the event
    targets the right database.

    Args:
        event_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Resume Hil Event

     After a user resolves a HIL event, build a resume payload.
    The frontend uses this payload to call the orchestrator's /run/resume endpoint,
    or a future iteration can proxy the call directly.

    DB note: hil_events lives in observability_db, NOT core_db. Using
    get_operations_db here (not get_db) so the SELECT for the event
    targets the right database.

    Args:
        event_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Resume Hil Event

     After a user resolves a HIL event, build a resume payload.
    The frontend uses this payload to call the orchestrator's /run/resume endpoint,
    or a future iteration can proxy the call directly.

    DB note: hil_events lives in observability_db, NOT core_db. Using
    get_operations_db here (not get_db) so the SELECT for the event
    targets the right database.

    Args:
        event_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Resume Hil Event

     After a user resolves a HIL event, build a resume payload.
    The frontend uses this payload to call the orchestrator's /run/resume endpoint,
    or a future iteration can proxy the call directly.

    DB note: hil_events lives in observability_db, NOT core_db. Using
    get_operations_db here (not get_db) so the SELECT for the event
    targets the right database.

    Args:
        event_id (str):
        authorization (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            authorization=authorization,
        )
    ).parsed
