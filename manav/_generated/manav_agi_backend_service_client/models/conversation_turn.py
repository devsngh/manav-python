from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationTurn")


@_attrs_define
class ConversationTurn:
    """One message in the flat conversation view (debate/meeting/group sources).

    Attributes:
        turn_id (UUID):
        turn_index (int | Unset):  Default: 0.
        who_id (None | Unset | UUID):
        who_name (str | Unset):  Default: ''.
        content (str | Unset):  Default: ''.
        posted_at (datetime.datetime | None | Unset):
    """

    turn_id: UUID
    turn_index: int | Unset = 0
    who_id: None | Unset | UUID = UNSET
    who_name: str | Unset = ""
    content: str | Unset = ""
    posted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        turn_id = str(self.turn_id)

        turn_index = self.turn_index

        who_id: None | str | Unset
        if isinstance(self.who_id, Unset):
            who_id = UNSET
        elif isinstance(self.who_id, UUID):
            who_id = str(self.who_id)
        else:
            who_id = self.who_id

        who_name = self.who_name

        content = self.content

        posted_at: None | str | Unset
        if isinstance(self.posted_at, Unset):
            posted_at = UNSET
        elif isinstance(self.posted_at, datetime.datetime):
            posted_at = self.posted_at.isoformat()
        else:
            posted_at = self.posted_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "turn_id": turn_id,
            }
        )
        if turn_index is not UNSET:
            field_dict["turn_index"] = turn_index
        if who_id is not UNSET:
            field_dict["who_id"] = who_id
        if who_name is not UNSET:
            field_dict["who_name"] = who_name
        if content is not UNSET:
            field_dict["content"] = content
        if posted_at is not UNSET:
            field_dict["posted_at"] = posted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        turn_id = UUID(d.pop("turn_id"))

        turn_index = d.pop("turn_index", UNSET)

        def _parse_who_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                who_id_type_0 = UUID(data)

                return who_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        who_id = _parse_who_id(d.pop("who_id", UNSET))

        who_name = d.pop("who_name", UNSET)

        content = d.pop("content", UNSET)

        def _parse_posted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                posted_at_type_0 = datetime.datetime.fromisoformat(data)

                return posted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        posted_at = _parse_posted_at(d.pop("posted_at", UNSET))

        conversation_turn = cls(
            turn_id=turn_id,
            turn_index=turn_index,
            who_id=who_id,
            who_name=who_name,
            content=content,
            posted_at=posted_at,
        )

        conversation_turn.additional_properties = d
        return conversation_turn

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
