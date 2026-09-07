from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.xlsx_sheet import XlsxSheet


T = TypeVar("T", bound="XlsxResponse")


@_attrs_define
class XlsxResponse:
    """
    Attributes:
        sheets (list[XlsxSheet]):
        sheet_count (int):
    """

    sheets: list[XlsxSheet]
    sheet_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheets = []
        for sheets_item_data in self.sheets:
            sheets_item = sheets_item_data.to_dict()
            sheets.append(sheets_item)

        sheet_count = self.sheet_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheets": sheets,
                "sheet_count": sheet_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.xlsx_sheet import XlsxSheet  # noqa: PLC0415

        d = dict(src_dict)
        sheets = []
        _sheets = d.pop("sheets")
        for sheets_item_data in _sheets:
            sheets_item = XlsxSheet.from_dict(sheets_item_data)

            sheets.append(sheets_item)

        sheet_count = d.pop("sheet_count")

        xlsx_response = cls(
            sheets=sheets,
            sheet_count=sheet_count,
        )

        xlsx_response.additional_properties = d
        return xlsx_response

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
