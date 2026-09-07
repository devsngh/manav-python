from enum import StrEnum


class SubAgentType(StrEnum):
    COMPILED = "compiled"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
