from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_public_profile import UserPublicProfile


T = TypeVar("T", bound="UserGroupMessageResponse")


@_attrs_define
class UserGroupMessageResponse:
    """Schema for user group message response

    Attributes:
        id (UUID):
        group_id (UUID):
        sender_id (UUID):
        content (str):
        message_type (str):
        is_edited (bool):
        is_deleted (bool):
        is_pinned (bool):
        pinned_at (datetime.datetime | None):
        created_at (datetime.datetime):
        sender (None | Unset | UserPublicProfile):
        read_by_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    group_id: UUID
    sender_id: UUID
    content: str
    message_type: str
    is_edited: bool
    is_deleted: bool
    is_pinned: bool
    pinned_at: datetime.datetime | None
    created_at: datetime.datetime
    sender: None | Unset | UserPublicProfile = UNSET
    read_by_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        id = str(self.id)

        group_id = str(self.group_id)

        sender_id = str(self.sender_id)

        content = self.content

        message_type = self.message_type

        is_edited = self.is_edited

        is_deleted = self.is_deleted

        is_pinned = self.is_pinned

        pinned_at: None | str
        if isinstance(self.pinned_at, datetime.datetime):
            pinned_at = self.pinned_at.isoformat()
        else:
            pinned_at = self.pinned_at

        created_at = self.created_at.isoformat()

        sender: dict[str, Any] | None | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        elif isinstance(self.sender, UserPublicProfile):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        read_by_count: int | None | Unset
        if isinstance(self.read_by_count, Unset):
            read_by_count = UNSET
        else:
            read_by_count = self.read_by_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "sender_id": sender_id,
                "content": content,
                "message_type": message_type,
                "is_edited": is_edited,
                "is_deleted": is_deleted,
                "is_pinned": is_pinned,
                "pinned_at": pinned_at,
                "created_at": created_at,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender
        if read_by_count is not UNSET:
            field_dict["read_by_count"] = read_by_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_id = UUID(d.pop("group_id"))

        sender_id = UUID(d.pop("sender_id"))

        content = d.pop("content")

        message_type = d.pop("message_type")

        is_edited = d.pop("is_edited")

        is_deleted = d.pop("is_deleted")

        is_pinned = d.pop("is_pinned")

        def _parse_pinned_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pinned_at_type_0 = datetime.datetime.fromisoformat(data)

                return pinned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        pinned_at = _parse_pinned_at(d.pop("pinned_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_sender(data: object) -> None | Unset | UserPublicProfile:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sender_type_0 = UserPublicProfile.from_dict(data)

                return sender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserPublicProfile, data)

        sender = _parse_sender(d.pop("sender", UNSET))

        def _parse_read_by_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        read_by_count = _parse_read_by_count(d.pop("read_by_count", UNSET))

        user_group_message_response = cls(
            id=id,
            group_id=group_id,
            sender_id=sender_id,
            content=content,
            message_type=message_type,
            is_edited=is_edited,
            is_deleted=is_deleted,
            is_pinned=is_pinned,
            pinned_at=pinned_at,
            created_at=created_at,
            sender=sender,
            read_by_count=read_by_count,
        )

        user_group_message_response.additional_properties = d
        return user_group_message_response

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
