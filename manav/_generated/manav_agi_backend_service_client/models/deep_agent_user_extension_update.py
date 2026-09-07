from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeepAgentUserExtensionUpdate")


@_attrs_define
class DeepAgentUserExtensionUpdate:
    """PUT payload — any subset. Missing fields are left unchanged; sending
    an empty list clears that field. model_id_override=null / name_override=
    null / profile_picture_override=null explicitly clears that field (fall
    back to publisher's arch value).

        Attributes:
            extra_skill_ids (list[str] | None | Unset):
            extra_datasource_ids (list[str] | None | Unset):
            extra_hil_rule_ids (list[str] | None | Unset):
            extra_guardrail_ids (list[str] | None | Unset):
            extra_policy_ids (list[str] | None | Unset):
            extra_subagent_ids (list[str] | None | Unset):
            model_id_override (None | str | Unset):
            name_override (None | str | Unset):
            profile_picture_override (None | str | Unset):
    """

    extra_skill_ids: list[str] | None | Unset = UNSET
    extra_datasource_ids: list[str] | None | Unset = UNSET
    extra_hil_rule_ids: list[str] | None | Unset = UNSET
    extra_guardrail_ids: list[str] | None | Unset = UNSET
    extra_policy_ids: list[str] | None | Unset = UNSET
    extra_subagent_ids: list[str] | None | Unset = UNSET
    model_id_override: None | str | Unset = UNSET
    name_override: None | str | Unset = UNSET
    profile_picture_override: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extra_skill_ids: list[str] | None | Unset
        if isinstance(self.extra_skill_ids, Unset):
            extra_skill_ids = UNSET
        elif isinstance(self.extra_skill_ids, list):
            extra_skill_ids = self.extra_skill_ids

        else:
            extra_skill_ids = self.extra_skill_ids

        extra_datasource_ids: list[str] | None | Unset
        if isinstance(self.extra_datasource_ids, Unset):
            extra_datasource_ids = UNSET
        elif isinstance(self.extra_datasource_ids, list):
            extra_datasource_ids = self.extra_datasource_ids

        else:
            extra_datasource_ids = self.extra_datasource_ids

        extra_hil_rule_ids: list[str] | None | Unset
        if isinstance(self.extra_hil_rule_ids, Unset):
            extra_hil_rule_ids = UNSET
        elif isinstance(self.extra_hil_rule_ids, list):
            extra_hil_rule_ids = self.extra_hil_rule_ids

        else:
            extra_hil_rule_ids = self.extra_hil_rule_ids

        extra_guardrail_ids: list[str] | None | Unset
        if isinstance(self.extra_guardrail_ids, Unset):
            extra_guardrail_ids = UNSET
        elif isinstance(self.extra_guardrail_ids, list):
            extra_guardrail_ids = self.extra_guardrail_ids

        else:
            extra_guardrail_ids = self.extra_guardrail_ids

        extra_policy_ids: list[str] | None | Unset
        if isinstance(self.extra_policy_ids, Unset):
            extra_policy_ids = UNSET
        elif isinstance(self.extra_policy_ids, list):
            extra_policy_ids = self.extra_policy_ids

        else:
            extra_policy_ids = self.extra_policy_ids

        extra_subagent_ids: list[str] | None | Unset
        if isinstance(self.extra_subagent_ids, Unset):
            extra_subagent_ids = UNSET
        elif isinstance(self.extra_subagent_ids, list):
            extra_subagent_ids = self.extra_subagent_ids

        else:
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
        field_dict.update({})
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

        def _parse_extra_skill_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_skill_ids_type_0 = cast(list[str], data)

                return extra_skill_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_skill_ids = _parse_extra_skill_ids(d.pop("extra_skill_ids", UNSET))

        def _parse_extra_datasource_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_datasource_ids_type_0 = cast(list[str], data)

                return extra_datasource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_datasource_ids = _parse_extra_datasource_ids(d.pop("extra_datasource_ids", UNSET))

        def _parse_extra_hil_rule_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_hil_rule_ids_type_0 = cast(list[str], data)

                return extra_hil_rule_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_hil_rule_ids = _parse_extra_hil_rule_ids(d.pop("extra_hil_rule_ids", UNSET))

        def _parse_extra_guardrail_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_guardrail_ids_type_0 = cast(list[str], data)

                return extra_guardrail_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_guardrail_ids = _parse_extra_guardrail_ids(d.pop("extra_guardrail_ids", UNSET))

        def _parse_extra_policy_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_policy_ids_type_0 = cast(list[str], data)

                return extra_policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_policy_ids = _parse_extra_policy_ids(d.pop("extra_policy_ids", UNSET))

        def _parse_extra_subagent_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extra_subagent_ids_type_0 = cast(list[str], data)

                return extra_subagent_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        extra_subagent_ids = _parse_extra_subagent_ids(d.pop("extra_subagent_ids", UNSET))

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

        deep_agent_user_extension_update = cls(
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

        deep_agent_user_extension_update.additional_properties = d
        return deep_agent_user_extension_update

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
