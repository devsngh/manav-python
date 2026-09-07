from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_society_state_row import AgentSocietyStateRow


T = TypeVar("T", bound="SocietyStateResponse")


@_attrs_define
class SocietyStateResponse:
    """Snapshot of master switch + every agent's Society state.

    Attributes:
        master_switch_enabled (bool):
        eligible_count (int):
        enabled_count (int):
        agents (list[AgentSocietyStateRow]):
        society_org_id (None | str | Unset):
    """

    master_switch_enabled: bool
    eligible_count: int
    enabled_count: int
    agents: list[AgentSocietyStateRow]
    society_org_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        master_switch_enabled = self.master_switch_enabled

        eligible_count = self.eligible_count

        enabled_count = self.enabled_count

        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        society_org_id: None | str | Unset
        if isinstance(self.society_org_id, Unset):
            society_org_id = UNSET
        else:
            society_org_id = self.society_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "master_switch_enabled": master_switch_enabled,
                "eligible_count": eligible_count,
                "enabled_count": enabled_count,
                "agents": agents,
            }
        )
        if society_org_id is not UNSET:
            field_dict["society_org_id"] = society_org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_society_state_row import AgentSocietyStateRow  # noqa: PLC0415

        d = dict(src_dict)
        master_switch_enabled = d.pop("master_switch_enabled")

        eligible_count = d.pop("eligible_count")

        enabled_count = d.pop("enabled_count")

        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = AgentSocietyStateRow.from_dict(agents_item_data)

            agents.append(agents_item)

        def _parse_society_org_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        society_org_id = _parse_society_org_id(d.pop("society_org_id", UNSET))

        society_state_response = cls(
            master_switch_enabled=master_switch_enabled,
            eligible_count=eligible_count,
            enabled_count=enabled_count,
            agents=agents,
            society_org_id=society_org_id,
        )

        society_state_response.additional_properties = d
        return society_state_response

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
