from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_node import TaskNode


T = TypeVar("T", bound="CreateTaskTreeRequest")


@_attrs_define
class CreateTaskTreeRequest:
    """
    Attributes:
        parent (TaskNode):
        subtasks (list[TaskNode]):
        auto_monitor (bool | Unset):  Default: True.
        check_interval_seconds (int | Unset):  Default: 300.
        max_duration_seconds (int | Unset):  Default: 7200.
    """

    parent: TaskNode
    subtasks: list[TaskNode]
    auto_monitor: bool | Unset = True
    check_interval_seconds: int | Unset = 300
    max_duration_seconds: int | Unset = 7200
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent.to_dict()

        subtasks = []
        for subtasks_item_data in self.subtasks:
            subtasks_item = subtasks_item_data.to_dict()
            subtasks.append(subtasks_item)

        auto_monitor = self.auto_monitor

        check_interval_seconds = self.check_interval_seconds

        max_duration_seconds = self.max_duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
                "subtasks": subtasks,
            }
        )
        if auto_monitor is not UNSET:
            field_dict["auto_monitor"] = auto_monitor
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.task_node import TaskNode  # noqa: PLC0415

        d = dict(src_dict)
        parent = TaskNode.from_dict(d.pop("parent"))

        subtasks = []
        _subtasks = d.pop("subtasks")
        for subtasks_item_data in _subtasks:
            subtasks_item = TaskNode.from_dict(subtasks_item_data)

            subtasks.append(subtasks_item)

        auto_monitor = d.pop("auto_monitor", UNSET)

        check_interval_seconds = d.pop("check_interval_seconds", UNSET)

        max_duration_seconds = d.pop("max_duration_seconds", UNSET)

        create_task_tree_request = cls(
            parent=parent,
            subtasks=subtasks,
            auto_monitor=auto_monitor,
            check_interval_seconds=check_interval_seconds,
            max_duration_seconds=max_duration_seconds,
        )

        create_task_tree_request.additional_properties = d
        return create_task_tree_request

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
