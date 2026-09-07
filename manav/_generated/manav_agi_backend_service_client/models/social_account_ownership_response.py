from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SocialAccountOwnershipResponse")


@_attrs_define
class SocialAccountOwnershipResponse:
    """
    Attributes:
        id (UUID):
        social_account_id (UUID):
        owner_type (str):
        owner_bot_id (None | UUID):
        owner_user_id (None | UUID):
        owner_persona_id (None | UUID):
        is_primary (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    social_account_id: UUID
    owner_type: str
    owner_bot_id: None | UUID
    owner_user_id: None | UUID
    owner_persona_id: None | UUID
    is_primary: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        social_account_id = str(self.social_account_id)

        owner_type = self.owner_type

        owner_bot_id: None | str
        if isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        owner_user_id: None | str
        if isinstance(self.owner_user_id, UUID):
            owner_user_id = str(self.owner_user_id)
        else:
            owner_user_id = self.owner_user_id

        owner_persona_id: None | str
        if isinstance(self.owner_persona_id, UUID):
            owner_persona_id = str(self.owner_persona_id)
        else:
            owner_persona_id = self.owner_persona_id

        is_primary = self.is_primary

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "social_account_id": social_account_id,
                "owner_type": owner_type,
                "owner_bot_id": owner_bot_id,
                "owner_user_id": owner_user_id,
                "owner_persona_id": owner_persona_id,
                "is_primary": is_primary,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        social_account_id = UUID(d.pop("social_account_id"))

        owner_type = d.pop("owner_type")

        def _parse_owner_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id"))

        def _parse_owner_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_user_id_type_0 = UUID(data)

                return owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id"))

        def _parse_owner_persona_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_persona_id_type_0 = UUID(data)

                return owner_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_persona_id = _parse_owner_persona_id(d.pop("owner_persona_id"))

        is_primary = d.pop("is_primary")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        social_account_ownership_response = cls(
            id=id,
            social_account_id=social_account_id,
            owner_type=owner_type,
            owner_bot_id=owner_bot_id,
            owner_user_id=owner_user_id,
            owner_persona_id=owner_persona_id,
            is_primary=is_primary,
            created_at=created_at,
        )

        social_account_ownership_response.additional_properties = d
        return social_account_ownership_response

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
