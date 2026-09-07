from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rollup_summary_detections import RollupSummaryDetections


T = TypeVar("T", bound="RollupSummary")


@_attrs_define
class RollupSummary:
    """
    Attributes:
        org_id (str):
        detectors_run (int):
        detections (RollupSummaryDetections):
        total_upserted (int):
    """

    org_id: str
    detectors_run: int
    detections: RollupSummaryDetections
    total_upserted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        detectors_run = self.detectors_run

        detections = self.detections.to_dict()

        total_upserted = self.total_upserted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "detectors_run": detectors_run,
                "detections": detections,
                "total_upserted": total_upserted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rollup_summary_detections import RollupSummaryDetections  # noqa: PLC0415

        d = dict(src_dict)
        org_id = d.pop("org_id")

        detectors_run = d.pop("detectors_run")

        detections = RollupSummaryDetections.from_dict(d.pop("detections"))

        total_upserted = d.pop("total_upserted")

        rollup_summary = cls(
            org_id=org_id,
            detectors_run=detectors_run,
            detections=detections,
            total_upserted=total_upserted,
        )

        rollup_summary.additional_properties = d
        return rollup_summary

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
