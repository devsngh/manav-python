from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeprecateSubAgentRequest")


@_attrs_define
class DeprecateSubAgentRequest:
    """
    Attributes:
        subagent_id (str):
        replacement_id (None | str | Unset):
    """

    subagent_id: str
    replacement_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subagent_id = self.subagent_id

        replacement_id: None | str | Unset
        if isinstance(self.replacement_id, Unset):
            replacement_id = UNSET
        else:
            replacement_id = self.replacement_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subagent_id": subagent_id,
            }
        )
        if replacement_id is not UNSET:
            field_dict["replacement_id"] = replacement_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subagent_id = d.pop("subagent_id")

        def _parse_replacement_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replacement_id = _parse_replacement_id(d.pop("replacement_id", UNSET))

        deprecate_sub_agent_request = cls(
            subagent_id=subagent_id,
            replacement_id=replacement_id,
        )

        deprecate_sub_agent_request.additional_properties = d
        return deprecate_sub_agent_request

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
