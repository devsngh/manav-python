from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchHit")


@_attrs_define
class SearchHit:
    """One message that matched the query.

    Attributes:
        thread_kind (str):
        thread_id (UUID):
        message_id (UUID):
        content_snippet (str):
        created_at (datetime.datetime):
        sender_id (None | Unset | UUID):
        sender_name (str | Unset):  Default: ''.
    """

    thread_kind: str
    thread_id: UUID
    message_id: UUID
    content_snippet: str
    created_at: datetime.datetime
    sender_id: None | Unset | UUID = UNSET
    sender_name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_kind = self.thread_kind

        thread_id = str(self.thread_id)

        message_id = str(self.message_id)

        content_snippet = self.content_snippet

        created_at = self.created_at.isoformat()

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        elif isinstance(self.sender_id, UUID):
            sender_id = str(self.sender_id)
        else:
            sender_id = self.sender_id

        sender_name = self.sender_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_kind": thread_kind,
                "thread_id": thread_id,
                "message_id": message_id,
                "content_snippet": content_snippet,
                "created_at": created_at,
            }
        )
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if sender_name is not UNSET:
            field_dict["sender_name"] = sender_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_kind = d.pop("thread_kind")

        thread_id = UUID(d.pop("thread_id"))

        message_id = UUID(d.pop("message_id"))

        content_snippet = d.pop("content_snippet")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_id_type_0 = UUID(data)

                return sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        sender_name = d.pop("sender_name", UNSET)

        search_hit = cls(
            thread_kind=thread_kind,
            thread_id=thread_id,
            message_id=message_id,
            content_snippet=content_snippet,
            created_at=created_at,
            sender_id=sender_id,
            sender_name=sender_name,
        )

        search_hit.additional_properties = d
        return search_hit

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
