from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DocxResponse")


@_attrs_define
class DocxResponse:
    """
    Attributes:
        paragraphs (list[str]):
        tables (list[list[list[str]]]):
    """

    paragraphs: list[str]
    tables: list[list[list[str]]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paragraphs = self.paragraphs

        tables = []
        for tables_item_data in self.tables:
            tables_item = []
            for tables_item_item_data in tables_item_data:
                tables_item_item = tables_item_item_data

                tables_item.append(tables_item_item)

            tables.append(tables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paragraphs": paragraphs,
                "tables": tables,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paragraphs = cast(list[str], d.pop("paragraphs"))

        tables = []
        _tables = d.pop("tables")
        for tables_item_data in _tables:
            tables_item = []
            _tables_item = tables_item_data
            for tables_item_item_data in _tables_item:
                tables_item_item = cast(list[str], tables_item_item_data)

                tables_item.append(tables_item_item)

            tables.append(tables_item)

        docx_response = cls(
            paragraphs=paragraphs,
            tables=tables,
        )

        docx_response.additional_properties = d
        return docx_response

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
