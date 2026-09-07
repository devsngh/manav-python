from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_ref import PromptRef
    from ..models.sub_agent_def import SubAgentDef


T = TypeVar("T", bound="OnboardDomainRequest")


@_attrs_define
class OnboardDomainRequest:
    """
    Attributes:
        department_name (str):
        position_title (str):
        bot_name (str):
        system_prompt (PromptRef): Reference to a prompt — either an existing ID or text to create a new one.
        config_name (None | str | Unset):
        description (None | str | Unset):
        skills (list[PromptRef] | None | Unset):
        guardrails (list[PromptRef] | None | Unset):
        policies (list[PromptRef] | None | Unset):
        format_instruction (None | PromptRef | Unset):
        subagents (list[SubAgentDef] | None | Unset):
        datasource_ids (list[str] | None | Unset):
        internal_tool_ids (list[str] | None | Unset):
        hil_rule_ids (list[str] | None | Unset):
        model_id (None | str | Unset):
        agents_md_content (None | str | Unset):
        create_social_group (bool | Unset):  Default: True.
    """

    department_name: str
    position_title: str
    bot_name: str
    system_prompt: PromptRef
    config_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    skills: list[PromptRef] | None | Unset = UNSET
    guardrails: list[PromptRef] | None | Unset = UNSET
    policies: list[PromptRef] | None | Unset = UNSET
    format_instruction: None | PromptRef | Unset = UNSET
    subagents: list[SubAgentDef] | None | Unset = UNSET
    datasource_ids: list[str] | None | Unset = UNSET
    internal_tool_ids: list[str] | None | Unset = UNSET
    hil_rule_ids: list[str] | None | Unset = UNSET
    model_id: None | str | Unset = UNSET
    agents_md_content: None | str | Unset = UNSET
    create_social_group: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415

        department_name = self.department_name

        position_title = self.position_title

        bot_name = self.bot_name

        system_prompt = self.system_prompt.to_dict()

        config_name: None | str | Unset
        if isinstance(self.config_name, Unset):
            config_name = UNSET
        else:
            config_name = self.config_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        format_instruction: dict[str, Any] | None | Unset
        if isinstance(self.format_instruction, Unset):
            format_instruction = UNSET
        elif isinstance(self.format_instruction, PromptRef):
            format_instruction = self.format_instruction.to_dict()
        else:
            format_instruction = self.format_instruction

        subagents: list[dict[str, Any]] | None | Unset
        if isinstance(self.subagents, Unset):
            subagents = UNSET
        elif isinstance(self.subagents, list):
            subagents = []
            for subagents_type_0_item_data in self.subagents:
                subagents_type_0_item = subagents_type_0_item_data.to_dict()
                subagents.append(subagents_type_0_item)

        else:
            subagents = self.subagents

        datasource_ids: list[str] | None | Unset
        if isinstance(self.datasource_ids, Unset):
            datasource_ids = UNSET
        elif isinstance(self.datasource_ids, list):
            datasource_ids = self.datasource_ids

        else:
            datasource_ids = self.datasource_ids

        internal_tool_ids: list[str] | None | Unset
        if isinstance(self.internal_tool_ids, Unset):
            internal_tool_ids = UNSET
        elif isinstance(self.internal_tool_ids, list):
            internal_tool_ids = self.internal_tool_ids

        else:
            internal_tool_ids = self.internal_tool_ids

        hil_rule_ids: list[str] | None | Unset
        if isinstance(self.hil_rule_ids, Unset):
            hil_rule_ids = UNSET
        elif isinstance(self.hil_rule_ids, list):
            hil_rule_ids = self.hil_rule_ids

        else:
            hil_rule_ids = self.hil_rule_ids

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        agents_md_content: None | str | Unset
        if isinstance(self.agents_md_content, Unset):
            agents_md_content = UNSET
        else:
            agents_md_content = self.agents_md_content

        create_social_group = self.create_social_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "department_name": department_name,
                "position_title": position_title,
                "bot_name": bot_name,
                "system_prompt": system_prompt,
            }
        )
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if description is not UNSET:
            field_dict["description"] = description
        if skills is not UNSET:
            field_dict["skills"] = skills
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if policies is not UNSET:
            field_dict["policies"] = policies
        if format_instruction is not UNSET:
            field_dict["format_instruction"] = format_instruction
        if subagents is not UNSET:
            field_dict["subagents"] = subagents
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if internal_tool_ids is not UNSET:
            field_dict["internal_tool_ids"] = internal_tool_ids
        if hil_rule_ids is not UNSET:
            field_dict["hil_rule_ids"] = hil_rule_ids
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if agents_md_content is not UNSET:
            field_dict["agents_md_content"] = agents_md_content
        if create_social_group is not UNSET:
            field_dict["create_social_group"] = create_social_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415
        from ..models.sub_agent_def import SubAgentDef  # noqa: PLC0415

        d = dict(src_dict)
        department_name = d.pop("department_name")

        position_title = d.pop("position_title")

        bot_name = d.pop("bot_name")

        system_prompt = PromptRef.from_dict(d.pop("system_prompt"))

        def _parse_config_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        config_name = _parse_config_name(d.pop("config_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_format_instruction(data: object) -> None | PromptRef | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                format_instruction_type_0 = PromptRef.from_dict(data)

                return format_instruction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromptRef | Unset, data)

        format_instruction = _parse_format_instruction(d.pop("format_instruction", UNSET))

        def _parse_subagents(data: object) -> list[SubAgentDef] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subagents_type_0 = []
                _subagents_type_0 = data
                for subagents_type_0_item_data in _subagents_type_0:
                    subagents_type_0_item = SubAgentDef.from_dict(subagents_type_0_item_data)

                    subagents_type_0.append(subagents_type_0_item)

                return subagents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SubAgentDef] | None | Unset, data)

        subagents = _parse_subagents(d.pop("subagents", UNSET))

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

        def _parse_internal_tool_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_tool_ids_type_0 = cast(list[str], data)

                return internal_tool_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        internal_tool_ids = _parse_internal_tool_ids(d.pop("internal_tool_ids", UNSET))

        def _parse_hil_rule_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hil_rule_ids_type_0 = cast(list[str], data)

                return hil_rule_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        hil_rule_ids = _parse_hil_rule_ids(d.pop("hil_rule_ids", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_agents_md_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agents_md_content = _parse_agents_md_content(d.pop("agents_md_content", UNSET))

        create_social_group = d.pop("create_social_group", UNSET)

        onboard_domain_request = cls(
            department_name=department_name,
            position_title=position_title,
            bot_name=bot_name,
            system_prompt=system_prompt,
            config_name=config_name,
            description=description,
            skills=skills,
            guardrails=guardrails,
            policies=policies,
            format_instruction=format_instruction,
            subagents=subagents,
            datasource_ids=datasource_ids,
            internal_tool_ids=internal_tool_ids,
            hil_rule_ids=hil_rule_ids,
            model_id=model_id,
            agents_md_content=agents_md_content,
            create_social_group=create_social_group,
        )

        onboard_domain_request.additional_properties = d
        return onboard_domain_request

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
