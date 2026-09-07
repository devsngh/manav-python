from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.voice_session_start_response_status import VoiceSessionStartResponseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceSessionStartResponse")


@_attrs_define
class VoiceSessionStartResponse:
    """
    Attributes:
        id (UUID):
        bridge_session_id (str):
        status (VoiceSessionStartResponseStatus):
        provider_call_id (None | str | Unset):
        ws_url (None | str | Unset):
    """

    id: UUID
    bridge_session_id: str
    status: VoiceSessionStartResponseStatus
    provider_call_id: None | str | Unset = UNSET
    ws_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bridge_session_id = self.bridge_session_id

        status = self.status.value

        provider_call_id: None | str | Unset
        if isinstance(self.provider_call_id, Unset):
            provider_call_id = UNSET
        else:
            provider_call_id = self.provider_call_id

        ws_url: None | str | Unset
        if isinstance(self.ws_url, Unset):
            ws_url = UNSET
        else:
            ws_url = self.ws_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bridge_session_id": bridge_session_id,
                "status": status,
            }
        )
        if provider_call_id is not UNSET:
            field_dict["provider_call_id"] = provider_call_id
        if ws_url is not UNSET:
            field_dict["ws_url"] = ws_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bridge_session_id = d.pop("bridge_session_id")

        status = VoiceSessionStartResponseStatus(d.pop("status"))

        def _parse_provider_call_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_call_id = _parse_provider_call_id(d.pop("provider_call_id", UNSET))

        def _parse_ws_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ws_url = _parse_ws_url(d.pop("ws_url", UNSET))

        voice_session_start_response = cls(
            id=id,
            bridge_session_id=bridge_session_id,
            status=status,
            provider_call_id=provider_call_id,
            ws_url=ws_url,
        )

        voice_session_start_response.additional_properties = d
        return voice_session_start_response

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
