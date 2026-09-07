from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_permission_response_conditions_type_0 import RolePermissionResponseConditionsType0


T = TypeVar("T", bound="RolePermissionResponse")


@_attrs_define
class RolePermissionResponse:
    """Role permission response

    Attributes:
        id (UUID):
        role_id (UUID):
        permission_id (UUID):
        granted_at (datetime.datetime):
        org_id (None | Unset | UUID):
        conditions (None | RolePermissionResponseConditionsType0 | Unset):
        granted_by_user_id (None | Unset | UUID):
        role_name (None | str | Unset):
        permission_resource (None | str | Unset):
        permission_action (None | str | Unset):
        permission_scope (None | str | Unset):
    """

    id: UUID
    role_id: UUID
    permission_id: UUID
    granted_at: datetime.datetime
    org_id: None | Unset | UUID = UNSET
    conditions: None | RolePermissionResponseConditionsType0 | Unset = UNSET
    granted_by_user_id: None | Unset | UUID = UNSET
    role_name: None | str | Unset = UNSET
    permission_resource: None | str | Unset = UNSET
    permission_action: None | str | Unset = UNSET
    permission_scope: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.role_permission_response_conditions_type_0 import (
            RolePermissionResponseConditionsType0,  # noqa: PLC0415
        )

        id = str(self.id)

        role_id = str(self.role_id)

        permission_id = str(self.permission_id)

        granted_at = self.granted_at.isoformat()

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        conditions: dict[str, Any] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, RolePermissionResponseConditionsType0):
            conditions = self.conditions.to_dict()
        else:
            conditions = self.conditions

        granted_by_user_id: None | str | Unset
        if isinstance(self.granted_by_user_id, Unset):
            granted_by_user_id = UNSET
        elif isinstance(self.granted_by_user_id, UUID):
            granted_by_user_id = str(self.granted_by_user_id)
        else:
            granted_by_user_id = self.granted_by_user_id

        role_name: None | str | Unset
        if isinstance(self.role_name, Unset):
            role_name = UNSET
        else:
            role_name = self.role_name

        permission_resource: None | str | Unset
        if isinstance(self.permission_resource, Unset):
            permission_resource = UNSET
        else:
            permission_resource = self.permission_resource

        permission_action: None | str | Unset
        if isinstance(self.permission_action, Unset):
            permission_action = UNSET
        else:
            permission_action = self.permission_action

        permission_scope: None | str | Unset
        if isinstance(self.permission_scope, Unset):
            permission_scope = UNSET
        else:
            permission_scope = self.permission_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role_id": role_id,
                "permission_id": permission_id,
                "granted_at": granted_at,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if granted_by_user_id is not UNSET:
            field_dict["granted_by_user_id"] = granted_by_user_id
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if permission_resource is not UNSET:
            field_dict["permission_resource"] = permission_resource
        if permission_action is not UNSET:
            field_dict["permission_action"] = permission_action
        if permission_scope is not UNSET:
            field_dict["permission_scope"] = permission_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_permission_response_conditions_type_0 import (
            RolePermissionResponseConditionsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        role_id = UUID(d.pop("role_id"))

        permission_id = UUID(d.pop("permission_id"))

        granted_at = datetime.datetime.fromisoformat(d.pop("granted_at"))

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

        def _parse_conditions(data: object) -> None | RolePermissionResponseConditionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_type_0 = RolePermissionResponseConditionsType0.from_dict(data)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RolePermissionResponseConditionsType0 | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        def _parse_granted_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                granted_by_user_id_type_0 = UUID(data)

                return granted_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        granted_by_user_id = _parse_granted_by_user_id(d.pop("granted_by_user_id", UNSET))

        def _parse_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_name = _parse_role_name(d.pop("role_name", UNSET))

        def _parse_permission_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permission_resource = _parse_permission_resource(d.pop("permission_resource", UNSET))

        def _parse_permission_action(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permission_action = _parse_permission_action(d.pop("permission_action", UNSET))

        def _parse_permission_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permission_scope = _parse_permission_scope(d.pop("permission_scope", UNSET))

        role_permission_response = cls(
            id=id,
            role_id=role_id,
            permission_id=permission_id,
            granted_at=granted_at,
            org_id=org_id,
            conditions=conditions,
            granted_by_user_id=granted_by_user_id,
            role_name=role_name,
            permission_resource=permission_resource,
            permission_action=permission_action,
            permission_scope=permission_scope,
        )

        role_permission_response.additional_properties = d
        return role_permission_response

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
