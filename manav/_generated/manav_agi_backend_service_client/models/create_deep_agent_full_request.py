from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_deep_agent_full_request_middleware_config_type_0 import (
        CreateDeepAgentFullRequestMiddlewareConfigType0,
    )
    from ..models.create_deep_agent_full_request_response_format_schema_type_0 import (
        CreateDeepAgentFullRequestResponseFormatSchemaType0,
    )
    from ..models.prompt_ref import PromptRef
    from ..models.sub_agent_def import SubAgentDef


T = TypeVar("T", bound="CreateDeepAgentFullRequest")


@_attrs_define
class CreateDeepAgentFullRequest:
    """
    Attributes:
        name (str):
        system_prompt (PromptRef): Reference to a prompt — either an existing ID or text to create a new one.
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
        assign_to_bot_id (None | str | Unset):
        backend_type (None | str | Unset):
        debug_mode (bool | Unset):  Default: False.
        middleware_config (CreateDeepAgentFullRequestMiddlewareConfigType0 | None | Unset):
        workspace_ids (list[str] | None | Unset):
        agent_name (None | str | Unset):
        cache_type (None | str | Unset):
        response_format_schema (CreateDeepAgentFullRequestResponseFormatSchemaType0 | None | Unset):
        excluded_tools (list[str] | None | Unset):
    """

    name: str
    system_prompt: PromptRef
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
    assign_to_bot_id: None | str | Unset = UNSET
    backend_type: None | str | Unset = UNSET
    debug_mode: bool | Unset = False
    middleware_config: CreateDeepAgentFullRequestMiddlewareConfigType0 | None | Unset = UNSET
    workspace_ids: list[str] | None | Unset = UNSET
    agent_name: None | str | Unset = UNSET
    cache_type: None | str | Unset = UNSET
    response_format_schema: CreateDeepAgentFullRequestResponseFormatSchemaType0 | None | Unset = UNSET
    excluded_tools: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_deep_agent_full_request_middleware_config_type_0 import (
            CreateDeepAgentFullRequestMiddlewareConfigType0,  # noqa: PLC0415
        )
        from ..models.create_deep_agent_full_request_response_format_schema_type_0 import (
            CreateDeepAgentFullRequestResponseFormatSchemaType0,  # noqa: PLC0415
        )
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415

        name = self.name

        system_prompt = self.system_prompt.to_dict()

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

        assign_to_bot_id: None | str | Unset
        if isinstance(self.assign_to_bot_id, Unset):
            assign_to_bot_id = UNSET
        else:
            assign_to_bot_id = self.assign_to_bot_id

        backend_type: None | str | Unset
        if isinstance(self.backend_type, Unset):
            backend_type = UNSET
        else:
            backend_type = self.backend_type

        debug_mode = self.debug_mode

        middleware_config: dict[str, Any] | None | Unset
        if isinstance(self.middleware_config, Unset):
            middleware_config = UNSET
        elif isinstance(self.middleware_config, CreateDeepAgentFullRequestMiddlewareConfigType0):
            middleware_config = self.middleware_config.to_dict()
        else:
            middleware_config = self.middleware_config

        workspace_ids: list[str] | None | Unset
        if isinstance(self.workspace_ids, Unset):
            workspace_ids = UNSET
        elif isinstance(self.workspace_ids, list):
            workspace_ids = self.workspace_ids

        else:
            workspace_ids = self.workspace_ids

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        cache_type: None | str | Unset
        if isinstance(self.cache_type, Unset):
            cache_type = UNSET
        else:
            cache_type = self.cache_type

        response_format_schema: dict[str, Any] | None | Unset
        if isinstance(self.response_format_schema, Unset):
            response_format_schema = UNSET
        elif isinstance(self.response_format_schema, CreateDeepAgentFullRequestResponseFormatSchemaType0):
            response_format_schema = self.response_format_schema.to_dict()
        else:
            response_format_schema = self.response_format_schema

        excluded_tools: list[str] | None | Unset
        if isinstance(self.excluded_tools, Unset):
            excluded_tools = UNSET
        elif isinstance(self.excluded_tools, list):
            excluded_tools = self.excluded_tools

        else:
            excluded_tools = self.excluded_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "system_prompt": system_prompt,
            }
        )
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
        if assign_to_bot_id is not UNSET:
            field_dict["assign_to_bot_id"] = assign_to_bot_id
        if backend_type is not UNSET:
            field_dict["backend_type"] = backend_type
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if middleware_config is not UNSET:
            field_dict["middleware_config"] = middleware_config
        if workspace_ids is not UNSET:
            field_dict["workspace_ids"] = workspace_ids
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if cache_type is not UNSET:
            field_dict["cache_type"] = cache_type
        if response_format_schema is not UNSET:
            field_dict["response_format_schema"] = response_format_schema
        if excluded_tools is not UNSET:
            field_dict["excluded_tools"] = excluded_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_deep_agent_full_request_middleware_config_type_0 import (
            CreateDeepAgentFullRequestMiddlewareConfigType0,  # noqa: PLC0415
        )
        from ..models.create_deep_agent_full_request_response_format_schema_type_0 import (
            CreateDeepAgentFullRequestResponseFormatSchemaType0,  # noqa: PLC0415
        )
        from ..models.prompt_ref import PromptRef  # noqa: PLC0415
        from ..models.sub_agent_def import SubAgentDef  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        system_prompt = PromptRef.from_dict(d.pop("system_prompt"))

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

        def _parse_assign_to_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_bot_id = _parse_assign_to_bot_id(d.pop("assign_to_bot_id", UNSET))

        def _parse_backend_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backend_type = _parse_backend_type(d.pop("backend_type", UNSET))

        debug_mode = d.pop("debug_mode", UNSET)

        def _parse_middleware_config(data: object) -> CreateDeepAgentFullRequestMiddlewareConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                middleware_config_type_0 = CreateDeepAgentFullRequestMiddlewareConfigType0.from_dict(data)

                return middleware_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateDeepAgentFullRequestMiddlewareConfigType0 | None | Unset, data)

        middleware_config = _parse_middleware_config(d.pop("middleware_config", UNSET))

        def _parse_workspace_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                workspace_ids_type_0 = cast(list[str], data)

                return workspace_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        workspace_ids = _parse_workspace_ids(d.pop("workspace_ids", UNSET))

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        def _parse_cache_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_type = _parse_cache_type(d.pop("cache_type", UNSET))

        def _parse_response_format_schema(
            data: object,
        ) -> CreateDeepAgentFullRequestResponseFormatSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_schema_type_0 = CreateDeepAgentFullRequestResponseFormatSchemaType0.from_dict(data)

                return response_format_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateDeepAgentFullRequestResponseFormatSchemaType0 | None | Unset, data)

        response_format_schema = _parse_response_format_schema(d.pop("response_format_schema", UNSET))

        def _parse_excluded_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                excluded_tools_type_0 = cast(list[str], data)

                return excluded_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        excluded_tools = _parse_excluded_tools(d.pop("excluded_tools", UNSET))

        create_deep_agent_full_request = cls(
            name=name,
            system_prompt=system_prompt,
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
            assign_to_bot_id=assign_to_bot_id,
            backend_type=backend_type,
            debug_mode=debug_mode,
            middleware_config=middleware_config,
            workspace_ids=workspace_ids,
            agent_name=agent_name,
            cache_type=cache_type,
            response_format_schema=response_format_schema,
            excluded_tools=excluded_tools,
        )

        create_deep_agent_full_request.additional_properties = d
        return create_deep_agent_full_request

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
