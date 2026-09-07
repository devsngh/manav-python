from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RubricResponse")


@_attrs_define
class RubricResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        description (None | str):
        rubric_text (str):
        max_iterations (int):
        grader_model_id (None | str):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | UUID):
        owner_org_id (None | UUID):
    """

    id: UUID
    name: str
    description: None | str
    rubric_text: str
    max_iterations: int
    grader_model_id: None | str
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | UUID
    owner_org_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        rubric_text = self.rubric_text

        max_iterations = self.max_iterations

        grader_model_id: None | str
        grader_model_id = self.grader_model_id

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        if isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        owner_org_id: None | str
        if isinstance(self.owner_org_id, UUID):
            owner_org_id = str(self.owner_org_id)
        else:
            owner_org_id = self.owner_org_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "rubric_text": rubric_text,
                "max_iterations": max_iterations,
                "grader_model_id": grader_model_id,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "owner_org_id": owner_org_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        rubric_text = d.pop("rubric_text")

        max_iterations = d.pop("max_iterations")

        def _parse_grader_model_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        grader_model_id = _parse_grader_model_id(d.pop("grader_model_id"))

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_created_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_owner_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_org_id_type_0 = UUID(data)

                return owner_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_org_id = _parse_owner_org_id(d.pop("owner_org_id"))

        rubric_response = cls(
            id=id,
            name=name,
            description=description,
            rubric_text=rubric_text,
            max_iterations=max_iterations,
            grader_model_id=grader_model_id,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            owner_org_id=owner_org_id,
        )

        rubric_response.additional_properties = d
        return rubric_response

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
