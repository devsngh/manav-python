from enum import StrEnum


class PermissionAction(StrEnum):
    ASSIGN = "assign"
    BACKUP = "backup"
    CREATE = "create"
    DELETE = "delete"
    EXECUTE = "execute"
    MIGRATE = "migrate"
    READ = "read"
    RESTORE = "restore"
    REVIEW = "review"
    REVOKE = "revoke"
    SEED = "seed"
    UPDATE = "update"

    def __str__(self) -> str:
        return str(self.value)
