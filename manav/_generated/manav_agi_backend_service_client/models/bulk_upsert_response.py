from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpsertResponse")


@_attrs_define
class BulkUpsertResponse:
    """
    Attributes:
        table (str):
        inserted (int):
        updated (int):
        message (str):
        skipped (int | Unset):  Default: 0.
        errors (int | Unset):  Default: 0.
    """

    table: str
    inserted: int
    updated: int
    message: str
    skipped: int | Unset = 0
    errors: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        inserted = self.inserted

        updated = self.updated

        message = self.message

        skipped = self.skipped

        errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
                "inserted": inserted,
                "updated": updated,
                "message": message,
            }
        )
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table = d.pop("table")

        inserted = d.pop("inserted")

        updated = d.pop("updated")

        message = d.pop("message")

        skipped = d.pop("skipped", UNSET)

        errors = d.pop("errors", UNSET)

        bulk_upsert_response = cls(
            table=table,
            inserted=inserted,
            updated=updated,
            message=message,
            skipped=skipped,
            errors=errors,
        )

        bulk_upsert_response.additional_properties = d
        return bulk_upsert_response

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
