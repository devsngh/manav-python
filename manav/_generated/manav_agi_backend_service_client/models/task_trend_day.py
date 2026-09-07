from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaskTrendDay")


@_attrs_define
class TaskTrendDay:
    """
    Attributes:
        date (str):
        completed (int):
        failed (int):
        in_progress (int):
        pending (int):
        cancelled (int):
        waiting_human (int):
    """

    date: str
    completed: int
    failed: int
    in_progress: int
    pending: int
    cancelled: int
    waiting_human: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        completed = self.completed

        failed = self.failed

        in_progress = self.in_progress

        pending = self.pending

        cancelled = self.cancelled

        waiting_human = self.waiting_human

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "completed": completed,
                "failed": failed,
                "in_progress": in_progress,
                "pending": pending,
                "cancelled": cancelled,
                "waiting_human": waiting_human,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        completed = d.pop("completed")

        failed = d.pop("failed")

        in_progress = d.pop("in_progress")

        pending = d.pop("pending")

        cancelled = d.pop("cancelled")

        waiting_human = d.pop("waiting_human")

        task_trend_day = cls(
            date=date,
            completed=completed,
            failed=failed,
            in_progress=in_progress,
            pending=pending,
            cancelled=cancelled,
            waiting_human=waiting_human,
        )

        task_trend_day.additional_properties = d
        return task_trend_day

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
