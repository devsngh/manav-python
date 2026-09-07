from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.component_type import ComponentType

T = TypeVar("T", bound="PromptComponentResponse")


@_attrs_define
class PromptComponentResponse:
    """
    Attributes:
        id (UUID):
        component_definition_id (UUID):
        component_name (str):
        component_type (ComponentType): Types of prompt components
        component_content (None | str):
        order (int):
        created_at (datetime.datetime):
    """

    id: UUID
    component_definition_id: UUID
    component_name: str
    component_type: ComponentType
    component_content: None | str
    order: int
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        component_definition_id = str(self.component_definition_id)

        component_name = self.component_name

        component_type = self.component_type.value

        component_content: None | str
        component_content = self.component_content

        order = self.order

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "component_definition_id": component_definition_id,
                "component_name": component_name,
                "component_type": component_type,
                "component_content": component_content,
                "order": order,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        component_definition_id = UUID(d.pop("component_definition_id"))

        component_name = d.pop("component_name")

        component_type = ComponentType(d.pop("component_type"))

        def _parse_component_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        component_content = _parse_component_content(d.pop("component_content"))

        order = d.pop("order")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        prompt_component_response = cls(
            id=id,
            component_definition_id=component_definition_id,
            component_name=component_name,
            component_type=component_type,
            component_content=component_content,
            order=order,
            created_at=created_at,
        )

        prompt_component_response.additional_properties = d
        return prompt_component_response

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
