from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_session_start_request_mode import VoiceSessionStartRequestMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_session_start_request_extra_context_type_0 import VoiceSessionStartRequestExtraContextType0


T = TypeVar("T", bound="VoiceSessionStartRequest")


@_attrs_define
class VoiceSessionStartRequest:
    """Body for POST /api/comms/voice/sessions.

    Attributes:
        to (str): E.164 phone number to call
        mode (VoiceSessionStartRequestMode | Unset):  Default: VoiceSessionStartRequestMode.LIVE_REALTIME.
        agent_id (None | Unset | UUID):
        llm_id (None | Unset | UUID):
        from_persona_id (None | Unset | UUID):
        voice_id (None | str | Unset):
        voice_provider (str | Unset):  Default: 'openai_realtime'.
        opening_line (None | str | Unset):
        max_duration_seconds (int | Unset):  Default: 600.
        record_call (bool | Unset):  Default: True.
        from_number (None | str | Unset):
        source_dept (str | Unset):  Default: 'generic'.
        source_agent_id (None | Unset | UUID):
        source_task_id (None | Unset | UUID):
        extra_context (None | Unset | VoiceSessionStartRequestExtraContextType0):
        explicit_datasource_id (None | Unset | UUID):
    """

    to: str
    mode: VoiceSessionStartRequestMode | Unset = VoiceSessionStartRequestMode.LIVE_REALTIME
    agent_id: None | Unset | UUID = UNSET
    llm_id: None | Unset | UUID = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    voice_id: None | str | Unset = UNSET
    voice_provider: str | Unset = "openai_realtime"
    opening_line: None | str | Unset = UNSET
    max_duration_seconds: int | Unset = 600
    record_call: bool | Unset = True
    from_number: None | str | Unset = UNSET
    source_dept: str | Unset = "generic"
    source_agent_id: None | Unset | UUID = UNSET
    source_task_id: None | Unset | UUID = UNSET
    extra_context: None | Unset | VoiceSessionStartRequestExtraContextType0 = UNSET
    explicit_datasource_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.voice_session_start_request_extra_context_type_0 import (
            VoiceSessionStartRequestExtraContextType0,  # noqa: PLC0415
        )

        to = self.to

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        agent_id: None | str | Unset
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        elif isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        llm_id: None | str | Unset
        if isinstance(self.llm_id, Unset):
            llm_id = UNSET
        elif isinstance(self.llm_id, UUID):
            llm_id = str(self.llm_id)
        else:
            llm_id = self.llm_id

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        voice_id: None | str | Unset
        if isinstance(self.voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = self.voice_id

        voice_provider = self.voice_provider

        opening_line: None | str | Unset
        if isinstance(self.opening_line, Unset):
            opening_line = UNSET
        else:
            opening_line = self.opening_line

        max_duration_seconds = self.max_duration_seconds

        record_call = self.record_call

        from_number: None | str | Unset
        if isinstance(self.from_number, Unset):
            from_number = UNSET
        else:
            from_number = self.from_number

        source_dept = self.source_dept

        source_agent_id: None | str | Unset
        if isinstance(self.source_agent_id, Unset):
            source_agent_id = UNSET
        elif isinstance(self.source_agent_id, UUID):
            source_agent_id = str(self.source_agent_id)
        else:
            source_agent_id = self.source_agent_id

        source_task_id: None | str | Unset
        if isinstance(self.source_task_id, Unset):
            source_task_id = UNSET
        elif isinstance(self.source_task_id, UUID):
            source_task_id = str(self.source_task_id)
        else:
            source_task_id = self.source_task_id

        extra_context: dict[str, Any] | None | Unset
        if isinstance(self.extra_context, Unset):
            extra_context = UNSET
        elif isinstance(self.extra_context, VoiceSessionStartRequestExtraContextType0):
            extra_context = self.extra_context.to_dict()
        else:
            extra_context = self.extra_context

        explicit_datasource_id: None | str | Unset
        if isinstance(self.explicit_datasource_id, Unset):
            explicit_datasource_id = UNSET
        elif isinstance(self.explicit_datasource_id, UUID):
            explicit_datasource_id = str(self.explicit_datasource_id)
        else:
            explicit_datasource_id = self.explicit_datasource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if llm_id is not UNSET:
            field_dict["llm_id"] = llm_id
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if voice_provider is not UNSET:
            field_dict["voice_provider"] = voice_provider
        if opening_line is not UNSET:
            field_dict["opening_line"] = opening_line
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds
        if record_call is not UNSET:
            field_dict["record_call"] = record_call
        if from_number is not UNSET:
            field_dict["from_number"] = from_number
        if source_dept is not UNSET:
            field_dict["source_dept"] = source_dept
        if source_agent_id is not UNSET:
            field_dict["source_agent_id"] = source_agent_id
        if source_task_id is not UNSET:
            field_dict["source_task_id"] = source_task_id
        if extra_context is not UNSET:
            field_dict["extra_context"] = extra_context
        if explicit_datasource_id is not UNSET:
            field_dict["explicit_datasource_id"] = explicit_datasource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_session_start_request_extra_context_type_0 import (
            VoiceSessionStartRequestExtraContextType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        to = d.pop("to")

        _mode = d.pop("mode", UNSET)
        mode: VoiceSessionStartRequestMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = VoiceSessionStartRequestMode(_mode)

        def _parse_agent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)

                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id", UNSET))

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

        def _parse_voice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_id = _parse_voice_id(d.pop("voice_id", UNSET))

        voice_provider = d.pop("voice_provider", UNSET)

        def _parse_opening_line(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_line = _parse_opening_line(d.pop("opening_line", UNSET))

        max_duration_seconds = d.pop("max_duration_seconds", UNSET)

        record_call = d.pop("record_call", UNSET)

        def _parse_from_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_number = _parse_from_number(d.pop("from_number", UNSET))

        source_dept = d.pop("source_dept", UNSET)

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

        def _parse_source_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_task_id_type_0 = UUID(data)

                return source_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_task_id = _parse_source_task_id(d.pop("source_task_id", UNSET))

        def _parse_extra_context(data: object) -> None | Unset | VoiceSessionStartRequestExtraContextType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_context_type_0 = VoiceSessionStartRequestExtraContextType0.from_dict(data)

                return extra_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VoiceSessionStartRequestExtraContextType0, data)

        extra_context = _parse_extra_context(d.pop("extra_context", UNSET))

        def _parse_explicit_datasource_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                explicit_datasource_id_type_0 = UUID(data)

                return explicit_datasource_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        explicit_datasource_id = _parse_explicit_datasource_id(d.pop("explicit_datasource_id", UNSET))

        voice_session_start_request = cls(
            to=to,
            mode=mode,
            agent_id=agent_id,
            llm_id=llm_id,
            from_persona_id=from_persona_id,
            voice_id=voice_id,
            voice_provider=voice_provider,
            opening_line=opening_line,
            max_duration_seconds=max_duration_seconds,
            record_call=record_call,
            from_number=from_number,
            source_dept=source_dept,
            source_agent_id=source_agent_id,
            source_task_id=source_task_id,
            extra_context=extra_context,
            explicit_datasource_id=explicit_datasource_id,
        )

        voice_session_start_request.additional_properties = d
        return voice_session_start_request

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
