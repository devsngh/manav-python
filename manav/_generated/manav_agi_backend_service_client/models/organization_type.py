from enum import StrEnum


class OrganizationType(StrEnum):
    CORPORATE = "corporate"
    FAMILY = "family"
    INDIVIDUAL = "individual"
    INTERNAL = "internal"
    SOCIETY = "society"

    def __str__(self) -> str:
        return str(self.value)
