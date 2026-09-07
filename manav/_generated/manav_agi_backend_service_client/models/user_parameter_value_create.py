from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserParameterValueCreate")


@_attrs_define
class UserParameterValueCreate:
    """Create user parameter value

    Attributes:
        parameter_id (UUID):
        parameter_value (Any):
        is_enabled (bool | Unset):  Default: True.
    """

    parameter_id: UUID
    parameter_value: Any
    is_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_id = str(self.parameter_id)

        parameter_value = self.parameter_value

        is_enabled = self.is_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameter_id": parameter_id,
                "parameter_value": parameter_value,
            }
        )
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_id = UUID(d.pop("parameter_id"))

        parameter_value = d.pop("parameter_value")

        is_enabled = d.pop("is_enabled", UNSET)

        user_parameter_value_create = cls(
            parameter_id=parameter_id,
            parameter_value=parameter_value,
            is_enabled=is_enabled,
        )

        user_parameter_value_create.additional_properties = d
        return user_parameter_value_create

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
