from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.employee_list_response import EmployeeListResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    employment_status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    department_code: None | str | Unset = UNSET,
    manager_employee_id: None | Unset | UUID = UNSET,
    country_code: None | str | Unset = UNSET,
    is_remote: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_employment_status: None | str | Unset
    if isinstance(employment_status, Unset):
        json_employment_status = UNSET
    else:
        json_employment_status = employment_status
    params["employment_status"] = json_employment_status

    json_legal_entity_id: None | str | Unset
    if isinstance(legal_entity_id, Unset):
        json_legal_entity_id = UNSET
    elif isinstance(legal_entity_id, UUID):
        json_legal_entity_id = str(legal_entity_id)
    else:
        json_legal_entity_id = legal_entity_id
    params["legal_entity_id"] = json_legal_entity_id

    json_department_code: None | str | Unset
    if isinstance(department_code, Unset):
        json_department_code = UNSET
    else:
        json_department_code = department_code
    params["department_code"] = json_department_code

    json_manager_employee_id: None | str | Unset
    if isinstance(manager_employee_id, Unset):
        json_manager_employee_id = UNSET
    elif isinstance(manager_employee_id, UUID):
        json_manager_employee_id = str(manager_employee_id)
    else:
        json_manager_employee_id = manager_employee_id
    params["manager_employee_id"] = json_manager_employee_id

    json_country_code: None | str | Unset
    if isinstance(country_code, Unset):
        json_country_code = UNSET
    else:
        json_country_code = country_code
    params["country_code"] = json_country_code

    json_is_remote: bool | None | Unset
    if isinstance(is_remote, Unset):
        json_is_remote = UNSET
    else:
        json_is_remote = is_remote
    params["is_remote"] = json_is_remote

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/platform/employees",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmployeeListResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EmployeeListResponse.from_dict(response.json())

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
) -> Response[EmployeeListResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    employment_status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    department_code: None | str | Unset = UNSET,
    manager_employee_id: None | Unset | UUID = UNSET,
    country_code: None | str | Unset = UNSET,
    is_remote: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[EmployeeListResponse | HTTPValidationError]:
    """List Employees

    Args:
        employment_status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        department_code (None | str | Unset):
        manager_employee_id (None | Unset | UUID):
        country_code (None | str | Unset):
        is_remote (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        employment_status=employment_status,
        legal_entity_id=legal_entity_id,
        department_code=department_code,
        manager_employee_id=manager_employee_id,
        country_code=country_code,
        is_remote=is_remote,
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
    employment_status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    department_code: None | str | Unset = UNSET,
    manager_employee_id: None | Unset | UUID = UNSET,
    country_code: None | str | Unset = UNSET,
    is_remote: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> EmployeeListResponse | HTTPValidationError | None:
    """List Employees

    Args:
        employment_status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        department_code (None | str | Unset):
        manager_employee_id (None | Unset | UUID):
        country_code (None | str | Unset):
        is_remote (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeListResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        employment_status=employment_status,
        legal_entity_id=legal_entity_id,
        department_code=department_code,
        manager_employee_id=manager_employee_id,
        country_code=country_code,
        is_remote=is_remote,
        page=page,
        page_size=page_size,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    employment_status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    department_code: None | str | Unset = UNSET,
    manager_employee_id: None | Unset | UUID = UNSET,
    country_code: None | str | Unset = UNSET,
    is_remote: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> Response[EmployeeListResponse | HTTPValidationError]:
    """List Employees

    Args:
        employment_status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        department_code (None | str | Unset):
        manager_employee_id (None | Unset | UUID):
        country_code (None | str | Unset):
        is_remote (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeListResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        employment_status=employment_status,
        legal_entity_id=legal_entity_id,
        department_code=department_code,
        manager_employee_id=manager_employee_id,
        country_code=country_code,
        is_remote=is_remote,
        page=page,
        page_size=page_size,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    employment_status: None | str | Unset = UNSET,
    legal_entity_id: None | Unset | UUID = UNSET,
    department_code: None | str | Unset = UNSET,
    manager_employee_id: None | Unset | UUID = UNSET,
    country_code: None | str | Unset = UNSET,
    is_remote: bool | None | Unset = UNSET,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    authorization: None | str | Unset = UNSET,
) -> EmployeeListResponse | HTTPValidationError | None:
    """List Employees

    Args:
        employment_status (None | str | Unset):
        legal_entity_id (None | Unset | UUID):
        department_code (None | str | Unset):
        manager_employee_id (None | Unset | UUID):
        country_code (None | str | Unset):
        is_remote (bool | None | Unset):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeListResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            employment_status=employment_status,
            legal_entity_id=legal_entity_id,
            department_code=department_code,
            manager_employee_id=manager_employee_id,
            country_code=country_code,
            is_remote=is_remote,
            page=page,
            page_size=page_size,
            authorization=authorization,
        )
    ).parsed
