from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesUpdate")


@_attrs_define
class UserPreferencesUpdate:
    """
    Attributes:
        location_metadata_enabled (bool | None | Unset):
        help_improve_enabled (bool | None | Unset):
        preferred_voice (None | str | Unset):
        preferred_tts_provider (None | str | Unset):
        notify_email_enabled (bool | None | Unset):
        notify_task_completed (bool | None | Unset):
        notify_agent_errors (bool | None | Unset):
        notify_hil_requests (bool | None | Unset):
        notify_security_alerts (bool | None | Unset):
        notify_weekly_digest (bool | None | Unset):
    """

    location_metadata_enabled: bool | None | Unset = UNSET
    help_improve_enabled: bool | None | Unset = UNSET
    preferred_voice: None | str | Unset = UNSET
    preferred_tts_provider: None | str | Unset = UNSET
    notify_email_enabled: bool | None | Unset = UNSET
    notify_task_completed: bool | None | Unset = UNSET
    notify_agent_errors: bool | None | Unset = UNSET
    notify_hil_requests: bool | None | Unset = UNSET
    notify_security_alerts: bool | None | Unset = UNSET
    notify_weekly_digest: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_metadata_enabled: bool | None | Unset
        if isinstance(self.location_metadata_enabled, Unset):
            location_metadata_enabled = UNSET
        else:
            location_metadata_enabled = self.location_metadata_enabled

        help_improve_enabled: bool | None | Unset
        if isinstance(self.help_improve_enabled, Unset):
            help_improve_enabled = UNSET
        else:
            help_improve_enabled = self.help_improve_enabled

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

        notify_email_enabled: bool | None | Unset
        if isinstance(self.notify_email_enabled, Unset):
            notify_email_enabled = UNSET
        else:
            notify_email_enabled = self.notify_email_enabled

        notify_task_completed: bool | None | Unset
        if isinstance(self.notify_task_completed, Unset):
            notify_task_completed = UNSET
        else:
            notify_task_completed = self.notify_task_completed

        notify_agent_errors: bool | None | Unset
        if isinstance(self.notify_agent_errors, Unset):
            notify_agent_errors = UNSET
        else:
            notify_agent_errors = self.notify_agent_errors

        notify_hil_requests: bool | None | Unset
        if isinstance(self.notify_hil_requests, Unset):
            notify_hil_requests = UNSET
        else:
            notify_hil_requests = self.notify_hil_requests

        notify_security_alerts: bool | None | Unset
        if isinstance(self.notify_security_alerts, Unset):
            notify_security_alerts = UNSET
        else:
            notify_security_alerts = self.notify_security_alerts

        notify_weekly_digest: bool | None | Unset
        if isinstance(self.notify_weekly_digest, Unset):
            notify_weekly_digest = UNSET
        else:
            notify_weekly_digest = self.notify_weekly_digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_metadata_enabled is not UNSET:
            field_dict["location_metadata_enabled"] = location_metadata_enabled
        if help_improve_enabled is not UNSET:
            field_dict["help_improve_enabled"] = help_improve_enabled
        if preferred_voice is not UNSET:
            field_dict["preferred_voice"] = preferred_voice
        if preferred_tts_provider is not UNSET:
            field_dict["preferred_tts_provider"] = preferred_tts_provider
        if notify_email_enabled is not UNSET:
            field_dict["notify_email_enabled"] = notify_email_enabled
        if notify_task_completed is not UNSET:
            field_dict["notify_task_completed"] = notify_task_completed
        if notify_agent_errors is not UNSET:
            field_dict["notify_agent_errors"] = notify_agent_errors
        if notify_hil_requests is not UNSET:
            field_dict["notify_hil_requests"] = notify_hil_requests
        if notify_security_alerts is not UNSET:
            field_dict["notify_security_alerts"] = notify_security_alerts
        if notify_weekly_digest is not UNSET:
            field_dict["notify_weekly_digest"] = notify_weekly_digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_location_metadata_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        location_metadata_enabled = _parse_location_metadata_enabled(d.pop("location_metadata_enabled", UNSET))

        def _parse_help_improve_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        help_improve_enabled = _parse_help_improve_enabled(d.pop("help_improve_enabled", UNSET))

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

        def _parse_notify_email_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_email_enabled = _parse_notify_email_enabled(d.pop("notify_email_enabled", UNSET))

        def _parse_notify_task_completed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_task_completed = _parse_notify_task_completed(d.pop("notify_task_completed", UNSET))

        def _parse_notify_agent_errors(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_agent_errors = _parse_notify_agent_errors(d.pop("notify_agent_errors", UNSET))

        def _parse_notify_hil_requests(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_hil_requests = _parse_notify_hil_requests(d.pop("notify_hil_requests", UNSET))

        def _parse_notify_security_alerts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_security_alerts = _parse_notify_security_alerts(d.pop("notify_security_alerts", UNSET))

        def _parse_notify_weekly_digest(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_weekly_digest = _parse_notify_weekly_digest(d.pop("notify_weekly_digest", UNSET))

        user_preferences_update = cls(
            location_metadata_enabled=location_metadata_enabled,
            help_improve_enabled=help_improve_enabled,
            preferred_voice=preferred_voice,
            preferred_tts_provider=preferred_tts_provider,
            notify_email_enabled=notify_email_enabled,
            notify_task_completed=notify_task_completed,
            notify_agent_errors=notify_agent_errors,
            notify_hil_requests=notify_hil_requests,
            notify_security_alerts=notify_security_alerts,
            notify_weekly_digest=notify_weekly_digest,
        )

        user_preferences_update.additional_properties = d
        return user_preferences_update

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
