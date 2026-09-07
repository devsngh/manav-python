from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clone_and_run_request import CloneAndRunRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CloneAndRunRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/tasks/clone-and-run",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = response.json()
        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: CloneAndRunRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Clone And Run

     Option B self-cloning: the caller (an agent's bot-user) fans out N parallel clones
    of itself, each running one slice; a MONITORING parent auto-merges the results
    (concatenate/vote in-backend; summarize wakes the parent to synthesize).

    Args:
        authorization (None | str | Unset): Bearer token
        body (CloneAndRunRequest): Spawn N parallel clones of the calling bot (one per slice),
            auto-merge results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CloneAndRunRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Clone And Run

     Option B self-cloning: the caller (an agent's bot-user) fans out N parallel clones
    of itself, each running one slice; a MONITORING parent auto-merges the results
    (concatenate/vote in-backend; summarize wakes the parent to synthesize).

    Args:
        authorization (None | str | Unset): Bearer token
        body (CloneAndRunRequest): Spawn N parallel clones of the calling bot (one per slice),
            auto-merge results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CloneAndRunRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Clone And Run

     Option B self-cloning: the caller (an agent's bot-user) fans out N parallel clones
    of itself, each running one slice; a MONITORING parent auto-merges the results
    (concatenate/vote in-backend; summarize wakes the parent to synthesize).

    Args:
        authorization (None | str | Unset): Bearer token
        body (CloneAndRunRequest): Spawn N parallel clones of the calling bot (one per slice),
            auto-merge results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CloneAndRunRequest,
    authorization: None | str | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Clone And Run

     Option B self-cloning: the caller (an agent's bot-user) fans out N parallel clones
    of itself, each running one slice; a MONITORING parent auto-merges the results
    (concatenate/vote in-backend; summarize wakes the parent to synthesize).

    Args:
        authorization (None | str | Unset): Bearer token
        body (CloneAndRunRequest): Spawn N parallel clones of the calling bot (one per slice),
            auto-merge results.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
