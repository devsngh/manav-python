from enum import StrEnum


class ReportAccessType(StrEnum):
    AGENT = "agent"
    ALL = "all"
    DEPARTMENT = "department"
    PERIOD = "period"

    def __str__(self) -> str:
        return str(self.value)
