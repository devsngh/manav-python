from enum import StrEnum


class AssignmentTargetType(StrEnum):
    BOT = "bot"
    DEFAULT = "default"
    ORG_DEFAULT = "org_default"
    ROLE = "role"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
