from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_ref import PromptRef


T = TypeVar("T", bound="SubAgentDef")


@_attrs_define
class SubAgentDef:
    """SubAgent definition — either existing ID or full spec to create.

    Attributes:
        id (None | Unset | UUID):
        name (None | str | Unset):
        description (None | str | Unset):
        agent_type (str | Unset):  Default: 'standard'.
        system_prompt (None | PromptRef | Unset):
        skills (list[PromptRef] | None | Unset):
        guardrails (list[PromptRef] | None | Unset):
        policies (list[PromptRef] | None | Unset):
        allowed_tool_ids (list[str] | None | Unset):
        datasource_ids (list[str] | None | Unset):
        model_id (None | str | Unset):
    """

    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    agent_type: str | Unset = "standard"
    system_prompt: None | PromptRef | Unset = UNSET
    skills: list[PromptRef] | None | Unset = UNSET
    guardrails: list[PromptRef] | None | Unset = UNSET
    policies: list[PromptRef] | None | Unset = UNSET
    allowed_tool_ids: list[str] | None | Unset = UNSET
    datasource_ids: list[str] | None | Unset = UNSET
    model_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        agent_type = self.agent_type

        system_prompt: dict[str, Any] | None | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        elif isinstance(self.system_prompt, PromptRef):
            system_prompt = self.system_prompt.to_dict()
        else:
            system_prompt = self.system_prompt

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if agent_type is not UNSET:
            field_dict["agent_type"] = agent_type
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        agent_type = d.pop("agent_type", UNSET)

        def _parse_system_prompt(data: object) -> None | PromptRef | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                system_prompt_type_0 = PromptRef.from_dict(data)

                return system_prompt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptRef | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

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

        sub_agent_def = cls(
            id=id,
            name=name,
            description=description,
            agent_type=agent_type,
            system_prompt=system_prompt,
            skills=skills,
            guardrails=guardrails,
            policies=policies,
            allowed_tool_ids=allowed_tool_ids,
            datasource_ids=datasource_ids,
            model_id=model_id,
        )

        sub_agent_def.additional_properties = d
        return sub_agent_def

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
