from enum import StrEnum


class VoiceSessionStatusUpdateStatus(StrEnum):
    ANSWERED = "answered"
    CANCELED = "canceled"
    COMPLETED = "completed"
    DECLINED = "declined"
    FAILED = "failed"
    INITIATED = "initiated"
    IN_PROGRESS = "in_progress"
    NO_ANSWER = "no_answer"
    RINGING = "ringing"

    def __str__(self) -> str:
        return str(self.value)
