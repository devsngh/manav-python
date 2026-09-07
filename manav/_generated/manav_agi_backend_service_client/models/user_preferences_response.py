from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesResponse")


@_attrs_define
class UserPreferencesResponse:
    """
    Attributes:
        id (UUID):
        user_id (UUID):
        location_metadata_enabled (bool):
        help_improve_enabled (bool):
        notify_email_enabled (bool):
        notify_task_completed (bool):
        notify_agent_errors (bool):
        notify_hil_requests (bool):
        notify_security_alerts (bool):
        notify_weekly_digest (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        preferred_voice (None | str | Unset):
        preferred_tts_provider (None | str | Unset):
    """

    id: UUID
    user_id: UUID
    location_metadata_enabled: bool
    help_improve_enabled: bool
    notify_email_enabled: bool
    notify_task_completed: bool
    notify_agent_errors: bool
    notify_hil_requests: bool
    notify_security_alerts: bool
    notify_weekly_digest: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    preferred_voice: None | str | Unset = UNSET
    preferred_tts_provider: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        location_metadata_enabled = self.location_metadata_enabled

        help_improve_enabled = self.help_improve_enabled

        notify_email_enabled = self.notify_email_enabled

        notify_task_completed = self.notify_task_completed

        notify_agent_errors = self.notify_agent_errors

        notify_hil_requests = self.notify_hil_requests

        notify_security_alerts = self.notify_security_alerts

        notify_weekly_digest = self.notify_weekly_digest

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        preferred_voice: None | str | Unset
        if isinstance(self.preferred_voice, Unset):
            preferred_voice = UNSET
        else:
            preferred_voice = self.preferred_voice

        preferred_tts_provider: None | str | Unset
        if isinstance(self.preferred_tts_provider, Unset):
            preferred_tts_provider = UNSET
        else:
            preferred_tts_provider = self.preferred_tts_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "location_metadata_enabled": location_metadata_enabled,
                "help_improve_enabled": help_improve_enabled,
                "notify_email_enabled": notify_email_enabled,
                "notify_task_completed": notify_task_completed,
                "notify_agent_errors": notify_agent_errors,
                "notify_hil_requests": notify_hil_requests,
                "notify_security_alerts": notify_security_alerts,
                "notify_weekly_digest": notify_weekly_digest,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if preferred_voice is not UNSET:
            field_dict["preferred_voice"] = preferred_voice
        if preferred_tts_provider is not UNSET:
            field_dict["preferred_tts_provider"] = preferred_tts_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        location_metadata_enabled = d.pop("location_metadata_enabled")

        help_improve_enabled = d.pop("help_improve_enabled")

        notify_email_enabled = d.pop("notify_email_enabled")

        notify_task_completed = d.pop("notify_task_completed")

        notify_agent_errors = d.pop("notify_agent_errors")

        notify_hil_requests = d.pop("notify_hil_requests")

        notify_security_alerts = d.pop("notify_security_alerts")

        notify_weekly_digest = d.pop("notify_weekly_digest")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_preferred_voice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_voice = _parse_preferred_voice(d.pop("preferred_voice", UNSET))

        def _parse_preferred_tts_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_tts_provider = _parse_preferred_tts_provider(d.pop("preferred_tts_provider", UNSET))

        user_preferences_response = cls(
            id=id,
            user_id=user_id,
            location_metadata_enabled=location_metadata_enabled,
            help_improve_enabled=help_improve_enabled,
            notify_email_enabled=notify_email_enabled,
            notify_task_completed=notify_task_completed,
            notify_agent_errors=notify_agent_errors,
            notify_hil_requests=notify_hil_requests,
            notify_security_alerts=notify_security_alerts,
            notify_weekly_digest=notify_weekly_digest,
            created_at=created_at,
            updated_at=updated_at,
            preferred_voice=preferred_voice,
            preferred_tts_provider=preferred_tts_provider,
        )

        user_preferences_response.additional_properties = d
        return user_preferences_response

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
