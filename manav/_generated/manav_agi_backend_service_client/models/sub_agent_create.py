from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sub_agent_status import SubAgentStatus
from ..models.sub_agent_type import SubAgentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_agent_create_interrupt_on import SubAgentCreateInterruptOn
    from ..models.sub_agent_create_middleware_config import SubAgentCreateMiddlewareConfig


T = TypeVar("T", bound="SubAgentCreate")


@_attrs_define
class SubAgentCreate:
    """
    Attributes:
        agent_name (str):
        description (str):
        agent_type (SubAgentType): Type of subagent — determines how it runs
        status (SubAgentStatus | Unset): SubAgent lifecycle status Default: SubAgentStatus.DRAFT.
        system_prompt_id (None | str | Unset):
        model_id (None | str | Unset):
        allowed_tools (list[str] | Unset):
        skills (list[str] | Unset):
        datasource_ids (list[str] | Unset):
        interrupt_on (SubAgentCreateInterruptOn | Unset):
        middleware_config (SubAgentCreateMiddlewareConfig | Unset):
        compiled_runnable_ref (None | str | Unset):
        agents_md_content (None | str | Unset):
        guardrail_ids (list[str] | Unset):
        policy_ids (list[str] | Unset):
    """

    agent_name: str
    description: str
    agent_type: SubAgentType
    status: SubAgentStatus | Unset = SubAgentStatus.DRAFT
    system_prompt_id: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    allowed_tools: list[str] | Unset = UNSET
    skills: list[str] | Unset = UNSET
    datasource_ids: list[str] | Unset = UNSET
    interrupt_on: SubAgentCreateInterruptOn | Unset = UNSET
    middleware_config: SubAgentCreateMiddlewareConfig | Unset = UNSET
    compiled_runnable_ref: None | str | Unset = UNSET
    agents_md_content: None | str | Unset = UNSET
    guardrail_ids: list[str] | Unset = UNSET
    policy_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name = self.agent_name

        description = self.description

        agent_type = self.agent_type.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        system_prompt_id: None | str | Unset
        if isinstance(self.system_prompt_id, Unset):
            system_prompt_id = UNSET
        else:
            system_prompt_id = self.system_prompt_id

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        allowed_tools: list[str] | Unset = UNSET
        if not isinstance(self.allowed_tools, Unset):
            allowed_tools = self.allowed_tools

        skills: list[str] | Unset = UNSET
        if not isinstance(self.skills, Unset):
            skills = self.skills

        datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.datasource_ids, Unset):
            datasource_ids = self.datasource_ids

        interrupt_on: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interrupt_on, Unset):
            interrupt_on = self.interrupt_on.to_dict()

        middleware_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.middleware_config, Unset):
            middleware_config = self.middleware_config.to_dict()

        compiled_runnable_ref: None | str | Unset
        if isinstance(self.compiled_runnable_ref, Unset):
            compiled_runnable_ref = UNSET
        else:
            compiled_runnable_ref = self.compiled_runnable_ref

        agents_md_content: None | str | Unset
        if isinstance(self.agents_md_content, Unset):
            agents_md_content = UNSET
        else:
            agents_md_content = self.agents_md_content

        guardrail_ids: list[str] | Unset = UNSET
        if not isinstance(self.guardrail_ids, Unset):
            guardrail_ids = self.guardrail_ids

        policy_ids: list[str] | Unset = UNSET
        if not isinstance(self.policy_ids, Unset):
            policy_ids = self.policy_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
                "description": description,
                "agent_type": agent_type,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if system_prompt_id is not UNSET:
            field_dict["system_prompt_id"] = system_prompt_id
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if allowed_tools is not UNSET:
            field_dict["allowed_tools"] = allowed_tools
        if skills is not UNSET:
            field_dict["skills"] = skills
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if interrupt_on is not UNSET:
            field_dict["interrupt_on"] = interrupt_on
        if middleware_config is not UNSET:
            field_dict["middleware_config"] = middleware_config
        if compiled_runnable_ref is not UNSET:
            field_dict["compiled_runnable_ref"] = compiled_runnable_ref
        if agents_md_content is not UNSET:
            field_dict["agents_md_content"] = agents_md_content
        if guardrail_ids is not UNSET:
            field_dict["guardrail_ids"] = guardrail_ids
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sub_agent_create_interrupt_on import SubAgentCreateInterruptOn  # noqa: PLC0415
        from ..models.sub_agent_create_middleware_config import SubAgentCreateMiddlewareConfig  # noqa: PLC0415

        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        description = d.pop("description")

        agent_type = SubAgentType(d.pop("agent_type"))

        _status = d.pop("status", UNSET)
        status: SubAgentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubAgentStatus(_status)

        def _parse_system_prompt_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt_id = _parse_system_prompt_id(d.pop("system_prompt_id", UNSET))

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        allowed_tools = cast(list[str], d.pop("allowed_tools", UNSET))

        skills = cast(list[str], d.pop("skills", UNSET))

        datasource_ids = cast(list[str], d.pop("datasource_ids", UNSET))

        _interrupt_on = d.pop("interrupt_on", UNSET)
        interrupt_on: SubAgentCreateInterruptOn | Unset
        if isinstance(_interrupt_on, Unset):
            interrupt_on = UNSET
        else:
            interrupt_on = SubAgentCreateInterruptOn.from_dict(_interrupt_on)

        _middleware_config = d.pop("middleware_config", UNSET)
        middleware_config: SubAgentCreateMiddlewareConfig | Unset
        if isinstance(_middleware_config, Unset):
            middleware_config = UNSET
        else:
            middleware_config = SubAgentCreateMiddlewareConfig.from_dict(_middleware_config)

        def _parse_compiled_runnable_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        compiled_runnable_ref = _parse_compiled_runnable_ref(d.pop("compiled_runnable_ref", UNSET))

        def _parse_agents_md_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agents_md_content = _parse_agents_md_content(d.pop("agents_md_content", UNSET))

        guardrail_ids = cast(list[str], d.pop("guardrail_ids", UNSET))

        policy_ids = cast(list[str], d.pop("policy_ids", UNSET))

        sub_agent_create = cls(
            agent_name=agent_name,
            description=description,
            agent_type=agent_type,
            status=status,
            system_prompt_id=system_prompt_id,
            model_id=model_id,
            allowed_tools=allowed_tools,
            skills=skills,
            datasource_ids=datasource_ids,
            interrupt_on=interrupt_on,
            middleware_config=middleware_config,
            compiled_runnable_ref=compiled_runnable_ref,
            agents_md_content=agents_md_content,
            guardrail_ids=guardrail_ids,
            policy_ids=policy_ids,
        )

        sub_agent_create.additional_properties = d
        return sub_agent_create

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
