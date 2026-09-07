from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserMessageCreate")


@_attrs_define
class UserMessageCreate:
    """Schema for sending a user message

    Attributes:
        conversation_id (UUID):
        content (str):
        message_type (str | Unset):  Default: 'text'.
        attachment_url (None | str | Unset):
        reply_to_message_id (None | Unset | UUID):
    """

    conversation_id: UUID
    content: str
    message_type: str | Unset = "text"
    attachment_url: None | str | Unset = UNSET
    reply_to_message_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = str(self.conversation_id)

        content = self.content

        message_type = self.message_type

        attachment_url: None | str | Unset
        if isinstance(self.attachment_url, Unset):
            attachment_url = UNSET
        else:
            attachment_url = self.attachment_url

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
                "conversation_id": conversation_id,
                "content": content,
            }
        )
        if message_type is not UNSET:
            field_dict["message_type"] = message_type
        if attachment_url is not UNSET:
            field_dict["attachment_url"] = attachment_url
        if reply_to_message_id is not UNSET:
            field_dict["reply_to_message_id"] = reply_to_message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = UUID(d.pop("conversation_id"))

        content = d.pop("content")

        message_type = d.pop("message_type", UNSET)

        def _parse_attachment_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        attachment_url = _parse_attachment_url(d.pop("attachment_url", UNSET))

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

        user_message_create = cls(
            conversation_id=conversation_id,
            content=content,
            message_type=message_type,
            attachment_url=attachment_url,
            reply_to_message_id=reply_to_message_id,
        )

        user_message_create.additional_properties = d
        return user_message_create

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
