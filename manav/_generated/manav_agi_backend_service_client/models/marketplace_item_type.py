from enum import StrEnum


class MarketplaceItemType(StrEnum):
    AGENT = "agent"
    MCP_TOOL = "mcp_tool"

    def __str__(self) -> str:
        return str(self.value)
