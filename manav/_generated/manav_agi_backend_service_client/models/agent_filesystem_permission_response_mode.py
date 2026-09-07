from enum import StrEnum


class AgentFilesystemPermissionResponseMode(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    INTERRUPT = "interrupt"

    def __str__(self) -> str:
        return str(self.value)
