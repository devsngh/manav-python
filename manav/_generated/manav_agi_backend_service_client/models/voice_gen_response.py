from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_gen_response_status import VoiceGenResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voice_gen_response_provider_response_type_0 import VoiceGenResponseProviderResponseType0


T = TypeVar("T", bound="VoiceGenResponse")


@_attrs_define
class VoiceGenResponse:
    """Generation result — returned from POST /api/comms/voicegen/synthesize.

    Attributes:
        status (VoiceGenResponseStatus):
        provider (str):
        asset_id (None | Unset | UUID):
        asset_url (None | str | Unset):
        duration_seconds (float | None | Unset):
        error (None | str | Unset):
        human_task_id (None | str | Unset):
        provider_response (None | Unset | VoiceGenResponseProviderResponseType0):
    """

    status: VoiceGenResponseStatus
    provider: str
    asset_id: None | Unset | UUID = UNSET
    asset_url: None | str | Unset = UNSET
    duration_seconds: float | None | Unset = UNSET
    error: None | str | Unset = UNSET
    human_task_id: None | str | Unset = UNSET
    provider_response: None | Unset | VoiceGenResponseProviderResponseType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.voice_gen_response_provider_response_type_0 import (
            VoiceGenResponseProviderResponseType0,  # noqa: PLC0415
        )

        status = self.status.value

        provider = self.provider

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        asset_url: None | str | Unset
        if isinstance(self.asset_url, Unset):
            asset_url = UNSET
        else:
            asset_url = self.asset_url

        duration_seconds: float | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        human_task_id: None | str | Unset
        if isinstance(self.human_task_id, Unset):
            human_task_id = UNSET
        else:
            human_task_id = self.human_task_id

        provider_response: dict[str, Any] | None | Unset
        if isinstance(self.provider_response, Unset):
            provider_response = UNSET
        elif isinstance(self.provider_response, VoiceGenResponseProviderResponseType0):
            provider_response = self.provider_response.to_dict()
        else:
            provider_response = self.provider_response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "provider": provider,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_url is not UNSET:
            field_dict["asset_url"] = asset_url
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if error is not UNSET:
            field_dict["error"] = error
        if human_task_id is not UNSET:
            field_dict["human_task_id"] = human_task_id
        if provider_response is not UNSET:
            field_dict["provider_response"] = provider_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_gen_response_provider_response_type_0 import (
            VoiceGenResponseProviderResponseType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = VoiceGenResponseStatus(d.pop("status"))

        provider = d.pop("provider")

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_asset_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_url = _parse_asset_url(d.pop("asset_url", UNSET))

        def _parse_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_human_task_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        human_task_id = _parse_human_task_id(d.pop("human_task_id", UNSET))

        def _parse_provider_response(data: object) -> None | Unset | VoiceGenResponseProviderResponseType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_response_type_0 = VoiceGenResponseProviderResponseType0.from_dict(data)

                return provider_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VoiceGenResponseProviderResponseType0, data)

        provider_response = _parse_provider_response(d.pop("provider_response", UNSET))

        voice_gen_response = cls(
            status=status,
            provider=provider,
            asset_id=asset_id,
            asset_url=asset_url,
            duration_seconds=duration_seconds,
            error=error,
            human_task_id=human_task_id,
            provider_response=provider_response,
        )

        voice_gen_response.additional_properties = d
        return voice_gen_response

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
