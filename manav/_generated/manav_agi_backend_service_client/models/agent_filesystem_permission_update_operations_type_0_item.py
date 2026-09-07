from enum import StrEnum


class AgentFilesystemPermissionUpdateOperationsType0Item(StrEnum):
    DELETE = "delete"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
