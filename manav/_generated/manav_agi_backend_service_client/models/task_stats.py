from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskStats")


@_attrs_define
class TaskStats:
    """
    Attributes:
        total (int | Unset):  Default: 0.
        pending (int | Unset):  Default: 0.
        assigned (int | Unset):  Default: 0.
        in_progress (int | Unset):  Default: 0.
        monitoring (int | Unset):  Default: 0.
        waiting_human (int | Unset):  Default: 0.
        completed (int | Unset):  Default: 0.
        failed (int | Unset):  Default: 0.
        cancelled (int | Unset):  Default: 0.
        avg_completion_seconds (float | None | Unset):
    """

    total: int | Unset = 0
    pending: int | Unset = 0
    assigned: int | Unset = 0
    in_progress: int | Unset = 0
    monitoring: int | Unset = 0
    waiting_human: int | Unset = 0
    completed: int | Unset = 0
    failed: int | Unset = 0
    cancelled: int | Unset = 0
    avg_completion_seconds: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        assigned = self.assigned

        in_progress = self.in_progress

        monitoring = self.monitoring

        waiting_human = self.waiting_human

        completed = self.completed

        failed = self.failed

        cancelled = self.cancelled

        avg_completion_seconds: float | None | Unset
        if isinstance(self.avg_completion_seconds, Unset):
            avg_completion_seconds = UNSET
        else:
            avg_completion_seconds = self.avg_completion_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if pending is not UNSET:
            field_dict["pending"] = pending
        if assigned is not UNSET:
            field_dict["assigned"] = assigned
        if in_progress is not UNSET:
            field_dict["in_progress"] = in_progress
        if monitoring is not UNSET:
            field_dict["monitoring"] = monitoring
        if waiting_human is not UNSET:
            field_dict["waiting_human"] = waiting_human
        if completed is not UNSET:
            field_dict["completed"] = completed
        if failed is not UNSET:
            field_dict["failed"] = failed
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if avg_completion_seconds is not UNSET:
            field_dict["avg_completion_seconds"] = avg_completion_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        pending = d.pop("pending", UNSET)

        assigned = d.pop("assigned", UNSET)

        in_progress = d.pop("in_progress", UNSET)

        monitoring = d.pop("monitoring", UNSET)

        waiting_human = d.pop("waiting_human", UNSET)

        completed = d.pop("completed", UNSET)

        failed = d.pop("failed", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        def _parse_avg_completion_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_completion_seconds = _parse_avg_completion_seconds(d.pop("avg_completion_seconds", UNSET))

        task_stats = cls(
            total=total,
            pending=pending,
            assigned=assigned,
            in_progress=in_progress,
            monitoring=monitoring,
            waiting_human=waiting_human,
            completed=completed,
            failed=failed,
            cancelled=cancelled,
            avg_completion_seconds=avg_completion_seconds,
        )

        task_stats.additional_properties = d
        return task_stats

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
