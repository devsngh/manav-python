from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionUpdate")


@_attrs_define
class PositionUpdate:
    """Update position schema

    Attributes:
        title (None | str | Unset):
        description (None | str | Unset):
        department (None | str | Unset):
        department_id (None | Unset | UUID):
        seniority_level (None | str | Unset):
        reports_to_position_id (None | Unset | UUID):
        responsibilities (None | str | Unset):
    """

    title: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    department_id: None | Unset | UUID = UNSET
    seniority_level: None | str | Unset = UNSET
    reports_to_position_id: None | Unset | UUID = UNSET
    responsibilities: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

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

        position_update = cls(
            title=title,
            description=description,
            department=department,
            department_id=department_id,
            seniority_level=seniority_level,
            reports_to_position_id=reports_to_position_id,
            responsibilities=responsibilities,
        )

        position_update.additional_properties = d
        return position_update

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
