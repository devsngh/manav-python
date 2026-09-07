from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.score_event_response import ScoreEventResponse


T = TypeVar("T", bound="ScoreEventListResponse")


@_attrs_define
class ScoreEventListResponse:
    """
    Attributes:
        events (list[ScoreEventResponse]):
        total (int):
        page (int):
        page_size (int):
        has_more (bool):
    """

    events: list[ScoreEventResponse]
    total: int
    page: int
    page_size: int
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        total = self.total

        page = self.page

        page_size = self.page_size

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "total": total,
                "page": page,
                "page_size": page_size,
                "has_more": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.score_event_response import ScoreEventResponse  # noqa: PLC0415

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = ScoreEventResponse.from_dict(events_item_data)

            events.append(events_item)

        total = d.pop("total")

        page = d.pop("page")

        page_size = d.pop("page_size")

        has_more = d.pop("has_more")

        score_event_list_response = cls(
            events=events,
            total=total,
            page=page,
            page_size=page_size,
            has_more=has_more,
        )

        score_event_list_response.additional_properties = d
        return score_event_list_response

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
