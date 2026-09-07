from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grep_match import GrepMatch


T = TypeVar("T", bound="GrepResponse")


@_attrs_define
class GrepResponse:
    """
    Attributes:
        pattern (str):
        matches (list[GrepMatch]):
        total (int):
    """

    pattern: str
    matches: list[GrepMatch]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        matches = []
        for matches_item_data in self.matches:
            matches_item = matches_item_data.to_dict()
            matches.append(matches_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern": pattern,
                "matches": matches,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grep_match import GrepMatch  # noqa: PLC0415

        d = dict(src_dict)
        pattern = d.pop("pattern")

        matches = []
        _matches = d.pop("matches")
        for matches_item_data in _matches:
            matches_item = GrepMatch.from_dict(matches_item_data)

            matches.append(matches_item)

        total = d.pop("total")

        grep_response = cls(
            pattern=pattern,
            matches=matches,
            total=total,
        )

        grep_response.additional_properties = d
        return grep_response

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
