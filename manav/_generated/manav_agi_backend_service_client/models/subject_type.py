from enum import StrEnum


class SubjectType(StrEnum):
    AGENT = "agent"
    DEBATE = "debate"
    DEPT = "dept"
    DIALOGUE = "dialogue"
    ORG = "org"
    THREAD = "thread"

    def __str__(self) -> str:
        return str(self.value)
