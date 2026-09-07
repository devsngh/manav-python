from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UIElementResponse")


@_attrs_define
class UIElementResponse:
    """
    Attributes:
        element_key (str):
        label (str):
        category (str):
        id (UUID):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        rule_count (int | Unset):  Default: 0.
    """

    element_key: str
    label: str
    category: str
    id: UUID
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    rule_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        element_key = self.element_key

        label = self.label

        category = self.category

        id = str(self.id)

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        rule_count = self.rule_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "element_key": element_key,
                "label": label,
                "category": category,
                "id": id,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if rule_count is not UNSET:
            field_dict["rule_count"] = rule_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        element_key = d.pop("element_key")

        label = d.pop("label")

        category = d.pop("category")

        id = UUID(d.pop("id"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        rule_count = d.pop("rule_count", UNSET)

        ui_element_response = cls(
            element_key=element_key,
            label=label,
            category=category,
            id=id,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            rule_count=rule_count,
        )

        ui_element_response.additional_properties = d
        return ui_element_response

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
