"""Exception hierarchy for the Manav SDK.

Users catch:
    - ManavError          : root — anything from the SDK
    - AuthenticationError : bad API key, expired, missing
    - RateLimitError      : hit rate limit; .retry_after has seconds
    - NotFoundError       : 404 — resource doesn't exist / no access
    - ValidationError     : 4xx from bad payload
    - APIError            : 5xx / unexpected server response
"""

from __future__ import annotations

from typing import Any


class ManavError(Exception):
    """Base for every SDK error."""

    def __init__(self, message: str, *, status_code: int | None = None, body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class AuthenticationError(ManavError):
    """Missing / invalid / expired API key (HTTP 401)."""


class RateLimitError(ManavError):
    """Per-key rate limit exceeded (HTTP 429).

    `retry_after` is the seconds hint from the `Retry-After` header
    when the server provides one.
    """

    def __init__(self, message: str, *, retry_after: int | None = None, **kwargs: Any):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class NotFoundError(ManavError):
    """Resource not found or not accessible with current permissions (HTTP 404)."""


class ValidationError(ManavError):
    """Request payload rejected as invalid (HTTP 4xx other than 401/404/429)."""


class APIError(ManavError):
    """Unexpected server-side error (HTTP 5xx or malformed response)."""
