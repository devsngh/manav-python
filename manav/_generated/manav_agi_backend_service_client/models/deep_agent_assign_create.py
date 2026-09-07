from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assignment_target_type import AssignmentTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepAgentAssignCreate")


@_attrs_define
class DeepAgentAssignCreate:
    """
    Attributes:
        target_type (AssignmentTargetType):
        target_id (None | Unset | UUID):
        target_label (None | str | Unset):
    """

    target_type: AssignmentTargetType
    target_id: None | Unset | UUID = UNSET
    target_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type = self.target_type.value

        target_id: None | str | Unset
        if isinstance(self.target_id, Unset):
            target_id = UNSET
        elif isinstance(self.target_id, UUID):
            target_id = str(self.target_id)
        else:
            target_id = self.target_id

        target_label: None | str | Unset
        if isinstance(self.target_label, Unset):
            target_label = UNSET
        else:
            target_label = self.target_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_type": target_type,
            }
        )
        if target_id is not UNSET:
            field_dict["target_id"] = target_id
        if target_label is not UNSET:
            field_dict["target_label"] = target_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = AssignmentTargetType(d.pop("target_type"))

        def _parse_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_id_type_0 = UUID(data)

                return target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        target_id = _parse_target_id(d.pop("target_id", UNSET))

        def _parse_target_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_label = _parse_target_label(d.pop("target_label", UNSET))

        deep_agent_assign_create = cls(
            target_type=target_type,
            target_id=target_id,
            target_label=target_label,
        )

        deep_agent_assign_create.additional_properties = d
        return deep_agent_assign_create

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
