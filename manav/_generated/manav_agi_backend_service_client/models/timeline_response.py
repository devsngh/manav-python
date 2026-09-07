from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subject_type import SubjectType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.canonical_event import CanonicalEvent
    from ..models.timeline_response_by_source import TimelineResponseBySource


T = TypeVar("T", bound="TimelineResponse")


@_attrs_define
class TimelineResponse:
    """
    Attributes:
        subject_type (SubjectType): What kind of thing we're pulling a timeline FOR.
        subject_id (UUID):
        window_start (datetime.datetime):
        window_end (datetime.datetime):
        total_events (int):
        events (list[CanonicalEvent]):
        truncated (bool | Unset): True if hit the limit — caller should narrow window or paginate. Default: False.
        by_source (TimelineResponseBySource | Unset): Count of events per source track — {'A': 234, 'C': 12}.
    """

    subject_type: SubjectType
    subject_id: UUID
    window_start: datetime.datetime
    window_end: datetime.datetime
    total_events: int
    events: list[CanonicalEvent]
    truncated: bool | Unset = False
    by_source: TimelineResponseBySource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_type = self.subject_type.value

        subject_id = str(self.subject_id)

        window_start = self.window_start.isoformat()

        window_end = self.window_end.isoformat()

        total_events = self.total_events

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        truncated = self.truncated

        by_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_source, Unset):
            by_source = self.by_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject_type": subject_type,
                "subject_id": subject_id,
                "window_start": window_start,
                "window_end": window_end,
                "total_events": total_events,
                "events": events,
            }
        )
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if by_source is not UNSET:
            field_dict["by_source"] = by_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.canonical_event import CanonicalEvent  # noqa: PLC0415
        from ..models.timeline_response_by_source import TimelineResponseBySource  # noqa: PLC0415

        d = dict(src_dict)
        subject_type = SubjectType(d.pop("subject_type"))

        subject_id = UUID(d.pop("subject_id"))

        window_start = datetime.datetime.fromisoformat(d.pop("window_start"))

        window_end = datetime.datetime.fromisoformat(d.pop("window_end"))

        total_events = d.pop("total_events")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = CanonicalEvent.from_dict(events_item_data)

            events.append(events_item)

        truncated = d.pop("truncated", UNSET)

        _by_source = d.pop("by_source", UNSET)
        by_source: TimelineResponseBySource | Unset
        if isinstance(_by_source, Unset):
            by_source = UNSET
        else:
            by_source = TimelineResponseBySource.from_dict(_by_source)

        timeline_response = cls(
            subject_type=subject_type,
            subject_id=subject_id,
            window_start=window_start,
            window_end=window_end,
            total_events=total_events,
            events=events,
            truncated=truncated,
            by_source=by_source,
        )

        timeline_response.additional_properties = d
        return timeline_response

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
