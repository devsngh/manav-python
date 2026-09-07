from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TasksByBotItem")


@_attrs_define
class TasksByBotItem:
    """
    Attributes:
        bot_id (str):
        bot_name (str):
        completed (int):
        failed (int):
        in_progress (int):
        pending (int):
        cancelled (int):
    """

    bot_id: str
    bot_name: str
    completed: int
    failed: int
    in_progress: int
    pending: int
    cancelled: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = self.bot_id

        bot_name = self.bot_name

        completed = self.completed

        failed = self.failed

        in_progress = self.in_progress

        pending = self.pending

        cancelled = self.cancelled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "bot_name": bot_name,
                "completed": completed,
                "failed": failed,
                "in_progress": in_progress,
                "pending": pending,
                "cancelled": cancelled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        bot_name = d.pop("bot_name")

        completed = d.pop("completed")

        failed = d.pop("failed")

        in_progress = d.pop("in_progress")

        pending = d.pop("pending")

        cancelled = d.pop("cancelled")

        tasks_by_bot_item = cls(
            bot_id=bot_id,
            bot_name=bot_name,
            completed=completed,
            failed=failed,
            in_progress=in_progress,
            pending=pending,
            cancelled=cancelled,
        )

        tasks_by_bot_item.additional_properties = d
        return tasks_by_bot_item

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
