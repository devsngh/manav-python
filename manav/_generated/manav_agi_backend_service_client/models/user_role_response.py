from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRoleResponse")


@_attrs_define
class UserRoleResponse:
    """User role response

    Attributes:
        id (UUID):
        user_id (UUID):
        role_id (UUID):
        assigned_at (datetime.datetime):
        org_id (None | Unset | UUID):
        assigned_by_user_id (None | Unset | UUID):
        user_email (None | str | Unset):
        role_name (None | str | Unset):
        org_name (None | str | Unset):
    """

    id: UUID
    user_id: UUID
    role_id: UUID
    assigned_at: datetime.datetime
    org_id: None | Unset | UUID = UNSET
    assigned_by_user_id: None | Unset | UUID = UNSET
    user_email: None | str | Unset = UNSET
    role_name: None | str | Unset = UNSET
    org_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user_id = str(self.user_id)

        role_id = str(self.role_id)

        assigned_at = self.assigned_at.isoformat()

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        assigned_by_user_id: None | str | Unset
        if isinstance(self.assigned_by_user_id, Unset):
            assigned_by_user_id = UNSET
        elif isinstance(self.assigned_by_user_id, UUID):
            assigned_by_user_id = str(self.assigned_by_user_id)
        else:
            assigned_by_user_id = self.assigned_by_user_id

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        role_name: None | str | Unset
        if isinstance(self.role_name, Unset):
            role_name = UNSET
        else:
            role_name = self.role_name

        org_name: None | str | Unset
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "role_id": role_id,
                "assigned_at": assigned_at,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if assigned_by_user_id is not UNSET:
            field_dict["assigned_by_user_id"] = assigned_by_user_id
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if org_name is not UNSET:
            field_dict["org_name"] = org_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        user_id = UUID(d.pop("user_id"))

        role_id = UUID(d.pop("role_id"))

        assigned_at = datetime.datetime.fromisoformat(d.pop("assigned_at"))

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

        def _parse_assigned_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_by_user_id_type_0 = UUID(data)

                return assigned_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_by_user_id = _parse_assigned_by_user_id(d.pop("assigned_by_user_id", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_name = _parse_role_name(d.pop("role_name", UNSET))

        def _parse_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_name = _parse_org_name(d.pop("org_name", UNSET))

        user_role_response = cls(
            id=id,
            user_id=user_id,
            role_id=role_id,
            assigned_at=assigned_at,
            org_id=org_id,
            assigned_by_user_id=assigned_by_user_id,
            user_email=user_email,
            role_name=role_name,
            org_name=org_name,
        )

        user_role_response.additional_properties = d
        return user_role_response

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
