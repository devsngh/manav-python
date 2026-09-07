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


T = TypeVar("T", bound="BotConversationResponse")


@_attrs_define
class BotConversationResponse:
    """Schema for bot conversation response

    Attributes:
        id (UUID):
        bot_1_id (UUID):
        bot_2_id (UUID):
        org_id (None | UUID):
        is_archived (bool):
        created_at (datetime.datetime):
        last_message_at (datetime.datetime | None):
        bot_1 (BotInfo | None | Unset):
        bot_2 (BotInfo | None | Unset):
        unread_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    bot_1_id: UUID
    bot_2_id: UUID
    org_id: None | UUID
    is_archived: bool
    created_at: datetime.datetime
    last_message_at: datetime.datetime | None
    bot_1: BotInfo | None | Unset = UNSET
    bot_2: BotInfo | None | Unset = UNSET
    unread_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_info import BotInfo  # noqa: PLC0415

        id = str(self.id)

        bot_1_id = str(self.bot_1_id)

        bot_2_id = str(self.bot_2_id)

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        is_archived = self.is_archived

        created_at = self.created_at.isoformat()

        last_message_at: None | str
        if isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        bot_1: dict[str, Any] | None | Unset
        if isinstance(self.bot_1, Unset):
            bot_1 = UNSET
        elif isinstance(self.bot_1, BotInfo):
            bot_1 = self.bot_1.to_dict()
        else:
            bot_1 = self.bot_1

        bot_2: dict[str, Any] | None | Unset
        if isinstance(self.bot_2, Unset):
            bot_2 = UNSET
        elif isinstance(self.bot_2, BotInfo):
            bot_2 = self.bot_2.to_dict()
        else:
            bot_2 = self.bot_2

        unread_count: int | None | Unset
        if isinstance(self.unread_count, Unset):
            unread_count = UNSET
        else:
            unread_count = self.unread_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_1_id": bot_1_id,
                "bot_2_id": bot_2_id,
                "org_id": org_id,
                "is_archived": is_archived,
                "created_at": created_at,
                "last_message_at": last_message_at,
            }
        )
        if bot_1 is not UNSET:
            field_dict["bot_1"] = bot_1
        if bot_2 is not UNSET:
            field_dict["bot_2"] = bot_2
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_info import BotInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_1_id = UUID(d.pop("bot_1_id"))

        bot_2_id = UUID(d.pop("bot_2_id"))

        def _parse_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        org_id = _parse_org_id(d.pop("org_id"))

        is_archived = d.pop("is_archived")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_last_message_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at"))

        def _parse_bot_1(data: object) -> BotInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bot_1_type_0 = BotInfo.from_dict(data)

                return bot_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotInfo | None | Unset, data)

        bot_1 = _parse_bot_1(d.pop("bot_1", UNSET))

        def _parse_bot_2(data: object) -> BotInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bot_2_type_0 = BotInfo.from_dict(data)

                return bot_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BotInfo | None | Unset, data)

        bot_2 = _parse_bot_2(d.pop("bot_2", UNSET))

        def _parse_unread_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unread_count = _parse_unread_count(d.pop("unread_count", UNSET))

        bot_conversation_response = cls(
            id=id,
            bot_1_id=bot_1_id,
            bot_2_id=bot_2_id,
            org_id=org_id,
            is_archived=is_archived,
            created_at=created_at,
            last_message_at=last_message_at,
            bot_1=bot_1,
            bot_2=bot_2,
            unread_count=unread_count,
        )

        bot_conversation_response.additional_properties = d
        return bot_conversation_response

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
