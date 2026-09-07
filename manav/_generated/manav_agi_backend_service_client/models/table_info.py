from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TableInfo")


@_attrs_define
class TableInfo:
    """
    Attributes:
        name (str):
        schema (None | str | Unset):
        row_count (int | None | Unset):
        size_mb (float | None | Unset):
    """

    name: str
    schema: None | str | Unset = UNSET
    row_count: int | None | Unset = UNSET
    size_mb: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema: None | str | Unset
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        size_mb: float | None | Unset
        if isinstance(self.size_mb, Unset):
            size_mb = UNSET
        else:
            size_mb = self.size_mb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["schema"] = schema
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if size_mb is not UNSET:
            field_dict["size_mb"] = size_mb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_schema(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        def _parse_size_mb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        size_mb = _parse_size_mb(d.pop("size_mb", UNSET))

        table_info = cls(
            name=name,
            schema=schema,
            row_count=row_count,
            size_mb=size_mb,
        )

        table_info.additional_properties = d
        return table_info

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
