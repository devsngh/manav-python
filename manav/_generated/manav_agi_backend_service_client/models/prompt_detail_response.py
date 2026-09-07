from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.prompt_role import PromptRole
from ..models.prompt_status import PromptStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_component_response import PromptComponentResponse


T = TypeVar("T", bound="PromptDetailResponse")


@_attrs_define
class PromptDetailResponse:
    """Extended response with components

    Attributes:
        id (UUID):
        prompt_name (str):
        category (None | str):
        sub_category (None | str):
        status (PromptStatus): Prompt lifecycle status
        version (str):
        compiled_prompt (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        prompt_role (None | PromptRole | Unset):
        description (None | str | Unset):
        allowed_tools (list[str] | Unset):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        components (list[PromptComponentResponse] | Unset):
    """

    id: UUID
    prompt_name: str
    category: None | str
    sub_category: None | str
    status: PromptStatus
    version: str
    compiled_prompt: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    prompt_role: None | PromptRole | Unset = UNSET
    description: None | str | Unset = UNSET
    allowed_tools: list[str] | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    components: list[PromptComponentResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        prompt_name = self.prompt_name

        category: None | str
        category = self.category

        sub_category: None | str
        sub_category = self.sub_category

        status = self.status.value

        version = self.version

        compiled_prompt: None | str
        compiled_prompt = self.compiled_prompt

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

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
                "id": id,
                "prompt_name": prompt_name,
                "category": category,
                "sub_category": sub_category,
                "status": status,
                "version": version,
                "compiled_prompt": compiled_prompt,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if prompt_role is not UNSET:
            field_dict["prompt_role"] = prompt_role
        if description is not UNSET:
            field_dict["description"] = description
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if components is not UNSET:
            field_dict["components"] = components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_component_response import PromptComponentResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        prompt_name = d.pop("prompt_name")

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        def _parse_sub_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sub_category = _parse_sub_category(d.pop("sub_category"))

        status = PromptStatus(d.pop("status"))

        version = d.pop("version")

        def _parse_compiled_prompt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        compiled_prompt = _parse_compiled_prompt(d.pop("compiled_prompt"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        _components = d.pop("components", UNSET)
        components: list[PromptComponentResponse] | Unset = UNSET
        if _components is not UNSET:
            components = []
            for components_item_data in _components:
                components_item = PromptComponentResponse.from_dict(components_item_data)

                components.append(components_item)

        prompt_detail_response = cls(
            id=id,
            prompt_name=prompt_name,
            category=category,
            sub_category=sub_category,
            status=status,
            version=version,
            compiled_prompt=compiled_prompt,
            created_at=created_at,
            updated_at=updated_at,
            prompt_role=prompt_role,
            description=description,
            allowed_tools=allowed_tools,
            created_by=created_by,
            updated_by=updated_by,
            components=components,
        )

        prompt_detail_response.additional_properties = d
        return prompt_detail_response

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
