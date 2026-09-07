from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_role import PromptRole
from ..models.prompt_status import PromptStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_component_create import PromptComponentCreate


T = TypeVar("T", bound="PromptCreate")


@_attrs_define
class PromptCreate:
    """
    Attributes:
        prompt_name (str):
        category (None | str | Unset):
        sub_category (None | str | Unset):
        status (PromptStatus | Unset): Prompt lifecycle status Default: PromptStatus.DRAFT.
        prompt_role (None | PromptRole | Unset):
        description (None | str | Unset):
        allowed_tools (list[str] | Unset):
        components (list[PromptComponentCreate] | Unset):
    """

    prompt_name: str
    category: None | str | Unset = UNSET
    sub_category: None | str | Unset = UNSET
    status: PromptStatus | Unset = PromptStatus.DRAFT
    prompt_role: None | PromptRole | Unset = UNSET
    description: None | str | Unset = UNSET
    allowed_tools: list[str] | Unset = UNSET
    components: list[PromptComponentCreate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt_name = self.prompt_name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        sub_category: None | str | Unset
        if isinstance(self.sub_category, Unset):
            sub_category = UNSET
        else:
            sub_category = self.sub_category

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        prompt_role: None | str | Unset
        if isinstance(self.prompt_role, Unset):
            prompt_role = UNSET
        elif isinstance(self.prompt_role, PromptRole):
            prompt_role = self.prompt_role.value
        else:
            prompt_role = self.prompt_role

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        allowed_tools: list[str] | Unset = UNSET
        if not isinstance(self.allowed_tools, Unset):
            allowed_tools = self.allowed_tools

        components: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = []
            for components_item_data in self.components:
                components_item = components_item_data.to_dict()
                components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt_name": prompt_name,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if sub_category is not UNSET:
            field_dict["sub_category"] = sub_category
        if status is not UNSET:
            field_dict["status"] = status
        if prompt_role is not UNSET:
            field_dict["prompt_role"] = prompt_role
        if description is not UNSET:
            field_dict["description"] = description
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_component_create import PromptComponentCreate  # noqa: PLC0415

        d = dict(src_dict)
        prompt_name = d.pop("prompt_name")

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_sub_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_category = _parse_sub_category(d.pop("sub_category", UNSET))

        _status = d.pop("status", UNSET)
        status: PromptStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PromptStatus(_status)

        def _parse_prompt_role(data: object) -> None | PromptRole | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                prompt_role_type_0 = PromptRole(data)

                return prompt_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptRole | Unset, data)

        prompt_role = _parse_prompt_role(d.pop("prompt_role", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        allowed_tools = cast(list[str], d.pop("allowed_tools", UNSET))

        _components = d.pop("components", UNSET)
        components: list[PromptComponentCreate] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = PromptComponentCreate.from_dict(components_item_data)

                components.append(components_item)

        prompt_create = cls(
            prompt_name=prompt_name,
            category=category,
            sub_category=sub_category,
            status=status,
            prompt_role=prompt_role,
            description=description,
            allowed_tools=allowed_tools,
            components=components,
        )

        prompt_create.additional_properties = d
        return prompt_create

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
