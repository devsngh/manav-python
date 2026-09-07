from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_attainment_summary_by_status import TargetAttainmentSummaryByStatus


T = TypeVar("T", bound="TargetAttainmentSummary")


@_attrs_define
class TargetAttainmentSummary:
    """
    Attributes:
        org_id (UUID):
        total_targets (int):
        by_status (TargetAttainmentSummaryByStatus):
        overall_attainment_pct (float):
        at_risk_count (int):
        window (None | str | Unset):
    """

    org_id: UUID
    total_targets: int
    by_status: TargetAttainmentSummaryByStatus
    overall_attainment_pct: float
    at_risk_count: int
    window: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = str(self.org_id)

        total_targets = self.total_targets

        by_status = self.by_status.to_dict()

        overall_attainment_pct = self.overall_attainment_pct

        at_risk_count = self.at_risk_count

        window: None | str | Unset
        if isinstance(self.window, Unset):
            window = UNSET
        else:
            window = self.window

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "total_targets": total_targets,
                "by_status": by_status,
                "overall_attainment_pct": overall_attainment_pct,
                "at_risk_count": at_risk_count,
            }
        )
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_attainment_summary_by_status import TargetAttainmentSummaryByStatus  # noqa: PLC0415

        d = dict(src_dict)
        org_id = UUID(d.pop("org_id"))

        total_targets = d.pop("total_targets")

        by_status = TargetAttainmentSummaryByStatus.from_dict(d.pop("by_status"))

        overall_attainment_pct = d.pop("overall_attainment_pct")

        at_risk_count = d.pop("at_risk_count")

        def _parse_window(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        window = _parse_window(d.pop("window", UNSET))

        target_attainment_summary = cls(
            org_id=org_id,
            total_targets=total_targets,
            by_status=by_status,
            overall_attainment_pct=overall_attainment_pct,
            at_risk_count=at_risk_count,
            window=window,
        )

        target_attainment_summary.additional_properties = d
        return target_attainment_summary

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
