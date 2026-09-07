from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.family_member_response import FamilyMemberResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_id: UUID,
    *,
    org_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    params: dict[str, Any] = {}

    json_org_id: None | str | Unset
    if isinstance(org_id, Unset):
        json_org_id = UNSET
    elif isinstance(org_id, UUID):
        json_org_id = str(org_id)
    else:
        json_org_id = org_id
    params["org_id"] = json_org_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/family/revoke/{member_id}".format(
            member_id=quote(str(member_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FamilyMemberResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = FamilyMemberResponse.from_dict(response.json())

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
) -> Response[FamilyMemberResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[FamilyMemberResponse | HTTPValidationError]:
    """Revoke Member

     Revoke platform access for a family member (unlink user_id).

    Args:
        member_id (UUID):
        org_id (None | Unset | UUID): Target org (admin only)
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FamilyMemberResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        member_id=member_id,
        org_id=org_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> FamilyMemberResponse | HTTPValidationError | None:
    """Revoke Member

     Revoke platform access for a family member (unlink user_id).

    Args:
        member_id (UUID):
        org_id (None | Unset | UUID): Target org (admin only)
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FamilyMemberResponse | HTTPValidationError
    """

    return sync_detailed(
        member_id=member_id,
        client=client,
        org_id=org_id,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> Response[FamilyMemberResponse | HTTPValidationError]:
    """Revoke Member

     Revoke platform access for a family member (unlink user_id).

    Args:
        member_id (UUID):
        org_id (None | Unset | UUID): Target org (admin only)
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FamilyMemberResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        member_id=member_id,
        org_id=org_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    org_id: None | Unset | UUID = UNSET,
    authorization: None | str | Unset = UNSET,
) -> FamilyMemberResponse | HTTPValidationError | None:
    """Revoke Member

     Revoke platform access for a family member (unlink user_id).

    Args:
        member_id (UUID):
        org_id (None | Unset | UUID): Target org (admin only)
        authorization (None | str | Unset): Bearer token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FamilyMemberResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            member_id=member_id,
            client=client,
            org_id=org_id,
            authorization=authorization,
        )
    ).parsed
