from enum import StrEnum


class PermissionRequestCreateScope(StrEnum):
    GLOBAL = "global"
    ORG = "org"
    OWN = "own"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
