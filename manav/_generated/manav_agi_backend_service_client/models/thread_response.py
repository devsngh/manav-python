from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreadResponse")


@_attrs_define
class ThreadResponse:
    """Schema for thread response

    Attributes:
        id (UUID):
        user_id (UUID):
        bot_id (UUID):
        title (str):
        org_id (None | UUID):
        is_archived (bool):
        is_deleted (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_message_at (datetime.datetime | None):
        deepagent_id (None | Unset | UUID):
        dialogue_count (int | None | Unset):  Default: 0.
    """

    id: UUID
    user_id: UUID
    bot_id: UUID
    title: str
    org_id: None | UUID
    is_archived: bool
    is_deleted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_message_at: datetime.datetime | None
    deepagent_id: None | Unset | UUID = UNSET
    dialogue_count: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        bot_id = str(self.bot_id)

        title = self.title

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        is_archived = self.is_archived

        is_deleted = self.is_deleted

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_message_at: None | str
        if isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        deepagent_id: None | str | Unset
        if isinstance(self.deepagent_id, Unset):
            deepagent_id = UNSET
        elif isinstance(self.deepagent_id, UUID):
            deepagent_id = str(self.deepagent_id)
        else:
            deepagent_id = self.deepagent_id

        dialogue_count: int | None | Unset
        if isinstance(self.dialogue_count, Unset):
            dialogue_count = UNSET
        else:
            dialogue_count = self.dialogue_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "bot_id": bot_id,
                "title": title,
                "org_id": org_id,
                "is_archived": is_archived,
                "is_deleted": is_deleted,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_message_at": last_message_at,
            }
        )
        if deepagent_id is not UNSET:
            field_dict["deepagent_id"] = deepagent_id
        if dialogue_count is not UNSET:
            field_dict["dialogue_count"] = dialogue_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        bot_id = UUID(d.pop("bot_id"))

        title = d.pop("title")

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

        is_deleted = d.pop("is_deleted")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_deepagent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deepagent_id_type_0 = UUID(data)

                return deepagent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        deepagent_id = _parse_deepagent_id(d.pop("deepagent_id", UNSET))

        def _parse_dialogue_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dialogue_count = _parse_dialogue_count(d.pop("dialogue_count", UNSET))

        thread_response = cls(
            id=id,
            user_id=user_id,
            bot_id=bot_id,
            title=title,
            org_id=org_id,
            is_archived=is_archived,
            is_deleted=is_deleted,
            created_at=created_at,
            updated_at=updated_at,
            last_message_at=last_message_at,
            deepagent_id=deepagent_id,
            dialogue_count=dialogue_count,
        )

        thread_response.additional_properties = d
        return thread_response

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
