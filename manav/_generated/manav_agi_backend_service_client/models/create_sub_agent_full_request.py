from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_ref import PromptRef


T = TypeVar("T", bound="CreateSubAgentFullRequest")


@_attrs_define
class CreateSubAgentFullRequest:
    """
    Attributes:
        name (str):
        description (str):
        system_prompt (PromptRef): Reference to a prompt — either an existing ID or text to create a new one.
        agent_type (str | Unset):  Default: 'standard'.
        skills (list[PromptRef] | None | Unset):
        guardrails (list[PromptRef] | None | Unset):
        policies (list[PromptRef] | None | Unset):
        allowed_tool_ids (list[str] | None | Unset):
        datasource_ids (list[str] | None | Unset):
        model_id (None | str | Unset):
        wire_into_config_id (None | str | Unset):
    """

    name: str
    description: str
    system_prompt: PromptRef
    agent_type: str | Unset = "standard"
    skills: list[PromptRef] | None | Unset = UNSET
    guardrails: list[PromptRef] | None | Unset = UNSET
    policies: list[PromptRef] | None | Unset = UNSET
    allowed_tool_ids: list[str] | None | Unset = UNSET
    datasource_ids: list[str] | None | Unset = UNSET
    model_id: None | str | Unset = UNSET
    wire_into_config_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        system_prompt = self.system_prompt.to_dict()

        agent_type = self.agent_type

        skills: list[dict[str, Any]] | None | Unset
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = []
            for skills_type_0_item_data in self.skills:
                skills_type_0_item = skills_type_0_item_data.to_dict()
                skills.append(skills_type_0_item)

        else:
            skills = self.skills

        guardrails: list[dict[str, Any]] | None | Unset
        if isinstance(self.guardrails, Unset):
            guardrails = UNSET
        elif isinstance(self.guardrails, list):
            guardrails = []
            for guardrails_type_0_item_data in self.guardrails:
                guardrails_type_0_item = guardrails_type_0_item_data.to_dict()
                guardrails.append(guardrails_type_0_item)

        else:
            guardrails = self.guardrails

        policies: list[dict[str, Any]] | None | Unset
        if isinstance(self.policies, Unset):
            policies = UNSET
        elif isinstance(self.policies, list):
            policies = []
            for policies_type_0_item_data in self.policies:
                policies_type_0_item = policies_type_0_item_data.to_dict()
                policies.append(policies_type_0_item)

        else:
            policies = self.policies

        allowed_tool_ids: list[str] | None | Unset
        if isinstance(self.allowed_tool_ids, Unset):
            allowed_tool_ids = UNSET
        elif isinstance(self.allowed_tool_ids, list):
            allowed_tool_ids = self.allowed_tool_ids

        else:
            allowed_tool_ids = self.allowed_tool_ids

        datasource_ids: list[str] | None | Unset
        if isinstance(self.datasource_ids, Unset):
            datasource_ids = UNSET
        elif isinstance(self.datasource_ids, list):
            datasource_ids = self.datasource_ids

        else:
            datasource_ids = self.datasource_ids

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        wire_into_config_id: None | str | Unset
        if isinstance(self.wire_into_config_id, Unset):
            wire_into_config_id = UNSET
        else:
            wire_into_config_id = self.wire_into_config_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "system_prompt": system_prompt,
            }
        )
        if agent_type is not UNSET:
            field_dict["agent_type"] = agent_type
        if skills is not UNSET:
            field_dict["skills"] = skills
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if policies is not UNSET:
            field_dict["policies"] = policies
        if allowed_tool_ids is not UNSET:
            field_dict["allowed_tool_ids"] = allowed_tool_ids
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if wire_into_config_id is not UNSET:
            field_dict["wire_into_config_id"] = wire_into_config_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        system_prompt = PromptRef.from_dict(d.pop("system_prompt"))

        agent_type = d.pop("agent_type", UNSET)

        def _parse_skills(data: object) -> list[PromptRef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = []
                _skills_type_0 = data
                for skills_type_0_item_data in _skills_type_0:
                    skills_type_0_item = PromptRef.from_dict(skills_type_0_item_data)

                    skills_type_0.append(skills_type_0_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PromptRef] | None | Unset, data)

        skills = _parse_skills(d.pop("skills", UNSET))

        def _parse_guardrails(data: object) -> list[PromptRef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrails_type_0 = []
                _guardrails_type_0 = data
                for guardrails_type_0_item_data in _guardrails_type_0:
                    guardrails_type_0_item = PromptRef.from_dict(guardrails_type_0_item_data)

                    guardrails_type_0.append(guardrails_type_0_item)

                return guardrails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PromptRef] | None | Unset, data)

        guardrails = _parse_guardrails(d.pop("guardrails", UNSET))

        def _parse_policies(data: object) -> list[PromptRef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = []
                _policies_type_0 = data
                for policies_type_0_item_data in _policies_type_0:
                    policies_type_0_item = PromptRef.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PromptRef] | None | Unset, data)

        policies = _parse_policies(d.pop("policies", UNSET))

        def _parse_allowed_tool_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tool_ids_type_0 = cast(list[str], data)

                return allowed_tool_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_tool_ids = _parse_allowed_tool_ids(d.pop("allowed_tool_ids", UNSET))

        def _parse_datasource_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                datasource_ids_type_0 = cast(list[str], data)

                return datasource_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        datasource_ids = _parse_datasource_ids(d.pop("datasource_ids", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_wire_into_config_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wire_into_config_id = _parse_wire_into_config_id(d.pop("wire_into_config_id", UNSET))

        create_sub_agent_full_request = cls(
            name=name,
            description=description,
            system_prompt=system_prompt,
            agent_type=agent_type,
            skills=skills,
            guardrails=guardrails,
            policies=policies,
            allowed_tool_ids=allowed_tool_ids,
            datasource_ids=datasource_ids,
            model_id=model_id,
            wire_into_config_id=wire_into_config_id,
        )

        create_sub_agent_full_request.additional_properties = d
        return create_sub_agent_full_request

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
