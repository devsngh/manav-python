from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorldSyncTablePerTable")


@_attrs_define
class WorldSyncTablePerTable:
    """
    Attributes:
        inserted (int):
        updated (int):
        errors (int | Unset):  Default: 0.
    """

    inserted: int
    updated: int
    errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inserted = self.inserted

        updated = self.updated

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inserted": inserted,
                "updated": updated,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inserted = d.pop("inserted")

        updated = d.pop("updated")

        errors = d.pop("errors", UNSET)

        world_sync_table_per_table = cls(
            inserted=inserted,
            updated=updated,
            errors=errors,
        )

        world_sync_table_per_table.additional_properties = d
        return world_sync_table_per_table

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
