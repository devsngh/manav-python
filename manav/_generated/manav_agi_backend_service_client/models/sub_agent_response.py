from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sub_agent_status import SubAgentStatus
from ..models.sub_agent_type import SubAgentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_agent_response_interrupt_on import SubAgentResponseInterruptOn
    from ..models.sub_agent_response_middleware_config import SubAgentResponseMiddlewareConfig


T = TypeVar("T", bound="SubAgentResponse")


@_attrs_define
class SubAgentResponse:
    """
    Attributes:
        id (UUID):
        agent_name (str):
        description (str):
        agent_type (SubAgentType): Type of subagent — determines how it runs
        status (SubAgentStatus): SubAgent lifecycle status
        system_prompt_id (None | str):
        model_id (None | str):
        allowed_tools (list[str]):
        skills (list[str]):
        interrupt_on (SubAgentResponseInterruptOn):
        middleware_config (SubAgentResponseMiddlewareConfig):
        compiled_runnable_ref (None | str):
        agents_md_content (None | str):
        version (str):
        is_active (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        datasource_ids (list[str] | Unset):
        guardrail_ids (list[str] | Unset):
        policy_ids (list[str] | Unset):
        created_by (None | Unset | UUID):
        updated_by (None | Unset | UUID):
        source (None | str | Unset):
    """

    id: UUID
    agent_name: str
    description: str
    agent_type: SubAgentType
    status: SubAgentStatus
    system_prompt_id: None | str
    model_id: None | str
    allowed_tools: list[str]
    skills: list[str]
    interrupt_on: SubAgentResponseInterruptOn
    middleware_config: SubAgentResponseMiddlewareConfig
    compiled_runnable_ref: None | str
    agents_md_content: None | str
    version: str
    is_active: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    datasource_ids: list[str] | Unset = UNSET
    guardrail_ids: list[str] | Unset = UNSET
    policy_ids: list[str] | Unset = UNSET
    created_by: None | Unset | UUID = UNSET
    updated_by: None | Unset | UUID = UNSET
    source: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_name = self.agent_name

        description = self.description

        agent_type = self.agent_type.value

        status = self.status.value

        system_prompt_id: None | str
        system_prompt_id = self.system_prompt_id

        model_id: None | str
        model_id = self.model_id

        allowed_tools = self.allowed_tools

        skills = self.skills

        interrupt_on = self.interrupt_on.to_dict()

        middleware_config = self.middleware_config.to_dict()

        compiled_runnable_ref: None | str
        compiled_runnable_ref = self.compiled_runnable_ref

        agents_md_content: None | str
        agents_md_content = self.agents_md_content

        version = self.version

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.datasource_ids, Unset):
            datasource_ids = self.datasource_ids

        guardrail_ids: list[str] | Unset = UNSET
        if not isinstance(self.guardrail_ids, Unset):
            guardrail_ids = self.guardrail_ids

        policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.policy_ids, Unset):
            policy_ids = self.policy_ids

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

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_name": agent_name,
                "description": description,
                "agent_type": agent_type,
                "status": status,
                "system_prompt_id": system_prompt_id,
                "model_id": model_id,
                "allowed_tools": allowed_tools,
                "skills": skills,
                "interrupt_on": interrupt_on,
                "middleware_config": middleware_config,
                "compiled_runnable_ref": compiled_runnable_ref,
                "agents_md_content": agents_md_content,
                "version": version,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if guardrail_ids is not UNSET:
            field_dict["guardrail_ids"] = guardrail_ids
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sub_agent_response_interrupt_on import SubAgentResponseInterruptOn  # noqa: PLC0415
        from ..models.sub_agent_response_middleware_config import SubAgentResponseMiddlewareConfig  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        agent_name = d.pop("agent_name")

        description = d.pop("description")

        agent_type = SubAgentType(d.pop("agent_type"))

        status = SubAgentStatus(d.pop("status"))

        def _parse_system_prompt_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        system_prompt_id = _parse_system_prompt_id(d.pop("system_prompt_id"))

        def _parse_model_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_id = _parse_model_id(d.pop("model_id"))

        allowed_tools = cast(list[str], d.pop("allowed_tools"))

        skills = cast(list[str], d.pop("skills"))

        interrupt_on = SubAgentResponseInterruptOn.from_dict(d.pop("interrupt_on"))

        middleware_config = SubAgentResponseMiddlewareConfig.from_dict(d.pop("middleware_config"))

        def _parse_compiled_runnable_ref(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        compiled_runnable_ref = _parse_compiled_runnable_ref(d.pop("compiled_runnable_ref"))

        def _parse_agents_md_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agents_md_content = _parse_agents_md_content(d.pop("agents_md_content"))

        version = d.pop("version")

        is_active = d.pop("is_active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        datasource_ids = cast(list[str], d.pop("datasource_ids", UNSET))

        guardrail_ids = cast(list[str], d.pop("guardrail_ids", UNSET))

        policy_ids = cast(list[str], d.pop("policy_ids", UNSET))

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

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        sub_agent_response = cls(
            id=id,
            agent_name=agent_name,
            description=description,
            agent_type=agent_type,
            status=status,
            system_prompt_id=system_prompt_id,
            model_id=model_id,
            allowed_tools=allowed_tools,
            skills=skills,
            interrupt_on=interrupt_on,
            middleware_config=middleware_config,
            compiled_runnable_ref=compiled_runnable_ref,
            agents_md_content=agents_md_content,
            version=version,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            datasource_ids=datasource_ids,
            guardrail_ids=guardrail_ids,
            policy_ids=policy_ids,
            created_by=created_by,
            updated_by=updated_by,
            source=source,
        )

        sub_agent_response.additional_properties = d
        return sub_agent_response

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
