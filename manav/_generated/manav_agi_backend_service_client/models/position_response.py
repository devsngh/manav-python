from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionResponse")


@_attrs_define
class PositionResponse:
    """Position response schema

    Attributes:
        title (str):
        id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        department (None | str | Unset):
        department_id (None | Unset | UUID):
        seniority_level (None | str | Unset):
        reports_to_position_id (None | Unset | UUID):
        responsibilities (None | str | Unset):
        org_id (None | Unset | UUID):
        org_name (None | str | Unset):
        reports_to_position_title (None | str | Unset):
        department_name (None | str | Unset):
        subordinate_count (int | Unset):  Default: 0.
    """

    title: str
    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    seniority_level: None | str | Unset = UNSET
    reports_to_position_id: None | Unset | UUID = UNSET
    responsibilities: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    org_name: None | str | Unset = UNSET
    reports_to_position_title: None | str | Unset = UNSET
    department_name: None | str | Unset = UNSET
    subordinate_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        seniority_level: None | str | Unset
        if isinstance(self.seniority_level, Unset):
            seniority_level = UNSET
        else:
            seniority_level = self.seniority_level

        reports_to_position_id: None | str | Unset
        if isinstance(self.reports_to_position_id, Unset):
            reports_to_position_id = UNSET
        elif isinstance(self.reports_to_position_id, UUID):
            reports_to_position_id = str(self.reports_to_position_id)
        else:
            reports_to_position_id = self.reports_to_position_id

        responsibilities: None | str | Unset
        if isinstance(self.responsibilities, Unset):
            responsibilities = UNSET
        else:
            responsibilities = self.responsibilities

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        org_name: None | str | Unset
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        reports_to_position_title: None | str | Unset
        if isinstance(self.reports_to_position_title, Unset):
            reports_to_position_title = UNSET
        else:
            reports_to_position_title = self.reports_to_position_title

        department_name: None | str | Unset
        if isinstance(self.department_name, Unset):
            department_name = UNSET
        else:
            department_name = self.department_name

        subordinate_count = self.subordinate_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if department is not UNSET:
            field_dict["department"] = department
        if department_id is not UNSET:
            field_dict["department_id"] = department_id
        if seniority_level is not UNSET:
            field_dict["seniority_level"] = seniority_level
        if reports_to_position_id is not UNSET:
            field_dict["reports_to_position_id"] = reports_to_position_id
        if responsibilities is not UNSET:
            field_dict["responsibilities"] = responsibilities
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if reports_to_position_title is not UNSET:
            field_dict["reports_to_position_title"] = reports_to_position_title
        if department_name is not UNSET:
            field_dict["department_name"] = department_name
        if subordinate_count is not UNSET:
            field_dict["subordinate_count"] = subordinate_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        id = UUID(d.pop("id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_seniority_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seniority_level = _parse_seniority_level(d.pop("seniority_level", UNSET))

        def _parse_reports_to_position_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reports_to_position_id_type_0 = UUID(data)

                return reports_to_position_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reports_to_position_id = _parse_reports_to_position_id(d.pop("reports_to_position_id", UNSET))

        def _parse_responsibilities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsibilities = _parse_responsibilities(d.pop("responsibilities", UNSET))

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

        def _parse_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_name = _parse_org_name(d.pop("org_name", UNSET))

        def _parse_reports_to_position_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reports_to_position_title = _parse_reports_to_position_title(d.pop("reports_to_position_title", UNSET))

        def _parse_department_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_name = _parse_department_name(d.pop("department_name", UNSET))

        subordinate_count = d.pop("subordinate_count", UNSET)

        position_response = cls(
            title=title,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            department=department,
            department_id=department_id,
            seniority_level=seniority_level,
            reports_to_position_id=reports_to_position_id,
            responsibilities=responsibilities,
            org_id=org_id,
            org_name=org_name,
            reports_to_position_title=reports_to_position_title,
            department_name=department_name,
            subordinate_count=subordinate_count,
        )

        position_response.additional_properties = d
        return position_response

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
