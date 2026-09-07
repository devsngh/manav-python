from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.permission_response import PermissionResponse


T = TypeVar("T", bound="RolePermissionsResponse")


@_attrs_define
class RolePermissionsResponse:
    """Response for role's assigned permissions

    Attributes:
        role_id (UUID):
        role_name (str):
        permissions (list[PermissionResponse]):
        total (int):
    """

    role_id: UUID
    role_name: str
    permissions: list[PermissionResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = str(self.role_id)

        role_name = self.role_name

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_id": role_id,
                "role_name": role_name,
                "permissions": permissions,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_response import PermissionResponse  # noqa: PLC0415

        d = dict(src_dict)
        role_id = UUID(d.pop("role_id"))

        role_name = d.pop("role_name")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = PermissionResponse.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        total = d.pop("total")

        role_permissions_response = cls(
            role_id=role_id,
            role_name=role_name,
            permissions=permissions,
            total=total,
        )

        role_permissions_response.additional_properties = d
        return role_permissions_response

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
