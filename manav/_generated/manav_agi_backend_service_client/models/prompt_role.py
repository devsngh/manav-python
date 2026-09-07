from enum import StrEnum


class PromptRole(StrEnum):
    FORMAT = "format"
    GUARDRAIL = "guardrail"
    MEMORY = "memory"
    POLICY = "policy"
    SKILL = "skill"
    SUBAGENT = "subagent"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
