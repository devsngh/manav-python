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


T = TypeVar("T", bound="PromptUpdate")


@_attrs_define
class PromptUpdate:
    """
    Attributes:
        category (None | str | Unset):
        sub_category (None | str | Unset):
        status (None | PromptStatus | Unset):
        prompt_role (None | PromptRole | Unset):
        description (None | str | Unset):
        allowed_tools (list[str] | None | Unset):
        components (list[PromptComponentCreate] | None | Unset):
    """

    category: None | str | Unset = UNSET
    sub_category: None | str | Unset = UNSET
    status: None | PromptStatus | Unset = UNSET
    prompt_role: None | PromptRole | Unset = UNSET
    description: None | str | Unset = UNSET
    allowed_tools: list[str] | None | Unset = UNSET
    components: list[PromptComponentCreate] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PromptStatus):
            status = self.status.value
        else:
            status = self.status

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

        allowed_tools: list[str] | None | Unset
        if isinstance(self.allowed_tools, Unset):
            allowed_tools = UNSET
        elif isinstance(self.allowed_tools, list):
            allowed_tools = self.allowed_tools

        else:
            allowed_tools = self.allowed_tools

        components: list[dict[str, Any]] | None | Unset
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, list):
            components = []
            for components_type_0_item_data in self.components:
                components_type_0_item = components_type_0_item_data.to_dict()
                components.append(components_type_0_item)

        else:
            components = self.components

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        def _parse_status(data: object) -> None | PromptStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = PromptStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_allowed_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tools_type_0 = cast(list[str], data)

                return allowed_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_tools = _parse_allowed_tools(d.pop("allowed_tools", UNSET))

        def _parse_components(data: object) -> list[PromptComponentCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                components_type_0 = []
                _components_type_0 = data
                for components_type_0_item_data in _components_type_0:
                    components_type_0_item = PromptComponentCreate.from_dict(components_type_0_item_data)

                    components_type_0.append(components_type_0_item)

                return components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PromptComponentCreate] | None | Unset, data)

        components = _parse_components(d.pop("components", UNSET))

        prompt_update = cls(
            category=category,
            sub_category=sub_category,
            status=status,
            prompt_role=prompt_role,
            description=description,
            allowed_tools=allowed_tools,
            components=components,
        )

        prompt_update.additional_properties = d
        return prompt_update

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
