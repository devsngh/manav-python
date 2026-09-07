from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_inbound_route_create_voice_provider import VoiceInboundRouteCreateVoiceProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceInboundRouteCreate")


@_attrs_define
class VoiceInboundRouteCreate:
    """
    Attributes:
        to_number (str): The Twilio number being called (E.164)
        agent_id (UUID):
        greeting_text (str):
        from_number_pattern (None | str | Unset): Optional regex matching caller-id; None = any caller
        caller_user_id (None | Unset | UUID):
        priority (int | Unset):  Default: 100.
        is_active (bool | Unset):  Default: True.
        name (None | str | Unset):
        description (None | str | Unset):
        llm_id (None | Unset | UUID):
        voice_id (None | str | Unset):
        voice_provider (VoiceInboundRouteCreateVoiceProvider | Unset):  Default:
            VoiceInboundRouteCreateVoiceProvider.OPENAI_REALTIME.
        from_persona_id (None | Unset | UUID):
        max_duration_seconds (int | Unset):  Default: 600.
        record_call (bool | Unset):  Default: True.
        datasource_id (None | Unset | UUID):
    """

    to_number: str
    agent_id: UUID
    greeting_text: str
    from_number_pattern: None | str | Unset = UNSET
    caller_user_id: None | Unset | UUID = UNSET
    priority: int | Unset = 100
    is_active: bool | Unset = True
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    llm_id: None | Unset | UUID = UNSET
    voice_id: None | str | Unset = UNSET
    voice_provider: VoiceInboundRouteCreateVoiceProvider | Unset = VoiceInboundRouteCreateVoiceProvider.OPENAI_REALTIME
    from_persona_id: None | Unset | UUID = UNSET
    max_duration_seconds: int | Unset = 600
    record_call: bool | Unset = True
    datasource_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_number = self.to_number

        agent_id = str(self.agent_id)

        greeting_text = self.greeting_text

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

        priority = self.priority

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

        voice_provider: str | Unset = UNSET
        if not isinstance(self.voice_provider, Unset):
            voice_provider = self.voice_provider.value

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        max_duration_seconds = self.max_duration_seconds

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
        field_dict.update(
            {
                "to_number": to_number,
                "agent_id": agent_id,
                "greeting_text": greeting_text,
            }
        )
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
        if llm_id is not UNSET:
            field_dict["llm_id"] = llm_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if voice_provider is not UNSET:
            field_dict["voice_provider"] = voice_provider
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
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
        to_number = d.pop("to_number")

        agent_id = UUID(d.pop("agent_id"))

        greeting_text = d.pop("greeting_text")

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

        priority = d.pop("priority", UNSET)

        is_active = d.pop("is_active", UNSET)

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

        _voice_provider = d.pop("voice_provider", UNSET)
        voice_provider: VoiceInboundRouteCreateVoiceProvider | Unset
        if isinstance(_voice_provider, Unset):
            voice_provider = UNSET
        else:
            voice_provider = VoiceInboundRouteCreateVoiceProvider(_voice_provider)

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

        max_duration_seconds = d.pop("max_duration_seconds", UNSET)

        record_call = d.pop("record_call", UNSET)

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

        voice_inbound_route_create = cls(
            to_number=to_number,
            agent_id=agent_id,
            greeting_text=greeting_text,
            from_number_pattern=from_number_pattern,
            caller_user_id=caller_user_id,
            priority=priority,
            is_active=is_active,
            name=name,
            description=description,
            llm_id=llm_id,
            voice_id=voice_id,
            voice_provider=voice_provider,
            from_persona_id=from_persona_id,
            max_duration_seconds=max_duration_seconds,
            record_call=record_call,
            datasource_id=datasource_id,
        )

        voice_inbound_route_create.additional_properties = d
        return voice_inbound_route_create

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
