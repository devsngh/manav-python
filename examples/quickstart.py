"""Quickstart — list your agents and send a chat message.

Set MANAV_API_KEY first:
    export MANAV_API_KEY=mnv_...

Then run:
    python examples/quickstart.py
"""

from manav import AuthenticationError, Client, RateLimitError


def main() -> None:
    try:
        with Client() as client:
            # 1. List agents you have access to
            agents = client.get("/api/agents")
            print(f"Found {len(agents) if isinstance(agents, list) else '?'} agents")

            # 2. Print the first few
            if isinstance(agents, list):
                for a in agents[:3]:
                    print(f"  - {a.get('agent_name', a.get('name', '?'))}")
    except AuthenticationError:
        print("Set MANAV_API_KEY environment variable — get a key from")
        print("https://platform.manavagi.com/settings/api-keys")
    except RateLimitError as e:
        print(f"Rate limited — try again in {e.retry_after or 60}s")


if __name__ == "__main__":
    main()
