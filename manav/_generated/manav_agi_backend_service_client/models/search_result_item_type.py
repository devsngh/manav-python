from enum import StrEnum


class SearchResultItemType(StrEnum):
    DIALOGUE = "dialogue"
    HIL_EVENT = "hil_event"
    PATTERN = "pattern"
    SPAN = "span"
    TASK = "task"
    THREAD = "thread"
    TRACE = "trace"

    def __str__(self) -> str:
        return str(self.value)
