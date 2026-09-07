from enum import StrEnum


class AgentFilesystemPermissionUpdateModeType0(StrEnum):
    ALLOW = "allow"
    DENY = "deny"
    INTERRUPT = "interrupt"

    def __str__(self) -> str:
        return str(self.value)
