from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_action import PermissionAction
from ..models.permission_scope import PermissionScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionResponse")


@_attrs_define
class PermissionResponse:
    """Permission response schema

    Attributes:
        resource (str):
        action (PermissionAction): Permission action enum
        scope (PermissionScope): Permission scope enum
        id (UUID):
        created_at (datetime.datetime):
        description (None | str | Unset):
    """

    resource: str
    action: PermissionAction
    scope: PermissionScope
    id: UUID
    created_at: datetime.datetime
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        action = self.action.value

        scope = self.scope.value

        id = str(self.id)

        created_at = self.created_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "action": action,
                "scope": scope,
                "id": id,
                "created_at": created_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        action = PermissionAction(d.pop("action"))

        scope = PermissionScope(d.pop("scope"))

        id = UUID(d.pop("id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        permission_response = cls(
            resource=resource,
            action=action,
            scope=scope,
            id=id,
            created_at=created_at,
            description=description,
        )

        permission_response.additional_properties = d
        return permission_response

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
