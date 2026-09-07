from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_type import ComponentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentDefinitionUpdate")


@_attrs_define
class ComponentDefinitionUpdate:
    """
    Attributes:
        component_name (None | str | Unset):
        component_type (ComponentType | None | Unset):
        description (None | str | Unset):
        is_active (bool | None | Unset):
    """

    component_name: None | str | Unset = UNSET
    component_type: ComponentType | None | Unset = UNSET
    description: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_name: None | str | Unset
        if isinstance(self.component_name, Unset):
            component_name = UNSET
        else:
            component_name = self.component_name

        component_type: None | str | Unset
        if isinstance(self.component_type, Unset):
            component_type = UNSET
        elif isinstance(self.component_type, ComponentType):
            component_type = self.component_type.value
        else:
            component_type = self.component_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_name is not UNSET:
            field_dict["component_name"] = component_name
        if component_type is not UNSET:
            field_dict["component_type"] = component_type
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_component_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component_name = _parse_component_name(d.pop("component_name", UNSET))

        def _parse_component_type(data: object) -> ComponentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                component_type_type_0 = ComponentType(data)

                return component_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ComponentType | None | Unset, data)

        component_type = _parse_component_type(d.pop("component_type", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        component_definition_update = cls(
            component_name=component_name,
            component_type=component_type,
            description=description,
            is_active=is_active,
        )

        component_definition_update.additional_properties = d
        return component_definition_update

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
