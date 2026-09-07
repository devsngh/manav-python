from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.legal_consent_input import LegalConsentInput
from ...models.legal_consent_record import LegalConsentRecord
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LegalConsentInput,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/legal-consents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LegalConsentRecord | None:
    if response.status_code == 201:
        response_201 = LegalConsentRecord.from_dict(response.json())

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
) -> Response[HTTPValidationError | LegalConsentRecord]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LegalConsentInput,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LegalConsentRecord]:
    """Record Legal Consent

     Record a legal-document acceptance (or marketing opt-out) for the
    *currently signed-in user*. Used when a policy version bumps and we
    re-prompt, or when the user updates their marketing preference.

    Append-only: this never updates an existing row. The most recent row
    per (user_id, document_type) reflects the user's current stance.

    Args:
        authorization (None | str | Unset): Bearer token
        body (LegalConsentInput): One legal-doc acceptance recorded at signup.

            Frontend sends one of these per document the user agreed to during
            the signup compliance gate (Terms, Privacy, optionally Cookies / DPA).
            The `document_version` is the version string the frontend rendered —
            it comes from the doc's frontmatter via /api/legal/{slug} on the
            marketing site, so we store exactly what the user saw.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LegalConsentRecord]
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
    body: LegalConsentInput,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LegalConsentRecord | None:
    """Record Legal Consent

     Record a legal-document acceptance (or marketing opt-out) for the
    *currently signed-in user*. Used when a policy version bumps and we
    re-prompt, or when the user updates their marketing preference.

    Append-only: this never updates an existing row. The most recent row
    per (user_id, document_type) reflects the user's current stance.

    Args:
        authorization (None | str | Unset): Bearer token
        body (LegalConsentInput): One legal-doc acceptance recorded at signup.

            Frontend sends one of these per document the user agreed to during
            the signup compliance gate (Terms, Privacy, optionally Cookies / DPA).
            The `document_version` is the version string the frontend rendered —
            it comes from the doc's frontmatter via /api/legal/{slug} on the
            marketing site, so we store exactly what the user saw.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LegalConsentRecord
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LegalConsentInput,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | LegalConsentRecord]:
    """Record Legal Consent

     Record a legal-document acceptance (or marketing opt-out) for the
    *currently signed-in user*. Used when a policy version bumps and we
    re-prompt, or when the user updates their marketing preference.

    Append-only: this never updates an existing row. The most recent row
    per (user_id, document_type) reflects the user's current stance.

    Args:
        authorization (None | str | Unset): Bearer token
        body (LegalConsentInput): One legal-doc acceptance recorded at signup.

            Frontend sends one of these per document the user agreed to during
            the signup compliance gate (Terms, Privacy, optionally Cookies / DPA).
            The `document_version` is the version string the frontend rendered —
            it comes from the doc's frontmatter via /api/legal/{slug} on the
            marketing site, so we store exactly what the user saw.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LegalConsentRecord]
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
    body: LegalConsentInput,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | LegalConsentRecord | None:
    """Record Legal Consent

     Record a legal-document acceptance (or marketing opt-out) for the
    *currently signed-in user*. Used when a policy version bumps and we
    re-prompt, or when the user updates their marketing preference.

    Append-only: this never updates an existing row. The most recent row
    per (user_id, document_type) reflects the user's current stance.

    Args:
        authorization (None | str | Unset): Bearer token
        body (LegalConsentInput): One legal-doc acceptance recorded at signup.

            Frontend sends one of these per document the user agreed to during
            the signup compliance gate (Terms, Privacy, optionally Cookies / DPA).
            The `document_version` is the version string the frontend rendered —
            it comes from the doc's frontmatter via /api/legal/{slug} on the
            marketing site, so we store exactly what the user saw.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LegalConsentRecord
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
