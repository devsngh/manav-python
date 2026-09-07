from enum import StrEnum


class ModelType(StrEnum):
    API = "api"
    CUSTOM = "custom"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
