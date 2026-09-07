from enum import StrEnum


class ReportStatus(StrEnum):
    ACKNOWLEDGED = "acknowledged"
    DRAFT = "draft"
    REVISION_REQUESTED = "revision_requested"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
