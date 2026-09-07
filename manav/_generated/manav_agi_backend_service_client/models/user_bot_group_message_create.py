from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_bot_group_message_create_message_metadata_type_0 import (
        UserBotGroupMessageCreateMessageMetadataType0,
    )


T = TypeVar("T", bound="UserBotGroupMessageCreate")


@_attrs_define
class UserBotGroupMessageCreate:
    """Schema for posting a message into a user-bot group.

    Attributes:
        content (str):
        sender_id (UUID):
        sender_type (str):
        message_metadata (None | Unset | UserBotGroupMessageCreateMessageMetadataType0):
        reply_to_message_id (None | Unset | UUID):
    """

    content: str
    sender_id: UUID
    sender_type: str
    message_metadata: None | Unset | UserBotGroupMessageCreateMessageMetadataType0 = UNSET
    reply_to_message_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_bot_group_message_create_message_metadata_type_0 import (
            UserBotGroupMessageCreateMessageMetadataType0,  # noqa: PLC0415
        )

        content = self.content

        sender_id = str(self.sender_id)

        sender_type = self.sender_type

        message_metadata: dict[str, Any] | None | Unset
        if isinstance(self.message_metadata, Unset):
            message_metadata = UNSET
        elif isinstance(self.message_metadata, UserBotGroupMessageCreateMessageMetadataType0):
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "sender_id": sender_id,
                "sender_type": sender_type,
            }
        )
        if message_metadata is not UNSET:
            field_dict["message_metadata"] = message_metadata
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_bot_group_message_create_message_metadata_type_0 import (
            UserBotGroupMessageCreateMessageMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        content = d.pop("content")

        sender_id = UUID(d.pop("sender_id"))

        sender_type = d.pop("sender_type")

        def _parse_message_metadata(data: object) -> None | Unset | UserBotGroupMessageCreateMessageMetadataType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_metadata_type_0 = UserBotGroupMessageCreateMessageMetadataType0.from_dict(data)

                return message_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserBotGroupMessageCreateMessageMetadataType0, data)

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

        user_bot_group_message_create = cls(
            content=content,
            sender_id=sender_id,
            sender_type=sender_type,
            message_metadata=message_metadata,
            reply_to_message_id=reply_to_message_id,
        )

        user_bot_group_message_create.additional_properties = d
        return user_bot_group_message_create

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
