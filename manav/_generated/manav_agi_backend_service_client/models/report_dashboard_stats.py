from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_dashboard_stats_by_department import ReportDashboardStatsByDepartment
    from ..models.report_dashboard_stats_by_period import ReportDashboardStatsByPeriod
    from ..models.report_dashboard_stats_by_status import ReportDashboardStatsByStatus


T = TypeVar("T", bound="ReportDashboardStats")


@_attrs_define
class ReportDashboardStats:
    """
    Attributes:
        total (int | Unset):  Default: 0.
        today (int | Unset):  Default: 0.
        pending_review (int | Unset):  Default: 0.
        revised (int | Unset):  Default: 0.
        by_period (ReportDashboardStatsByPeriod | Unset):
        by_department (ReportDashboardStatsByDepartment | Unset):
        by_status (ReportDashboardStatsByStatus | Unset):
    """

    total: int | Unset = 0
    today: int | Unset = 0
    pending_review: int | Unset = 0
    revised: int | Unset = 0
    by_period: ReportDashboardStatsByPeriod | Unset = UNSET
    by_department: ReportDashboardStatsByDepartment | Unset = UNSET
    by_status: ReportDashboardStatsByStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        today = self.today

        pending_review = self.pending_review

        revised = self.revised

        by_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_period, Unset):
            by_period = self.by_period.to_dict()

        by_department: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_department, Unset):
            by_department = self.by_department.to_dict()

        by_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_status, Unset):
            by_status = self.by_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if today is not UNSET:
            field_dict["today"] = today
        if pending_review is not UNSET:
            field_dict["pending_review"] = pending_review
        if revised is not UNSET:
            field_dict["revised"] = revised
        if by_period is not UNSET:
            field_dict["by_period"] = by_period
        if by_department is not UNSET:
            field_dict["by_department"] = by_department
        if by_status is not UNSET:
            field_dict["by_status"] = by_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.report_dashboard_stats_by_department import ReportDashboardStatsByDepartment  # noqa: PLC0415
        from ..models.report_dashboard_stats_by_period import ReportDashboardStatsByPeriod  # noqa: PLC0415
        from ..models.report_dashboard_stats_by_status import ReportDashboardStatsByStatus  # noqa: PLC0415

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        today = d.pop("today", UNSET)

        pending_review = d.pop("pending_review", UNSET)

        revised = d.pop("revised", UNSET)

        _by_period = d.pop("by_period", UNSET)
        by_period: ReportDashboardStatsByPeriod | Unset
        if isinstance(_by_period, Unset):
            by_period = UNSET
        else:
            by_period = ReportDashboardStatsByPeriod.from_dict(_by_period)

        _by_department = d.pop("by_department", UNSET)
        by_department: ReportDashboardStatsByDepartment | Unset
        if isinstance(_by_department, Unset):
            by_department = UNSET
        else:
            by_department = ReportDashboardStatsByDepartment.from_dict(_by_department)

        _by_status = d.pop("by_status", UNSET)
        by_status: ReportDashboardStatsByStatus | Unset
        if isinstance(_by_status, Unset):
            by_status = UNSET
        else:
            by_status = ReportDashboardStatsByStatus.from_dict(_by_status)

        report_dashboard_stats = cls(
            total=total,
            today=today,
            pending_review=pending_review,
            revised=revised,
            by_period=by_period,
            by_department=by_department,
            by_status=by_status,
        )

        report_dashboard_stats.additional_properties = d
        return report_dashboard_stats

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
