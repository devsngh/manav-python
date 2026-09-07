from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="XlsxSheet")


@_attrs_define
class XlsxSheet:
    """
    Attributes:
        name (str):
        row_count (int):
        headers (list[str]):
        sample_rows (list[list[Any]]):
    """

    name: str
    row_count: int
    headers: list[str]
    sample_rows: list[list[Any]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        row_count = self.row_count

        headers = self.headers

        sample_rows = []
        for sample_rows_item_data in self.sample_rows:
            sample_rows_item = sample_rows_item_data

            sample_rows.append(sample_rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "row_count": row_count,
                "headers": headers,
                "sample_rows": sample_rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        row_count = d.pop("row_count")

        headers = cast(list[str], d.pop("headers"))

        sample_rows = []
        _sample_rows = d.pop("sample_rows")
        for sample_rows_item_data in _sample_rows:
            sample_rows_item = cast(list[Any], sample_rows_item_data)

            sample_rows.append(sample_rows_item)

        xlsx_sheet = cls(
            name=name,
            row_count=row_count,
            headers=headers,
            sample_rows=sample_rows,
        )

        xlsx_sheet.additional_properties = d
        return xlsx_sheet

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
