"""Manav — official Python SDK.

Basic usage:
    from manav import Client

    client = Client(api_key="mnv_...")
    agents = client.agents.list()

Async:
    from manav import AsyncClient

    async with AsyncClient(api_key="mnv_...") as client:
        agents = await client.agents.list()
"""

from manav._client import AsyncClient, Client
from manav._version import __version__
from manav.exceptions import (
    APIError,
    AuthenticationError,
    ManavError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)

__all__ = [
    "APIError",
    "AsyncClient",
    "AuthenticationError",
    "Client",
    "ManavError",
    "NotFoundError",
    "RateLimitError",
    "ValidationError",
    "__version__",
]
