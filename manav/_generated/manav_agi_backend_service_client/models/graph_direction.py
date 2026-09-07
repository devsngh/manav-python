from enum import StrEnum


class GraphDirection(StrEnum):
    BOTH = "both"
    INCOMING = "incoming"
    OUTGOING = "outgoing"

    def __str__(self) -> str:
        return str(self.value)
