from enum import StrEnum


class OrganizationStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
