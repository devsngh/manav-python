from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.training_progress_summary import TrainingProgressSummary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trainee_bot_id: UUID,
    *,
    org_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/training/rounds/progress/{trainee_bot_id}".format(
            trainee_bot_id=quote(str(trainee_bot_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TrainingProgressSummary | None:
    if response.status_code == 200:
        response_200 = TrainingProgressSummary.from_dict(response.json())

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
) -> Response[HTTPValidationError | TrainingProgressSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trainee_bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TrainingProgressSummary]:
    """Summarize Training Progress

     Manav / Cyra reads this to track a trainee's threshold status.

    Args:
        trainee_bot_id (UUID):
        org_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TrainingProgressSummary]
    """

    kwargs = _get_kwargs(
        trainee_bot_id=trainee_bot_id,
        org_id=org_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trainee_bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TrainingProgressSummary | None:
    """Summarize Training Progress

     Manav / Cyra reads this to track a trainee's threshold status.

    Args:
        trainee_bot_id (UUID):
        org_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TrainingProgressSummary
    """

    return sync_detailed(
        trainee_bot_id=trainee_bot_id,
        client=client,
        org_id=org_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    trainee_bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | TrainingProgressSummary]:
    """Summarize Training Progress

     Manav / Cyra reads this to track a trainee's threshold status.

    Args:
        trainee_bot_id (UUID):
        org_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TrainingProgressSummary]
    """

    kwargs = _get_kwargs(
        trainee_bot_id=trainee_bot_id,
        org_id=org_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trainee_bot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | TrainingProgressSummary | None:
    """Summarize Training Progress

     Manav / Cyra reads this to track a trainee's threshold status.

    Args:
        trainee_bot_id (UUID):
        org_id (UUID):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TrainingProgressSummary
    """

    return (
        await asyncio_detailed(
            trainee_bot_id=trainee_bot_id,
            client=client,
            org_id=org_id,
            authorization=authorization,
        )
    ).parsed
