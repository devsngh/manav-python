from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.live_event import LiveEvent


T = TypeVar("T", bound="LiveFeedResponse")


@_attrs_define
class LiveFeedResponse:
    """
    Attributes:
        events (list[LiveEvent]):
        since (datetime.datetime | None | Unset):
        until (datetime.datetime | None | Unset):
        is_live (bool | Unset):  Default: True.
    """

    events: list[LiveEvent]
    since: datetime.datetime | None | Unset = UNSET
    until: datetime.datetime | None | Unset = UNSET
    is_live: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        since: None | str | Unset
        if isinstance(self.since, Unset):
            since = UNSET
        elif isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        until: None | str | Unset
        if isinstance(self.until, Unset):
            until = UNSET
        elif isinstance(self.until, datetime.datetime):
            until = self.until.isoformat()
        else:
            until = self.until

        is_live = self.is_live

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )
        if since is not UNSET:
            field_dict["since"] = since
        if until is not UNSET:
            field_dict["until"] = until
        if is_live is not UNSET:
            field_dict["is_live"] = is_live

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_event import LiveEvent  # noqa: PLC0415

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = LiveEvent.from_dict(events_item_data)

            events.append(events_item)

        def _parse_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = datetime.datetime.fromisoformat(data)

                return since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        since = _parse_since(d.pop("since", UNSET))

        def _parse_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                until_type_0 = datetime.datetime.fromisoformat(data)

                return until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        until = _parse_until(d.pop("until", UNSET))

        is_live = d.pop("is_live", UNSET)

        live_feed_response = cls(
            events=events,
            since=since,
            until=until,
            is_live=is_live,
        )

        live_feed_response.additional_properties = d
        return live_feed_response

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
