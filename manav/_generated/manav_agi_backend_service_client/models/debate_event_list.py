from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debate_event import DebateEvent


T = TypeVar("T", bound="DebateEventList")


@_attrs_define
class DebateEventList:
    """
    Attributes:
        debate_id (UUID):
        group_id (UUID):
        events (list[DebateEvent]):
        total (int):
        started_at (datetime.datetime):
        concluded_at (datetime.datetime | None | Unset):
    """

    debate_id: UUID
    group_id: UUID
    events: list[DebateEvent]
    total: int
    started_at: datetime.datetime
    concluded_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        debate_id = str(self.debate_id)

        group_id = str(self.group_id)

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        total = self.total

        started_at = self.started_at.isoformat()

        concluded_at: None | str | Unset
        if isinstance(self.concluded_at, Unset):
            concluded_at = UNSET
        elif isinstance(self.concluded_at, datetime.datetime):
            concluded_at = self.concluded_at.isoformat()
        else:
            concluded_at = self.concluded_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "debate_id": debate_id,
                "group_id": group_id,
                "events": events,
                "total": total,
                "started_at": started_at,
            }
        )
        if concluded_at is not UNSET:
            field_dict["concluded_at"] = concluded_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debate_event import DebateEvent  # noqa: PLC0415

        d = dict(src_dict)
        debate_id = UUID(d.pop("debate_id"))

        group_id = UUID(d.pop("group_id"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = DebateEvent.from_dict(events_item_data)

            events.append(events_item)

        total = d.pop("total")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        def _parse_concluded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                concluded_at_type_0 = datetime.datetime.fromisoformat(data)

                return concluded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        concluded_at = _parse_concluded_at(d.pop("concluded_at", UNSET))

        debate_event_list = cls(
            debate_id=debate_id,
            group_id=group_id,
            events=events,
            total=total,
            started_at=started_at,
            concluded_at=concluded_at,
        )

        debate_event_list.additional_properties = d
        return debate_event_list

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
