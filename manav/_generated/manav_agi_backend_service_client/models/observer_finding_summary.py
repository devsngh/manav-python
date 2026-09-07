from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.observer_finding_summary_by_finding_type import ObserverFindingSummaryByFindingType
    from ..models.observer_finding_summary_by_observer_role import ObserverFindingSummaryByObserverRole
    from ..models.observer_finding_summary_by_severity import ObserverFindingSummaryBySeverity
    from ..models.observer_finding_summary_top_observed_bots_item import ObserverFindingSummaryTopObservedBotsItem


T = TypeVar("T", bound="ObserverFindingSummary")


@_attrs_define
class ObserverFindingSummary:
    """GET .../findings/summary — Cyra reads this each morning.

    Attributes:
        window_days (int):
        total_findings (int):
        by_severity (ObserverFindingSummaryBySeverity):
        by_finding_type (ObserverFindingSummaryByFindingType):
        by_observer_role (ObserverFindingSummaryByObserverRole):
        top_observed_bots (list[ObserverFindingSummaryTopObservedBotsItem]):
    """

    window_days: int
    total_findings: int
    by_severity: ObserverFindingSummaryBySeverity
    by_finding_type: ObserverFindingSummaryByFindingType
    by_observer_role: ObserverFindingSummaryByObserverRole
    top_observed_bots: list[ObserverFindingSummaryTopObservedBotsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window_days = self.window_days

        total_findings = self.total_findings

        by_severity = self.by_severity.to_dict()

        by_finding_type = self.by_finding_type.to_dict()

        by_observer_role = self.by_observer_role.to_dict()

        top_observed_bots = []
        for top_observed_bots_item_data in self.top_observed_bots:
            top_observed_bots_item = top_observed_bots_item_data.to_dict()
            top_observed_bots.append(top_observed_bots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window_days": window_days,
                "total_findings": total_findings,
                "by_severity": by_severity,
                "by_finding_type": by_finding_type,
                "by_observer_role": by_observer_role,
                "top_observed_bots": top_observed_bots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observer_finding_summary_by_finding_type import (
            ObserverFindingSummaryByFindingType,  # noqa: PLC0415
        )
        from ..models.observer_finding_summary_by_observer_role import (
            ObserverFindingSummaryByObserverRole,  # noqa: PLC0415
        )
        from ..models.observer_finding_summary_by_severity import ObserverFindingSummaryBySeverity  # noqa: PLC0415
        from ..models.observer_finding_summary_top_observed_bots_item import (
            ObserverFindingSummaryTopObservedBotsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        window_days = d.pop("window_days")

        total_findings = d.pop("total_findings")

        by_severity = ObserverFindingSummaryBySeverity.from_dict(d.pop("by_severity"))

        by_finding_type = ObserverFindingSummaryByFindingType.from_dict(d.pop("by_finding_type"))

        by_observer_role = ObserverFindingSummaryByObserverRole.from_dict(d.pop("by_observer_role"))

        top_observed_bots = []
        _top_observed_bots = d.pop("top_observed_bots")
        for top_observed_bots_item_data in _top_observed_bots:
            top_observed_bots_item = ObserverFindingSummaryTopObservedBotsItem.from_dict(top_observed_bots_item_data)

            top_observed_bots.append(top_observed_bots_item)

        observer_finding_summary = cls(
            window_days=window_days,
            total_findings=total_findings,
            by_severity=by_severity,
            by_finding_type=by_finding_type,
            by_observer_role=by_observer_role,
            top_observed_bots=top_observed_bots,
        )

        observer_finding_summary.additional_properties = d
        return observer_finding_summary

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
