from enum import StrEnum


class WebhookRegistryUpdateStatusType0(StrEnum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    ERROR = "error"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
