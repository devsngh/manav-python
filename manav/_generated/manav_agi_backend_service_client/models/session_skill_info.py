from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionSkillInfo")


@_attrs_define
class SessionSkillInfo:
    """A skill (prompt_role=SKILL) resolved for SKILL.md generation

    Attributes:
        id (str):
        skill_name (str):
        description (None | str | Unset):
        compiled_prompt (None | str | Unset):
        allowed_tools (list[str] | Unset):
    """

    id: str
    skill_name: str
    description: None | str | Unset = UNSET
    compiled_prompt: None | str | Unset = UNSET
    allowed_tools: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        skill_name = self.skill_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        compiled_prompt: None | str | Unset
        if isinstance(self.compiled_prompt, Unset):
            compiled_prompt = UNSET
        else:
            compiled_prompt = self.compiled_prompt

        allowed_tools: list[str] | Unset = UNSET
        if not isinstance(self.allowed_tools, Unset):
            allowed_tools = self.allowed_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "skill_name": skill_name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if compiled_prompt is not UNSET:
            field_dict["compiled_prompt"] = compiled_prompt
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        skill_name = d.pop("skill_name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_compiled_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compiled_prompt = _parse_compiled_prompt(d.pop("compiled_prompt", UNSET))

        allowed_tools = cast(list[str], d.pop("allowed_tools", UNSET))

        session_skill_info = cls(
            id=id,
            skill_name=skill_name,
            description=description,
            compiled_prompt=compiled_prompt,
            allowed_tools=allowed_tools,
        )

        session_skill_info.additional_properties = d
        return session_skill_info

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
