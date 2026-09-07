from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkpoint_timeline_entry import CheckpointTimelineEntry


T = TypeVar("T", bound="CheckpointTimelineResponse")


@_attrs_define
class CheckpointTimelineResponse:
    """
    Attributes:
        thread_id (str):
        count (int):
        entries (list[CheckpointTimelineEntry]):
        ns (str | Unset):  Default: ''.
    """

    thread_id: str
    count: int
    entries: list[CheckpointTimelineEntry]
    ns: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_id = self.thread_id

        count = self.count

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        ns = self.ns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
                "count": count,
                "entries": entries,
            }
        )
        if ns is not UNSET:
            field_dict["ns"] = ns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checkpoint_timeline_entry import CheckpointTimelineEntry  # noqa: PLC0415

        d = dict(src_dict)
        thread_id = d.pop("thread_id")

        count = d.pop("count")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = CheckpointTimelineEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        ns = d.pop("ns", UNSET)

        checkpoint_timeline_response = cls(
            thread_id=thread_id,
            count=count,
            entries=entries,
            ns=ns,
        )

        checkpoint_timeline_response.additional_properties = d
        return checkpoint_timeline_response

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
