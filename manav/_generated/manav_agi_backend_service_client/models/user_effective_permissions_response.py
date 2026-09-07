from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.effective_permission import EffectivePermission


T = TypeVar("T", bound="UserEffectivePermissionsResponse")


@_attrs_define
class UserEffectivePermissionsResponse:
    """User's effective permissions

    Attributes:
        user_id (UUID):
        user_email (str):
        permissions (list[EffectivePermission]):
        total (int):
    """

    user_id: UUID
    user_email: str
    permissions: list[EffectivePermission]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        user_email = self.user_email

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "user_email": user_email,
                "permissions": permissions,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.effective_permission import EffectivePermission  # noqa: PLC0415

        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        user_email = d.pop("user_email")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = EffectivePermission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        total = d.pop("total")

        user_effective_permissions_response = cls(
            user_id=user_id,
            user_email=user_email,
            permissions=permissions,
            total=total,
        )

        user_effective_permissions_response.additional_properties = d
        return user_effective_permissions_response

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
