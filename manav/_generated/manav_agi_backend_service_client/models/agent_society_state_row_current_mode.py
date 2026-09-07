from enum import StrEnum


class AgentSocietyStateRowCurrentMode(StrEnum):
    CONTEMPLATIVE = "contemplative"
    LIFE = "life"
    SLEEP = "sleep"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
