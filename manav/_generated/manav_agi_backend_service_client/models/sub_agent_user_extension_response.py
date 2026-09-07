from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubAgentUserExtensionResponse")


@_attrs_define
class SubAgentUserExtensionResponse:
    """Always returned. model_id_override=null means the caller hasn't set one.

    Attributes:
        subagent_id (UUID):
        user_id (UUID):
        model_id_override (None | str | Unset):
    """

    subagent_id: UUID
    user_id: UUID
    model_id_override: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subagent_id = str(self.subagent_id)

        user_id = str(self.user_id)

        model_id_override: None | str | Unset
        if isinstance(self.model_id_override, Unset):
            model_id_override = UNSET
        else:
            model_id_override = self.model_id_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subagent_id": subagent_id,
                "user_id": user_id,
            }
        )
        if model_id_override is not UNSET:
            field_dict["model_id_override"] = model_id_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subagent_id = UUID(d.pop("subagent_id"))

        user_id = UUID(d.pop("user_id"))

        def _parse_model_id_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id_override = _parse_model_id_override(d.pop("model_id_override", UNSET))

        sub_agent_user_extension_response = cls(
            subagent_id=subagent_id,
            user_id=user_id,
            model_id_override=model_id_override,
        )

        sub_agent_user_extension_response.additional_properties = d
        return sub_agent_user_extension_response

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
