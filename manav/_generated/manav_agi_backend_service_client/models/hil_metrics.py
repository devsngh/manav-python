from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hil_metrics_by_status import HILMetricsByStatus


T = TypeVar("T", bound="HILMetrics")


@_attrs_define
class HILMetrics:
    """
    Attributes:
        total_rules (int):
        by_status (HILMetricsByStatus):
        active_count (int):
        tools_covered (int):
    """

    total_rules: int
    by_status: HILMetricsByStatus
    active_count: int
    tools_covered: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rules = self.total_rules

        by_status = self.by_status.to_dict()

        active_count = self.active_count

        tools_covered = self.tools_covered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_rules": total_rules,
                "by_status": by_status,
                "active_count": active_count,
                "tools_covered": tools_covered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hil_metrics_by_status import HILMetricsByStatus  # noqa: PLC0415

        d = dict(src_dict)
        total_rules = d.pop("total_rules")

        by_status = HILMetricsByStatus.from_dict(d.pop("by_status"))

        active_count = d.pop("active_count")

        tools_covered = d.pop("tools_covered")

        hil_metrics = cls(
            total_rules=total_rules,
            by_status=by_status,
            active_count=active_count,
            tools_covered=tools_covered,
        )

        hil_metrics.additional_properties = d
        return hil_metrics

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
