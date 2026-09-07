from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_agent_status import DeepAgentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_agent_create_memory_config_type_0 import DeepAgentCreateMemoryConfigType0
    from ..models.deep_agent_create_middleware_config import DeepAgentCreateMiddlewareConfig
    from ..models.deep_agent_create_response_format_schema_type_0 import DeepAgentCreateResponseFormatSchemaType0


T = TypeVar("T", bound="DeepAgentCreate")


@_attrs_define
class DeepAgentCreate:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        status (DeepAgentStatus | Unset):  Default: DeepAgentStatus.DRAFT.
        model_id (None | str | Unset):
        system_prompt_id (None | Unset | UUID):
        hil_rule_ids (list[str] | Unset):
        subagent_ids (list[str] | Unset):
        internal_tool_ids (list[str] | Unset):
        datasource_ids (list[str] | Unset):
        memory_config (DeepAgentCreateMemoryConfigType0 | None | Unset):
        agent_name (None | str | Unset):
        skill_ids (list[str] | Unset):
        agents_md_content (None | str | Unset):
        backend_type (None | str | Unset):
        debug_mode (bool | Unset):  Default: False.
        cache_type (None | str | Unset):
        response_format_schema (DeepAgentCreateResponseFormatSchemaType0 | None | Unset):
        guardrail_ids (list[str] | Unset):
        policy_ids (list[str] | Unset):
        format_instruction_id (None | str | Unset):
        is_internal (bool | Unset):  Default: False.
        owner_org_id (None | Unset | UUID):
        workspace_ids (list[str] | Unset):
        owner_user_id (None | Unset | UUID):
        hil_reviewer_user_ids (list[str] | Unset):
        is_judge (bool | Unset):  Default: False.
        is_ingestion (bool | Unset):  Default: False.
        middleware_config (DeepAgentCreateMiddlewareConfig | Unset):
        harness_profile (None | str | Unset):
        excluded_tools (list[str] | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    status: DeepAgentStatus | Unset = DeepAgentStatus.DRAFT
    model_id: None | str | Unset = UNSET
    system_prompt_id: None | Unset | UUID = UNSET
    hil_rule_ids: list[str] | Unset = UNSET
    subagent_ids: list[str] | Unset = UNSET
    internal_tool_ids: list[str] | Unset = UNSET
    datasource_ids: list[str] | Unset = UNSET
    memory_config: DeepAgentCreateMemoryConfigType0 | None | Unset = UNSET
    agent_name: None | str | Unset = UNSET
    skill_ids: list[str] | Unset = UNSET
    agents_md_content: None | str | Unset = UNSET
    backend_type: None | str | Unset = UNSET
    debug_mode: bool | Unset = False
    cache_type: None | str | Unset = UNSET
    response_format_schema: DeepAgentCreateResponseFormatSchemaType0 | None | Unset = UNSET
    guardrail_ids: list[str] | Unset = UNSET
    policy_ids: list[str] | Unset = UNSET
    format_instruction_id: None | str | Unset = UNSET
    is_internal: bool | Unset = False
    owner_org_id: None | Unset | UUID = UNSET
    workspace_ids: list[str] | Unset = UNSET
    owner_user_id: None | Unset | UUID = UNSET
    hil_reviewer_user_ids: list[str] | Unset = UNSET
    is_judge: bool | Unset = False
    is_ingestion: bool | Unset = False
    middleware_config: DeepAgentCreateMiddlewareConfig | Unset = UNSET
    harness_profile: None | str | Unset = UNSET
    excluded_tools: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deep_agent_create_memory_config_type_0 import DeepAgentCreateMemoryConfigType0  # noqa: PLC0415
        from ..models.deep_agent_create_response_format_schema_type_0 import (
            DeepAgentCreateResponseFormatSchemaType0,  # noqa: PLC0415
        )

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        system_prompt_id: None | str | Unset
        if isinstance(self.system_prompt_id, Unset):
            system_prompt_id = UNSET
        elif isinstance(self.system_prompt_id, UUID):
            system_prompt_id = str(self.system_prompt_id)
        else:
            system_prompt_id = self.system_prompt_id

        hil_rule_ids: list[str] | Unset = UNSET
        if not isinstance(self.hil_rule_ids, Unset):
            hil_rule_ids = self.hil_rule_ids

        subagent_ids: list[str] | Unset = UNSET
        if not isinstance(self.subagent_ids, Unset):
            subagent_ids = self.subagent_ids

        internal_tool_ids: list[str] | Unset = UNSET
        if not isinstance(self.internal_tool_ids, Unset):
            internal_tool_ids = self.internal_tool_ids

        datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.datasource_ids, Unset):
            datasource_ids = self.datasource_ids

        memory_config: dict[str, Any] | None | Unset
        if isinstance(self.memory_config, Unset):
            memory_config = UNSET
        elif isinstance(self.memory_config, DeepAgentCreateMemoryConfigType0):
            memory_config = self.memory_config.to_dict()
        else:
            memory_config = self.memory_config

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        skill_ids: list[str] | Unset = UNSET
        if not isinstance(self.skill_ids, Unset):
            skill_ids = self.skill_ids

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
        elif isinstance(self.response_format_schema, DeepAgentCreateResponseFormatSchemaType0):
            response_format_schema = self.response_format_schema.to_dict()
        else:
            response_format_schema = self.response_format_schema

        guardrail_ids: list[str] | Unset = UNSET
        if not isinstance(self.guardrail_ids, Unset):
            guardrail_ids = self.guardrail_ids

        policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.policy_ids, Unset):
            policy_ids = self.policy_ids

        format_instruction_id: None | str | Unset
        if isinstance(self.format_instruction_id, Unset):
            format_instruction_id = UNSET
        else:
            format_instruction_id = self.format_instruction_id

        is_internal = self.is_internal

        owner_org_id: None | str | Unset
        if isinstance(self.owner_org_id, Unset):
            owner_org_id = UNSET
        elif isinstance(self.owner_org_id, UUID):
            owner_org_id = str(self.owner_org_id)
        else:
            owner_org_id = self.owner_org_id

        workspace_ids: list[str] | Unset = UNSET
        if not isinstance(self.workspace_ids, Unset):
            workspace_ids = self.workspace_ids

        owner_user_id: None | str | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        elif isinstance(self.owner_user_id, UUID):
            owner_user_id = str(self.owner_user_id)
        else:
            owner_user_id = self.owner_user_id

        hil_reviewer_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.hil_reviewer_user_ids, Unset):
            hil_reviewer_user_ids = self.hil_reviewer_user_ids

        is_judge = self.is_judge

        is_ingestion = self.is_ingestion

        middleware_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.middleware_config, Unset):
            middleware_config = self.middleware_config.to_dict()

        harness_profile: None | str | Unset
        if isinstance(self.harness_profile, Unset):
            harness_profile = UNSET
        else:
            harness_profile = self.harness_profile

        excluded_tools: list[str] | Unset = UNSET
        if not isinstance(self.excluded_tools, Unset):
            excluded_tools = self.excluded_tools

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if system_prompt_id is not UNSET:
            field_dict["system_prompt_id"] = system_prompt_id
        if hil_rule_ids is not UNSET:
            field_dict["hil_rule_ids"] = hil_rule_ids
        if subagent_ids is not UNSET:
            field_dict["subagent_ids"] = subagent_ids
        if internal_tool_ids is not UNSET:
            field_dict["internal_tool_ids"] = internal_tool_ids
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if memory_config is not UNSET:
            field_dict["memory_config"] = memory_config
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if skill_ids is not UNSET:
            field_dict["skill_ids"] = skill_ids
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
        if guardrail_ids is not UNSET:
            field_dict["guardrail_ids"] = guardrail_ids
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids
        if format_instruction_id is not UNSET:
            field_dict["format_instruction_id"] = format_instruction_id
        if is_internal is not UNSET:
            field_dict["is_internal"] = is_internal
        if owner_org_id is not UNSET:
            field_dict["owner_org_id"] = owner_org_id
        if workspace_ids is not UNSET:
            field_dict["workspace_ids"] = workspace_ids
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if hil_reviewer_user_ids is not UNSET:
            field_dict["hil_reviewer_user_ids"] = hil_reviewer_user_ids
        if is_judge is not UNSET:
            field_dict["is_judge"] = is_judge
        if is_ingestion is not UNSET:
            field_dict["is_ingestion"] = is_ingestion
        if middleware_config is not UNSET:
            field_dict["middleware_config"] = middleware_config
        if harness_profile is not UNSET:
            field_dict["harness_profile"] = harness_profile
        if excluded_tools is not UNSET:
            field_dict["excluded_tools"] = excluded_tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_agent_create_memory_config_type_0 import DeepAgentCreateMemoryConfigType0  # noqa: PLC0415
        from ..models.deep_agent_create_middleware_config import DeepAgentCreateMiddlewareConfig  # noqa: PLC0415
        from ..models.deep_agent_create_response_format_schema_type_0 import (
            DeepAgentCreateResponseFormatSchemaType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: DeepAgentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DeepAgentStatus(_status)

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_system_prompt_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_prompt_id_type_0 = UUID(data)

                return system_prompt_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_prompt_id = _parse_system_prompt_id(d.pop("system_prompt_id", UNSET))

        hil_rule_ids = cast(list[str], d.pop("hil_rule_ids", UNSET))

        subagent_ids = cast(list[str], d.pop("subagent_ids", UNSET))

        internal_tool_ids = cast(list[str], d.pop("internal_tool_ids", UNSET))

        datasource_ids = cast(list[str], d.pop("datasource_ids", UNSET))

        def _parse_memory_config(data: object) -> DeepAgentCreateMemoryConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_config_type_0 = DeepAgentCreateMemoryConfigType0.from_dict(data)

                return memory_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentCreateMemoryConfigType0 | None | Unset, data)

        memory_config = _parse_memory_config(d.pop("memory_config", UNSET))

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        skill_ids = cast(list[str], d.pop("skill_ids", UNSET))

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

        def _parse_response_format_schema(data: object) -> DeepAgentCreateResponseFormatSchemaType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_schema_type_0 = DeepAgentCreateResponseFormatSchemaType0.from_dict(data)

                return response_format_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentCreateResponseFormatSchemaType0 | None | Unset, data)

        response_format_schema = _parse_response_format_schema(d.pop("response_format_schema", UNSET))

        guardrail_ids = cast(list[str], d.pop("guardrail_ids", UNSET))

        policy_ids = cast(list[str], d.pop("policy_ids", UNSET))

        def _parse_format_instruction_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_instruction_id = _parse_format_instruction_id(d.pop("format_instruction_id", UNSET))

        is_internal = d.pop("is_internal", UNSET)

        def _parse_owner_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_org_id_type_0 = UUID(data)

                return owner_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_org_id = _parse_owner_org_id(d.pop("owner_org_id", UNSET))

        workspace_ids = cast(list[str], d.pop("workspace_ids", UNSET))

        def _parse_owner_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_user_id_type_0 = UUID(data)

                return owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        hil_reviewer_user_ids = cast(list[str], d.pop("hil_reviewer_user_ids", UNSET))

        is_judge = d.pop("is_judge", UNSET)

        is_ingestion = d.pop("is_ingestion", UNSET)

        _middleware_config = d.pop("middleware_config", UNSET)
        middleware_config: DeepAgentCreateMiddlewareConfig | Unset
        if isinstance(_middleware_config, Unset):
            middleware_config = UNSET
        else:
            middleware_config = DeepAgentCreateMiddlewareConfig.from_dict(_middleware_config)

        def _parse_harness_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harness_profile = _parse_harness_profile(d.pop("harness_profile", UNSET))

        excluded_tools = cast(list[str], d.pop("excluded_tools", UNSET))

        deep_agent_create = cls(
            name=name,
            description=description,
            status=status,
            model_id=model_id,
            system_prompt_id=system_prompt_id,
            hil_rule_ids=hil_rule_ids,
            subagent_ids=subagent_ids,
            internal_tool_ids=internal_tool_ids,
            datasource_ids=datasource_ids,
            memory_config=memory_config,
            agent_name=agent_name,
            skill_ids=skill_ids,
            agents_md_content=agents_md_content,
            backend_type=backend_type,
            debug_mode=debug_mode,
            cache_type=cache_type,
            response_format_schema=response_format_schema,
            guardrail_ids=guardrail_ids,
            policy_ids=policy_ids,
            format_instruction_id=format_instruction_id,
            is_internal=is_internal,
            owner_org_id=owner_org_id,
            workspace_ids=workspace_ids,
            owner_user_id=owner_user_id,
            hil_reviewer_user_ids=hil_reviewer_user_ids,
            is_judge=is_judge,
            is_ingestion=is_ingestion,
            middleware_config=middleware_config,
            harness_profile=harness_profile,
            excluded_tools=excluded_tools,
        )

        deep_agent_create.additional_properties = d
        return deep_agent_create

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
