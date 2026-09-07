from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeptOverviewItem")


@_attrs_define
class DeptOverviewItem:
    """
    Attributes:
        department_id (str):
        department_name (str):
        task_total (int):
        task_completed (int):
        task_failed (int):
        task_in_progress (int):
        task_pending (int):
        task_cancelled (int):
        completion_rate (float):
        agent_count (int):
        top_agent_tasks (int):
        top_agent_name (None | str | Unset):
    """

    department_id: str
    department_name: str
    task_total: int
    task_completed: int
    task_failed: int
    task_in_progress: int
    task_pending: int
    task_cancelled: int
    completion_rate: float
    agent_count: int
    top_agent_tasks: int
    top_agent_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        department_id = self.department_id

        department_name = self.department_name

        task_total = self.task_total

        task_completed = self.task_completed

        task_failed = self.task_failed

        task_in_progress = self.task_in_progress

        task_pending = self.task_pending

        task_cancelled = self.task_cancelled

        completion_rate = self.completion_rate

        agent_count = self.agent_count

        top_agent_tasks = self.top_agent_tasks

        top_agent_name: None | str | Unset
        if isinstance(self.top_agent_name, Unset):
            top_agent_name = UNSET
        else:
            top_agent_name = self.top_agent_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department_id": department_id,
                "department_name": department_name,
                "task_total": task_total,
                "task_completed": task_completed,
                "task_failed": task_failed,
                "task_in_progress": task_in_progress,
                "task_pending": task_pending,
                "task_cancelled": task_cancelled,
                "completion_rate": completion_rate,
                "agent_count": agent_count,
                "top_agent_tasks": top_agent_tasks,
            }
        )
        if top_agent_name is not UNSET:
            field_dict["top_agent_name"] = top_agent_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        department_id = d.pop("department_id")

        department_name = d.pop("department_name")

        task_total = d.pop("task_total")

        task_completed = d.pop("task_completed")

        task_failed = d.pop("task_failed")

        task_in_progress = d.pop("task_in_progress")

        task_pending = d.pop("task_pending")

        task_cancelled = d.pop("task_cancelled")

        completion_rate = d.pop("completion_rate")

        agent_count = d.pop("agent_count")

        top_agent_tasks = d.pop("top_agent_tasks")

        def _parse_top_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        top_agent_name = _parse_top_agent_name(d.pop("top_agent_name", UNSET))

        dept_overview_item = cls(
            department_id=department_id,
            department_name=department_name,
            task_total=task_total,
            task_completed=task_completed,
            task_failed=task_failed,
            task_in_progress=task_in_progress,
            task_pending=task_pending,
            task_cancelled=task_cancelled,
            completion_rate=completion_rate,
            agent_count=agent_count,
            top_agent_tasks=top_agent_tasks,
            top_agent_name=top_agent_name,
        )

        dept_overview_item.additional_properties = d
        return dept_overview_item

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
