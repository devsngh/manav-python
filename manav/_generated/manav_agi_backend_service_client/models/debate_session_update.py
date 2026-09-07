from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debate_session_update_cross_patterns_identified_type_0_item import (
        DebateSessionUpdateCrossPatternsIdentifiedType0Item,
    )
    from ..models.debate_session_update_positions_type_0_item import DebateSessionUpdatePositionsType0Item
    from ..models.debate_session_update_rebuttals_type_0_item import DebateSessionUpdateRebuttalsType0Item
    from ..models.debate_session_update_speaker_queue_type_0_item import DebateSessionUpdateSpeakerQueueType0Item
    from ..models.debate_session_update_speakers_completed_in_phase_type_0_item import (
        DebateSessionUpdateSpeakersCompletedInPhaseType0Item,
    )


T = TypeVar("T", bound="DebateSessionUpdate")


@_attrs_define
class DebateSessionUpdate:
    """Patch — phase advance, speaker swap, positions/rebuttals append, etc.

    Attributes:
        current_phase (None | str | Unset):
        phase_started_at (datetime.datetime | None | Unset):
        phase_deadline_at (datetime.datetime | None | Unset):
        current_speaker_id (None | Unset | UUID):
        speaker_queue (list[DebateSessionUpdateSpeakerQueueType0Item] | None | Unset):
        speakers_completed_in_phase (list[DebateSessionUpdateSpeakersCompletedInPhaseType0Item] | None | Unset):
        speaking_budget_seconds (int | None | Unset):
        positions (list[DebateSessionUpdatePositionsType0Item] | None | Unset):
        rebuttals (list[DebateSessionUpdateRebuttalsType0Item] | None | Unset):
        cross_patterns_identified (list[DebateSessionUpdateCrossPatternsIdentifiedType0Item] | None | Unset):
        moderator_id (None | Unset | UUID):
        conclusion (None | str | Unset):
        conclusion_action (None | str | Unset):
    """

    current_phase: None | str | Unset = UNSET
    phase_started_at: datetime.datetime | None | Unset = UNSET
    phase_deadline_at: datetime.datetime | None | Unset = UNSET
    current_speaker_id: None | Unset | UUID = UNSET
    speaker_queue: list[DebateSessionUpdateSpeakerQueueType0Item] | None | Unset = UNSET
    speakers_completed_in_phase: list[DebateSessionUpdateSpeakersCompletedInPhaseType0Item] | None | Unset = UNSET
    speaking_budget_seconds: int | None | Unset = UNSET
    positions: list[DebateSessionUpdatePositionsType0Item] | None | Unset = UNSET
    rebuttals: list[DebateSessionUpdateRebuttalsType0Item] | None | Unset = UNSET
    cross_patterns_identified: list[DebateSessionUpdateCrossPatternsIdentifiedType0Item] | None | Unset = UNSET
    moderator_id: None | Unset | UUID = UNSET
    conclusion: None | str | Unset = UNSET
    conclusion_action: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_phase: None | str | Unset
        if isinstance(self.current_phase, Unset):
            current_phase = UNSET
        else:
            current_phase = self.current_phase

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

        speaker_queue: list[dict[str, Any]] | None | Unset
        if isinstance(self.speaker_queue, Unset):
            speaker_queue = UNSET
        elif isinstance(self.speaker_queue, list):
            speaker_queue = []
            for speaker_queue_type_0_item_data in self.speaker_queue:
                speaker_queue_type_0_item = speaker_queue_type_0_item_data.to_dict()
                speaker_queue.append(speaker_queue_type_0_item)

        else:
            speaker_queue = self.speaker_queue

        speakers_completed_in_phase: list[dict[str, Any]] | None | Unset
        if isinstance(self.speakers_completed_in_phase, Unset):
            speakers_completed_in_phase = UNSET
        elif isinstance(self.speakers_completed_in_phase, list):
            speakers_completed_in_phase = []
            for speakers_completed_in_phase_type_0_item_data in self.speakers_completed_in_phase:
                speakers_completed_in_phase_type_0_item = speakers_completed_in_phase_type_0_item_data.to_dict()
                speakers_completed_in_phase.append(speakers_completed_in_phase_type_0_item)

        else:
            speakers_completed_in_phase = self.speakers_completed_in_phase

        speaking_budget_seconds: int | None | Unset
        if isinstance(self.speaking_budget_seconds, Unset):
            speaking_budget_seconds = UNSET
        else:
            speaking_budget_seconds = self.speaking_budget_seconds

        positions: list[dict[str, Any]] | None | Unset
        if isinstance(self.positions, Unset):
            positions = UNSET
        elif isinstance(self.positions, list):
            positions = []
            for positions_type_0_item_data in self.positions:
                positions_type_0_item = positions_type_0_item_data.to_dict()
                positions.append(positions_type_0_item)

        else:
            positions = self.positions

        rebuttals: list[dict[str, Any]] | None | Unset
        if isinstance(self.rebuttals, Unset):
            rebuttals = UNSET
        elif isinstance(self.rebuttals, list):
            rebuttals = []
            for rebuttals_type_0_item_data in self.rebuttals:
                rebuttals_type_0_item = rebuttals_type_0_item_data.to_dict()
                rebuttals.append(rebuttals_type_0_item)

        else:
            rebuttals = self.rebuttals

        cross_patterns_identified: list[dict[str, Any]] | None | Unset
        if isinstance(self.cross_patterns_identified, Unset):
            cross_patterns_identified = UNSET
        elif isinstance(self.cross_patterns_identified, list):
            cross_patterns_identified = []
            for cross_patterns_identified_type_0_item_data in self.cross_patterns_identified:
                cross_patterns_identified_type_0_item = cross_patterns_identified_type_0_item_data.to_dict()
                cross_patterns_identified.append(cross_patterns_identified_type_0_item)

        else:
            cross_patterns_identified = self.cross_patterns_identified

        moderator_id: None | str | Unset
        if isinstance(self.moderator_id, Unset):
            moderator_id = UNSET
        elif isinstance(self.moderator_id, UUID):
            moderator_id = str(self.moderator_id)
        else:
            moderator_id = self.moderator_id

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_phase is not UNSET:
            field_dict["current_phase"] = current_phase
        if phase_started_at is not UNSET:
            field_dict["phase_started_at"] = phase_started_at
        if phase_deadline_at is not UNSET:
            field_dict["phase_deadline_at"] = phase_deadline_at
        if current_speaker_id is not UNSET:
            field_dict["current_speaker_id"] = current_speaker_id
        if speaker_queue is not UNSET:
            field_dict["speaker_queue"] = speaker_queue
        if speakers_completed_in_phase is not UNSET:
            field_dict["speakers_completed_in_phase"] = speakers_completed_in_phase
        if speaking_budget_seconds is not UNSET:
            field_dict["speaking_budget_seconds"] = speaking_budget_seconds
        if positions is not UNSET:
            field_dict["positions"] = positions
        if rebuttals is not UNSET:
            field_dict["rebuttals"] = rebuttals
        if cross_patterns_identified is not UNSET:
            field_dict["cross_patterns_identified"] = cross_patterns_identified
        if moderator_id is not UNSET:
            field_dict["moderator_id"] = moderator_id
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if conclusion_action is not UNSET:
            field_dict["conclusion_action"] = conclusion_action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debate_session_update_cross_patterns_identified_type_0_item import (
            DebateSessionUpdateCrossPatternsIdentifiedType0Item,  # noqa: PLC0415
        )
        from ..models.debate_session_update_positions_type_0_item import (
            DebateSessionUpdatePositionsType0Item,  # noqa: PLC0415
        )
        from ..models.debate_session_update_rebuttals_type_0_item import (
            DebateSessionUpdateRebuttalsType0Item,  # noqa: PLC0415
        )
        from ..models.debate_session_update_speaker_queue_type_0_item import (
            DebateSessionUpdateSpeakerQueueType0Item,  # noqa: PLC0415
        )
        from ..models.debate_session_update_speakers_completed_in_phase_type_0_item import (
            DebateSessionUpdateSpeakersCompletedInPhaseType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_current_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_phase = _parse_current_phase(d.pop("current_phase", UNSET))

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

        def _parse_speaker_queue(data: object) -> list[DebateSessionUpdateSpeakerQueueType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                speaker_queue_type_0 = []
                _speaker_queue_type_0 = data
                for speaker_queue_type_0_item_data in _speaker_queue_type_0:
                    speaker_queue_type_0_item = DebateSessionUpdateSpeakerQueueType0Item.from_dict(
                        speaker_queue_type_0_item_data
                    )

                    speaker_queue_type_0.append(speaker_queue_type_0_item)

                return speaker_queue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DebateSessionUpdateSpeakerQueueType0Item] | None | Unset, data)

        speaker_queue = _parse_speaker_queue(d.pop("speaker_queue", UNSET))

        def _parse_speakers_completed_in_phase(
            data: object,
        ) -> list[DebateSessionUpdateSpeakersCompletedInPhaseType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                speakers_completed_in_phase_type_0 = []
                _speakers_completed_in_phase_type_0 = data
                for speakers_completed_in_phase_type_0_item_data in _speakers_completed_in_phase_type_0:
                    speakers_completed_in_phase_type_0_item = (
                        DebateSessionUpdateSpeakersCompletedInPhaseType0Item.from_dict(
                            speakers_completed_in_phase_type_0_item_data
                        )
                    )

                    speakers_completed_in_phase_type_0.append(speakers_completed_in_phase_type_0_item)

                return speakers_completed_in_phase_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DebateSessionUpdateSpeakersCompletedInPhaseType0Item] | None | Unset, data)

        speakers_completed_in_phase = _parse_speakers_completed_in_phase(d.pop("speakers_completed_in_phase", UNSET))

        def _parse_speaking_budget_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        speaking_budget_seconds = _parse_speaking_budget_seconds(d.pop("speaking_budget_seconds", UNSET))

        def _parse_positions(data: object) -> list[DebateSessionUpdatePositionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positions_type_0 = []
                _positions_type_0 = data
                for positions_type_0_item_data in _positions_type_0:
                    positions_type_0_item = DebateSessionUpdatePositionsType0Item.from_dict(positions_type_0_item_data)

                    positions_type_0.append(positions_type_0_item)

                return positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DebateSessionUpdatePositionsType0Item] | None | Unset, data)

        positions = _parse_positions(d.pop("positions", UNSET))

        def _parse_rebuttals(data: object) -> list[DebateSessionUpdateRebuttalsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rebuttals_type_0 = []
                _rebuttals_type_0 = data
                for rebuttals_type_0_item_data in _rebuttals_type_0:
                    rebuttals_type_0_item = DebateSessionUpdateRebuttalsType0Item.from_dict(rebuttals_type_0_item_data)

                    rebuttals_type_0.append(rebuttals_type_0_item)

                return rebuttals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DebateSessionUpdateRebuttalsType0Item] | None | Unset, data)

        rebuttals = _parse_rebuttals(d.pop("rebuttals", UNSET))

        def _parse_cross_patterns_identified(
            data: object,
        ) -> list[DebateSessionUpdateCrossPatternsIdentifiedType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cross_patterns_identified_type_0 = []
                _cross_patterns_identified_type_0 = data
                for cross_patterns_identified_type_0_item_data in _cross_patterns_identified_type_0:
                    cross_patterns_identified_type_0_item = (
                        DebateSessionUpdateCrossPatternsIdentifiedType0Item.from_dict(
                            cross_patterns_identified_type_0_item_data
                        )
                    )

                    cross_patterns_identified_type_0.append(cross_patterns_identified_type_0_item)

                return cross_patterns_identified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DebateSessionUpdateCrossPatternsIdentifiedType0Item] | None | Unset, data)

        cross_patterns_identified = _parse_cross_patterns_identified(d.pop("cross_patterns_identified", UNSET))

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

        debate_session_update = cls(
            current_phase=current_phase,
            phase_started_at=phase_started_at,
            phase_deadline_at=phase_deadline_at,
            current_speaker_id=current_speaker_id,
            speaker_queue=speaker_queue,
            speakers_completed_in_phase=speakers_completed_in_phase,
            speaking_budget_seconds=speaking_budget_seconds,
            positions=positions,
            rebuttals=rebuttals,
            cross_patterns_identified=cross_patterns_identified,
            moderator_id=moderator_id,
            conclusion=conclusion,
            conclusion_action=conclusion_action,
        )

        debate_session_update.additional_properties = d
        return debate_session_update

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
