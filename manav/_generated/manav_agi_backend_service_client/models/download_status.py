from enum import StrEnum


class DownloadStatus(StrEnum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    DOWNLOADING = "downloading"
    FAILED = "failed"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
