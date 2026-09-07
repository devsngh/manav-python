from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.position_reporting_entry import PositionReportingEntry


T = TypeVar("T", bound="PositionReportsToResponse")


@_attrs_define
class PositionReportsToResponse:
    """All positions that a given position reports to (from position_reporting)

    Attributes:
        position_id (str):
        title (str):
        reports_to (list[PositionReportingEntry]):
        total (int):
    """

    position_id: str
    title: str
    reports_to: list[PositionReportingEntry]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position_id = self.position_id

        title = self.title

        reports_to = []
        for reports_to_item_data in self.reports_to:
            reports_to_item = reports_to_item_data.to_dict()
            reports_to.append(reports_to_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position_id": position_id,
                "title": title,
                "reports_to": reports_to,
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

        reports_to = []
        _reports_to = d.pop("reports_to")
        for reports_to_item_data in _reports_to:
            reports_to_item = PositionReportingEntry.from_dict(reports_to_item_data)

            reports_to.append(reports_to_item)

        total = d.pop("total")

        position_reports_to_response = cls(
            position_id=position_id,
            title=title,
            reports_to=reports_to,
            total=total,
        )

        position_reports_to_response.additional_properties = d
        return position_reports_to_response

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
