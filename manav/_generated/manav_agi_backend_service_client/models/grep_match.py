from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GrepMatch")


@_attrs_define
class GrepMatch:
    """
    Attributes:
        path (str):
        line_number (int):
        line (str):
        match (str):
    """

    path: str
    line_number: int
    line: str
    match: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        line_number = self.line_number

        line = self.line

        match = self.match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "line_number": line_number,
                "line": line,
                "match": match,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        line_number = d.pop("line_number")

        line = d.pop("line")

        match = d.pop("match")

        grep_match = cls(
            path=path,
            line_number=line_number,
            line=line,
            match=match,
        )

        grep_match.additional_properties = d
        return grep_match

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
