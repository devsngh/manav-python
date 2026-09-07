from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleCreate")


@_attrs_define
class RoleCreate:
    """Create role schema

    Attributes:
        name (str):
        description (None | str | Unset):
        level (int | Unset):  Default: 1.
        department (None | str | Unset):
        department_id (None | Unset | UUID):
        reports_to_role_id (None | Unset | UUID):
        org_id (None | Unset | UUID):
    """

    name: str
    description: None | str | Unset = UNSET
    level: int | Unset = 1
    department: None | str | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    reports_to_role_id: None | Unset | UUID = UNSET
    org_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        level = self.level

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        department_id: None | str | Unset
        if isinstance(self.department_id, Unset):
            department_id = UNSET
        elif isinstance(self.department_id, UUID):
            department_id = str(self.department_id)
        else:
            department_id = self.department_id

        reports_to_role_id: None | str | Unset
        if isinstance(self.reports_to_role_id, Unset):
            reports_to_role_id = UNSET
        elif isinstance(self.reports_to_role_id, UUID):
            reports_to_role_id = str(self.reports_to_role_id)
        else:
            reports_to_role_id = self.reports_to_role_id

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
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if level is not UNSET:
            field_dict["level"] = level
        if department is not UNSET:
            field_dict["department"] = department
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if reports_to_role_id is not UNSET:
            field_dict["reports_to_role_id"] = reports_to_role_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        level = d.pop("level", UNSET)

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

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

        def _parse_reports_to_role_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reports_to_role_id_type_0 = UUID(data)

                return reports_to_role_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reports_to_role_id = _parse_reports_to_role_id(d.pop("reports_to_role_id", UNSET))

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

        role_create = cls(
            name=name,
            description=description,
            level=level,
            department=department,
            department_id=department_id,
            reports_to_role_id=reports_to_role_id,
            org_id=org_id,
        )

        role_create.additional_properties = d
        return role_create

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
