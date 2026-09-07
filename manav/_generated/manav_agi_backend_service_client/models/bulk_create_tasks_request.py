from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_create_tasks_request_common_input_data_type_0 import BulkCreateTasksRequestCommonInputDataType0
    from ..models.bulk_task_item import BulkTaskItem


T = TypeVar("T", bound="BulkCreateTasksRequest")


@_attrs_define
class BulkCreateTasksRequest:
    """
    Attributes:
        tasks (list[BulkTaskItem]):
        common_input_data (BulkCreateTasksRequestCommonInputDataType0 | None | Unset):
        common_priority (None | str | Unset):
        common_due_at (None | str | Unset):
    """

    tasks: list[BulkTaskItem]
    common_input_data: BulkCreateTasksRequestCommonInputDataType0 | None | Unset = UNSET
    common_priority: None | str | Unset = UNSET
    common_due_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_create_tasks_request_common_input_data_type_0 import (
            BulkCreateTasksRequestCommonInputDataType0,  # noqa: PLC0415
        )

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        common_input_data: dict[str, Any] | None | Unset
        if isinstance(self.common_input_data, Unset):
            common_input_data = UNSET
        elif isinstance(self.common_input_data, BulkCreateTasksRequestCommonInputDataType0):
            common_input_data = self.common_input_data.to_dict()
        else:
            common_input_data = self.common_input_data

        common_priority: None | str | Unset
        if isinstance(self.common_priority, Unset):
            common_priority = UNSET
        else:
            common_priority = self.common_priority

        common_due_at: None | str | Unset
        if isinstance(self.common_due_at, Unset):
            common_due_at = UNSET
        else:
            common_due_at = self.common_due_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tasks": tasks,
            }
        )
        if common_input_data is not UNSET:
            field_dict["common_input_data"] = common_input_data
        if common_priority is not UNSET:
            field_dict["common_priority"] = common_priority
        if common_due_at is not UNSET:
            field_dict["common_due_at"] = common_due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_create_tasks_request_common_input_data_type_0 import (
            BulkCreateTasksRequestCommonInputDataType0,  # noqa: PLC0415
        )
        from ..models.bulk_task_item import BulkTaskItem  # noqa: PLC0415

        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = BulkTaskItem.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        def _parse_common_input_data(data: object) -> BulkCreateTasksRequestCommonInputDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                common_input_data_type_0 = BulkCreateTasksRequestCommonInputDataType0.from_dict(data)

                return common_input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkCreateTasksRequestCommonInputDataType0 | None | Unset, data)

        common_input_data = _parse_common_input_data(d.pop("common_input_data", UNSET))

        def _parse_common_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        common_priority = _parse_common_priority(d.pop("common_priority", UNSET))

        def _parse_common_due_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        common_due_at = _parse_common_due_at(d.pop("common_due_at", UNSET))

        bulk_create_tasks_request = cls(
            tasks=tasks,
            common_input_data=common_input_data,
            common_priority=common_priority,
            common_due_at=common_due_at,
        )

        bulk_create_tasks_request.additional_properties = d
        return bulk_create_tasks_request

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
