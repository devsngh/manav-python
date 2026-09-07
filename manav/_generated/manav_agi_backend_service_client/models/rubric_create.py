from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RubricCreate")


@_attrs_define
class RubricCreate:
    """
    Attributes:
        name (str):
        rubric_text (str):
        description (None | str | Unset):
        max_iterations (int | Unset):  Default: 3.
        grader_model_id (None | str | Unset):
        owner_org_id (None | Unset | UUID):
        is_active (bool | Unset):  Default: True.
    """

    name: str
    rubric_text: str
    description: None | str | Unset = UNSET
    max_iterations: int | Unset = 3
    grader_model_id: None | str | Unset = UNSET
    owner_org_id: None | Unset | UUID = UNSET
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        rubric_text = self.rubric_text

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        max_iterations = self.max_iterations

        grader_model_id: None | str | Unset
        if isinstance(self.grader_model_id, Unset):
            grader_model_id = UNSET
        else:
            grader_model_id = self.grader_model_id

        owner_org_id: None | str | Unset
        if isinstance(self.owner_org_id, Unset):
            owner_org_id = UNSET
        elif isinstance(self.owner_org_id, UUID):
            owner_org_id = str(self.owner_org_id)
        else:
            owner_org_id = self.owner_org_id

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "rubric_text": rubric_text,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if max_iterations is not UNSET:
            field_dict["max_iterations"] = max_iterations
        if grader_model_id is not UNSET:
            field_dict["grader_model_id"] = grader_model_id
        if owner_org_id is not UNSET:
            field_dict["owner_org_id"] = owner_org_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        rubric_text = d.pop("rubric_text")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        max_iterations = d.pop("max_iterations", UNSET)

        def _parse_grader_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grader_model_id = _parse_grader_model_id(d.pop("grader_model_id", UNSET))

        def _parse_owner_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_org_id_type_0 = UUID(data)

                return owner_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_org_id = _parse_owner_org_id(d.pop("owner_org_id", UNSET))

        is_active = d.pop("is_active", UNSET)

        rubric_create = cls(
            name=name,
            rubric_text=rubric_text,
            description=description,
            max_iterations=max_iterations,
            grader_model_id=grader_model_id,
            owner_org_id=owner_org_id,
            is_active=is_active,
        )

        rubric_create.additional_properties = d
        return rubric_create

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
