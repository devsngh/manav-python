from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatStats")


@_attrs_define
class ChatStats:
    """Schema for chat statistics

    Attributes:
        total_threads (int):
        active_threads (int):
        archived_threads (int):
        total_dialogues (int):
        avg_dialogues_per_thread (float):
        liked_dialogues (int):
        dialogues_with_feedback (int):
    """

    total_threads: int
    active_threads: int
    archived_threads: int
    total_dialogues: int
    avg_dialogues_per_thread: float
    liked_dialogues: int
    dialogues_with_feedback: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_threads = self.total_threads

        active_threads = self.active_threads

        archived_threads = self.archived_threads

        total_dialogues = self.total_dialogues

        avg_dialogues_per_thread = self.avg_dialogues_per_thread

        liked_dialogues = self.liked_dialogues

        dialogues_with_feedback = self.dialogues_with_feedback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_threads": total_threads,
                "active_threads": active_threads,
                "archived_threads": archived_threads,
                "total_dialogues": total_dialogues,
                "avg_dialogues_per_thread": avg_dialogues_per_thread,
                "liked_dialogues": liked_dialogues,
                "dialogues_with_feedback": dialogues_with_feedback,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_threads = d.pop("total_threads")

        active_threads = d.pop("active_threads")

        archived_threads = d.pop("archived_threads")

        total_dialogues = d.pop("total_dialogues")

        avg_dialogues_per_thread = d.pop("avg_dialogues_per_thread")

        liked_dialogues = d.pop("liked_dialogues")

        dialogues_with_feedback = d.pop("dialogues_with_feedback")

        chat_stats = cls(
            total_threads=total_threads,
            active_threads=active_threads,
            archived_threads=archived_threads,
            total_dialogues=total_dialogues,
            avg_dialogues_per_thread=avg_dialogues_per_thread,
            liked_dialogues=liked_dialogues,
            dialogues_with_feedback=dialogues_with_feedback,
        )

        chat_stats.additional_properties = d
        return chat_stats

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
