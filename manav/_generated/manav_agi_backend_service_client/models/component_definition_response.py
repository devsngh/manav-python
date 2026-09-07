from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_type import ComponentType

T = TypeVar("T", bound="ComponentDefinitionResponse")


@_attrs_define
class ComponentDefinitionResponse:
    """
    Attributes:
        id (UUID):
        component_name (str):
        component_type (ComponentType): Types of prompt components
        description (None | str):
        is_custom (bool):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    component_name: str
    component_type: ComponentType
    description: None | str
    is_custom: bool
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        component_name = self.component_name

        component_type = self.component_type.value

        description: None | str
        description = self.description

        is_custom = self.is_custom

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "component_name": component_name,
                "component_type": component_type,
                "description": description,
                "is_custom": is_custom,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        component_name = d.pop("component_name")

        component_type = ComponentType(d.pop("component_type"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        is_custom = d.pop("is_custom")

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        component_definition_response = cls(
            id=id,
            component_name=component_name,
            component_type=component_type,
            description=description,
            is_custom=is_custom,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
        )

        component_definition_response.additional_properties = d
        return component_definition_response

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
