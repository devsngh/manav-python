from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxThread")


@_attrs_define
class InboxThread:
    """One thread row in the Social Launcher's left rail.

    `thread_kind` tells the UI which chat-window variant to open + which
    sub-header line to render.

        Attributes:
            thread_kind (str):
            thread_id (UUID):
            title (str):
            avatar_url (None | str | Unset):
            last_message_preview (str | Unset):  Default: ''.
            last_message_at (datetime.datetime | None | Unset):
            unread_count (int | Unset):  Default: 0.
            participant_count (int | Unset):  Default: 0.
            org_id (None | Unset | UUID):
            archived (bool | Unset):  Default: False.
    """

    thread_kind: str
    thread_id: UUID
    title: str
    avatar_url: None | str | Unset = UNSET
    last_message_preview: str | Unset = ""
    last_message_at: datetime.datetime | None | Unset = UNSET
    unread_count: int | Unset = 0
    participant_count: int | Unset = 0
    org_id: None | Unset | UUID = UNSET
    archived: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_kind = self.thread_kind

        thread_id = str(self.thread_id)

        title = self.title

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        last_message_preview = self.last_message_preview

        last_message_at: None | str | Unset
        if isinstance(self.last_message_at, Unset):
            last_message_at = UNSET
        elif isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        unread_count = self.unread_count

        participant_count = self.participant_count

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_kind": thread_kind,
                "thread_id": thread_id,
                "title": title,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if last_message_preview is not UNSET:
            field_dict["last_message_preview"] = last_message_preview
        if last_message_at is not UNSET:
            field_dict["last_message_at"] = last_message_at
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if participant_count is not UNSET:
            field_dict["participant_count"] = participant_count
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_kind = d.pop("thread_kind")

        thread_id = UUID(d.pop("thread_id"))

        title = d.pop("title")

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        last_message_preview = d.pop("last_message_preview", UNSET)

        def _parse_last_message_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_message_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_message_at = _parse_last_message_at(d.pop("last_message_at", UNSET))

        unread_count = d.pop("unread_count", UNSET)

        participant_count = d.pop("participant_count", UNSET)

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        archived = d.pop("archived", UNSET)

        inbox_thread = cls(
            thread_kind=thread_kind,
            thread_id=thread_id,
            title=title,
            avatar_url=avatar_url,
            last_message_preview=last_message_preview,
            last_message_at=last_message_at,
            unread_count=unread_count,
            participant_count=participant_count,
            org_id=org_id,
            archived=archived,
        )

        inbox_thread.additional_properties = d
        return inbox_thread

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
