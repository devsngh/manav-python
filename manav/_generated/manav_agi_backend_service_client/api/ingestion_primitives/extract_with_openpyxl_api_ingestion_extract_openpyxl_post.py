from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_request import ExtractRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.xlsx_response import XlsxResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExtractRequest,
    authorization: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["authorization"] = authorization

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/ingestion/extract/openpyxl",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | XlsxResponse | None:
    if response.status_code == 200:
        response_200 = XlsxResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | XlsxResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExtractRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | XlsxResponse]:
    """Extract With Openpyxl

     Extract STRUCTURAL data from an XLSX using openpyxl.

    Each sheet returns:
      - name
      - row_count (total non-empty rows in the sheet)
      - headers (first row, if present)
      - sample_rows (up to 20 — the agent's responsibility to fetch more if needed)

    Primitive: no flat-text dump, no row-cap enforcement beyond the sample.
    Agent decides whether to treat each sheet as a table (write to
    ingestion_tables) or as a document.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | XlsxResponse]
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
    body: ExtractRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | XlsxResponse | None:
    """Extract With Openpyxl

     Extract STRUCTURAL data from an XLSX using openpyxl.

    Each sheet returns:
      - name
      - row_count (total non-empty rows in the sheet)
      - headers (first row, if present)
      - sample_rows (up to 20 — the agent's responsibility to fetch more if needed)

    Primitive: no flat-text dump, no row-cap enforcement beyond the sample.
    Agent decides whether to treat each sheet as a table (write to
    ingestion_tables) or as a document.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | XlsxResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExtractRequest,
    authorization: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | XlsxResponse]:
    """Extract With Openpyxl

     Extract STRUCTURAL data from an XLSX using openpyxl.

    Each sheet returns:
      - name
      - row_count (total non-empty rows in the sheet)
      - headers (first row, if present)
      - sample_rows (up to 20 — the agent's responsibility to fetch more if needed)

    Primitive: no flat-text dump, no row-cap enforcement beyond the sample.
    Agent decides whether to treat each sheet as a table (write to
    ingestion_tables) or as a document.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | XlsxResponse]
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
    body: ExtractRequest,
    authorization: None | str | Unset = UNSET,
) -> HTTPValidationError | XlsxResponse | None:
    """Extract With Openpyxl

     Extract STRUCTURAL data from an XLSX using openpyxl.

    Each sheet returns:
      - name
      - row_count (total non-empty rows in the sheet)
      - headers (first row, if present)
      - sample_rows (up to 20 — the agent's responsibility to fetch more if needed)

    Primitive: no flat-text dump, no row-cap enforcement beyond the sample.
    Agent decides whether to treat each sheet as a table (write to
    ingestion_tables) or as a document.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | XlsxResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
