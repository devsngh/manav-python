from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkUserStatusUpdate")


@_attrs_define
class BulkUserStatusUpdate:
    """Bulk update user status

    Attributes:
        user_ids (list[UUID]):
        is_active (bool):
    """

    user_ids: list[UUID]
    is_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_ids = []
        for user_ids_item_data in self.user_ids:
            user_ids_item = str(user_ids_item_data)
            user_ids.append(user_ids_item)

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_ids": user_ids,
                "is_active": is_active,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_ids = []
        _user_ids = d.pop("user_ids")
        for user_ids_item_data in _user_ids:
            user_ids_item = UUID(user_ids_item_data)

            user_ids.append(user_ids_item)

        is_active = d.pop("is_active")

        bulk_user_status_update = cls(
            user_ids=user_ids,
            is_active=is_active,
        )

        bulk_user_status_update.additional_properties = d
        return bulk_user_status_update

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
