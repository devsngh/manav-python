from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deep_agent_status import DeepAgentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deep_agent_response_comms_config_type_0 import DeepAgentResponseCommsConfigType0
    from ..models.deep_agent_response_memory_config_type_0 import DeepAgentResponseMemoryConfigType0
    from ..models.deep_agent_response_middleware_config import DeepAgentResponseMiddlewareConfig
    from ..models.deep_agent_response_response_format_schema_type_0 import DeepAgentResponseResponseFormatSchemaType0


T = TypeVar("T", bound="DeepAgentResponse")


@_attrs_define
class DeepAgentResponse:
    """
    Attributes:
        id (UUID):
        name (str):
        description (None | str):
        status (DeepAgentStatus):
        model_id (None | str):
        system_prompt_id (None | UUID):
        hil_rule_ids (list[str]):
        subagent_ids (list[str]):
        internal_tool_ids (list[str]):
        datasource_ids (list[str]):
        memory_config (DeepAgentResponseMemoryConfigType0 | None):
        agent_name (None | str):
        skill_ids (list[str]):
        agents_md_content (None | str):
        backend_type (None | str):
        debug_mode (bool):
        cache_type (None | str):
        response_format_schema (DeepAgentResponseResponseFormatSchemaType0 | None):
        format_instruction_id (None | str):
        is_active (bool):
        version (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        guardrail_ids (list[str] | Unset):
        policy_ids (list[str] | Unset):
        excluded_tools (list[str] | Unset):
        is_internal (bool | Unset):  Default: False.
        owner_org_id (None | Unset | UUID):
        workspace_ids (list[str] | Unset):
        owner_user_id (None | Unset | UUID):
        hil_reviewer_user_ids (list[str] | Unset):
        is_judge (bool | Unset):  Default: False.
        is_ingestion (bool | Unset):  Default: False.
        middleware_config (DeepAgentResponseMiddlewareConfig | Unset):
        harness_profile (None | str | Unset):
        comms_config (DeepAgentResponseCommsConfigType0 | None | Unset):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        bot_id (None | Unset | UUID):
        profile_picture_url (None | str | Unset):
        bot_name (None | str | Unset):
        source (str | Unset):  Default: 'created'.
    """

    id: UUID
    name: str
    description: None | str
    status: DeepAgentStatus
    model_id: None | str
    system_prompt_id: None | UUID
    hil_rule_ids: list[str]
    subagent_ids: list[str]
    internal_tool_ids: list[str]
    datasource_ids: list[str]
    memory_config: DeepAgentResponseMemoryConfigType0 | None
    agent_name: None | str
    skill_ids: list[str]
    agents_md_content: None | str
    backend_type: None | str
    debug_mode: bool
    cache_type: None | str
    response_format_schema: DeepAgentResponseResponseFormatSchemaType0 | None
    format_instruction_id: None | str
    is_active: bool
    version: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    guardrail_ids: list[str] | Unset = UNSET
    policy_ids: list[str] | Unset = UNSET
    excluded_tools: list[str] | Unset = UNSET
    is_internal: bool | Unset = False
    owner_org_id: None | Unset | UUID = UNSET
    workspace_ids: list[str] | Unset = UNSET
    owner_user_id: None | Unset | UUID = UNSET
    hil_reviewer_user_ids: list[str] | Unset = UNSET
    is_judge: bool | Unset = False
    is_ingestion: bool | Unset = False
    middleware_config: DeepAgentResponseMiddlewareConfig | Unset = UNSET
    harness_profile: None | str | Unset = UNSET
    comms_config: DeepAgentResponseCommsConfigType0 | None | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    bot_id: None | Unset | UUID = UNSET
    profile_picture_url: None | str | Unset = UNSET
    bot_name: None | str | Unset = UNSET
    source: str | Unset = "created"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.deep_agent_response_comms_config_type_0 import DeepAgentResponseCommsConfigType0  # noqa: PLC0415
        from ..models.deep_agent_response_memory_config_type_0 import (
            DeepAgentResponseMemoryConfigType0,  # noqa: PLC0415
        )
        from ..models.deep_agent_response_response_format_schema_type_0 import (
            DeepAgentResponseResponseFormatSchemaType0,  # noqa: PLC0415
        )

        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        status = self.status.value

        model_id: None | str
        model_id = self.model_id

        system_prompt_id: None | str
        if isinstance(self.system_prompt_id, UUID):
            system_prompt_id = str(self.system_prompt_id)
        else:
            system_prompt_id = self.system_prompt_id

        hil_rule_ids = self.hil_rule_ids

        subagent_ids = self.subagent_ids

        internal_tool_ids = self.internal_tool_ids

        datasource_ids = self.datasource_ids

        memory_config: dict[str, Any] | None
        if isinstance(self.memory_config, DeepAgentResponseMemoryConfigType0):
            memory_config = self.memory_config.to_dict()
        else:
            memory_config = self.memory_config

        agent_name: None | str
        agent_name = self.agent_name

        skill_ids = self.skill_ids

        agents_md_content: None | str
        agents_md_content = self.agents_md_content

        backend_type: None | str
        backend_type = self.backend_type

        debug_mode = self.debug_mode

        cache_type: None | str
        cache_type = self.cache_type

        response_format_schema: dict[str, Any] | None
        if isinstance(self.response_format_schema, DeepAgentResponseResponseFormatSchemaType0):
            response_format_schema = self.response_format_schema.to_dict()
        else:
            response_format_schema = self.response_format_schema

        format_instruction_id: None | str
        format_instruction_id = self.format_instruction_id

        is_active = self.is_active

        version = self.version

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        guardrail_ids: list[str] | Unset = UNSET
        if not isinstance(self.guardrail_ids, Unset):
            guardrail_ids = self.guardrail_ids

        policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.policy_ids, Unset):
            policy_ids = self.policy_ids

        excluded_tools: list[str] | Unset = UNSET
        if not isinstance(self.excluded_tools, Unset):
            excluded_tools = self.excluded_tools

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

        comms_config: dict[str, Any] | None | Unset
        if isinstance(self.comms_config, Unset):
            comms_config = UNSET
        elif isinstance(self.comms_config, DeepAgentResponseCommsConfigType0):
            comms_config = self.comms_config.to_dict()
        else:
            comms_config = self.comms_config

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, UUID):
            created_by = str(self.created_by)
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        elif isinstance(self.bot_id, UUID):
            bot_id = str(self.bot_id)
        else:
            bot_id = self.bot_id

        profile_picture_url: None | str | Unset
        if isinstance(self.profile_picture_url, Unset):
            profile_picture_url = UNSET
        else:
            profile_picture_url = self.profile_picture_url

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "status": status,
                "model_id": model_id,
                "system_prompt_id": system_prompt_id,
                "hil_rule_ids": hil_rule_ids,
                "subagent_ids": subagent_ids,
                "internal_tool_ids": internal_tool_ids,
                "datasource_ids": datasource_ids,
                "memory_config": memory_config,
                "agent_name": agent_name,
                "skill_ids": skill_ids,
                "agents_md_content": agents_md_content,
                "backend_type": backend_type,
                "debug_mode": debug_mode,
                "cache_type": cache_type,
                "response_format_schema": response_format_schema,
                "format_instruction_id": format_instruction_id,
                "is_active": is_active,
                "version": version,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if guardrail_ids is not UNSET:
            field_dict["guardrail_ids"] = guardrail_ids
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids
        if excluded_tools is not UNSET:
            field_dict["excluded_tools"] = excluded_tools
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
        if comms_config is not UNSET:
            field_dict["comms_config"] = comms_config
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if profile_picture_url is not UNSET:
            field_dict["profile_picture_url"] = profile_picture_url
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deep_agent_response_comms_config_type_0 import DeepAgentResponseCommsConfigType0  # noqa: PLC0415
        from ..models.deep_agent_response_memory_config_type_0 import (
            DeepAgentResponseMemoryConfigType0,  # noqa: PLC0415
        )
        from ..models.deep_agent_response_middleware_config import DeepAgentResponseMiddlewareConfig  # noqa: PLC0415
        from ..models.deep_agent_response_response_format_schema_type_0 import (
            DeepAgentResponseResponseFormatSchemaType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        status = DeepAgentStatus(d.pop("status"))

        def _parse_model_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_id = _parse_model_id(d.pop("model_id"))

        def _parse_system_prompt_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_prompt_id_type_0 = UUID(data)

                return system_prompt_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        system_prompt_id = _parse_system_prompt_id(d.pop("system_prompt_id"))

        hil_rule_ids = cast(list[str], d.pop("hil_rule_ids"))

        subagent_ids = cast(list[str], d.pop("subagent_ids"))

        internal_tool_ids = cast(list[str], d.pop("internal_tool_ids"))

        datasource_ids = cast(list[str], d.pop("datasource_ids"))

        def _parse_memory_config(data: object) -> DeepAgentResponseMemoryConfigType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                memory_config_type_0 = DeepAgentResponseMemoryConfigType0.from_dict(data)

                return memory_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentResponseMemoryConfigType0 | None, data)

        memory_config = _parse_memory_config(d.pop("memory_config"))

        def _parse_agent_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_name = _parse_agent_name(d.pop("agent_name"))

        skill_ids = cast(list[str], d.pop("skill_ids"))

        def _parse_agents_md_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agents_md_content = _parse_agents_md_content(d.pop("agents_md_content"))

        def _parse_backend_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        backend_type = _parse_backend_type(d.pop("backend_type"))

        debug_mode = d.pop("debug_mode")

        def _parse_cache_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cache_type = _parse_cache_type(d.pop("cache_type"))

        def _parse_response_format_schema(data: object) -> DeepAgentResponseResponseFormatSchemaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_schema_type_0 = DeepAgentResponseResponseFormatSchemaType0.from_dict(data)

                return response_format_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentResponseResponseFormatSchemaType0 | None, data)

        response_format_schema = _parse_response_format_schema(d.pop("response_format_schema"))

        def _parse_format_instruction_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        format_instruction_id = _parse_format_instruction_id(d.pop("format_instruction_id"))

        is_active = d.pop("is_active")

        version = d.pop("version")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        guardrail_ids = cast(list[str], d.pop("guardrail_ids", UNSET))

        policy_ids = cast(list[str], d.pop("policy_ids", UNSET))

        excluded_tools = cast(list[str], d.pop("excluded_tools", UNSET))

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
        middleware_config: DeepAgentResponseMiddlewareConfig | Unset
        if isinstance(_middleware_config, Unset):
            middleware_config = UNSET
        else:
            middleware_config = DeepAgentResponseMiddlewareConfig.from_dict(_middleware_config)

        def _parse_harness_profile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        harness_profile = _parse_harness_profile(d.pop("harness_profile", UNSET))

        def _parse_comms_config(data: object) -> DeepAgentResponseCommsConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                comms_config_type_0 = DeepAgentResponseCommsConfigType0.from_dict(data)

                return comms_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeepAgentResponseCommsConfigType0 | None | Unset, data)

        comms_config = _parse_comms_config(d.pop("comms_config", UNSET))

        def _parse_created_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_type_0 = UUID(data)

                return created_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bot_id_type_0 = UUID(data)

                return bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_profile_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_picture_url = _parse_profile_picture_url(d.pop("profile_picture_url", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        source = d.pop("source", UNSET)

        deep_agent_response = cls(
            id=id,
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
            format_instruction_id=format_instruction_id,
            is_active=is_active,
            version=version,
            created_at=created_at,
            updated_at=updated_at,
            guardrail_ids=guardrail_ids,
            policy_ids=policy_ids,
            excluded_tools=excluded_tools,
            is_internal=is_internal,
            owner_org_id=owner_org_id,
            workspace_ids=workspace_ids,
            owner_user_id=owner_user_id,
            hil_reviewer_user_ids=hil_reviewer_user_ids,
            is_judge=is_judge,
            is_ingestion=is_ingestion,
            middleware_config=middleware_config,
            harness_profile=harness_profile,
            comms_config=comms_config,
            created_by=created_by,
            updated_by=updated_by,
            bot_id=bot_id,
            profile_picture_url=profile_picture_url,
            bot_name=bot_name,
            source=source,
        )

        deep_agent_response.additional_properties = d
        return deep_agent_response

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
