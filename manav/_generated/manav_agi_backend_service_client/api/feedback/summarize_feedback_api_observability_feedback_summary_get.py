from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feedback_summary import FeedbackSummary
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    org_id: UUID,
    window_days: int | Unset = 7,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id = str(org_id)
    params["org_id"] = json_org_id

    params["window_days"] = window_days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/feedback/summary",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FeedbackSummary | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FeedbackSummary.from_dict(response.json())

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
) -> Response[FeedbackSummary | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    window_days: int | Unset = 7,
    authorization: None | str | Unset = UNSET,
) -> Response[FeedbackSummary | HTTPValidationError]:
    """Summarize Feedback

     Aggregate over a window — counts by kind / target / apply_status /
    author_role + overall apply_success_rate.

    Args:
        org_id (UUID):
        window_days (int | Unset):  Default: 7.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedbackSummary | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        window_days=window_days,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    window_days: int | Unset = 7,
    authorization: None | str | Unset = UNSET,
) -> FeedbackSummary | HTTPValidationError | None:
    """Summarize Feedback

     Aggregate over a window — counts by kind / target / apply_status /
    author_role + overall apply_success_rate.

    Args:
        org_id (UUID):
        window_days (int | Unset):  Default: 7.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedbackSummary | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        org_id=org_id,
        window_days=window_days,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    window_days: int | Unset = 7,
    authorization: None | str | Unset = UNSET,
) -> Response[FeedbackSummary | HTTPValidationError]:
    """Summarize Feedback

     Aggregate over a window — counts by kind / target / apply_status /
    author_role + overall apply_success_rate.

    Args:
        org_id (UUID):
        window_days (int | Unset):  Default: 7.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedbackSummary | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        window_days=window_days,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    org_id: UUID,
    window_days: int | Unset = 7,
    authorization: None | str | Unset = UNSET,
) -> FeedbackSummary | HTTPValidationError | None:
    """Summarize Feedback

     Aggregate over a window — counts by kind / target / apply_status /
    author_role + overall apply_success_rate.

    Args:
        org_id (UUID):
        window_days (int | Unset):  Default: 7.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedbackSummary | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            org_id=org_id,
            window_days=window_days,
            authorization=authorization,
        )
    ).parsed
