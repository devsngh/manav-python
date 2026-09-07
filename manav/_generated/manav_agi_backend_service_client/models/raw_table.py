from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_column import RawColumn


T = TypeVar("T", bound="RawTable")


@_attrs_define
class RawTable:
    """
    Attributes:
        raw_name (str):
        columns (list[RawColumn]):
        schema_name (None | str | Unset):
        row_count (int | None | Unset):
        is_view (bool | Unset):  Default: False.
    """

    raw_name: str
    columns: list[RawColumn]
    schema_name: None | str | Unset = UNSET
    row_count: int | None | Unset = UNSET
    is_view: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        raw_name = self.raw_name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)

        schema_name: None | str | Unset
        if isinstance(self.schema_name, Unset):
            schema_name = UNSET
        else:
            schema_name = self.schema_name

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        is_view = self.is_view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "raw_name": raw_name,
                "columns": columns,
            }
        )
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if is_view is not UNSET:
            field_dict["is_view"] = is_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_column import RawColumn  # noqa: PLC0415

        d = dict(src_dict)
        raw_name = d.pop("raw_name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in _columns:
            columns_item = RawColumn.from_dict(columns_item_data)

            columns.append(columns_item)

        def _parse_schema_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schema_name = _parse_schema_name(d.pop("schema_name", UNSET))

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        is_view = d.pop("is_view", UNSET)

        raw_table = cls(
            raw_name=raw_name,
            columns=columns,
            schema_name=schema_name,
            row_count=row_count,
            is_view=is_view,
        )

        raw_table.additional_properties = d
        return raw_table

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
