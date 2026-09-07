from enum import StrEnum


class PermissionScope(StrEnum):
    GLOBAL = "global"
    ORG = "org"
    OWN = "own"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
