from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CurrentTaskSummary")


@_attrs_define
class CurrentTaskSummary:
    """
    Attributes:
        id (str):
        title (str):
        status (str):
        priority (str):
        parent_task_id (None | str):
        thread_id (None | str):
        started_at (datetime.datetime | None):
        duration_seconds (int | None):
    """

    id: str
    title: str
    status: str
    priority: str
    parent_task_id: None | str
    thread_id: None | str
    started_at: datetime.datetime | None
    duration_seconds: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        status = self.status

        priority = self.priority

        parent_task_id: None | str
        parent_task_id = self.parent_task_id

        thread_id: None | str
        thread_id = self.thread_id

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        duration_seconds: int | None
        duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "status": status,
                "priority": priority,
                "parent_task_id": parent_task_id,
                "thread_id": thread_id,
                "started_at": started_at,
                "duration_seconds": duration_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        status = d.pop("status")

        priority = d.pop("priority")

        def _parse_parent_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_task_id = _parse_parent_task_id(d.pop("parent_task_id"))

        def _parse_thread_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        thread_id = _parse_thread_id(d.pop("thread_id"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_duration_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds"))

        current_task_summary = cls(
            id=id,
            title=title,
            status=status,
            priority=priority,
            parent_task_id=parent_task_id,
            thread_id=thread_id,
            started_at=started_at,
            duration_seconds=duration_seconds,
        )

        current_task_summary.additional_properties = d
        return current_task_summary

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
