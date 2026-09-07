from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position_reporting_entry import PositionReportingEntry


T = TypeVar("T", bound="PositionSubordinatesResponse")


@_attrs_define
class PositionSubordinatesResponse:
    """All positions that report to a given position (from position_reporting)

    Attributes:
        position_id (str):
        title (str):
        subordinates (list[PositionReportingEntry]):
        total (int):
    """

    position_id: str
    title: str
    subordinates: list[PositionReportingEntry]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position_id = self.position_id

        title = self.title

        subordinates = []
        for subordinates_item_data in self.subordinates:
            subordinates_item = subordinates_item_data.to_dict()
            subordinates.append(subordinates_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position_id": position_id,
                "title": title,
                "subordinates": subordinates,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position_reporting_entry import PositionReportingEntry  # noqa: PLC0415

        d = dict(src_dict)
        position_id = d.pop("position_id")

        title = d.pop("title")

        subordinates = []
        _subordinates = d.pop("subordinates")
        for subordinates_item_data in _subordinates:
            subordinates_item = PositionReportingEntry.from_dict(subordinates_item_data)

            subordinates.append(subordinates_item)

        total = d.pop("total")

        position_subordinates_response = cls(
            position_id=position_id,
            title=title,
            subordinates=subordinates,
            total=total,
        )

        position_subordinates_response.additional_properties = d
        return position_subordinates_response

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
