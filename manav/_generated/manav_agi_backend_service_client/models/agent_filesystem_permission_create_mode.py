from enum import StrEnum


class AgentFilesystemPermissionCreateMode(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    INTERRUPT = "interrupt"

    def __str__(self) -> str:
        return str(self.value)
