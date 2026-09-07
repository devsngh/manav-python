from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parameter_type import ParameterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LLMParameterCreate")


@_attrs_define
class LLMParameterCreate:
    """Create LLM parameter

    Attributes:
        parameter_name (str):
        parameter_type (ParameterType): Parameter data types
        default_value (Any | Unset):
        min_value (float | None | Unset):
        max_value (float | None | Unset):
        is_required (bool | Unset):  Default: True.
        description (None | str | Unset):
        order (int | Unset):  Default: 0.
    """

    parameter_name: str
    parameter_type: ParameterType
    default_value: Any | Unset = UNSET
    min_value: float | None | Unset = UNSET
    max_value: float | None | Unset = UNSET
    is_required: bool | Unset = True
    description: None | str | Unset = UNSET
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_name = self.parameter_name

        parameter_type = self.parameter_type.value

        default_value = self.default_value

        min_value: float | None | Unset
        if isinstance(self.min_value, Unset):
            min_value = UNSET
        else:
            min_value = self.min_value

        max_value: float | None | Unset
        if isinstance(self.max_value, Unset):
            max_value = UNSET
        else:
            max_value = self.max_value

        is_required = self.is_required

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parameter_name": parameter_name,
                "parameter_type": parameter_type,
            }
        )
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parameter_name = d.pop("parameter_name")

        parameter_type = ParameterType(d.pop("parameter_type"))

        default_value = d.pop("default_value", UNSET)

        def _parse_min_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_value = _parse_min_value(d.pop("min_value", UNSET))

        def _parse_max_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_value = _parse_max_value(d.pop("max_value", UNSET))

        is_required = d.pop("is_required", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        order = d.pop("order", UNSET)

        llm_parameter_create = cls(
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            is_required=is_required,
            description=description,
            order=order,
        )

        llm_parameter_create.additional_properties = d
        return llm_parameter_create

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
