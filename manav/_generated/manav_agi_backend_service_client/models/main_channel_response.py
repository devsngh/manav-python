from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MainChannelResponse")


@_attrs_define
class MainChannelResponse:
    """Schema for main channel response

    Attributes:
        id (UUID):
        channel_name (str):
        channel_description (None | str):
        org_id (UUID):
        is_active (bool):
        created_at (datetime.datetime):
        message_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    channel_name: str
    channel_description: None | str
    org_id: UUID
    is_active: bool
    created_at: datetime.datetime
    message_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        channel_name = self.channel_name

        channel_description: None | str
        channel_description = self.channel_description

        org_id = str(self.org_id)

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        message_count: int | None | Unset
        if isinstance(self.message_count, Unset):
            message_count = UNSET
        else:
            message_count = self.message_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "channel_name": channel_name,
                "channel_description": channel_description,
                "org_id": org_id,
                "is_active": is_active,
                "created_at": created_at,
            }
        )
        if message_count is not UNSET:
            field_dict["message_count"] = message_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        channel_name = d.pop("channel_name")

        def _parse_channel_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        channel_description = _parse_channel_description(d.pop("channel_description"))

        org_id = UUID(d.pop("org_id"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_message_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        message_count = _parse_message_count(d.pop("message_count", UNSET))

        main_channel_response = cls(
            id=id,
            channel_name=channel_name,
            channel_description=channel_description,
            org_id=org_id,
            is_active=is_active,
            created_at=created_at,
            message_count=message_count,
        )

        main_channel_response.additional_properties = d
        return main_channel_response

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
