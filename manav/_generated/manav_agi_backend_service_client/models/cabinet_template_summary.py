from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CabinetTemplateSummary")


@_attrs_define
class CabinetTemplateSummary:
    """Trimmed projection used in bucket-listings (no content body).

    Attributes:
        id (UUID):
        bucket (str):
        path (str):
        version (int):
        is_active (bool):
        source (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        agent_name (None | str | Unset):
        role (None | str | Unset):
        org_id (None | Unset | UUID):
        department_id (None | Unset | UUID):
        description (None | str | Unset):
    """

    id: UUID
    bucket: str
    path: str
    version: int
    is_active: bool
    source: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    agent_name: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    department_id: None | Unset | UUID = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bucket = self.bucket

        path = self.path

        version = self.version

        is_active = self.is_active

        source = self.source

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bucket": bucket,
                "path": path,
                "version": version,
                "is_active": is_active,
                "source": source,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if role is not UNSET:
            field_dict["role"] = role
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bucket = d.pop("bucket")

        path = d.pop("path")

        version = d.pop("version")

        is_active = d.pop("is_active")

        source = d.pop("source")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

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

        def _parse_department_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                department_id_type_0 = UUID(data)

                return department_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        department_id = _parse_department_id(d.pop("department_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        cabinet_template_summary = cls(
            id=id,
            bucket=bucket,
            path=path,
            version=version,
            is_active=is_active,
            source=source,
            created_at=created_at,
            updated_at=updated_at,
            agent_name=agent_name,
            role=role,
            org_id=org_id,
            department_id=department_id,
            description=description,
        )

        cabinet_template_summary.additional_properties = d
        return cabinet_template_summary

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
