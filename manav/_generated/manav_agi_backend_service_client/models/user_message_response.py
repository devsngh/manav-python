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


T = TypeVar("T", bound="UserMessageResponse")


@_attrs_define
class UserMessageResponse:
    """Schema for user message response

    Attributes:
        id (UUID):
        conversation_id (UUID):
        sender_id (UUID):
        content (str):
        message_type (str):
        attachment_url (None | str):
        reply_to_message_id (None | UUID):
        is_edited (bool):
        edited_at (datetime.datetime | None):
        is_deleted (bool):
        read_by_recipient (bool):
        read_at (datetime.datetime | None):
        created_at (datetime.datetime):
        sender (None | Unset | UserPublicProfile):
    """

    id: UUID
    conversation_id: UUID
    sender_id: UUID
    content: str
    message_type: str
    attachment_url: None | str
    reply_to_message_id: None | UUID
    is_edited: bool
    edited_at: datetime.datetime | None
    is_deleted: bool
    read_by_recipient: bool
    read_at: datetime.datetime | None
    created_at: datetime.datetime
    sender: None | Unset | UserPublicProfile = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        id = str(self.id)

        conversation_id = str(self.conversation_id)

        sender_id = str(self.sender_id)

        content = self.content

        message_type = self.message_type

        attachment_url: None | str
        attachment_url = self.attachment_url

        reply_to_message_id: None | str
        if isinstance(self.reply_to_message_id, UUID):
            reply_to_message_id = str(self.reply_to_message_id)
        else:
            reply_to_message_id = self.reply_to_message_id

        is_edited = self.is_edited

        edited_at: None | str
        if isinstance(self.edited_at, datetime.datetime):
            edited_at = self.edited_at.isoformat()
        else:
            edited_at = self.edited_at

        is_deleted = self.is_deleted

        read_by_recipient = self.read_by_recipient

        read_at: None | str
        if isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at

        created_at = self.created_at.isoformat()

        sender: dict[str, Any] | None | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        elif isinstance(self.sender, UserPublicProfile):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conversation_id": conversation_id,
                "sender_id": sender_id,
                "content": content,
                "message_type": message_type,
                "attachment_url": attachment_url,
                "reply_to_message_id": reply_to_message_id,
                "is_edited": is_edited,
                "edited_at": edited_at,
                "is_deleted": is_deleted,
                "read_by_recipient": read_by_recipient,
                "read_at": read_at,
                "created_at": created_at,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        conversation_id = UUID(d.pop("conversation_id"))

        sender_id = UUID(d.pop("sender_id"))

        content = d.pop("content")

        message_type = d.pop("message_type")

        def _parse_attachment_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        attachment_url = _parse_attachment_url(d.pop("attachment_url"))

        def _parse_reply_to_message_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reply_to_message_id_type_0 = UUID(data)

                return reply_to_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        reply_to_message_id = _parse_reply_to_message_id(d.pop("reply_to_message_id"))

        is_edited = d.pop("is_edited")

        def _parse_edited_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                edited_at_type_0 = datetime.datetime.fromisoformat(data)

                return edited_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        edited_at = _parse_edited_at(d.pop("edited_at"))

        is_deleted = d.pop("is_deleted")

        read_by_recipient = d.pop("read_by_recipient")

        def _parse_read_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = datetime.datetime.fromisoformat(data)

                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        read_at = _parse_read_at(d.pop("read_at"))

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

        user_message_response = cls(
            id=id,
            conversation_id=conversation_id,
            sender_id=sender_id,
            content=content,
            message_type=message_type,
            attachment_url=attachment_url,
            reply_to_message_id=reply_to_message_id,
            is_edited=is_edited,
            edited_at=edited_at,
            is_deleted=is_deleted,
            read_by_recipient=read_by_recipient,
            read_at=read_at,
            created_at=created_at,
            sender=sender,
        )

        user_message_response.additional_properties = d
        return user_message_response

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
