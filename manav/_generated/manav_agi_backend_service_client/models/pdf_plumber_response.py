from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pdf_plumber_table import PdfPlumberTable


T = TypeVar("T", bound="PdfPlumberResponse")


@_attrs_define
class PdfPlumberResponse:
    """
    Attributes:
        text (str):
        tables (list[PdfPlumberTable]):
        page_count (int):
        char_count (int):
        table_count (int):
    """

    text: str
    tables: list[PdfPlumberTable]
    page_count: int
    char_count: int
    table_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        tables = []
        for tables_item_data in self.tables:
            tables_item = tables_item_data.to_dict()
            tables.append(tables_item)

        page_count = self.page_count

        char_count = self.char_count

        table_count = self.table_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "tables": tables,
                "page_count": page_count,
                "char_count": char_count,
                "table_count": table_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_plumber_table import PdfPlumberTable  # noqa: PLC0415

        d = dict(src_dict)
        text = d.pop("text")

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = PdfPlumberTable.from_dict(tables_item_data)

            tables.append(tables_item)

        page_count = d.pop("page_count")

        char_count = d.pop("char_count")

        table_count = d.pop("table_count")

        pdf_plumber_response = cls(
            text=text,
            tables=tables,
            page_count=page_count,
            char_count=char_count,
            table_count=table_count,
        )

        pdf_plumber_response.additional_properties = d
        return pdf_plumber_response

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
