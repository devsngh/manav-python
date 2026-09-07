from enum import StrEnum


class MemberStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
