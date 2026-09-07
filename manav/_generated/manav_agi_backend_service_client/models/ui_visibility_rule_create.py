from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UIVisibilityRuleCreate")


@_attrs_define
class UIVisibilityRuleCreate:
    """
    Attributes:
        element_id (UUID):
        rule_type (str):
        target_id (str):
        is_visible (bool):
        priority (int | Unset):  Default: 0.
    """

    element_id: UUID
    rule_type: str
    target_id: str
    is_visible: bool
    priority: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_id = str(self.element_id)

        rule_type = self.rule_type

        target_id = self.target_id

        is_visible = self.is_visible

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_id": element_id,
                "rule_type": rule_type,
                "target_id": target_id,
                "is_visible": is_visible,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_id = UUID(d.pop("element_id"))

        rule_type = d.pop("rule_type")

        target_id = d.pop("target_id")

        is_visible = d.pop("is_visible")

        priority = d.pop("priority", UNSET)

        ui_visibility_rule_create = cls(
            element_id=element_id,
            rule_type=rule_type,
            target_id=target_id,
            is_visible=is_visible,
            priority=priority,
        )

        ui_visibility_rule_create.additional_properties = d
        return ui_visibility_rule_create

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
