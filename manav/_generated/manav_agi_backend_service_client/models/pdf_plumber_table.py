from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PdfPlumberTable")


@_attrs_define
class PdfPlumberTable:
    """
    Attributes:
        page (int):
        rows (list[list[Any]]):
    """

    page: int
    rows: list[list[Any]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data

            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page = d.pop("page")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = cast(list[Any], rows_item_data)

            rows.append(rows_item)

        pdf_plumber_table = cls(
            page=page,
            rows=rows,
        )

        pdf_plumber_table.additional_properties = d
        return pdf_plumber_table

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
