from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_life_mode_response_current_mode import AgentLifeModeResponseCurrentMode
from ..models.agent_life_mode_response_eligibility import AgentLifeModeResponseEligibility

T = TypeVar("T", bound="AgentLifeModeResponse")


@_attrs_define
class AgentLifeModeResponse:
    """
    Attributes:
        agent_id (str):
        agent_name (str):
        eligibility (AgentLifeModeResponseEligibility):
        enabled (bool):
        current_mode (AgentLifeModeResponseCurrentMode):
        updated_at (datetime.datetime):
    """

    agent_id: str
    agent_name: str
    eligibility: AgentLifeModeResponseEligibility
    enabled: bool
    current_mode: AgentLifeModeResponseCurrentMode
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_name = self.agent_name

        eligibility = self.eligibility.value

        enabled = self.enabled

        current_mode = self.current_mode.value

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_name": agent_name,
                "eligibility": eligibility,
                "enabled": enabled,
                "current_mode": current_mode,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_name = d.pop("agent_name")

        eligibility = AgentLifeModeResponseEligibility(d.pop("eligibility"))

        enabled = d.pop("enabled")

        current_mode = AgentLifeModeResponseCurrentMode(d.pop("current_mode"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        agent_life_mode_response = cls(
            agent_id=agent_id,
            agent_name=agent_name,
            eligibility=eligibility,
            enabled=enabled,
            current_mode=current_mode,
            updated_at=updated_at,
        )

        agent_life_mode_response.additional_properties = d
        return agent_life_mode_response

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
