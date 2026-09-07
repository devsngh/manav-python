from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectedDatabase")


@_attrs_define
class ConnectedDatabase:
    """
    Attributes:
        source_id (str):
        name (str):
        type_ (str):
        status (str):
        table_count (int | Unset):  Default: 0.
    """

    source_id: str
    name: str
    type_: str
    status: str
    table_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_id = self.source_id

        name = self.name

        type_ = self.type_

        status = self.status

        table_count = self.table_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_id": source_id,
                "name": name,
                "type": type_,
                "status": status,
            }
        )
        if table_count is not UNSET:
            field_dict["table_count"] = table_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_id = d.pop("source_id")

        name = d.pop("name")

        type_ = d.pop("type")

        status = d.pop("status")

        table_count = d.pop("table_count", UNSET)

        connected_database = cls(
            source_id=source_id,
            name=name,
            type_=type_,
            status=status,
            table_count=table_count,
        )

        connected_database.additional_properties = d
        return connected_database

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
