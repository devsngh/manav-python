from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_session_status_update_status import VoiceSessionStatusUpdateStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceSessionStatusUpdate")


@_attrs_define
class VoiceSessionStatusUpdate:
    """Body sent by Twilio status webhook or the bridge service.

    Attributes:
        status (VoiceSessionStatusUpdateStatus):
        failure_reason (None | str | Unset):
        duration_seconds (int | None | Unset):
        recording_asset_id (None | Unset | UUID):
        transcript_text (None | str | Unset):
        transcript_summary (None | str | Unset):
        twilio_cost_cents (int | None | Unset):
        realtime_cost_cents (int | None | Unset):
    """

    status: VoiceSessionStatusUpdateStatus
    failure_reason: None | str | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    recording_asset_id: None | Unset | UUID = UNSET
    transcript_text: None | str | Unset = UNSET
    transcript_summary: None | str | Unset = UNSET
    twilio_cost_cents: int | None | Unset = UNSET
    realtime_cost_cents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        failure_reason: None | str | Unset
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        recording_asset_id: None | str | Unset
        if isinstance(self.recording_asset_id, Unset):
            recording_asset_id = UNSET
        elif isinstance(self.recording_asset_id, UUID):
            recording_asset_id = str(self.recording_asset_id)
        else:
            recording_asset_id = self.recording_asset_id

        transcript_text: None | str | Unset
        if isinstance(self.transcript_text, Unset):
            transcript_text = UNSET
        else:
            transcript_text = self.transcript_text

        transcript_summary: None | str | Unset
        if isinstance(self.transcript_summary, Unset):
            transcript_summary = UNSET
        else:
            transcript_summary = self.transcript_summary

        twilio_cost_cents: int | None | Unset
        if isinstance(self.twilio_cost_cents, Unset):
            twilio_cost_cents = UNSET
        else:
            twilio_cost_cents = self.twilio_cost_cents

        realtime_cost_cents: int | None | Unset
        if isinstance(self.realtime_cost_cents, Unset):
            realtime_cost_cents = UNSET
        else:
            realtime_cost_cents = self.realtime_cost_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if recording_asset_id is not UNSET:
            field_dict["recording_asset_id"] = recording_asset_id
        if transcript_text is not UNSET:
            field_dict["transcript_text"] = transcript_text
        if transcript_summary is not UNSET:
            field_dict["transcript_summary"] = transcript_summary
        if twilio_cost_cents is not UNSET:
            field_dict["twilio_cost_cents"] = twilio_cost_cents
        if realtime_cost_cents is not UNSET:
            field_dict["realtime_cost_cents"] = realtime_cost_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = VoiceSessionStatusUpdateStatus(d.pop("status"))

        def _parse_failure_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_reason = _parse_failure_reason(d.pop("failure_reason", UNSET))

        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

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

        def _parse_transcript_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_text = _parse_transcript_text(d.pop("transcript_text", UNSET))

        def _parse_transcript_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transcript_summary = _parse_transcript_summary(d.pop("transcript_summary", UNSET))

        def _parse_twilio_cost_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        twilio_cost_cents = _parse_twilio_cost_cents(d.pop("twilio_cost_cents", UNSET))

        def _parse_realtime_cost_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        realtime_cost_cents = _parse_realtime_cost_cents(d.pop("realtime_cost_cents", UNSET))

        voice_session_status_update = cls(
            status=status,
            failure_reason=failure_reason,
            duration_seconds=duration_seconds,
            recording_asset_id=recording_asset_id,
            transcript_text=transcript_text,
            transcript_summary=transcript_summary,
            twilio_cost_cents=twilio_cost_cents,
            realtime_cost_cents=realtime_cost_cents,
        )

        voice_session_status_update.additional_properties = d
        return voice_session_status_update

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
