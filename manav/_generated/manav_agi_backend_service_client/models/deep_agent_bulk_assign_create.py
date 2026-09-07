from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_target_type import AssignmentTargetType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_agent_bulk_assign_target import DeepAgentBulkAssignTarget


T = TypeVar("T", bound="DeepAgentBulkAssignCreate")


@_attrs_define
class DeepAgentBulkAssignCreate:
    """
    Attributes:
        target_type (AssignmentTargetType):
        targets (list[DeepAgentBulkAssignTarget] | Unset):
    """

    target_type: AssignmentTargetType
    targets: list[DeepAgentBulkAssignTarget] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        targets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_type": target_type,
            }
        )
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_agent_bulk_assign_target import DeepAgentBulkAssignTarget  # noqa: PLC0415

        d = dict(src_dict)
        target_type = AssignmentTargetType(d.pop("target_type"))

        _targets = d.pop("targets", UNSET)
        targets: list[DeepAgentBulkAssignTarget] | Unset = UNSET
        if _targets is not UNSET:
            targets = []
            for targets_item_data in _targets:
                targets_item = DeepAgentBulkAssignTarget.from_dict(targets_item_data)

                targets.append(targets_item)

        deep_agent_bulk_assign_create = cls(
            target_type=target_type,
            targets=targets,
        )

        deep_agent_bulk_assign_create.additional_properties = d
        return deep_agent_bulk_assign_create

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
