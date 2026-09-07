from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateConversation")


@_attrs_define
class CreateConversation:
    """Request to create a timer-based bot conversation (group or 1:1).

    Attributes:
        title (str):
        purpose (str):
        participant_bot_ids (list[UUID]):
        channel_type (str | Unset):  Default: 'bot_group'.
        channel_id (None | Unset | UUID):
        duration_minutes (int | Unset):  Default: 10.
        check_interval_seconds (int | Unset):  Default: 60.
    """

    title: str
    purpose: str
    participant_bot_ids: list[UUID]
    channel_type: str | Unset = "bot_group"
    channel_id: None | Unset | UUID = UNSET
    duration_minutes: int | Unset = 10
    check_interval_seconds: int | Unset = 60
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        purpose = self.purpose

        participant_bot_ids = []
        for participant_bot_ids_item_data in self.participant_bot_ids:
            participant_bot_ids_item = str(participant_bot_ids_item_data)
            participant_bot_ids.append(participant_bot_ids_item)

        channel_type = self.channel_type

        channel_id: None | str | Unset
        if isinstance(self.channel_id, Unset):
            channel_id = UNSET
        elif isinstance(self.channel_id, UUID):
            channel_id = str(self.channel_id)
        else:
            channel_id = self.channel_id

        duration_minutes = self.duration_minutes

        check_interval_seconds = self.check_interval_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "purpose": purpose,
                "participant_bot_ids": participant_bot_ids,
            }
        )
        if channel_type is not UNSET:
            field_dict["channel_type"] = channel_type
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        purpose = d.pop("purpose")

        participant_bot_ids = []
        _participant_bot_ids = d.pop("participant_bot_ids")
        for participant_bot_ids_item_data in _participant_bot_ids:
            participant_bot_ids_item = UUID(participant_bot_ids_item_data)

            participant_bot_ids.append(participant_bot_ids_item)

        channel_type = d.pop("channel_type", UNSET)

        def _parse_channel_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                channel_id_type_0 = UUID(data)

                return channel_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        channel_id = _parse_channel_id(d.pop("channel_id", UNSET))

        duration_minutes = d.pop("duration_minutes", UNSET)

        check_interval_seconds = d.pop("check_interval_seconds", UNSET)

        create_conversation = cls(
            title=title,
            purpose=purpose,
            participant_bot_ids=participant_bot_ids,
            channel_type=channel_type,
            channel_id=channel_id,
            duration_minutes=duration_minutes,
            check_interval_seconds=check_interval_seconds,
        )

        create_conversation.additional_properties = d
        return create_conversation

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
