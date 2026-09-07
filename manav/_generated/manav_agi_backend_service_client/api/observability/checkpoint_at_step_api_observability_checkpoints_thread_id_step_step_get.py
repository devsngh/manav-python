from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.checkpoint_detail import CheckpointDetail
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thread_id: str,
    step: int,
    *,
    ns: str | Unset = "",
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    params["ns"] = ns

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/observability/checkpoints/{thread_id}/step/{step}".format(
            thread_id=quote(str(thread_id), safe=""),
            step=quote(str(step), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckpointDetail | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CheckpointDetail.from_dict(response.json())

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
) -> Response[CheckpointDetail | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    step: int,
    *,
    client: AuthenticatedClient | Client,
    ns: str | Unset = "",
    authorization: None | str | Unset = UNSET,
) -> Response[CheckpointDetail | HTTPValidationError]:
    """Checkpoint At Step

     Return the checkpoint at metadata.step == :step (latest wins if duped).

    Args:
        thread_id (str):
        step (int):
        ns (str | Unset): LangGraph checkpoint_ns; defaults to root Default: ''.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckpointDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        step=step,
        ns=ns,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    step: int,
    *,
    client: AuthenticatedClient | Client,
    ns: str | Unset = "",
    authorization: None | str | Unset = UNSET,
) -> CheckpointDetail | HTTPValidationError | None:
    """Checkpoint At Step

     Return the checkpoint at metadata.step == :step (latest wins if duped).

    Args:
        thread_id (str):
        step (int):
        ns (str | Unset): LangGraph checkpoint_ns; defaults to root Default: ''.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckpointDetail | HTTPValidationError
    """

    return sync_detailed(
        thread_id=thread_id,
        step=step,
        client=client,
        ns=ns,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    step: int,
    *,
    client: AuthenticatedClient | Client,
    ns: str | Unset = "",
    authorization: None | str | Unset = UNSET,
) -> Response[CheckpointDetail | HTTPValidationError]:
    """Checkpoint At Step

     Return the checkpoint at metadata.step == :step (latest wins if duped).

    Args:
        thread_id (str):
        step (int):
        ns (str | Unset): LangGraph checkpoint_ns; defaults to root Default: ''.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckpointDetail | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        step=step,
        ns=ns,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    step: int,
    *,
    client: AuthenticatedClient | Client,
    ns: str | Unset = "",
    authorization: None | str | Unset = UNSET,
) -> CheckpointDetail | HTTPValidationError | None:
    """Checkpoint At Step

     Return the checkpoint at metadata.step == :step (latest wins if duped).

    Args:
        thread_id (str):
        step (int):
        ns (str | Unset): LangGraph checkpoint_ns; defaults to root Default: ''.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckpointDetail | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            step=step,
            client=client,
            ns=ns,
            authorization=authorization,
        )
    ).parsed
