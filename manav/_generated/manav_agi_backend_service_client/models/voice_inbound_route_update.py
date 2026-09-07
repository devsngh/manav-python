from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_inbound_route_update_voice_provider_type_0 import VoiceInboundRouteUpdateVoiceProviderType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceInboundRouteUpdate")


@_attrs_define
class VoiceInboundRouteUpdate:
    """
    Attributes:
        from_number_pattern (None | str | Unset):
        caller_user_id (None | Unset | UUID):
        priority (int | None | Unset):
        is_active (bool | None | Unset):
        name (None | str | Unset):
        description (None | str | Unset):
        agent_id (None | Unset | UUID):
        llm_id (None | Unset | UUID):
        voice_id (None | str | Unset):
        voice_provider (None | Unset | VoiceInboundRouteUpdateVoiceProviderType0):
        from_persona_id (None | Unset | UUID):
        greeting_text (None | str | Unset):
        max_duration_seconds (int | None | Unset):
        record_call (bool | None | Unset):
        datasource_id (None | Unset | UUID):
    """

    from_number_pattern: None | str | Unset = UNSET
    caller_user_id: None | Unset | UUID = UNSET
    priority: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    agent_id: None | Unset | UUID = UNSET
    llm_id: None | Unset | UUID = UNSET
    voice_id: None | str | Unset = UNSET
    voice_provider: None | Unset | VoiceInboundRouteUpdateVoiceProviderType0 = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    greeting_text: None | str | Unset = UNSET
    max_duration_seconds: int | None | Unset = UNSET
    record_call: bool | None | Unset = UNSET
    datasource_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_number_pattern: None | str | Unset
        if isinstance(self.from_number_pattern, Unset):
            from_number_pattern = UNSET
        else:
            from_number_pattern = self.from_number_pattern

        caller_user_id: None | str | Unset
        if isinstance(self.caller_user_id, Unset):
            caller_user_id = UNSET
        elif isinstance(self.caller_user_id, UUID):
            caller_user_id = str(self.caller_user_id)
        else:
            caller_user_id = self.caller_user_id

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        voice_id: None | str | Unset
        if isinstance(self.voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = self.voice_id

        voice_provider: None | str | Unset
        if isinstance(self.voice_provider, Unset):
            voice_provider = UNSET
        elif isinstance(self.voice_provider, VoiceInboundRouteUpdateVoiceProviderType0):
            voice_provider = self.voice_provider.value
        else:
            voice_provider = self.voice_provider

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        greeting_text: None | str | Unset
        if isinstance(self.greeting_text, Unset):
            greeting_text = UNSET
        else:
            greeting_text = self.greeting_text

        max_duration_seconds: int | None | Unset
        if isinstance(self.max_duration_seconds, Unset):
            max_duration_seconds = UNSET
        else:
            max_duration_seconds = self.max_duration_seconds

        record_call: bool | None | Unset
        if isinstance(self.record_call, Unset):
            record_call = UNSET
        else:
            record_call = self.record_call

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        elif isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_number_pattern is not UNSET:
            field_dict["from_number_pattern"] = from_number_pattern
        if caller_user_id is not UNSET:
            field_dict["caller_user_id"] = caller_user_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if llm_id is not UNSET:
            field_dict["llm_id"] = llm_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if voice_provider is not UNSET:
            field_dict["voice_provider"] = voice_provider
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if greeting_text is not UNSET:
            field_dict["greeting_text"] = greeting_text
        if max_duration_seconds is not UNSET:
            field_dict["max_duration_seconds"] = max_duration_seconds
        if record_call is not UNSET:
            field_dict["record_call"] = record_call
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_number_pattern(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_number_pattern = _parse_from_number_pattern(d.pop("from_number_pattern", UNSET))

        def _parse_caller_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                caller_user_id_type_0 = UUID(data)

                return caller_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        caller_user_id = _parse_caller_user_id(d.pop("caller_user_id", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_voice_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voice_id = _parse_voice_id(d.pop("voice_id", UNSET))

        def _parse_voice_provider(data: object) -> None | Unset | VoiceInboundRouteUpdateVoiceProviderType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                voice_provider_type_0 = VoiceInboundRouteUpdateVoiceProviderType0(data)

                return voice_provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VoiceInboundRouteUpdateVoiceProviderType0, data)

        voice_provider = _parse_voice_provider(d.pop("voice_provider", UNSET))

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

        def _parse_greeting_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        greeting_text = _parse_greeting_text(d.pop("greeting_text", UNSET))

        def _parse_max_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_duration_seconds = _parse_max_duration_seconds(d.pop("max_duration_seconds", UNSET))

        def _parse_record_call(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        record_call = _parse_record_call(d.pop("record_call", UNSET))

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

        voice_inbound_route_update = cls(
            from_number_pattern=from_number_pattern,
            caller_user_id=caller_user_id,
            priority=priority,
            is_active=is_active,
            name=name,
            description=description,
            agent_id=agent_id,
            llm_id=llm_id,
            voice_id=voice_id,
            voice_provider=voice_provider,
            from_persona_id=from_persona_id,
            greeting_text=greeting_text,
            max_duration_seconds=max_duration_seconds,
            record_call=record_call,
            datasource_id=datasource_id,
        )

        voice_inbound_route_update.additional_properties = d
        return voice_inbound_route_update

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
