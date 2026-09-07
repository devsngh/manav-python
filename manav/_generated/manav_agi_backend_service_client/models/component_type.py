from enum import StrEnum


class ComponentType(StrEnum):
    ADVANCED = "advanced"
    CONDITIONAL = "conditional"
    CORE = "core"
    META = "meta"
    OPTIMIZATION = "optimization"
    REASONING = "reasoning"
    STRUCTURED_OUTPUT = "structured_output"

    def __str__(self) -> str:
        return str(self.value)
