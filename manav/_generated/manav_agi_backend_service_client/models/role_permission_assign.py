from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_permission_assign_conditions_type_0 import RolePermissionAssignConditionsType0


T = TypeVar("T", bound="RolePermissionAssign")


@_attrs_define
class RolePermissionAssign:
    """Assign permission to role

    Attributes:
        role_id (UUID):
        permission_id (UUID):
        org_id (None | Unset | UUID):
        conditions (None | RolePermissionAssignConditionsType0 | Unset):
    """

    role_id: UUID
    permission_id: UUID
    org_id: None | Unset | UUID = UNSET
    conditions: None | RolePermissionAssignConditionsType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.role_permission_assign_conditions_type_0 import (
            RolePermissionAssignConditionsType0,  # noqa: PLC0415
        )

        role_id = str(self.role_id)

        permission_id = str(self.permission_id)

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
        elif isinstance(self.conditions, RolePermissionAssignConditionsType0):
            conditions = self.conditions.to_dict()
        else:
            conditions = self.conditions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_id": role_id,
                "permission_id": permission_id,
            }
        )
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_permission_assign_conditions_type_0 import (
            RolePermissionAssignConditionsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        role_id = UUID(d.pop("role_id"))

        permission_id = UUID(d.pop("permission_id"))

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

        def _parse_conditions(data: object) -> None | RolePermissionAssignConditionsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_type_0 = RolePermissionAssignConditionsType0.from_dict(data)

                return conditions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RolePermissionAssignConditionsType0 | Unset, data)

        conditions = _parse_conditions(d.pop("conditions", UNSET))

        role_permission_assign = cls(
            role_id=role_id,
            permission_id=permission_id,
            org_id=org_id,
            conditions=conditions,
        )

        role_permission_assign.additional_properties = d
        return role_permission_assign

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
