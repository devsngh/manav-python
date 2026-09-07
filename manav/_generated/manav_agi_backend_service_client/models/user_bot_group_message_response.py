from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_bot_group_message_response_message_metadata_type_0 import (
        UserBotGroupMessageResponseMessageMetadataType0,
    )


T = TypeVar("T", bound="UserBotGroupMessageResponse")


@_attrs_define
class UserBotGroupMessageResponse:
    """Single message in a user-bot group.

    Attributes:
        id (UUID):
        group_id (UUID):
        sender_id (UUID):
        sender_type (str):
        content (str):
        is_edited (bool):
        is_deleted (bool):
        is_pinned (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        message_metadata (None | Unset | UserBotGroupMessageResponseMessageMetadataType0):
        reply_to_message_id (None | Unset | UUID):
        edited_at (datetime.datetime | None | Unset):
        pinned_at (datetime.datetime | None | Unset):
    """

    id: UUID
    group_id: UUID
    sender_id: UUID
    sender_type: str
    content: str
    is_edited: bool
    is_deleted: bool
    is_pinned: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    message_metadata: None | Unset | UserBotGroupMessageResponseMessageMetadataType0 = UNSET
    reply_to_message_id: None | Unset | UUID = UNSET
    edited_at: datetime.datetime | None | Unset = UNSET
    pinned_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_bot_group_message_response_message_metadata_type_0 import (
            UserBotGroupMessageResponseMessageMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        group_id = str(self.group_id)

        sender_id = str(self.sender_id)

        sender_type = self.sender_type

        content = self.content

        is_edited = self.is_edited

        is_deleted = self.is_deleted

        is_pinned = self.is_pinned

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        message_metadata: dict[str, Any] | None | Unset
        if isinstance(self.message_metadata, Unset):
            message_metadata = UNSET
        elif isinstance(self.message_metadata, UserBotGroupMessageResponseMessageMetadataType0):
            message_metadata = self.message_metadata.to_dict()
        else:
            message_metadata = self.message_metadata

        reply_to_message_id: None | str | Unset
        if isinstance(self.reply_to_message_id, Unset):
            reply_to_message_id = UNSET
        elif isinstance(self.reply_to_message_id, UUID):
            reply_to_message_id = str(self.reply_to_message_id)
        else:
            reply_to_message_id = self.reply_to_message_id

        edited_at: None | str | Unset
        if isinstance(self.edited_at, Unset):
            edited_at = UNSET
        elif isinstance(self.edited_at, datetime.datetime):
            edited_at = self.edited_at.isoformat()
        else:
            edited_at = self.edited_at

        pinned_at: None | str | Unset
        if isinstance(self.pinned_at, Unset):
            pinned_at = UNSET
        elif isinstance(self.pinned_at, datetime.datetime):
            pinned_at = self.pinned_at.isoformat()
        else:
            pinned_at = self.pinned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "group_id": group_id,
                "sender_id": sender_id,
                "sender_type": sender_type,
                "content": content,
                "is_edited": is_edited,
                "is_deleted": is_deleted,
                "is_pinned": is_pinned,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if message_metadata is not UNSET:
            field_dict["message_metadata"] = message_metadata
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if pinned_at is not UNSET:
            field_dict["pinned_at"] = pinned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_bot_group_message_response_message_metadata_type_0 import (
            UserBotGroupMessageResponseMessageMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_id = UUID(d.pop("group_id"))

        sender_id = UUID(d.pop("sender_id"))

        sender_type = d.pop("sender_type")

        content = d.pop("content")

        is_edited = d.pop("is_edited")

        is_deleted = d.pop("is_deleted")

        is_pinned = d.pop("is_pinned")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_message_metadata(data: object) -> None | Unset | UserBotGroupMessageResponseMessageMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_metadata_type_0 = UserBotGroupMessageResponseMessageMetadataType0.from_dict(data)

                return message_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserBotGroupMessageResponseMessageMetadataType0, data)

        message_metadata = _parse_message_metadata(d.pop("message_metadata", UNSET))

        def _parse_reply_to_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reply_to_message_id_type_0 = UUID(data)

                return reply_to_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reply_to_message_id = _parse_reply_to_message_id(d.pop("reply_to_message_id", UNSET))

        def _parse_edited_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                edited_at_type_0 = datetime.datetime.fromisoformat(data)

                return edited_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        edited_at = _parse_edited_at(d.pop("edited_at", UNSET))

        def _parse_pinned_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pinned_at_type_0 = datetime.datetime.fromisoformat(data)

                return pinned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pinned_at = _parse_pinned_at(d.pop("pinned_at", UNSET))

        user_bot_group_message_response = cls(
            id=id,
            group_id=group_id,
            sender_id=sender_id,
            sender_type=sender_type,
            content=content,
            is_edited=is_edited,
            is_deleted=is_deleted,
            is_pinned=is_pinned,
            created_at=created_at,
            updated_at=updated_at,
            message_metadata=message_metadata,
            reply_to_message_id=reply_to_message_id,
            edited_at=edited_at,
            pinned_at=pinned_at,
        )

        user_bot_group_message_response.additional_properties = d
        return user_bot_group_message_response

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
