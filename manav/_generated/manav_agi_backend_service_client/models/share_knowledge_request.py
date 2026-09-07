from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareKnowledgeRequest")


@_attrs_define
class ShareKnowledgeRequest:
    """
    Attributes:
        content (str):
        tags (list[str] | Unset):
        relevant_departments (list[str] | Unset):
        bot_name (None | str | Unset):
    """

    content: str
    tags: list[str] | Unset = UNSET
    relevant_departments: list[str] | Unset = UNSET
    bot_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        relevant_departments: list[str] | Unset = UNSET
        if not isinstance(self.relevant_departments, Unset):
            relevant_departments = self.relevant_departments

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if relevant_departments is not UNSET:
            field_dict["relevant_departments"] = relevant_departments
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        tags = cast(list[str], d.pop("tags", UNSET))

        relevant_departments = cast(list[str], d.pop("relevant_departments", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        share_knowledge_request = cls(
            content=content,
            tags=tags,
            relevant_departments=relevant_departments,
            bot_name=bot_name,
        )

        share_knowledge_request.additional_properties = d
        return share_knowledge_request

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
