from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sub_agent_status import SubAgentStatus
from ..models.sub_agent_type import SubAgentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_agent_update_interrupt_on_type_0 import SubAgentUpdateInterruptOnType0
    from ..models.sub_agent_update_middleware_config_type_0 import SubAgentUpdateMiddlewareConfigType0


T = TypeVar("T", bound="SubAgentUpdate")


@_attrs_define
class SubAgentUpdate:
    """
    Attributes:
        agent_name (None | str | Unset):
        description (None | str | Unset):
        agent_type (None | SubAgentType | Unset):
        status (None | SubAgentStatus | Unset):
        system_prompt_id (None | str | Unset):
        model_id (None | str | Unset):
        allowed_tools (list[str] | None | Unset):
        skills (list[str] | None | Unset):
        datasource_ids (list[str] | None | Unset):
        interrupt_on (None | SubAgentUpdateInterruptOnType0 | Unset):
        middleware_config (None | SubAgentUpdateMiddlewareConfigType0 | Unset):
        compiled_runnable_ref (None | str | Unset):
        agents_md_content (None | str | Unset):
        is_active (bool | None | Unset):
        guardrail_ids (list[str] | None | Unset):
        policy_ids (list[str] | None | Unset):
    """

    agent_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    agent_type: None | SubAgentType | Unset = UNSET
    status: None | SubAgentStatus | Unset = UNSET
    system_prompt_id: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    allowed_tools: list[str] | None | Unset = UNSET
    skills: list[str] | None | Unset = UNSET
    datasource_ids: list[str] | None | Unset = UNSET
    interrupt_on: None | SubAgentUpdateInterruptOnType0 | Unset = UNSET
    middleware_config: None | SubAgentUpdateMiddlewareConfigType0 | Unset = UNSET
    compiled_runnable_ref: None | str | Unset = UNSET
    agents_md_content: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    guardrail_ids: list[str] | None | Unset = UNSET
    policy_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sub_agent_update_interrupt_on_type_0 import SubAgentUpdateInterruptOnType0  # noqa: PLC0415
        from ..models.sub_agent_update_middleware_config_type_0 import (
            SubAgentUpdateMiddlewareConfigType0,  # noqa: PLC0415
        )

        agent_name: None | str | Unset
        if isinstance(self.agent_name, Unset):
            agent_name = UNSET
        else:
            agent_name = self.agent_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        agent_type: None | str | Unset
        if isinstance(self.agent_type, Unset):
            agent_type = UNSET
        elif isinstance(self.agent_type, SubAgentType):
            agent_type = self.agent_type.value
        else:
            agent_type = self.agent_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SubAgentStatus):
            status = self.status.value
        else:
            status = self.status

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

        allowed_tools: list[str] | None | Unset
        if isinstance(self.allowed_tools, Unset):
            allowed_tools = UNSET
        elif isinstance(self.allowed_tools, list):
            allowed_tools = self.allowed_tools

        else:
            allowed_tools = self.allowed_tools

        skills: list[str] | None | Unset
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = self.skills

        else:
            skills = self.skills

        datasource_ids: list[str] | None | Unset
        if isinstance(self.datasource_ids, Unset):
            datasource_ids = UNSET
        elif isinstance(self.datasource_ids, list):
            datasource_ids = self.datasource_ids

        else:
            datasource_ids = self.datasource_ids

        interrupt_on: dict[str, Any] | None | Unset
        if isinstance(self.interrupt_on, Unset):
            interrupt_on = UNSET
        elif isinstance(self.interrupt_on, SubAgentUpdateInterruptOnType0):
            interrupt_on = self.interrupt_on.to_dict()
        else:
            interrupt_on = self.interrupt_on

        middleware_config: dict[str, Any] | None | Unset
        if isinstance(self.middleware_config, Unset):
            middleware_config = UNSET
        elif isinstance(self.middleware_config, SubAgentUpdateMiddlewareConfigType0):
            middleware_config = self.middleware_config.to_dict()
        else:
            middleware_config = self.middleware_config

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

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        guardrail_ids: list[str] | None | Unset
        if isinstance(self.guardrail_ids, Unset):
            guardrail_ids = UNSET
        elif isinstance(self.guardrail_ids, list):
            guardrail_ids = self.guardrail_ids

        else:
            guardrail_ids = self.guardrail_ids

        policy_ids: list[str] | None | Unset
        if isinstance(self.policy_ids, Unset):
            policy_ids = UNSET
        elif isinstance(self.policy_ids, list):
            policy_ids = self.policy_ids

        else:
            policy_ids = self.policy_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if description is not UNSET:
            field_dict["description"] = description
        if agent_type is not UNSET:
            field_dict["agent_type"] = agent_type
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
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if guardrail_ids is not UNSET:
            field_dict["guardrail_ids"] = guardrail_ids
        if policy_ids is not UNSET:
            field_dict["policy_ids"] = policy_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sub_agent_update_interrupt_on_type_0 import SubAgentUpdateInterruptOnType0  # noqa: PLC0415
        from ..models.sub_agent_update_middleware_config_type_0 import (
            SubAgentUpdateMiddlewareConfigType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_name = _parse_agent_name(d.pop("agent_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_agent_type(data: object) -> None | SubAgentType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_type_type_0 = SubAgentType(data)

                return agent_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubAgentType | Unset, data)

        agent_type = _parse_agent_type(d.pop("agent_type", UNSET))

        def _parse_status(data: object) -> None | SubAgentStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = SubAgentStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubAgentStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_allowed_tools(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_tools_type_0 = cast(list[str], data)

                return allowed_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        allowed_tools = _parse_allowed_tools(d.pop("allowed_tools", UNSET))

        def _parse_skills(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = cast(list[str], data)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        skills = _parse_skills(d.pop("skills", UNSET))

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

        def _parse_interrupt_on(data: object) -> None | SubAgentUpdateInterruptOnType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                interrupt_on_type_0 = SubAgentUpdateInterruptOnType0.from_dict(data)

                return interrupt_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubAgentUpdateInterruptOnType0 | Unset, data)

        interrupt_on = _parse_interrupt_on(d.pop("interrupt_on", UNSET))

        def _parse_middleware_config(data: object) -> None | SubAgentUpdateMiddlewareConfigType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                middleware_config_type_0 = SubAgentUpdateMiddlewareConfigType0.from_dict(data)

                return middleware_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubAgentUpdateMiddlewareConfigType0 | Unset, data)

        middleware_config = _parse_middleware_config(d.pop("middleware_config", UNSET))

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

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_guardrail_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guardrail_ids_type_0 = cast(list[str], data)

                return guardrail_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guardrail_ids = _parse_guardrail_ids(d.pop("guardrail_ids", UNSET))

        def _parse_policy_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policy_ids_type_0 = cast(list[str], data)

                return policy_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        policy_ids = _parse_policy_ids(d.pop("policy_ids", UNSET))

        sub_agent_update = cls(
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
            is_active=is_active,
            guardrail_ids=guardrail_ids,
            policy_ids=policy_ids,
        )

        sub_agent_update.additional_properties = d
        return sub_agent_update

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
