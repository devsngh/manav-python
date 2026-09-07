from enum import StrEnum


class ToolType(StrEnum):
    DATASOURCE = "datasource"
    GENERAL = "general"

    def __str__(self) -> str:
        return str(self.value)
