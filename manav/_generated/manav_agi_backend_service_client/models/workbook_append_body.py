from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkbookAppendBody")


@_attrs_define
class WorkbookAppendBody:
    """
    Attributes:
        entry_content (str): Markdown content of the entry.
        workbook_type (str | Unset):  Default: 'personal'.
        entry_title (None | str | Unset):
        entry_date_iso (None | str | Unset):
        auto_create_title (None | str | Unset):
    """

    entry_content: str
    workbook_type: str | Unset = "personal"
    entry_title: None | str | Unset = UNSET
    entry_date_iso: None | str | Unset = UNSET
    auto_create_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_content = self.entry_content

        workbook_type = self.workbook_type

        entry_title: None | str | Unset
        if isinstance(self.entry_title, Unset):
            entry_title = UNSET
        else:
            entry_title = self.entry_title

        entry_date_iso: None | str | Unset
        if isinstance(self.entry_date_iso, Unset):
            entry_date_iso = UNSET
        else:
            entry_date_iso = self.entry_date_iso

        auto_create_title: None | str | Unset
        if isinstance(self.auto_create_title, Unset):
            auto_create_title = UNSET
        else:
            auto_create_title = self.auto_create_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_content": entry_content,
            }
        )
        if workbook_type is not UNSET:
            field_dict["workbook_type"] = workbook_type
        if entry_title is not UNSET:
            field_dict["entry_title"] = entry_title
        if entry_date_iso is not UNSET:
            field_dict["entry_date_iso"] = entry_date_iso
        if auto_create_title is not UNSET:
            field_dict["auto_create_title"] = auto_create_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entry_content = d.pop("entry_content")

        workbook_type = d.pop("workbook_type", UNSET)

        def _parse_entry_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entry_title = _parse_entry_title(d.pop("entry_title", UNSET))

        def _parse_entry_date_iso(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entry_date_iso = _parse_entry_date_iso(d.pop("entry_date_iso", UNSET))

        def _parse_auto_create_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_create_title = _parse_auto_create_title(d.pop("auto_create_title", UNSET))

        workbook_append_body = cls(
            entry_content=entry_content,
            workbook_type=workbook_type,
            entry_title=entry_title,
            entry_date_iso=entry_date_iso,
            auto_create_title=auto_create_title,
        )

        workbook_append_body.additional_properties = d
        return workbook_append_body

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
