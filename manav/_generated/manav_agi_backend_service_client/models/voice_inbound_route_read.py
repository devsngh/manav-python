from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_inbound_route_read_voice_provider import VoiceInboundRouteReadVoiceProvider
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceInboundRouteRead")


@_attrs_define
class VoiceInboundRouteRead:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        to_number (str):
        priority (int):
        is_active (bool):
        agent_id (UUID):
        voice_provider (VoiceInboundRouteReadVoiceProvider):
        greeting_text (str):
        max_duration_seconds (int):
        record_call (bool):
        match_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        from_number_pattern (None | str | Unset):
        caller_user_id (None | Unset | UUID):
        name (None | str | Unset):
        description (None | str | Unset):
        llm_id (None | Unset | UUID):
        voice_id (None | str | Unset):
        from_persona_id (None | Unset | UUID):
        datasource_id (None | Unset | UUID):
        last_matched_at (datetime.datetime | None | Unset):
        last_call_status (None | str | Unset):
    """

    id: UUID
    org_id: UUID
    to_number: str
    priority: int
    is_active: bool
    agent_id: UUID
    voice_provider: VoiceInboundRouteReadVoiceProvider
    greeting_text: str
    max_duration_seconds: int
    record_call: bool
    match_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    from_number_pattern: None | str | Unset = UNSET
    caller_user_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    llm_id: None | Unset | UUID = UNSET
    voice_id: None | str | Unset = UNSET
    from_persona_id: None | Unset | UUID = UNSET
    datasource_id: None | Unset | UUID = UNSET
    last_matched_at: datetime.datetime | None | Unset = UNSET
    last_call_status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        to_number = self.to_number

        priority = self.priority

        is_active = self.is_active

        agent_id = str(self.agent_id)

        voice_provider = self.voice_provider.value

        greeting_text = self.greeting_text

        max_duration_seconds = self.max_duration_seconds

        record_call = self.record_call

        match_count = self.match_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        from_persona_id: None | str | Unset
        if isinstance(self.from_persona_id, Unset):
            from_persona_id = UNSET
        elif isinstance(self.from_persona_id, UUID):
            from_persona_id = str(self.from_persona_id)
        else:
            from_persona_id = self.from_persona_id

        datasource_id: None | str | Unset
        if isinstance(self.datasource_id, Unset):
            datasource_id = UNSET
        elif isinstance(self.datasource_id, UUID):
            datasource_id = str(self.datasource_id)
        else:
            datasource_id = self.datasource_id

        last_matched_at: None | str | Unset
        if isinstance(self.last_matched_at, Unset):
            last_matched_at = UNSET
        elif isinstance(self.last_matched_at, datetime.datetime):
            last_matched_at = self.last_matched_at.isoformat()
        else:
            last_matched_at = self.last_matched_at

        last_call_status: None | str | Unset
        if isinstance(self.last_call_status, Unset):
            last_call_status = UNSET
        else:
            last_call_status = self.last_call_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "to_number": to_number,
                "priority": priority,
                "is_active": is_active,
                "agent_id": agent_id,
                "voice_provider": voice_provider,
                "greeting_text": greeting_text,
                "max_duration_seconds": max_duration_seconds,
                "record_call": record_call,
                "match_count": match_count,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if from_number_pattern is not UNSET:
            field_dict["from_number_pattern"] = from_number_pattern
        if caller_user_id is not UNSET:
            field_dict["caller_user_id"] = caller_user_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if llm_id is not UNSET:
            field_dict["llm_id"] = llm_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id
        if from_persona_id is not UNSET:
            field_dict["from_persona_id"] = from_persona_id
        if datasource_id is not UNSET:
            field_dict["datasource_id"] = datasource_id
        if last_matched_at is not UNSET:
            field_dict["last_matched_at"] = last_matched_at
        if last_call_status is not UNSET:
            field_dict["last_call_status"] = last_call_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        to_number = d.pop("to_number")

        priority = d.pop("priority")

        is_active = d.pop("is_active")

        agent_id = UUID(d.pop("agent_id"))

        voice_provider = VoiceInboundRouteReadVoiceProvider(d.pop("voice_provider"))

        greeting_text = d.pop("greeting_text")

        max_duration_seconds = d.pop("max_duration_seconds")

        record_call = d.pop("record_call")

        match_count = d.pop("match_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_last_matched_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_matched_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_matched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_matched_at = _parse_last_matched_at(d.pop("last_matched_at", UNSET))

        def _parse_last_call_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_call_status = _parse_last_call_status(d.pop("last_call_status", UNSET))

        voice_inbound_route_read = cls(
            id=id,
            org_id=org_id,
            to_number=to_number,
            priority=priority,
            is_active=is_active,
            agent_id=agent_id,
            voice_provider=voice_provider,
            greeting_text=greeting_text,
            max_duration_seconds=max_duration_seconds,
            record_call=record_call,
            match_count=match_count,
            created_at=created_at,
            updated_at=updated_at,
            from_number_pattern=from_number_pattern,
            caller_user_id=caller_user_id,
            name=name,
            description=description,
            llm_id=llm_id,
            voice_id=voice_id,
            from_persona_id=from_persona_id,
            datasource_id=datasource_id,
            last_matched_at=last_matched_at,
            last_call_status=last_call_status,
        )

        voice_inbound_route_read.additional_properties = d
        return voice_inbound_route_read

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
