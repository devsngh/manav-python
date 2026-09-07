from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_society_state_row_current_mode import AgentSocietyStateRowCurrentMode
from ..models.agent_society_state_row_eligibility import AgentSocietyStateRowEligibility

T = TypeVar("T", bound="AgentSocietyStateRow")


@_attrs_define
class AgentSocietyStateRow:
    """One row in the agent table on the admin UI.

    Attributes:
        id (str):
        name (str):
        eligibility (AgentSocietyStateRowEligibility):
        enabled (bool):
        current_mode (AgentSocietyStateRowCurrentMode):
    """

    id: str
    name: str
    eligibility: AgentSocietyStateRowEligibility
    enabled: bool
    current_mode: AgentSocietyStateRowCurrentMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        eligibility = self.eligibility.value

        enabled = self.enabled

        current_mode = self.current_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "eligibility": eligibility,
                "enabled": enabled,
                "current_mode": current_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        eligibility = AgentSocietyStateRowEligibility(d.pop("eligibility"))

        enabled = d.pop("enabled")

        current_mode = AgentSocietyStateRowCurrentMode(d.pop("current_mode"))

        agent_society_state_row = cls(
            id=id,
            name=name,
            eligibility=eligibility,
            enabled=enabled,
            current_mode=current_mode,
        )

        agent_society_state_row.additional_properties = d
        return agent_society_state_row

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
