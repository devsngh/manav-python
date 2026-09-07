from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RubricUpdate")


@_attrs_define
class RubricUpdate:
    """
    Attributes:
        description (None | str | Unset):
        rubric_text (None | str | Unset):
        max_iterations (int | None | Unset):
        grader_model_id (None | str | Unset):
        is_active (bool | None | Unset):
    """

    description: None | str | Unset = UNSET
    rubric_text: None | str | Unset = UNSET
    max_iterations: int | None | Unset = UNSET
    grader_model_id: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        rubric_text: None | str | Unset
        if isinstance(self.rubric_text, Unset):
            rubric_text = UNSET
        else:
            rubric_text = self.rubric_text

        max_iterations: int | None | Unset
        if isinstance(self.max_iterations, Unset):
            max_iterations = UNSET
        else:
            max_iterations = self.max_iterations

        grader_model_id: None | str | Unset
        if isinstance(self.grader_model_id, Unset):
            grader_model_id = UNSET
        else:
            grader_model_id = self.grader_model_id

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if rubric_text is not UNSET:
            field_dict["rubric_text"] = rubric_text
        if max_iterations is not UNSET:
            field_dict["max_iterations"] = max_iterations
        if grader_model_id is not UNSET:
            field_dict["grader_model_id"] = grader_model_id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_rubric_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rubric_text = _parse_rubric_text(d.pop("rubric_text", UNSET))

        def _parse_max_iterations(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_iterations = _parse_max_iterations(d.pop("max_iterations", UNSET))

        def _parse_grader_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grader_model_id = _parse_grader_model_id(d.pop("grader_model_id", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        rubric_update = cls(
            description=description,
            rubric_text=rubric_text,
            max_iterations=max_iterations,
            grader_model_id=grader_model_id,
            is_active=is_active,
        )

        rubric_update.additional_properties = d
        return rubric_update

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
