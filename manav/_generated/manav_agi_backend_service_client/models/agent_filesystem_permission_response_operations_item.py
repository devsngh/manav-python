from enum import StrEnum


class AgentFilesystemPermissionResponseOperationsItem(StrEnum):
    DELETE = "delete"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
