from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EffectivePermission")


@_attrs_define
class EffectivePermission:
    """Effective permission for a user

    Attributes:
        resource (str):
        action (str):
        scope (str):
        source (str):
        role_name (None | str | Unset):
        org_id (None | Unset | UUID):
    """

    resource: str
    action: str
    scope: str
    source: str
    role_name: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        action = self.action

        scope = self.scope

        source = self.source

        role_name: None | str | Unset
        if isinstance(self.role_name, Unset):
            role_name = UNSET
        else:
            role_name = self.role_name

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "action": action,
                "scope": scope,
                "source": source,
            }
        )
        if role_name is not UNSET:
            field_dict["role_name"] = role_name
        if org_id is not UNSET:
            field_dict["org_id"] = org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        action = d.pop("action")

        scope = d.pop("scope")

        source = d.pop("source")

        def _parse_role_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role_name = _parse_role_name(d.pop("role_name", UNSET))

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

        effective_permission = cls(
            resource=resource,
            action=action,
            scope=scope,
            source=source,
            role_name=role_name,
            org_id=org_id,
        )

        effective_permission.additional_properties = d
        return effective_permission

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
