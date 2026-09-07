from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deep_agent_response import DeepAgentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_user_id: None | str | Unset
    if isinstance(user_id, Unset):
        json_user_id = UNSET
    else:
        json_user_id = user_id
    params["user_id"] = json_user_id

    json_bot_id: None | str | Unset
    if isinstance(bot_id, Unset):
        json_bot_id = UNSET
    else:
        json_bot_id = bot_id
    params["bot_id"] = json_bot_id

    json_role_id: None | str | Unset
    if isinstance(role_id, Unset):
        json_role_id = UNSET
    else:
        json_role_id = role_id
    params["role_id"] = json_role_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/deepagents/resolve",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeepAgentResponse | None | HTTPValidationError | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> DeepAgentResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = DeepAgentResponse.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentResponse | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[DeepAgentResponse | None | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentResponse | None | HTTPValidationError]:
    """Resolve Deepagent

     Resolve which DeepAgent applies for a given context.
    Priority: user > role > default. Used by orchestrator at session start.

    Args:
        user_id (None | str | Unset):
        bot_id (None | str | Unset):
        role_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bot_id=bot_id,
        role_id=role_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentResponse | None | HTTPValidationError | None:
    """Resolve Deepagent

     Resolve which DeepAgent applies for a given context.
    Priority: user > role > default. Used by orchestrator at session start.

    Args:
        user_id (None | str | Unset):
        bot_id (None | str | Unset):
        role_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentResponse | None | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        bot_id=bot_id,
        role_id=role_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[DeepAgentResponse | None | HTTPValidationError]:
    """Resolve Deepagent

     Resolve which DeepAgent applies for a given context.
    Priority: user > role > default. Used by orchestrator at session start.

    Args:
        user_id (None | str | Unset):
        bot_id (None | str | Unset):
        role_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeepAgentResponse | None | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bot_id=bot_id,
        role_id=role_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    user_id: None | str | Unset = UNSET,
    bot_id: None | str | Unset = UNSET,
    role_id: None | str | Unset = UNSET,
    authorization: None | str | Unset = UNSET,
) -> DeepAgentResponse | None | HTTPValidationError | None:
    """Resolve Deepagent

     Resolve which DeepAgent applies for a given context.
    Priority: user > role > default. Used by orchestrator at session start.

    Args:
        user_id (None | str | Unset):
        bot_id (None | str | Unset):
        role_id (None | str | Unset):
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeepAgentResponse | None | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            bot_id=bot_id,
            role_id=role_id,
            authorization=authorization,
        )
    ).parsed
