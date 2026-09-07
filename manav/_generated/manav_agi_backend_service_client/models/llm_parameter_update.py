from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.parameter_type import ParameterType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LLMParameterUpdate")


@_attrs_define
class LLMParameterUpdate:
    """Update LLM parameter

    Attributes:
        parameter_name (None | str | Unset):
        parameter_type (None | ParameterType | Unset):
        default_value (Any | None | Unset):
        min_value (float | None | Unset):
        max_value (float | None | Unset):
        is_required (bool | None | Unset):
        description (None | str | Unset):
        order (int | None | Unset):
    """

    parameter_name: None | str | Unset = UNSET
    parameter_type: None | ParameterType | Unset = UNSET
    default_value: Any | None | Unset = UNSET
    min_value: float | None | Unset = UNSET
    max_value: float | None | Unset = UNSET
    is_required: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    order: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parameter_name: None | str | Unset
        if isinstance(self.parameter_name, Unset):
            parameter_name = UNSET
        else:
            parameter_name = self.parameter_name

        parameter_type: None | str | Unset
        if isinstance(self.parameter_type, Unset):
            parameter_type = UNSET
        elif isinstance(self.parameter_type, ParameterType):
            parameter_type = self.parameter_type.value
        else:
            parameter_type = self.parameter_type

        default_value: Any | None | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
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

        is_required: bool | None | Unset
        if isinstance(self.is_required, Unset):
            is_required = UNSET
        else:
            is_required = self.is_required

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        order: int | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        else:
            order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_name is not UNSET:
            field_dict["parameter_name"] = parameter_name
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type
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

        def _parse_parameter_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parameter_name = _parse_parameter_name(d.pop("parameter_name", UNSET))

        def _parse_parameter_type(data: object) -> None | ParameterType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parameter_type_type_0 = ParameterType(data)

                return parameter_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ParameterType | Unset, data)

        parameter_type = _parse_parameter_type(d.pop("parameter_type", UNSET))

        def _parse_default_value(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

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

        def _parse_is_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_required = _parse_is_required(d.pop("is_required", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

        llm_parameter_update = cls(
            parameter_name=parameter_name,
            parameter_type=parameter_type,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            is_required=is_required,
            description=description,
            order=order,
        )

        llm_parameter_update.additional_properties = d
        return llm_parameter_update

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
