from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.role_response import RoleResponse


T = TypeVar("T", bound="UserRolesResponse")


@_attrs_define
class UserRolesResponse:
    """Response for user's assigned roles

    Attributes:
        user_id (UUID):
        user_email (str):
        roles (list[RoleResponse]):
        total (int):
    """

    user_id: UUID
    user_email: str
    roles: list[RoleResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        user_email = self.user_email

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "user_email": user_email,
                "roles": roles,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_response import RoleResponse  # noqa: PLC0415

        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        user_email = d.pop("user_email")

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleResponse.from_dict(roles_item_data)

            roles.append(roles_item)

        total = d.pop("total")

        user_roles_response = cls(
            user_id=user_id,
            user_email=user_email,
            roles=roles,
            total=total,
        )

        user_roles_response.additional_properties = d
        return user_roles_response

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
