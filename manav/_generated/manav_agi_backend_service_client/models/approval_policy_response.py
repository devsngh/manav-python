from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ApprovalPolicyResponse")


@_attrs_define
class ApprovalPolicyResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        resource_type (str):
        description (None | str):
        is_active (bool):
        effective_from (datetime.date | None):
        effective_until (datetime.date | None):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    org_id: UUID
    name: str
    resource_type: str
    description: None | str
    is_active: bool
    effective_from: datetime.date | None
    effective_until: datetime.date | None
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        resource_type = self.resource_type

        description: None | str
        description = self.description

        is_active = self.is_active

        effective_from: None | str
        if isinstance(self.effective_from, datetime.date):
            effective_from = self.effective_from.isoformat()
        else:
            effective_from = self.effective_from

        effective_until: None | str
        if isinstance(self.effective_until, datetime.date):
            effective_until = self.effective_until.isoformat()
        else:
            effective_until = self.effective_until

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "name": name,
                "resource_type": resource_type,
                "description": description,
                "is_active": is_active,
                "effective_from": effective_from,
                "effective_until": effective_until,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        resource_type = d.pop("resource_type")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        is_active = d.pop("is_active")

        def _parse_effective_from(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_from_type_0 = datetime.date.fromisoformat(data)

                return effective_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_from = _parse_effective_from(d.pop("effective_from"))

        def _parse_effective_until(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_until_type_0 = datetime.date.fromisoformat(data)

                return effective_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_until = _parse_effective_until(d.pop("effective_until"))

        def _parse_created_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        approval_policy_response = cls(
            id=id,
            org_id=org_id,
            name=name,
            resource_type=resource_type,
            description=description,
            is_active=is_active,
            effective_from=effective_from,
            effective_until=effective_until,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        approval_policy_response.additional_properties = d
        return approval_policy_response

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
