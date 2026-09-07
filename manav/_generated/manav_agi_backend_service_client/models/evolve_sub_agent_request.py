from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evolve_sub_agent_request_changes import EvolveSubAgentRequestChanges


T = TypeVar("T", bound="EvolveSubAgentRequest")


@_attrs_define
class EvolveSubAgentRequest:
    """
    Attributes:
        source_subagent_id (str):
        changes (EvolveSubAgentRequestChanges):
        swap_in_all_configs (bool | Unset):  Default: True.
        deprecate_old (bool | Unset):  Default: True.
    """

    source_subagent_id: str
    changes: EvolveSubAgentRequestChanges
    swap_in_all_configs: bool | Unset = True
    deprecate_old: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_subagent_id = self.source_subagent_id

        changes = self.changes.to_dict()

        swap_in_all_configs = self.swap_in_all_configs

        deprecate_old = self.deprecate_old

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_subagent_id": source_subagent_id,
                "changes": changes,
            }
        )
        if swap_in_all_configs is not UNSET:
            field_dict["swap_in_all_configs"] = swap_in_all_configs
        if deprecate_old is not UNSET:
            field_dict["deprecate_old"] = deprecate_old

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evolve_sub_agent_request_changes import EvolveSubAgentRequestChanges  # noqa: PLC0415

        d = dict(src_dict)
        source_subagent_id = d.pop("source_subagent_id")

        changes = EvolveSubAgentRequestChanges.from_dict(d.pop("changes"))

        swap_in_all_configs = d.pop("swap_in_all_configs", UNSET)

        deprecate_old = d.pop("deprecate_old", UNSET)

        evolve_sub_agent_request = cls(
            source_subagent_id=source_subagent_id,
            changes=changes,
            swap_in_all_configs=swap_in_all_configs,
            deprecate_old=deprecate_old,
        )

        evolve_sub_agent_request.additional_properties = d
        return evolve_sub_agent_request

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
