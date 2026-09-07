from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bot_score_response import BotScoreResponse
    from ..models.score_event_response import ScoreEventResponse


T = TypeVar("T", bound="BotScoreWithEventsResponse")


@_attrs_define
class BotScoreWithEventsResponse:
    """Score + recent events. Used by `read_bot_score` MCP tool.

    Attributes:
        score (BotScoreResponse): Single bot's current score + thresholds.
        recent_events (list[ScoreEventResponse]):
    """

    score: BotScoreResponse
    recent_events: list[ScoreEventResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score.to_dict()

        recent_events = []
        for recent_events_item_data in self.recent_events:
            recent_events_item = recent_events_item_data.to_dict()
            recent_events.append(recent_events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "score": score,
                "recent_events": recent_events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_score_response import BotScoreResponse  # noqa: PLC0415
        from ..models.score_event_response import ScoreEventResponse  # noqa: PLC0415

        d = dict(src_dict)
        score = BotScoreResponse.from_dict(d.pop("score"))

        recent_events = []
        _recent_events = d.pop("recent_events")
        for recent_events_item_data in _recent_events:
            recent_events_item = ScoreEventResponse.from_dict(recent_events_item_data)

            recent_events.append(recent_events_item)

        bot_score_with_events_response = cls(
            score=score,
            recent_events=recent_events,
        )

        bot_score_with_events_response.additional_properties = d
        return bot_score_with_events_response

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
