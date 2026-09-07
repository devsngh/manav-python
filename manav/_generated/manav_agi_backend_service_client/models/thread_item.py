from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.thread_participant import ThreadParticipant


T = TypeVar("T", bound="ThreadItem")


@_attrs_define
class ThreadItem:
    """One row in the Pane-1 thread list.

    Attributes:
        source_type (str):
        source_id (UUID):
        title (str):
        participants (list[ThreadParticipant] | Unset):
        turn_count (int | Unset):  Default: 0.
        span_count (int | Unset):  Default: 0.
        error_count (int | Unset):  Default: 0.
        last_activity (datetime.datetime | None | Unset):
        cumulative_cost_usd (float | Unset):  Default: 0.0.
        cumulative_tokens (int | Unset):  Default: 0.
        status (str | Unset):  Default: 'ok'.
    """

    source_type: str
    source_id: UUID
    title: str
    participants: list[ThreadParticipant] | Unset = UNSET
    turn_count: int | Unset = 0
    span_count: int | Unset = 0
    error_count: int | Unset = 0
    last_activity: datetime.datetime | None | Unset = UNSET
    cumulative_cost_usd: float | Unset = 0.0
    cumulative_tokens: int | Unset = 0
    status: str | Unset = "ok"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        source_id = str(self.source_id)

        title = self.title

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        turn_count = self.turn_count

        span_count = self.span_count

        error_count = self.error_count

        last_activity: None | str | Unset
        if isinstance(self.last_activity, Unset):
            last_activity = UNSET
        elif isinstance(self.last_activity, datetime.datetime):
            last_activity = self.last_activity.isoformat()
        else:
            last_activity = self.last_activity

        cumulative_cost_usd = self.cumulative_cost_usd

        cumulative_tokens = self.cumulative_tokens

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
                "source_id": source_id,
                "title": title,
            }
        )
        if participants is not UNSET:
            field_dict["participants"] = participants
        if turn_count is not UNSET:
            field_dict["turn_count"] = turn_count
        if span_count is not UNSET:
            field_dict["span_count"] = span_count
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if cumulative_cost_usd is not UNSET:
            field_dict["cumulative_cost_usd"] = cumulative_cost_usd
        if cumulative_tokens is not UNSET:
            field_dict["cumulative_tokens"] = cumulative_tokens
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.thread_participant import ThreadParticipant  # noqa: PLC0415

        d = dict(src_dict)
        source_type = d.pop("source_type")

        source_id = UUID(d.pop("source_id"))

        title = d.pop("title")

        _participants = d.pop("participants", UNSET)
        participants: list[ThreadParticipant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = ThreadParticipant.from_dict(participants_item_data)

                participants.append(participants_item)

        turn_count = d.pop("turn_count", UNSET)

        span_count = d.pop("span_count", UNSET)

        error_count = d.pop("error_count", UNSET)

        def _parse_last_activity(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_activity_type_0 = datetime.datetime.fromisoformat(data)

                return last_activity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_activity = _parse_last_activity(d.pop("last_activity", UNSET))

        cumulative_cost_usd = d.pop("cumulative_cost_usd", UNSET)

        cumulative_tokens = d.pop("cumulative_tokens", UNSET)

        status = d.pop("status", UNSET)

        thread_item = cls(
            source_type=source_type,
            source_id=source_id,
            title=title,
            participants=participants,
            turn_count=turn_count,
            span_count=span_count,
            error_count=error_count,
            last_activity=last_activity,
            cumulative_cost_usd=cumulative_cost_usd,
            cumulative_tokens=cumulative_tokens,
            status=status,
        )

        thread_item.additional_properties = d
        return thread_item

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
