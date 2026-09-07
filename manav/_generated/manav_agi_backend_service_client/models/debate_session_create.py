from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debate_session_create_speaker_queue_item import DebateSessionCreateSpeakerQueueItem


T = TypeVar("T", bound="DebateSessionCreate")


@_attrs_define
class DebateSessionCreate:
    """
    Attributes:
        group_id (UUID):
        topic (str):
        org_id (UUID):
        moderator_id (None | Unset | UUID):
        meeting_id (None | Unset | UUID):
        speaker_queue (list[DebateSessionCreateSpeakerQueueItem] | Unset):
        speaking_budget_seconds (int | Unset):  Default: 300.
    """

    group_id: UUID
    topic: str
    org_id: UUID
    moderator_id: None | Unset | UUID = UNSET
    meeting_id: None | Unset | UUID = UNSET
    speaker_queue: list[DebateSessionCreateSpeakerQueueItem] | Unset = UNSET
    speaking_budget_seconds: int | Unset = 300
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = str(self.group_id)

        topic = self.topic

        org_id = str(self.org_id)

        moderator_id: None | str | Unset
        if isinstance(self.moderator_id, Unset):
            moderator_id = UNSET
        elif isinstance(self.moderator_id, UUID):
            moderator_id = str(self.moderator_id)
        else:
            moderator_id = self.moderator_id

        meeting_id: None | str | Unset
        if isinstance(self.meeting_id, Unset):
            meeting_id = UNSET
        elif isinstance(self.meeting_id, UUID):
            meeting_id = str(self.meeting_id)
        else:
            meeting_id = self.meeting_id

        speaker_queue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.speaker_queue, Unset):
            speaker_queue = []
            for speaker_queue_item_data in self.speaker_queue:
                speaker_queue_item = speaker_queue_item_data.to_dict()
                speaker_queue.append(speaker_queue_item)

        speaking_budget_seconds = self.speaking_budget_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_id": group_id,
                "topic": topic,
                "org_id": org_id,
            }
        )
        if moderator_id is not UNSET:
            field_dict["moderator_id"] = moderator_id
        if meeting_id is not UNSET:
            field_dict["meeting_id"] = meeting_id
        if speaker_queue is not UNSET:
            field_dict["speaker_queue"] = speaker_queue
        if speaking_budget_seconds is not UNSET:
            field_dict["speaking_budget_seconds"] = speaking_budget_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debate_session_create_speaker_queue_item import (
            DebateSessionCreateSpeakerQueueItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        group_id = UUID(d.pop("group_id"))

        topic = d.pop("topic")

        org_id = UUID(d.pop("org_id"))

        def _parse_moderator_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                moderator_id_type_0 = UUID(data)

                return moderator_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        moderator_id = _parse_moderator_id(d.pop("moderator_id", UNSET))

        def _parse_meeting_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meeting_id_type_0 = UUID(data)

                return meeting_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        meeting_id = _parse_meeting_id(d.pop("meeting_id", UNSET))

        _speaker_queue = d.pop("speaker_queue", UNSET)
        speaker_queue: list[DebateSessionCreateSpeakerQueueItem] | Unset = UNSET
        if _speaker_queue is not UNSET:
            speaker_queue = []
            for speaker_queue_item_data in _speaker_queue:
                speaker_queue_item = DebateSessionCreateSpeakerQueueItem.from_dict(speaker_queue_item_data)

                speaker_queue.append(speaker_queue_item)

        speaking_budget_seconds = d.pop("speaking_budget_seconds", UNSET)

        debate_session_create = cls(
            group_id=group_id,
            topic=topic,
            org_id=org_id,
            moderator_id=moderator_id,
            meeting_id=meeting_id,
            speaker_queue=speaker_queue,
            speaking_budget_seconds=speaking_budget_seconds,
        )

        debate_session_create.additional_properties = d
        return debate_session_create

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
