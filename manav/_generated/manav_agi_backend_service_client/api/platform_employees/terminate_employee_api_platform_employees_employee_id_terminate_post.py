from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.employee_response import EmployeeResponse
from ...models.http_validation_error import HTTPValidationError
from ...models.terminate_employee_request import TerminateEmployeeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    employee_id: UUID,
    *,
    body: TerminateEmployeeRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/platform/employees/{employee_id}/terminate".format(
            employee_id=quote(str(employee_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmployeeResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EmployeeResponse.from_dict(response.json())

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
) -> Response[EmployeeResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TerminateEmployeeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[EmployeeResponse | HTTPValidationError]:
    """Terminate Employee

    Args:
        employee_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TerminateEmployeeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TerminateEmployeeRequest,
    authorization: None | str | Unset = UNSET,
) -> EmployeeResponse | HTTPValidationError | None:
    """Terminate Employee

    Args:
        employee_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TerminateEmployeeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeResponse | HTTPValidationError
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TerminateEmployeeRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[EmployeeResponse | HTTPValidationError]:
    """Terminate Employee

    Args:
        employee_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TerminateEmployeeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: TerminateEmployeeRequest,
    authorization: None | str | Unset = UNSET,
) -> EmployeeResponse | HTTPValidationError | None:
    """Terminate Employee

    Args:
        employee_id (UUID):
        authorization (None | str | Unset): Bearer token
        body (TerminateEmployeeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
