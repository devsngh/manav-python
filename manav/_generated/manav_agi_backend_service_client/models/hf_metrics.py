from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HFMetrics")


@_attrs_define
class HFMetrics:
    """HF download metrics

    Attributes:
        total_downloads (int):
        queued_downloads (int):
        active_downloads (int):
        completed_downloads (int):
        failed_downloads (int):
        registered_downloads (int):
    """

    total_downloads: int
    queued_downloads: int
    active_downloads: int
    completed_downloads: int
    failed_downloads: int
    registered_downloads: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_downloads = self.total_downloads

        queued_downloads = self.queued_downloads

        active_downloads = self.active_downloads

        completed_downloads = self.completed_downloads

        failed_downloads = self.failed_downloads

        registered_downloads = self.registered_downloads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_downloads": total_downloads,
                "queued_downloads": queued_downloads,
                "active_downloads": active_downloads,
                "completed_downloads": completed_downloads,
                "failed_downloads": failed_downloads,
                "registered_downloads": registered_downloads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_downloads = d.pop("total_downloads")

        queued_downloads = d.pop("queued_downloads")

        active_downloads = d.pop("active_downloads")

        completed_downloads = d.pop("completed_downloads")

        failed_downloads = d.pop("failed_downloads")

        registered_downloads = d.pop("registered_downloads")

        hf_metrics = cls(
            total_downloads=total_downloads,
            queued_downloads=queued_downloads,
            active_downloads=active_downloads,
            completed_downloads=completed_downloads,
            failed_downloads=failed_downloads,
            registered_downloads=registered_downloads,
        )

        hf_metrics.additional_properties = d
        return hf_metrics

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
