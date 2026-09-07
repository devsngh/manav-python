from enum import StrEnum


class TargetLayer(StrEnum):
    AGENT_RECONFIG = "agent_reconfig"
    EXISTING_SKILL_REVISION = "existing_skill_revision"
    FACTORY_VALIDATOR = "factory_validator"
    INFRA_CHANGE = "infra_change"
    NEW_SKILL = "new_skill"
    VERTICAL_OPENING = "vertical_opening"

    def __str__(self) -> str:
        return str(self.value)
