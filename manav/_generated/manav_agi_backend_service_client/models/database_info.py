from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatabaseInfo")


@_attrs_define
class DatabaseInfo:
    """
    Attributes:
        name (str):
        size_mb (float | None | Unset):
        table_count (int | None | Unset):
        is_selected (bool | Unset):  Default: False.
        is_system (bool | Unset):  Default: False.
    """

    name: str
    size_mb: float | None | Unset = UNSET
    table_count: int | None | Unset = UNSET
    is_selected: bool | Unset = False
    is_system: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        size_mb: float | None | Unset
        if isinstance(self.size_mb, Unset):
            size_mb = UNSET
        else:
            size_mb = self.size_mb

        table_count: int | None | Unset
        if isinstance(self.table_count, Unset):
            table_count = UNSET
        else:
            table_count = self.table_count

        is_selected = self.is_selected

        is_system = self.is_system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if size_mb is not UNSET:
            field_dict["size_mb"] = size_mb
        if table_count is not UNSET:
            field_dict["table_count"] = table_count
        if is_selected is not UNSET:
            field_dict["is_selected"] = is_selected
        if is_system is not UNSET:
            field_dict["is_system"] = is_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_size_mb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

        def _parse_table_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        table_count = _parse_table_count(d.pop("table_count", UNSET))

        is_selected = d.pop("is_selected", UNSET)

        is_system = d.pop("is_system", UNSET)

        database_info = cls(
            name=name,
            size_mb=size_mb,
            table_count=table_count,
            is_selected=is_selected,
            is_system=is_system,
        )

        database_info.additional_properties = d
        return database_info

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
