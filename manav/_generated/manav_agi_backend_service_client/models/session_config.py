from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_execution_config import LLMExecutionConfig
    from ..models.session_config_filesystem_permissions_item import SessionConfigFilesystemPermissionsItem
    from ..models.session_config_memory_config_type_0 import SessionConfigMemoryConfigType0
    from ..models.session_config_middleware_config import SessionConfigMiddlewareConfig
    from ..models.session_config_response_format_schema_type_0 import SessionConfigResponseFormatSchemaType0
    from ..models.session_config_rubric_type_0 import SessionConfigRubricType0
    from ..models.session_datasource_info import SessionDatasourceInfo
    from ..models.session_hil_rule import SessionHILRule
    from ..models.session_skill_info import SessionSkillInfo
    from ..models.session_sub_agent_info import SessionSubAgentInfo
    from ..models.session_tool_info import SessionToolInfo


T = TypeVar("T", bound="SessionConfig")


@_attrs_define
class SessionConfig:
    """Complete session configuration assembled from the resolved DeepAgent.
    Returned to the orchestrator at session/thread start.

        Attributes:
            tools (list[SessionToolInfo]):
            hil_rules (list[SessionHILRule]):
            subagents (list[SessionSubAgentInfo]):
            resolved_via (str):
            deepagent_id (None | str | Unset):
            deepagent_name (None | str | Unset):
            model_id (None | str | Unset):
            llm_config (LLMExecutionConfig | None | Unset):
            system_prompt (None | str | Unset):
            datasources (list[SessionDatasourceInfo] | Unset):
            memory_config (None | SessionConfigMemoryConfigType0 | Unset):
            agent_name (None | str | Unset):
            skills (list[SessionSkillInfo] | Unset):
            agents_md_content (None | str | Unset):
            backend_type (None | str | Unset):
            debug_mode (bool | Unset):  Default: False.
            cache_type (None | str | Unset):
            response_format_schema (None | SessionConfigResponseFormatSchemaType0 | Unset):
            guardrails_text (None | str | Unset):
            policies_text (None | str | Unset):
            format_instruction (None | str | Unset):
            bot_id (None | str | Unset):
            workspace_ids (list[str] | Unset):
            middleware_config (SessionConfigMiddlewareConfig | Unset):
            harness_profile (None | str | Unset):
            filesystem_permissions (list[SessionConfigFilesystemPermissionsItem] | Unset):
            rubric (None | SessionConfigRubricType0 | Unset):
            excluded_tools (list[str] | Unset):
            bot_name_override (None | str | Unset):
    """

    tools: list[SessionToolInfo]
    hil_rules: list[SessionHILRule]
    subagents: list[SessionSubAgentInfo]
    resolved_via: str
    deepagent_id: None | str | Unset = UNSET
    deepagent_name: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    llm_config: LLMExecutionConfig | None | Unset = UNSET
    system_prompt: None | str | Unset = UNSET
    datasources: list[SessionDatasourceInfo] | Unset = UNSET
    memory_config: None | SessionConfigMemoryConfigType0 | Unset = UNSET
    agent_name: None | str | Unset = UNSET
    skills: list[SessionSkillInfo] | Unset = UNSET
    agents_md_content: None | str | Unset = UNSET
    backend_type: None | str | Unset = UNSET
    debug_mode: bool | Unset = False
    cache_type: None | str | Unset = UNSET
    response_format_schema: None | SessionConfigResponseFormatSchemaType0 | Unset = UNSET
    guardrails_text: None | str | Unset = UNSET
    policies_text: None | str | Unset = UNSET
    format_instruction: None | str | Unset = UNSET
    bot_id: None | str | Unset = UNSET
    workspace_ids: list[str] | Unset = UNSET
    middleware_config: SessionConfigMiddlewareConfig | Unset = UNSET
    harness_profile: None | str | Unset = UNSET
    filesystem_permissions: list[SessionConfigFilesystemPermissionsItem] | Unset = UNSET
    rubric: None | SessionConfigRubricType0 | Unset = UNSET
    excluded_tools: list[str] | Unset = UNSET
    bot_name_override: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_execution_config import LLMExecutionConfig  # noqa: PLC0415
        from ..models.session_config_memory_config_type_0 import SessionConfigMemoryConfigType0  # noqa: PLC0415
        from ..models.session_config_response_format_schema_type_0 import (
            SessionConfigResponseFormatSchemaType0,  # noqa: PLC0415
        )
        from ..models.session_config_rubric_type_0 import SessionConfigRubricType0  # noqa: PLC0415

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        hil_rules = []
        for hil_rules_item_data in self.hil_rules:
            hil_rules_item = hil_rules_item_data.to_dict()
            hil_rules.append(hil_rules_item)

        subagents = []
        for subagents_item_data in self.subagents:
            subagents_item = subagents_item_data.to_dict()
            subagents.append(subagents_item)

        resolved_via = self.resolved_via

        deepagent_id: None | str | Unset
        if isinstance(self.deepagent_id, Unset):
            deepagent_id = UNSET
        else:
            deepagent_id = self.deepagent_id

        deepagent_name: None | str | Unset
        if isinstance(self.deepagent_name, Unset):
            deepagent_name = UNSET
        else:
            deepagent_name = self.deepagent_name

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        llm_config: dict[str, Any] | None | Unset
        if isinstance(self.llm_config, Unset):
            llm_config = UNSET
        elif isinstance(self.llm_config, LLMExecutionConfig):
            llm_config = self.llm_config.to_dict()
        else:
            llm_config = self.llm_config

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

        datasources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.datasources, Unset):
            datasources = []
            for datasources_item_data in self.datasources:
                datasources_item = datasources_item_data.to_dict()
                datasources.append(datasources_item)

        memory_config: dict[str, Any] | None | Unset
        if isinstance(self.memory_config, Unset):
            memory_config = UNSET
        elif isinstance(self.memory_config, SessionConfigMemoryConfigType0):
            memory_config = self.memory_config.to_dict()
        else:
            memory_config = self.memory_config

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        skills: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = []
            for skills_item_data in self.skills:
                skills_item = skills_item_data.to_dict()
                skills.append(skills_item)

        agents_md_content: None | str | Unset
        if isinstance(self.agents_md_content, Unset):
            agents_md_content = UNSET
        else:
            agents_md_content = self.agents_md_content

        backend_type: None | str | Unset
        if isinstance(self.backend_type, Unset):
            backend_type = UNSET
        else:
            backend_type = self.backend_type

        debug_mode = self.debug_mode

        cache_type: None | str | Unset
        if isinstance(self.cache_type, Unset):
            cache_type = UNSET
        else:
            cache_type = self.cache_type

        response_format_schema: dict[str, Any] | None | Unset
        if isinstance(self.response_format_schema, Unset):
            response_format_schema = UNSET
        elif isinstance(self.response_format_schema, SessionConfigResponseFormatSchemaType0):
            response_format_schema = self.response_format_schema.to_dict()
        else:
            response_format_schema = self.response_format_schema

        guardrails_text: None | str | Unset
        if isinstance(self.guardrails_text, Unset):
            guardrails_text = UNSET
        else:
            guardrails_text = self.guardrails_text

        policies_text: None | str | Unset
        if isinstance(self.policies_text, Unset):
            policies_text = UNSET
        else:
            policies_text = self.policies_text

        format_instruction: None | str | Unset
        if isinstance(self.format_instruction, Unset):
            format_instruction = UNSET
        else:
            format_instruction = self.format_instruction

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        workspace_ids: list[str] | Unset = UNSET
        if not isinstance(self.workspace_ids, Unset):
            workspace_ids = self.workspace_ids

        middleware_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.middleware_config, Unset):
            middleware_config = self.middleware_config.to_dict()

        harness_profile: None | str | Unset
        if isinstance(self.harness_profile, Unset):
            harness_profile = UNSET
        else:
            harness_profile = self.harness_profile

        filesystem_permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filesystem_permissions, Unset):
            filesystem_permissions = []
            for filesystem_permissions_item_data in self.filesystem_permissions:
                filesystem_permissions_item = filesystem_permissions_item_data.to_dict()
                filesystem_permissions.append(filesystem_permissions_item)

        rubric: dict[str, Any] | None | Unset
        if isinstance(self.rubric, Unset):
            rubric = UNSET
        elif isinstance(self.rubric, SessionConfigRubricType0):
            rubric = self.rubric.to_dict()
        else:
            rubric = self.rubric

        excluded_tools: list[str] | Unset = UNSET
        if not isinstance(self.excluded_tools, Unset):
            excluded_tools = self.excluded_tools

        bot_name_override: None | str | Unset
        if isinstance(self.bot_name_override, Unset):
            bot_name_override = UNSET
        else:
            bot_name_override = self.bot_name_override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tools": tools,
                "hil_rules": hil_rules,
                "subagents": subagents,
                "resolved_via": resolved_via,
            }
        )
        if deepagent_id is not UNSET:
            field_dict["deepagent_id"] = deepagent_id
        if deepagent_name is not UNSET:
            field_dict["deepagent_name"] = deepagent_name
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if llm_config is not UNSET:
            field_dict["llm_config"] = llm_config
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if datasources is not UNSET:
            field_dict["datasources"] = datasources
        if memory_config is not UNSET:
            field_dict["memory_config"] = memory_config
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if skills is not UNSET:
            field_dict["skills"] = skills
        if agents_md_content is not UNSET:
            field_dict["agents_md_content"] = agents_md_content
        if backend_type is not UNSET:
            field_dict["backend_type"] = backend_type
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if cache_type is not UNSET:
            field_dict["cache_type"] = cache_type
        if response_format_schema is not UNSET:
            field_dict["response_format_schema"] = response_format_schema
        if guardrails_text is not UNSET:
            field_dict["guardrails_text"] = guardrails_text
        if policies_text is not UNSET:
            field_dict["policies_text"] = policies_text
        if format_instruction is not UNSET:
            field_dict["format_instruction"] = format_instruction
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if workspace_ids is not UNSET:
            field_dict["workspace_ids"] = workspace_ids
        if middleware_config is not UNSET:
            field_dict["middleware_config"] = middleware_config
        if harness_profile is not UNSET:
            field_dict["harness_profile"] = harness_profile
        if filesystem_permissions is not UNSET:
            field_dict["filesystem_permissions"] = filesystem_permissions
        if rubric is not UNSET:
            field_dict["rubric"] = rubric
        if excluded_tools is not UNSET:
            field_dict["excluded_tools"] = excluded_tools
        if bot_name_override is not UNSET:
            field_dict["bot_name_override"] = bot_name_override

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_execution_config import LLMExecutionConfig  # noqa: PLC0415
        from ..models.session_config_filesystem_permissions_item import (
            SessionConfigFilesystemPermissionsItem,  # noqa: PLC0415
        )
        from ..models.session_config_memory_config_type_0 import SessionConfigMemoryConfigType0  # noqa: PLC0415
        from ..models.session_config_middleware_config import SessionConfigMiddlewareConfig  # noqa: PLC0415
        from ..models.session_config_response_format_schema_type_0 import (
            SessionConfigResponseFormatSchemaType0,  # noqa: PLC0415
        )
        from ..models.session_config_rubric_type_0 import SessionConfigRubricType0  # noqa: PLC0415
        from ..models.session_datasource_info import SessionDatasourceInfo  # noqa: PLC0415
        from ..models.session_hil_rule import SessionHILRule  # noqa: PLC0415
        from ..models.session_skill_info import SessionSkillInfo  # noqa: PLC0415
        from ..models.session_sub_agent_info import SessionSubAgentInfo  # noqa: PLC0415
        from ..models.session_tool_info import SessionToolInfo  # noqa: PLC0415

        d = dict(src_dict)
        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = SessionToolInfo.from_dict(tools_item_data)

            tools.append(tools_item)

        hil_rules = []
        _hil_rules = d.pop("hil_rules")
        for hil_rules_item_data in _hil_rules:
            hil_rules_item = SessionHILRule.from_dict(hil_rules_item_data)

            hil_rules.append(hil_rules_item)

        subagents = []
        _subagents = d.pop("subagents")
        for subagents_item_data in _subagents:
            subagents_item = SessionSubAgentInfo.from_dict(subagents_item_data)

            subagents.append(subagents_item)

        resolved_via = d.pop("resolved_via")

        def _parse_deepagent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deepagent_id = _parse_deepagent_id(d.pop("deepagent_id", UNSET))

        def _parse_deepagent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deepagent_name = _parse_deepagent_name(d.pop("deepagent_name", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_llm_config(data: object) -> LLMExecutionConfig | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                llm_config_type_0 = LLMExecutionConfig.from_dict(data)

                return llm_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LLMExecutionConfig | None | Unset, data)

        llm_config = _parse_llm_config(d.pop("llm_config", UNSET))

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

        _datasources = d.pop("datasources", UNSET)
        datasources: list[SessionDatasourceInfo] | Unset = UNSET
        if _datasources is not UNSET:
            datasources = []
            for datasources_item_data in _datasources:
                datasources_item = SessionDatasourceInfo.from_dict(datasources_item_data)

                datasources.append(datasources_item)

        def _parse_memory_config(data: object) -> None | SessionConfigMemoryConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_config_type_0 = SessionConfigMemoryConfigType0.from_dict(data)

                return memory_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionConfigMemoryConfigType0 | Unset, data)

        memory_config = _parse_memory_config(d.pop("memory_config", UNSET))

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        _skills = d.pop("skills", UNSET)
        skills: list[SessionSkillInfo] | Unset = UNSET
        if _skills is not UNSET:
            skills = []
            for skills_item_data in _skills:
                skills_item = SessionSkillInfo.from_dict(skills_item_data)

                skills.append(skills_item)

        def _parse_agents_md_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agents_md_content = _parse_agents_md_content(d.pop("agents_md_content", UNSET))

        def _parse_backend_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backend_type = _parse_backend_type(d.pop("backend_type", UNSET))

        debug_mode = d.pop("debug_mode", UNSET)

        def _parse_cache_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_type = _parse_cache_type(d.pop("cache_type", UNSET))

        def _parse_response_format_schema(data: object) -> None | SessionConfigResponseFormatSchemaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_schema_type_0 = SessionConfigResponseFormatSchemaType0.from_dict(data)

                return response_format_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionConfigResponseFormatSchemaType0 | Unset, data)

        response_format_schema = _parse_response_format_schema(d.pop("response_format_schema", UNSET))

        def _parse_guardrails_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guardrails_text = _parse_guardrails_text(d.pop("guardrails_text", UNSET))

        def _parse_policies_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policies_text = _parse_policies_text(d.pop("policies_text", UNSET))

        def _parse_format_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_instruction = _parse_format_instruction(d.pop("format_instruction", UNSET))

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        workspace_ids = cast(list[str], d.pop("workspace_ids", UNSET))

        _middleware_config = d.pop("middleware_config", UNSET)
        middleware_config: SessionConfigMiddlewareConfig | Unset
        if isinstance(_middleware_config, Unset):
            middleware_config = UNSET
        else:
            middleware_config = SessionConfigMiddlewareConfig.from_dict(_middleware_config)

        def _parse_harness_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harness_profile = _parse_harness_profile(d.pop("harness_profile", UNSET))

        _filesystem_permissions = d.pop("filesystem_permissions", UNSET)
        filesystem_permissions: list[SessionConfigFilesystemPermissionsItem] | Unset = UNSET
        if _filesystem_permissions is not UNSET:
            filesystem_permissions = []
            for filesystem_permissions_item_data in _filesystem_permissions:
                filesystem_permissions_item = SessionConfigFilesystemPermissionsItem.from_dict(
                    filesystem_permissions_item_data
                )

                filesystem_permissions.append(filesystem_permissions_item)

        def _parse_rubric(data: object) -> None | SessionConfigRubricType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rubric_type_0 = SessionConfigRubricType0.from_dict(data)

                return rubric_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionConfigRubricType0 | Unset, data)

        rubric = _parse_rubric(d.pop("rubric", UNSET))

        excluded_tools = cast(list[str], d.pop("excluded_tools", UNSET))

        def _parse_bot_name_override(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name_override = _parse_bot_name_override(d.pop("bot_name_override", UNSET))

        session_config = cls(
            tools=tools,
            hil_rules=hil_rules,
            subagents=subagents,
            resolved_via=resolved_via,
            deepagent_id=deepagent_id,
            deepagent_name=deepagent_name,
            model_id=model_id,
            llm_config=llm_config,
            system_prompt=system_prompt,
            datasources=datasources,
            memory_config=memory_config,
            agent_name=agent_name,
            skills=skills,
            agents_md_content=agents_md_content,
            backend_type=backend_type,
            debug_mode=debug_mode,
            cache_type=cache_type,
            response_format_schema=response_format_schema,
            guardrails_text=guardrails_text,
            policies_text=policies_text,
            format_instruction=format_instruction,
            bot_id=bot_id,
            workspace_ids=workspace_ids,
            middleware_config=middleware_config,
            harness_profile=harness_profile,
            filesystem_permissions=filesystem_permissions,
            rubric=rubric,
            excluded_tools=excluded_tools,
            bot_name_override=bot_name_override,
        )

        session_config.additional_properties = d
        return session_config

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
