from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SkillSearchResult")


@_attrs_define
class SkillSearchResult:
    """
    Attributes:
        id (UUID):
        prompt_name (str):
        description (None | str):
        compiled_prompt (None | str):
    """

    id: UUID
    prompt_name: str
    description: None | str
    compiled_prompt: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        prompt_name = self.prompt_name

        description: None | str
        description = self.description

        compiled_prompt: None | str
        compiled_prompt = self.compiled_prompt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "prompt_name": prompt_name,
                "description": description,
                "compiled_prompt": compiled_prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        prompt_name = d.pop("prompt_name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_compiled_prompt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        compiled_prompt = _parse_compiled_prompt(d.pop("compiled_prompt"))

        skill_search_result = cls(
            id=id,
            prompt_name=prompt_name,
            description=description,
            compiled_prompt=compiled_prompt,
        )

        skill_search_result.additional_properties = d
        return skill_search_result

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
