from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_filesystem_permission_response import AgentFilesystemPermissionResponse


T = TypeVar("T", bound="AgentFilesystemPermissionListResponse")


@_attrs_define
class AgentFilesystemPermissionListResponse:
    """
    Attributes:
        permissions (list[AgentFilesystemPermissionResponse]):
        total (int):
    """

    permissions: list[AgentFilesystemPermissionResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_filesystem_permission_response import AgentFilesystemPermissionResponse  # noqa: PLC0415

        d = dict(src_dict)
        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = AgentFilesystemPermissionResponse.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        total = d.pop("total")

        agent_filesystem_permission_list_response = cls(
            permissions=permissions,
            total=total,
        )

        agent_filesystem_permission_list_response.additional_properties = d
        return agent_filesystem_permission_list_response

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
