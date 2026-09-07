from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_session_read_direction import VoiceSessionReadDirection
from ..models.voice_session_read_mode import VoiceSessionReadMode
from ..models.voice_session_read_status import VoiceSessionReadStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_tool_call_read import VoiceToolCallRead
    from ..models.voice_turn_read import VoiceTurnRead


T = TypeVar("T", bound="VoiceSessionRead")


@_attrs_define
class VoiceSessionRead:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        mode (VoiceSessionReadMode):
        source_dept (str):
        to_number (str):
        status (VoiceSessionReadStatus):
        initiated_at (datetime.datetime):
        direction (VoiceSessionReadDirection | Unset):  Default: VoiceSessionReadDirection.OUTBOUND.
        source_agent_id (None | Unset | UUID):
        from_persona_id (None | Unset | UUID):
        from_number (None | str | Unset):
        datasource_id (None | Unset | UUID):
        provider_call_id (None | str | Unset):
        provider (None | str | Unset):
        llm_id (None | Unset | UUID):
        voice_id (None | str | Unset):
        voice_provider (None | str | Unset):
        bridge_session_id (None | str | Unset):
        answered_at (datetime.datetime | None | Unset):
        ended_at (datetime.datetime | None | Unset):
        duration_seconds (int | None | Unset):
        failure_reason (None | str | Unset):
        recording_asset_id (None | Unset | UUID):
        transcript_summary (None | str | Unset):
        transcript_text (None | str | Unset):
        twilio_cost_cents (int | Unset):  Default: 0.
        realtime_cost_cents (int | Unset):  Default: 0.
        tts_cost_cents (int | Unset):  Default: 0.
        turns (list[VoiceTurnRead] | Unset):
        tool_calls (list[VoiceToolCallRead] | Unset):
    """

    id: UUID
    org_id: UUID
    mode: VoiceSessionReadMode
    source_dept: str
    to_number: str
    status: VoiceSessionReadStatus
    initiated_at: datetime.datetime
    direction: VoiceSessionReadDirection | Unset = VoiceSessionReadDirection.OUTBOUND
    source_agent_id: None | Unset | UUID = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    from_number: None | str | Unset = UNSET
    datasource_id: None | Unset | UUID = UNSET
    provider_call_id: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    llm_id: None | Unset | UUID = UNSET
    voice_id: None | str | Unset = UNSET
    voice_provider: None | str | Unset = UNSET
    bridge_session_id: None | str | Unset = UNSET
    answered_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    failure_reason: None | str | Unset = UNSET
    recording_asset_id: None | Unset | UUID = UNSET
    transcript_summary: None | str | Unset = UNSET
    transcript_text: None | str | Unset = UNSET
    twilio_cost_cents: int | Unset = 0
    realtime_cost_cents: int | Unset = 0
    tts_cost_cents: int | Unset = 0
    turns: list[VoiceTurnRead] | Unset = UNSET
    tool_calls: list[VoiceToolCallRead] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        mode = self.mode.value

        source_dept = self.source_dept

        to_number = self.to_number

        status = self.status.value

        initiated_at = self.initiated_at.isoformat()

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        source_agent_id: None | str | Unset
        if isinstance(self.source_agent_id, Unset):
            source_agent_id = UNSET
        elif isinstance(self.source_agent_id, UUID):
            source_agent_id = str(self.source_agent_id)
        else:
            source_agent_id = self.source_agent_id

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        from_number: None | str | Unset
        if isinstance(self.from_number, Unset):
            from_number = UNSET
        else:
            from_number = self.from_number

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        elif isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        provider_call_id: None | str | Unset
        if isinstance(self.provider_call_id, Unset):
            provider_call_id = UNSET
        else:
            provider_call_id = self.provider_call_id

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        llm_id: None | str | Unset
        if isinstance(self.llm_id, Unset):
            llm_id = UNSET
        elif isinstance(self.llm_id, UUID):
            llm_id = str(self.llm_id)
        else:
            llm_id = self.llm_id

        voice_id: None | str | Unset
        if isinstance(self.voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = self.voice_id

        voice_provider: None | str | Unset
        if isinstance(self.voice_provider, Unset):
            voice_provider = UNSET
        else:
            voice_provider = self.voice_provider

        bridge_session_id: None | str | Unset
        if isinstance(self.bridge_session_id, Unset):
            bridge_session_id = UNSET
        else:
            bridge_session_id = self.bridge_session_id

        answered_at: None | str | Unset
        if isinstance(self.answered_at, Unset):
            answered_at = UNSET
        elif isinstance(self.answered_at, datetime.datetime):
            answered_at = self.answered_at.isoformat()
        else:
            answered_at = self.answered_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        recording_asset_id: None | str | Unset
        if isinstance(self.recording_asset_id, Unset):
            recording_asset_id = UNSET
        elif isinstance(self.recording_asset_id, UUID):
            recording_asset_id = str(self.recording_asset_id)
        else:
            recording_asset_id = self.recording_asset_id

        transcript_summary: None | str | Unset
        if isinstance(self.transcript_summary, Unset):
            transcript_summary = UNSET
        else:
            transcript_summary = self.transcript_summary

        transcript_text: None | str | Unset
        if isinstance(self.transcript_text, Unset):
            transcript_text = UNSET
        else:
            transcript_text = self.transcript_text

        twilio_cost_cents = self.twilio_cost_cents

        realtime_cost_cents = self.realtime_cost_cents

        tts_cost_cents = self.tts_cost_cents

        turns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.turns, Unset):
            turns = []
            for turns_item_data in self.turns:
                turns_item = turns_item_data.to_dict()
                turns.append(turns_item)

        tool_calls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data.to_dict()
                tool_calls.append(tool_calls_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "mode": mode,
                "source_dept": source_dept,
                "to_number": to_number,
                "status": status,
                "initiated_at": initiated_at,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if source_agent_id is not UNSET:
            field_dict["source_agent_id"] = source_agent_id
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if from_number is not UNSET:
            field_dict["from_number"] = from_number
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if provider_call_id is not UNSET:
            field_dict["provider_call_id"] = provider_call_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if llm_id is not UNSET:
            field_dict["llm_id"] = llm_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if voice_provider is not UNSET:
            field_dict["voice_provider"] = voice_provider
        if bridge_session_id is not UNSET:
            field_dict["bridge_session_id"] = bridge_session_id
        if answered_at is not UNSET:
            field_dict["answered_at"] = answered_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if recording_asset_id is not UNSET:
            field_dict["recording_asset_id"] = recording_asset_id
        if transcript_summary is not UNSET:
            field_dict["transcript_summary"] = transcript_summary
        if transcript_text is not UNSET:
            field_dict["transcript_text"] = transcript_text
        if twilio_cost_cents is not UNSET:
            field_dict["twilio_cost_cents"] = twilio_cost_cents
        if realtime_cost_cents is not UNSET:
            field_dict["realtime_cost_cents"] = realtime_cost_cents
        if tts_cost_cents is not UNSET:
            field_dict["tts_cost_cents"] = tts_cost_cents
        if turns is not UNSET:
            field_dict["turns"] = turns
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_tool_call_read import VoiceToolCallRead  # noqa: PLC0415
        from ..models.voice_turn_read import VoiceTurnRead  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        mode = VoiceSessionReadMode(d.pop("mode"))

        source_dept = d.pop("source_dept")

        to_number = d.pop("to_number")

        status = VoiceSessionReadStatus(d.pop("status"))

        initiated_at = datetime.datetime.fromisoformat(d.pop("initiated_at"))

        _direction = d.pop("direction", UNSET)
        direction: VoiceSessionReadDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = VoiceSessionReadDirection(_direction)

        def _parse_source_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_agent_id_type_0 = UUID(data)

                return source_agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_agent_id = _parse_source_agent_id(d.pop("source_agent_id", UNSET))

        def _parse_from_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_persona_id_type_0 = UUID(data)

                return from_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        from_persona_id = _parse_from_persona_id(d.pop("from_persona_id", UNSET))

        def _parse_from_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_number = _parse_from_number(d.pop("from_number", UNSET))

        def _parse_datasource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datasource_id_type_0 = UUID(data)

                return datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        datasource_id = _parse_datasource_id(d.pop("datasource_id", UNSET))

        def _parse_provider_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_call_id = _parse_provider_call_id(d.pop("provider_call_id", UNSET))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_llm_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                llm_id_type_0 = UUID(data)

                return llm_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        llm_id = _parse_llm_id(d.pop("llm_id", UNSET))

        def _parse_voice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_id = _parse_voice_id(d.pop("voice_id", UNSET))

        def _parse_voice_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_provider = _parse_voice_provider(d.pop("voice_provider", UNSET))

        def _parse_bridge_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bridge_session_id = _parse_bridge_session_id(d.pop("bridge_session_id", UNSET))

        def _parse_answered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                answered_at_type_0 = datetime.datetime.fromisoformat(data)

                return answered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        answered_at = _parse_answered_at(d.pop("answered_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason", UNSET))

        def _parse_recording_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recording_asset_id_type_0 = UUID(data)

                return recording_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recording_asset_id = _parse_recording_asset_id(d.pop("recording_asset_id", UNSET))

        def _parse_transcript_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_summary = _parse_transcript_summary(d.pop("transcript_summary", UNSET))

        def _parse_transcript_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_text = _parse_transcript_text(d.pop("transcript_text", UNSET))

        twilio_cost_cents = d.pop("twilio_cost_cents", UNSET)

        realtime_cost_cents = d.pop("realtime_cost_cents", UNSET)

        tts_cost_cents = d.pop("tts_cost_cents", UNSET)

        _turns = d.pop("turns", UNSET)
        turns: list[VoiceTurnRead] | Unset = UNSET
        if _turns is not UNSET:
            turns = []
            for turns_item_data in _turns:
                turns_item = VoiceTurnRead.from_dict(turns_item_data)

                turns.append(turns_item)

        _tool_calls = d.pop("tool_calls", UNSET)
        tool_calls: list[VoiceToolCallRead] | Unset = UNSET
        if _tool_calls is not UNSET:
            tool_calls = []
            for tool_calls_item_data in _tool_calls:
                tool_calls_item = VoiceToolCallRead.from_dict(tool_calls_item_data)

                tool_calls.append(tool_calls_item)

        voice_session_read = cls(
            id=id,
            org_id=org_id,
            mode=mode,
            source_dept=source_dept,
            to_number=to_number,
            status=status,
            initiated_at=initiated_at,
            direction=direction,
            source_agent_id=source_agent_id,
            from_persona_id=from_persona_id,
            from_number=from_number,
            datasource_id=datasource_id,
            provider_call_id=provider_call_id,
            provider=provider,
            llm_id=llm_id,
            voice_id=voice_id,
            voice_provider=voice_provider,
            bridge_session_id=bridge_session_id,
            answered_at=answered_at,
            ended_at=ended_at,
            duration_seconds=duration_seconds,
            failure_reason=failure_reason,
            recording_asset_id=recording_asset_id,
            transcript_summary=transcript_summary,
            transcript_text=transcript_text,
            twilio_cost_cents=twilio_cost_cents,
            realtime_cost_cents=realtime_cost_cents,
            tts_cost_cents=tts_cost_cents,
            turns=turns,
            tool_calls=tool_calls,
        )

        voice_session_read.additional_properties = d
        return voice_session_read

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
