from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_message_response import UserMessageResponse
    from ..models.user_public_profile import UserPublicProfile


T = TypeVar("T", bound="UserConversationResponse")


@_attrs_define
class UserConversationResponse:
    """Schema for user conversation response

    Attributes:
        id (UUID):
        participant_1_id (UUID):
        participant_2_id (UUID):
        org_id (None | UUID):
        is_archived (bool):
        is_blocked (bool):
        created_at (datetime.datetime):
        last_message_at (datetime.datetime | None):
        participant_1 (None | Unset | UserPublicProfile):
        participant_2 (None | Unset | UserPublicProfile):
        unread_count (int | None | Unset):  Default: 0.
        last_message (None | Unset | UserMessageResponse):
    """

    id: UUID
    participant_1_id: UUID
    participant_2_id: UUID
    org_id: None | UUID
    is_archived: bool
    is_blocked: bool
    created_at: datetime.datetime
    last_message_at: datetime.datetime | None
    participant_1: None | Unset | UserPublicProfile = UNSET
    participant_2: None | Unset | UserPublicProfile = UNSET
    unread_count: int | None | Unset = 0
    last_message: None | Unset | UserMessageResponse = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.user_message_response import UserMessageResponse  # noqa: PLC0415
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        id = str(self.id)

        participant_1_id = str(self.participant_1_id)

        participant_2_id = str(self.participant_2_id)

        org_id: None | str
        if isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        is_archived = self.is_archived

        is_blocked = self.is_blocked

        created_at = self.created_at.isoformat()

        last_message_at: None | str
        if isinstance(self.last_message_at, datetime.datetime):
            last_message_at = self.last_message_at.isoformat()
        else:
            last_message_at = self.last_message_at

        participant_1: dict[str, Any] | None | Unset
        if isinstance(self.participant_1, Unset):
            participant_1 = UNSET
        elif isinstance(self.participant_1, UserPublicProfile):
            participant_1 = self.participant_1.to_dict()
        else:
            participant_1 = self.participant_1

        participant_2: dict[str, Any] | None | Unset
        if isinstance(self.participant_2, Unset):
            participant_2 = UNSET
        elif isinstance(self.participant_2, UserPublicProfile):
            participant_2 = self.participant_2.to_dict()
        else:
            participant_2 = self.participant_2

        unread_count: int | None | Unset
        if isinstance(self.unread_count, Unset):
            unread_count = UNSET
        else:
            unread_count = self.unread_count

        last_message: dict[str, Any] | None | Unset
        if isinstance(self.last_message, Unset):
            last_message = UNSET
        elif isinstance(self.last_message, UserMessageResponse):
            last_message = self.last_message.to_dict()
        else:
            last_message = self.last_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "participant_1_id": participant_1_id,
                "participant_2_id": participant_2_id,
                "org_id": org_id,
                "is_archived": is_archived,
                "is_blocked": is_blocked,
                "created_at": created_at,
                "last_message_at": last_message_at,
            }
        )
        if participant_1 is not UNSET:
            field_dict["participant_1"] = participant_1
        if participant_2 is not UNSET:
            field_dict["participant_2"] = participant_2
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if last_message is not UNSET:
            field_dict["last_message"] = last_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_message_response import UserMessageResponse  # noqa: PLC0415
        from ..models.user_public_profile import UserPublicProfile  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        participant_1_id = UUID(d.pop("participant_1_id"))

        participant_2_id = UUID(d.pop("participant_2_id"))

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

        is_blocked = d.pop("is_blocked")

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

        def _parse_participant_1(data: object) -> None | Unset | UserPublicProfile:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                participant_1_type_0 = UserPublicProfile.from_dict(data)

                return participant_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserPublicProfile, data)

        participant_1 = _parse_participant_1(d.pop("participant_1", UNSET))

        def _parse_participant_2(data: object) -> None | Unset | UserPublicProfile:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                participant_2_type_0 = UserPublicProfile.from_dict(data)

                return participant_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserPublicProfile, data)

        participant_2 = _parse_participant_2(d.pop("participant_2", UNSET))

        def _parse_unread_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unread_count = _parse_unread_count(d.pop("unread_count", UNSET))

        def _parse_last_message(data: object) -> None | Unset | UserMessageResponse:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_message_type_0 = UserMessageResponse.from_dict(data)

                return last_message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserMessageResponse, data)

        last_message = _parse_last_message(d.pop("last_message", UNSET))

        user_conversation_response = cls(
            id=id,
            participant_1_id=participant_1_id,
            participant_2_id=participant_2_id,
            org_id=org_id,
            is_archived=is_archived,
            is_blocked=is_blocked,
            created_at=created_at,
            last_message_at=last_message_at,
            participant_1=participant_1,
            participant_2=participant_2,
            unread_count=unread_count,
            last_message=last_message,
        )

        user_conversation_response.additional_properties = d
        return user_conversation_response

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
