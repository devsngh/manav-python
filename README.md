# Manav Python SDK

Official Python client for the [Manav AI](https://manavagi.com) platform.

## Install

```bash
pip install manav
```

Requires Python 3.9+.

## Quick start

Generate an API key at [platform.manavagi.com/settings/api-keys](https://platform.manavagi.com/settings/api-keys), then:

```python
from manav import Client

client = Client(api_key="mnv_...")

# List your agents
agents = client.get("/api/agents")
print(agents)

# Send a message to an agent
response = client.post("/api/chat/dialogues/stream", json={
    "agent_name": "manav",
    "message": "What's on my task list today?",
})
```

Or set the API key via environment variable:

```bash
export MANAV_API_KEY=mnv_...
```

```python
from manav import Client
client = Client()  # picks up MANAV_API_KEY automatically
```

## Async usage

```python
import asyncio
from manav import AsyncClient

async def main():
    async with AsyncClient(api_key="mnv_...") as client:
        agents = await client.get("/api/agents")
        print(agents)

asyncio.run(main())
```

## Error handling

The SDK raises typed exceptions:

```python
from manav import Client, AuthenticationError, RateLimitError, NotFoundError

client = Client(api_key="mnv_...")

try:
    result = client.post("/api/agents", json={"name": "my-bot"})
except AuthenticationError:
    print("Bad or expired API key")
except RateLimitError as e:
    print(f"Rate limited — retry after {e.retry_after} seconds")
except NotFoundError:
    print("Resource not found")
```

Exception hierarchy:

```
ManavError                    # root — catch-all
├── AuthenticationError       # 401 — bad/missing/expired API key
├── NotFoundError             # 404 — resource doesn't exist / no access
├── RateLimitError            # 429 — .retry_after has seconds
├── ValidationError           # other 4xx — bad payload
└── APIError                  # 5xx — unexpected server error
```

Every exception also exposes `.status_code` and `.body` for debugging.

## Configuration

```python
client = Client(
    api_key="mnv_...",
    base_url="https://api.manavagi.com",  # default
    timeout=30.0,                          # default (seconds)
    max_retries=2,                         # default — retries on 429/5xx
)
```

## Retries

By default the SDK retries on `429` (rate limit) and `5xx` (server error), honoring the
`Retry-After` header when present and falling back to exponential backoff otherwise.
Set `max_retries=0` to disable.

## Versioning

Follows [semantic versioning](https://semver.org/). While the SDK is in `0.x`,
minor releases may include breaking changes — pin exact versions in production.

## Development

```bash
git clone https://github.com/devsngh/manav-python.git
cd manav-python
pip install -e ".[dev]"
pytest
```

## Regenerating the low-level API client

The low-level client under `manav/_generated/` is regenerated from the live
OpenAPI schema at `https://api.manavagi.com/openapi.json`:

```bash
openapi-python-client generate --url https://api.manavagi.com/openapi.json \
    --output-path manav/_generated \
    --overwrite
```

A weekly GitHub Actions workflow does this automatically and opens a PR when
new endpoints appear.

## License

MIT — see [LICENSE](./LICENSE).

## Links

- [Platform](https://manavagi.com)
- [App](https://platform.manavagi.com)
- [Docs](https://docs.manavagi.com)
- [Issues](https://github.com/devsngh/manav-python/issues)
