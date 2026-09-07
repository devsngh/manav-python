from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentCreate")


@_attrs_define
class DepartmentCreate:
    """Create department schema

    Attributes:
        name (str):
        org_id (UUID):
        description (None | str | Unset):
        head_position_id (None | Unset | UUID):
    """

    name: str
    org_id: UUID
    description: None | str | Unset = UNSET
    head_position_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        org_id = str(self.org_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        head_position_id: None | str | Unset
        if isinstance(self.head_position_id, Unset):
            head_position_id = UNSET
        elif isinstance(self.head_position_id, UUID):
            head_position_id = str(self.head_position_id)
        else:
            head_position_id = self.head_position_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "org_id": org_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if head_position_id is not UNSET:
            field_dict["head_position_id"] = head_position_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        org_id = UUID(d.pop("org_id"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_head_position_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                head_position_id_type_0 = UUID(data)

                return head_position_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        head_position_id = _parse_head_position_id(d.pop("head_position_id", UNSET))

        department_create = cls(
            name=name,
            org_id=org_id,
            description=description,
            head_position_id=head_position_id,
        )

        department_create.additional_properties = d
        return department_create

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
