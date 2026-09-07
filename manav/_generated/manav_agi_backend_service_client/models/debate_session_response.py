from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debate_session_response_cross_patterns_identified_item import (
        DebateSessionResponseCrossPatternsIdentifiedItem,
    )
    from ..models.debate_session_response_positions_item import DebateSessionResponsePositionsItem
    from ..models.debate_session_response_rebuttals_item import DebateSessionResponseRebuttalsItem
    from ..models.debate_session_response_speaker_queue_item import DebateSessionResponseSpeakerQueueItem
    from ..models.debate_session_response_speakers_completed_in_phase_item import (
        DebateSessionResponseSpeakersCompletedInPhaseItem,
    )


T = TypeVar("T", bound="DebateSessionResponse")


@_attrs_define
class DebateSessionResponse:
    """
    Attributes:
        id (UUID):
        group_id (UUID):
        topic (str):
        current_phase (str):
        speaker_queue (list[DebateSessionResponseSpeakerQueueItem]):
        speakers_completed_in_phase (list[DebateSessionResponseSpeakersCompletedInPhaseItem]):
        speaking_budget_seconds (int):
        positions (list[DebateSessionResponsePositionsItem]):
        rebuttals (list[DebateSessionResponseRebuttalsItem]):
        cross_patterns_identified (list[DebateSessionResponseCrossPatternsIdentifiedItem]):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        meeting_id (None | Unset | UUID):
        phase_started_at (datetime.datetime | None | Unset):
        phase_deadline_at (datetime.datetime | None | Unset):
        current_speaker_id (None | Unset | UUID):
        conclusion (None | str | Unset):
        conclusion_action (None | str | Unset):
        moderator_id (None | Unset | UUID):
        participant_count (int | None | Unset):
        last_message_at (datetime.datetime | None | Unset):
        is_active_now (bool | None | Unset):
    """

    id: UUID
    group_id: UUID
    topic: str
    current_phase: str
    speaker_queue: list[DebateSessionResponseSpeakerQueueItem]
    speakers_completed_in_phase: list[DebateSessionResponseSpeakersCompletedInPhaseItem]
    speaking_budget_seconds: int
    positions: list[DebateSessionResponsePositionsItem]
    rebuttals: list[DebateSessionResponseRebuttalsItem]
    cross_patterns_identified: list[DebateSessionResponseCrossPatternsIdentifiedItem]
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    meeting_id: None | Unset | UUID = UNSET
    phase_started_at: datetime.datetime | None | Unset = UNSET
    phase_deadline_at: datetime.datetime | None | Unset = UNSET
    current_speaker_id: None | Unset | UUID = UNSET
    conclusion: None | str | Unset = UNSET
    conclusion_action: None | str | Unset = UNSET
    moderator_id: None | Unset | UUID = UNSET
    participant_count: int | None | Unset = UNSET
    last_message_at: datetime.datetime | None | Unset = UNSET
    is_active_now: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        group_id = str(self.group_id)

        topic = self.topic

        current_phase = self.current_phase

        speaker_queue = []
        for speaker_queue_item_data in self.speaker_queue:
            speaker_queue_item = speaker_queue_item_data.to_dict()
            speaker_queue.append(speaker_queue_item)

        speakers_completed_in_phase = []
        for speakers_completed_in_phase_item_data in self.speakers_completed_in_phase:
            speakers_completed_in_phase_item = speakers_completed_in_phase_item_data.to_dict()
            speakers_completed_in_phase.append(speakers_completed_in_phase_item)

        speaking_budget_seconds = self.speaking_budget_seconds

        positions = []
        for positions_item_data in self.positions:
            positions_item = positions_item_data.to_dict()
            positions.append(positions_item)

        rebuttals = []
        for rebuttals_item_data in self.rebuttals:
            rebuttals_item = rebuttals_item_data.to_dict()
            rebuttals.append(rebuttals_item)

        cross_patterns_identified = []
        for cross_patterns_identified_item_data in self.cross_patterns_identified:
            cross_patterns_identified_item = cross_patterns_identified_item_data.to_dict()
            cross_patterns_identified.append(cross_patterns_identified_item)

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        meeting_id: None | str | Unset
        if isinstance(self.meeting_id, Unset):
            meeting_id = UNSET
        elif isinstance(self.meeting_id, UUID):
            meeting_id = str(self.meeting_id)
        else:
            meeting_id = self.meeting_id

        phase_started_at: None | str | Unset
        if isinstance(self.phase_started_at, Unset):
            phase_started_at = UNSET
        elif isinstance(self.phase_started_at, datetime.datetime):
            phase_started_at = self.phase_started_at.isoformat()
        else:
            phase_started_at = self.phase_started_at

        phase_deadline_at: None | str | Unset
        if isinstance(self.phase_deadline_at, Unset):
            phase_deadline_at = UNSET
        elif isinstance(self.phase_deadline_at, datetime.datetime):
            phase_deadline_at = self.phase_deadline_at.isoformat()
        else:
            phase_deadline_at = self.phase_deadline_at

        current_speaker_id: None | str | Unset
        if isinstance(self.current_speaker_id, Unset):
            current_speaker_id = UNSET
        elif isinstance(self.current_speaker_id, UUID):
            current_speaker_id = str(self.current_speaker_id)
        else:
            current_speaker_id = self.current_speaker_id

        conclusion: None | str | Unset
        if isinstance(self.conclusion, Unset):
            conclusion = UNSET
        else:
            conclusion = self.conclusion

        conclusion_action: None | str | Unset
        if isinstance(self.conclusion_action, Unset):
            conclusion_action = UNSET
        else:
            conclusion_action = self.conclusion_action

        moderator_id: None | str | Unset
        if isinstance(self.moderator_id, Unset):
            moderator_id = UNSET
        elif isinstance(self.moderator_id, UUID):
            moderator_id = str(self.moderator_id)
        else:
            moderator_id = self.moderator_id

        participant_count: int | None | Unset
        if isinstance(self.participant_count, Unset):
            participant_count = UNSET
        else:
            participant_count = self.participant_count

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        is_active_now: bool | None | Unset
        if isinstance(self.is_active_now, Unset):
            is_active_now = UNSET
        else:
            is_active_now = self.is_active_now

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "topic": topic,
                "current_phase": current_phase,
                "speaker_queue": speaker_queue,
                "speakers_completed_in_phase": speakers_completed_in_phase,
                "speaking_budget_seconds": speaking_budget_seconds,
                "positions": positions,
                "rebuttals": rebuttals,
                "cross_patterns_identified": cross_patterns_identified,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if meeting_id is not UNSET:
            field_dict["meeting_id"] = meeting_id
        if phase_started_at is not UNSET:
            field_dict["phase_started_at"] = phase_started_at
        if phase_deadline_at is not UNSET:
            field_dict["phase_deadline_at"] = phase_deadline_at
        if current_speaker_id is not UNSET:
            field_dict["current_speaker_id"] = current_speaker_id
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if conclusion_action is not UNSET:
            field_dict["conclusion_action"] = conclusion_action
        if moderator_id is not UNSET:
            field_dict["moderator_id"] = moderator_id
        if participant_count is not UNSET:
            field_dict["participant_count"] = participant_count
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at
        if is_active_now is not UNSET:
            field_dict["is_active_now"] = is_active_now

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debate_session_response_cross_patterns_identified_item import (
            DebateSessionResponseCrossPatternsIdentifiedItem,  # noqa: PLC0415
        )
        from ..models.debate_session_response_positions_item import DebateSessionResponsePositionsItem  # noqa: PLC0415
        from ..models.debate_session_response_rebuttals_item import DebateSessionResponseRebuttalsItem  # noqa: PLC0415
        from ..models.debate_session_response_speaker_queue_item import (
            DebateSessionResponseSpeakerQueueItem,  # noqa: PLC0415
        )
        from ..models.debate_session_response_speakers_completed_in_phase_item import (
            DebateSessionResponseSpeakersCompletedInPhaseItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_id = UUID(d.pop("group_id"))

        topic = d.pop("topic")

        current_phase = d.pop("current_phase")

        speaker_queue = []
        _speaker_queue = d.pop("speaker_queue")
        for speaker_queue_item_data in _speaker_queue:
            speaker_queue_item = DebateSessionResponseSpeakerQueueItem.from_dict(speaker_queue_item_data)

            speaker_queue.append(speaker_queue_item)

        speakers_completed_in_phase = []
        _speakers_completed_in_phase = d.pop("speakers_completed_in_phase")
        for speakers_completed_in_phase_item_data in _speakers_completed_in_phase:
            speakers_completed_in_phase_item = DebateSessionResponseSpeakersCompletedInPhaseItem.from_dict(
                speakers_completed_in_phase_item_data
            )

            speakers_completed_in_phase.append(speakers_completed_in_phase_item)

        speaking_budget_seconds = d.pop("speaking_budget_seconds")

        positions = []
        _positions = d.pop("positions")
        for positions_item_data in _positions:
            positions_item = DebateSessionResponsePositionsItem.from_dict(positions_item_data)

            positions.append(positions_item)

        rebuttals = []
        _rebuttals = d.pop("rebuttals")
        for rebuttals_item_data in _rebuttals:
            rebuttals_item = DebateSessionResponseRebuttalsItem.from_dict(rebuttals_item_data)

            rebuttals.append(rebuttals_item)

        cross_patterns_identified = []
        _cross_patterns_identified = d.pop("cross_patterns_identified")
        for cross_patterns_identified_item_data in _cross_patterns_identified:
            cross_patterns_identified_item = DebateSessionResponseCrossPatternsIdentifiedItem.from_dict(
                cross_patterns_identified_item_data
            )

            cross_patterns_identified.append(cross_patterns_identified_item)

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_phase_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                phase_started_at_type_0 = datetime.datetime.fromisoformat(data)

                return phase_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        phase_started_at = _parse_phase_started_at(d.pop("phase_started_at", UNSET))

        def _parse_phase_deadline_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                phase_deadline_at_type_0 = datetime.datetime.fromisoformat(data)

                return phase_deadline_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        phase_deadline_at = _parse_phase_deadline_at(d.pop("phase_deadline_at", UNSET))

        def _parse_current_speaker_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_speaker_id_type_0 = UUID(data)

                return current_speaker_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        current_speaker_id = _parse_current_speaker_id(d.pop("current_speaker_id", UNSET))

        def _parse_conclusion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conclusion = _parse_conclusion(d.pop("conclusion", UNSET))

        def _parse_conclusion_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conclusion_action = _parse_conclusion_action(d.pop("conclusion_action", UNSET))

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

        def _parse_participant_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        participant_count = _parse_participant_count(d.pop("participant_count", UNSET))

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at", UNSET))

        def _parse_is_active_now(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active_now = _parse_is_active_now(d.pop("is_active_now", UNSET))

        debate_session_response = cls(
            id=id,
            group_id=group_id,
            topic=topic,
            current_phase=current_phase,
            speaker_queue=speaker_queue,
            speakers_completed_in_phase=speakers_completed_in_phase,
            speaking_budget_seconds=speaking_budget_seconds,
            positions=positions,
            rebuttals=rebuttals,
            cross_patterns_identified=cross_patterns_identified,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            meeting_id=meeting_id,
            phase_started_at=phase_started_at,
            phase_deadline_at=phase_deadline_at,
            current_speaker_id=current_speaker_id,
            conclusion=conclusion,
            conclusion_action=conclusion_action,
            moderator_id=moderator_id,
            participant_count=participant_count,
            last_message_at=last_message_at,
            is_active_now=is_active_now,
        )

        debate_session_response.additional_properties = d
        return debate_session_response

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
