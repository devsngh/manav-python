from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolParameterCreate")


@_attrs_define
class ToolParameterCreate:
    """
    Attributes:
        parameter_name (str):
        parameter_type (str):
        parameter_description (None | str | Unset):
        required (bool | Unset):  Default: False.
        default_value (None | str | Unset):
        order (int | Unset):  Default: 0.
    """

    parameter_name: str
    parameter_type: str
    parameter_description: None | str | Unset = UNSET
    required: bool | Unset = False
    default_value: None | str | Unset = UNSET
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_name = self.parameter_name

        parameter_type = self.parameter_type

        parameter_description: None | str | Unset
        if isinstance(self.parameter_description, Unset):
            parameter_description = UNSET
        else:
            parameter_description = self.parameter_description

        required = self.required

        default_value: None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameter_name": parameter_name,
                "parameter_type": parameter_type,
            }
        )
        if parameter_description is not UNSET:
            field_dict["parameter_description"] = parameter_description
        if required is not UNSET:
            field_dict["required"] = required
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_name = d.pop("parameter_name")

        parameter_type = d.pop("parameter_type")

        def _parse_parameter_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parameter_description = _parse_parameter_description(d.pop("parameter_description", UNSET))

        required = d.pop("required", UNSET)

        def _parse_default_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        order = d.pop("order", UNSET)

        tool_parameter_create = cls(
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            parameter_description=parameter_description,
            required=required,
            default_value=default_value,
            order=order,
        )

        tool_parameter_create.additional_properties = d
        return tool_parameter_create

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
