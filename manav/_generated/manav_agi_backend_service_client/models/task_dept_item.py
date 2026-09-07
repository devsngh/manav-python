from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TaskDeptItem")


@_attrs_define
class TaskDeptItem:
    """
    Attributes:
        department_id (str):
        department_name (str):
        total (int):
        completed (int):
        failed (int):
        completion_rate (float):
    """

    department_id: str
    department_name: str
    total: int
    completed: int
    failed: int
    completion_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        department_id = self.department_id

        department_name = self.department_name

        total = self.total

        completed = self.completed

        failed = self.failed

        completion_rate = self.completion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department_id": department_id,
                "department_name": department_name,
                "total": total,
                "completed": completed,
                "failed": failed,
                "completion_rate": completion_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        department_id = d.pop("department_id")

        department_name = d.pop("department_name")

        total = d.pop("total")

        completed = d.pop("completed")

        failed = d.pop("failed")

        completion_rate = d.pop("completion_rate")

        task_dept_item = cls(
            department_id=department_id,
            department_name=department_name,
            total=total,
            completed=completed,
            failed=failed,
            completion_rate=completion_rate,
        )

        task_dept_item.additional_properties = d
        return task_dept_item

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
