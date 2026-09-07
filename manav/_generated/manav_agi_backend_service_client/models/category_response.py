from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CategoryResponse")


@_attrs_define
class CategoryResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        display_name (str):
        description (None | str):
        icon (None | str):
        sort_order (int):
        parent_id (None | UUID):
        is_active (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    name: str
    display_name: str
    description: None | str
    icon: None | str
    sort_order: int
    parent_id: None | UUID
    is_active: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        display_name = self.display_name

        description: None | str
        description = self.description

        icon: None | str
        icon = self.icon

        sort_order = self.sort_order

        parent_id: None | str
        if isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "display_name": display_name,
                "description": description,
                "icon": icon,
                "sort_order": sort_order,
                "parent_id": parent_id,
                "is_active": is_active,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        display_name = d.pop("display_name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_icon(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon = _parse_icon(d.pop("icon"))

        sort_order = d.pop("sort_order")

        def _parse_parent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        category_response = cls(
            id=id,
            name=name,
            display_name=display_name,
            description=description,
            icon=icon,
            sort_order=sort_order,
            parent_id=parent_id,
            is_active=is_active,
            created_at=created_at,
        )

        category_response.additional_properties = d
        return category_response

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
