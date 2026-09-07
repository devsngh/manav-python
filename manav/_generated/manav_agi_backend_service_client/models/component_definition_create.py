from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_type import ComponentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentDefinitionCreate")


@_attrs_define
class ComponentDefinitionCreate:
    """
    Attributes:
        component_name (str):
        component_type (ComponentType): Types of prompt components
        description (None | str | Unset):
        is_custom (bool | Unset):  Default: True.
    """

    component_name: str
    component_type: ComponentType
    description: None | str | Unset = UNSET
    is_custom: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_name = self.component_name

        component_type = self.component_type.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_custom = self.is_custom

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_name": component_name,
                "component_type": component_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_custom is not UNSET:
            field_dict["is_custom"] = is_custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_name = d.pop("component_name")

        component_type = ComponentType(d.pop("component_type"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_custom = d.pop("is_custom", UNSET)

        component_definition_create = cls(
            component_name=component_name,
            component_type=component_type,
            description=description,
            is_custom=is_custom,
        )

        component_definition_create.additional_properties = d
        return component_definition_create

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
