from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentResponse")


@_attrs_define
class DepartmentResponse:
    """Department response schema

    Attributes:
        name (str):
        id (UUID):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (None | str | Unset):
        head_position_id (None | Unset | UUID):
        created_by_user_id (None | Unset | UUID):
        org_name (None | str | Unset):
        head_position_title (None | str | Unset):
        position_count (int | Unset):  Default: 0.
        role_count (int | Unset):  Default: 0.
    """

    name: str
    id: UUID
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: None | str | Unset = UNSET
    head_position_id: None | Unset | UUID = UNSET
    created_by_user_id: None | Unset | UUID = UNSET
    org_name: None | str | Unset = UNSET
    head_position_title: None | str | Unset = UNSET
    position_count: int | Unset = 0
    role_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = str(self.id)

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        created_by_user_id: None | str | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        elif isinstance(self.created_by_user_id, UUID):
            created_by_user_id = str(self.created_by_user_id)
        else:
            created_by_user_id = self.created_by_user_id

        org_name: None | str | Unset
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        head_position_title: None | str | Unset
        if isinstance(self.head_position_title, Unset):
            head_position_title = UNSET
        else:
            head_position_title = self.head_position_title

        position_count = self.position_count

        role_count = self.role_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if head_position_id is not UNSET:
            field_dict["head_position_id"] = head_position_id
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if head_position_title is not UNSET:
            field_dict["head_position_title"] = head_position_title
        if position_count is not UNSET:
            field_dict["position_count"] = position_count
        if role_count is not UNSET:
            field_dict["role_count"] = role_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_created_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_id_type_0 = UUID(data)

                return created_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))

        def _parse_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_name = _parse_org_name(d.pop("org_name", UNSET))

        def _parse_head_position_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        head_position_title = _parse_head_position_title(d.pop("head_position_title", UNSET))

        position_count = d.pop("position_count", UNSET)

        role_count = d.pop("role_count", UNSET)

        department_response = cls(
            name=name,
            id=id,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            head_position_id=head_position_id,
            created_by_user_id=created_by_user_id,
            org_name=org_name,
            head_position_title=head_position_title,
            position_count=position_count,
            role_count=role_count,
        )

        department_response.additional_properties = d
        return department_response

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
