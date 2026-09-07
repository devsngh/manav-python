from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentsMdWriteBack")


@_attrs_define
class AgentsMdWriteBack:
    """
    Attributes:
        agents_md_content (str):
        change_summary (None | str | Unset):
    """

    agents_md_content: str
    change_summary: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents_md_content = self.agents_md_content

        change_summary: None | str | Unset
        if isinstance(self.change_summary, Unset):
            change_summary = UNSET
        else:
            change_summary = self.change_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents_md_content": agents_md_content,
            }
        )
        if change_summary is not UNSET:
            field_dict["change_summary"] = change_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agents_md_content = d.pop("agents_md_content")

        def _parse_change_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_summary = _parse_change_summary(d.pop("change_summary", UNSET))

        agents_md_write_back = cls(
            agents_md_content=agents_md_content,
            change_summary=change_summary,
        )

        agents_md_write_back.additional_properties = d
        return agents_md_write_back

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
