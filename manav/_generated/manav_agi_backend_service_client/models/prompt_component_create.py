from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromptComponentCreate")


@_attrs_define
class PromptComponentCreate:
    """
    Attributes:
        component_definition_id (str):
        component_content (None | str | Unset):
        order (int | Unset):  Default: 0.
    """

    component_definition_id: str
    component_content: None | str | Unset = UNSET
    order: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_definition_id = self.component_definition_id

        component_content: None | str | Unset
        if isinstance(self.component_content, Unset):
            component_content = UNSET
        else:
            component_content = self.component_content

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_definition_id": component_definition_id,
            }
        )
        if component_content is not UNSET:
            field_dict["component_content"] = component_content
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_definition_id = d.pop("component_definition_id")

        def _parse_component_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        component_content = _parse_component_content(d.pop("component_content", UNSET))

        order = d.pop("order", UNSET)

        prompt_component_create = cls(
            component_definition_id=component_definition_id,
            component_content=component_content,
            order=order,
        )

        prompt_component_create.additional_properties = d
        return prompt_component_create

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
