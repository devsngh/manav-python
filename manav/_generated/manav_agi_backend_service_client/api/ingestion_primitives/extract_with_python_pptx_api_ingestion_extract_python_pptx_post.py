from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extract_request import ExtractRequest
from ...models.http_validation_error import HTTPValidationError
from ...models.pptx_response import PptxResponse
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
        "url": "/api/ingestion/extract/python_pptx",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PptxResponse | None:
    if response.status_code == 200:
        response_200 = PptxResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | PptxResponse]:
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
) -> Response[HTTPValidationError | PptxResponse]:
    """Extract With Python Pptx

     Extract per-slide content from a PPTX using python-pptx.

    Each slide returns:
      - slide_number, title, bullets, speaker_notes
      - has_charts (boolean flag — agent can decide to call vision per chart)
      - has_images (boolean flag)

    Primitive: no chart description, no image embedding. Agent escalates to
    Claude vision via a separate tool if it wants chart understanding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PptxResponse]
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
) -> HTTPValidationError | PptxResponse | None:
    """Extract With Python Pptx

     Extract per-slide content from a PPTX using python-pptx.

    Each slide returns:
      - slide_number, title, bullets, speaker_notes
      - has_charts (boolean flag — agent can decide to call vision per chart)
      - has_images (boolean flag)

    Primitive: no chart description, no image embedding. Agent escalates to
    Claude vision via a separate tool if it wants chart understanding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PptxResponse
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
) -> Response[HTTPValidationError | PptxResponse]:
    """Extract With Python Pptx

     Extract per-slide content from a PPTX using python-pptx.

    Each slide returns:
      - slide_number, title, bullets, speaker_notes
      - has_charts (boolean flag — agent can decide to call vision per chart)
      - has_images (boolean flag)

    Primitive: no chart description, no image embedding. Agent escalates to
    Claude vision via a separate tool if it wants chart understanding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PptxResponse]
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
) -> HTTPValidationError | PptxResponse | None:
    """Extract With Python Pptx

     Extract per-slide content from a PPTX using python-pptx.

    Each slide returns:
      - slide_number, title, bullets, speaker_notes
      - has_charts (boolean flag — agent can decide to call vision per chart)
      - has_images (boolean flag)

    Primitive: no chart description, no image embedding. Agent escalates to
    Claude vision via a separate tool if it wants chart understanding.

    Args:
        authorization (None | str | Unset): Bearer token
        body (ExtractRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PptxResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            authorization=authorization,
        )
    ).parsed
