from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_info import BotInfo
    from ..models.bot_message_response_message_metadata_type_0 import BotMessageResponseMessageMetadataType0


T = TypeVar("T", bound="BotMessageResponse")


@_attrs_define
class BotMessageResponse:
    """Schema for bot message response

    Attributes:
        id (UUID):
        conversation_id (UUID):
        sender_bot_id (UUID):
        content (str):
        is_deleted (bool):
        read_by_recipient (bool):
        read_at (datetime.datetime | None):
        created_at (datetime.datetime):
        sender (BotInfo | None | Unset):
        message_metadata (BotMessageResponseMessageMetadataType0 | None | Unset):
        is_edited (bool | Unset):  Default: False.
        edited_at (datetime.datetime | None | Unset):
    """

    id: UUID
    conversation_id: UUID
    sender_bot_id: UUID
    content: str
    is_deleted: bool
    read_by_recipient: bool
    read_at: datetime.datetime | None
    created_at: datetime.datetime
    sender: BotInfo | None | Unset = UNSET
    message_metadata: BotMessageResponseMessageMetadataType0 | None | Unset = UNSET
    is_edited: bool | Unset = False
    edited_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_info import BotInfo  # noqa: PLC0415
        from ..models.bot_message_response_message_metadata_type_0 import (
            BotMessageResponseMessageMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        conversation_id = str(self.conversation_id)

        sender_bot_id = str(self.sender_bot_id)

        content = self.content

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
        elif isinstance(self.sender, BotInfo):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        message_metadata: dict[str, Any] | None | Unset
        if isinstance(self.message_metadata, Unset):
            message_metadata = UNSET
        elif isinstance(self.message_metadata, BotMessageResponseMessageMetadataType0):
            message_metadata = self.message_metadata.to_dict()
        else:
            message_metadata = self.message_metadata

        is_edited = self.is_edited

        edited_at: None | str | Unset
        if isinstance(self.edited_at, Unset):
            edited_at = UNSET
        elif isinstance(self.edited_at, datetime.datetime):
            edited_at = self.edited_at.isoformat()
        else:
            edited_at = self.edited_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conversation_id": conversation_id,
                "sender_bot_id": sender_bot_id,
                "content": content,
                "is_deleted": is_deleted,
                "read_by_recipient": read_by_recipient,
                "read_at": read_at,
                "created_at": created_at,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender
        if message_metadata is not UNSET:
            field_dict["message_metadata"] = message_metadata
        if is_edited is not UNSET:
            field_dict["is_edited"] = is_edited
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_info import BotInfo  # noqa: PLC0415
        from ..models.bot_message_response_message_metadata_type_0 import (
            BotMessageResponseMessageMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        conversation_id = UUID(d.pop("conversation_id"))

        sender_bot_id = UUID(d.pop("sender_bot_id"))

        content = d.pop("content")

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

        def _parse_sender(data: object) -> BotInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sender_type_0 = BotInfo.from_dict(data)

                return sender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotInfo | None | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))

        def _parse_message_metadata(data: object) -> BotMessageResponseMessageMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_metadata_type_0 = BotMessageResponseMessageMetadataType0.from_dict(data)

                return message_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotMessageResponseMessageMetadataType0 | None | Unset, data)

        message_metadata = _parse_message_metadata(d.pop("message_metadata", UNSET))

        is_edited = d.pop("is_edited", UNSET)

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

        bot_message_response = cls(
            id=id,
            conversation_id=conversation_id,
            sender_bot_id=sender_bot_id,
            content=content,
            is_deleted=is_deleted,
            read_by_recipient=read_by_recipient,
            read_at=read_at,
            created_at=created_at,
            sender=sender,
            message_metadata=message_metadata,
            is_edited=is_edited,
            edited_at=edited_at,
        )

        bot_message_response.additional_properties = d
        return bot_message_response

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
