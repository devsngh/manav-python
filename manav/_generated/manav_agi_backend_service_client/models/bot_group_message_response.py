from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bot_group_message_response_metadata_type_0 import BotGroupMessageResponseMetadataType0
    from ..models.bot_sender_info import BotSenderInfo


T = TypeVar("T", bound="BotGroupMessageResponse")


@_attrs_define
class BotGroupMessageResponse:
    """Schema for bot group message response

    Attributes:
        id (UUID):
        group_id (UUID):
        sender_bot_id (UUID):
        content (str):
        is_deleted (bool):
        is_pinned (bool):
        created_at (datetime.datetime):
        sender_id (UUID): Alias for sender_bot_id — frontend expects sender_id.
        sender (BotSenderInfo | None | Unset):
        metadata (BotGroupMessageResponseMetadataType0 | None | Unset):
        read_by_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    group_id: UUID
    sender_bot_id: UUID
    content: str
    is_deleted: bool
    is_pinned: bool
    created_at: datetime.datetime
    sender_id: UUID
    sender: BotSenderInfo | None | Unset = UNSET
    metadata: BotGroupMessageResponseMetadataType0 | None | Unset = UNSET
    read_by_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_group_message_response_metadata_type_0 import (
            BotGroupMessageResponseMetadataType0,  # noqa: PLC0415
        )
        from ..models.bot_sender_info import BotSenderInfo  # noqa: PLC0415

        id = str(self.id)

        group_id = str(self.group_id)

        sender_bot_id = str(self.sender_bot_id)

        content = self.content

        is_deleted = self.is_deleted

        is_pinned = self.is_pinned

        created_at = self.created_at.isoformat()

        sender_id = str(self.sender_id)

        sender: dict[str, Any] | None | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        elif isinstance(self.sender, BotSenderInfo):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, BotGroupMessageResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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
                "sender_bot_id": sender_bot_id,
                "content": content,
                "is_deleted": is_deleted,
                "is_pinned": is_pinned,
                "created_at": created_at,
                "sender_id": sender_id,
            }
        )
        if sender is not UNSET:
            field_dict["sender"] = sender
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if read_by_count is not UNSET:
            field_dict["read_by_count"] = read_by_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_group_message_response_metadata_type_0 import (
            BotGroupMessageResponseMetadataType0,  # noqa: PLC0415
        )
        from ..models.bot_sender_info import BotSenderInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        group_id = UUID(d.pop("group_id"))

        sender_bot_id = UUID(d.pop("sender_bot_id"))

        content = d.pop("content")

        is_deleted = d.pop("is_deleted")

        is_pinned = d.pop("is_pinned")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        sender_id = UUID(d.pop("sender_id"))

        def _parse_sender(data: object) -> BotSenderInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sender_type_0 = BotSenderInfo.from_dict(data)

                return sender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotSenderInfo | None | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))

        def _parse_metadata(data: object) -> BotGroupMessageResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = BotGroupMessageResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotGroupMessageResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_read_by_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        read_by_count = _parse_read_by_count(d.pop("read_by_count", UNSET))

        bot_group_message_response = cls(
            id=id,
            group_id=group_id,
            sender_bot_id=sender_bot_id,
            content=content,
            is_deleted=is_deleted,
            is_pinned=is_pinned,
            created_at=created_at,
            sender_id=sender_id,
            sender=sender,
            metadata=metadata,
            read_by_count=read_by_count,
        )

        bot_group_message_response.additional_properties = d
        return bot_group_message_response

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
