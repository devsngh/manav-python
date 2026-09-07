from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepAgentUserExtensionResponse")


@_attrs_define
class DeepAgentUserExtensionResponse:
    """Always returned — an empty row (all lists = [], override = null)
    means the user has no extensions on this agent yet.

        Attributes:
            deepagent_id (UUID):
            user_id (UUID):
            extra_skill_ids (list[str] | Unset):
            extra_datasource_ids (list[str] | Unset):
            extra_hil_rule_ids (list[str] | Unset):
            extra_guardrail_ids (list[str] | Unset):
            extra_policy_ids (list[str] | Unset):
            extra_subagent_ids (list[str] | Unset):
            model_id_override (None | str | Unset):
            name_override (None | str | Unset):
            profile_picture_override (None | str | Unset):
    """

    deepagent_id: UUID
    user_id: UUID
    extra_skill_ids: list[str] | Unset = UNSET
    extra_datasource_ids: list[str] | Unset = UNSET
    extra_hil_rule_ids: list[str] | Unset = UNSET
    extra_guardrail_ids: list[str] | Unset = UNSET
    extra_policy_ids: list[str] | Unset = UNSET
    extra_subagent_ids: list[str] | Unset = UNSET
    model_id_override: None | str | Unset = UNSET
    name_override: None | str | Unset = UNSET
    profile_picture_override: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deepagent_id = str(self.deepagent_id)

        user_id = str(self.user_id)

        extra_skill_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_skill_ids, Unset):
            extra_skill_ids = self.extra_skill_ids

        extra_datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_datasource_ids, Unset):
            extra_datasource_ids = self.extra_datasource_ids

        extra_hil_rule_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_hil_rule_ids, Unset):
            extra_hil_rule_ids = self.extra_hil_rule_ids

        extra_guardrail_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_guardrail_ids, Unset):
            extra_guardrail_ids = self.extra_guardrail_ids

        extra_policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_policy_ids, Unset):
            extra_policy_ids = self.extra_policy_ids

        extra_subagent_ids: list[str] | Unset = UNSET
        if not isinstance(self.extra_subagent_ids, Unset):
            extra_subagent_ids = self.extra_subagent_ids

        model_id_override: None | str | Unset
        if isinstance(self.model_id_override, Unset):
            model_id_override = UNSET
        else:
            model_id_override = self.model_id_override

        name_override: None | str | Unset
        if isinstance(self.name_override, Unset):
            name_override = UNSET
        else:
            name_override = self.name_override

        profile_picture_override: None | str | Unset
        if isinstance(self.profile_picture_override, Unset):
            profile_picture_override = UNSET
        else:
            profile_picture_override = self.profile_picture_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deepagent_id": deepagent_id,
                "user_id": user_id,
            }
        )
        if extra_skill_ids is not UNSET:
            field_dict["extra_skill_ids"] = extra_skill_ids
        if extra_datasource_ids is not UNSET:
            field_dict["extra_datasource_ids"] = extra_datasource_ids
        if extra_hil_rule_ids is not UNSET:
            field_dict["extra_hil_rule_ids"] = extra_hil_rule_ids
        if extra_guardrail_ids is not UNSET:
            field_dict["extra_guardrail_ids"] = extra_guardrail_ids
        if extra_policy_ids is not UNSET:
            field_dict["extra_policy_ids"] = extra_policy_ids
        if extra_subagent_ids is not UNSET:
            field_dict["extra_subagent_ids"] = extra_subagent_ids
        if model_id_override is not UNSET:
            field_dict["model_id_override"] = model_id_override
        if name_override is not UNSET:
            field_dict["name_override"] = name_override
        if profile_picture_override is not UNSET:
            field_dict["profile_picture_override"] = profile_picture_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deepagent_id = UUID(d.pop("deepagent_id"))

        user_id = UUID(d.pop("user_id"))

        extra_skill_ids = cast(list[str], d.pop("extra_skill_ids", UNSET))

        extra_datasource_ids = cast(list[str], d.pop("extra_datasource_ids", UNSET))

        extra_hil_rule_ids = cast(list[str], d.pop("extra_hil_rule_ids", UNSET))

        extra_guardrail_ids = cast(list[str], d.pop("extra_guardrail_ids", UNSET))

        extra_policy_ids = cast(list[str], d.pop("extra_policy_ids", UNSET))

        extra_subagent_ids = cast(list[str], d.pop("extra_subagent_ids", UNSET))

        def _parse_model_id_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id_override = _parse_model_id_override(d.pop("model_id_override", UNSET))

        def _parse_name_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_override = _parse_name_override(d.pop("name_override", UNSET))

        def _parse_profile_picture_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_override = _parse_profile_picture_override(d.pop("profile_picture_override", UNSET))

        deep_agent_user_extension_response = cls(
            deepagent_id=deepagent_id,
            user_id=user_id,
            extra_skill_ids=extra_skill_ids,
            extra_datasource_ids=extra_datasource_ids,
            extra_hil_rule_ids=extra_hil_rule_ids,
            extra_guardrail_ids=extra_guardrail_ids,
            extra_policy_ids=extra_policy_ids,
            extra_subagent_ids=extra_subagent_ids,
            model_id_override=model_id_override,
            name_override=name_override,
            profile_picture_override=profile_picture_override,
        )

        deep_agent_user_extension_response.additional_properties = d
        return deep_agent_user_extension_response

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
