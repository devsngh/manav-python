from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.llm_execution_config import LLMExecutionConfig
    from ..models.session_sub_agent_info_interrupt_on import SessionSubAgentInfoInterruptOn
    from ..models.session_tool_info import SessionToolInfo


T = TypeVar("T", bound="SessionSubAgentInfo")


@_attrs_define
class SessionSubAgentInfo:
    """A subagent available for spawning in this session

    Attributes:
        id (str):
        agent_name (str):
        description (str):
        agent_type (str):
        tools (list[SessionToolInfo]):
        skills (list[Any]):
        interrupt_on (SessionSubAgentInfoInterruptOn):
        system_prompt (None | str | Unset):
        model_id (None | str | Unset):
        llm_config (LLMExecutionConfig | None | Unset):
        datasource_ids (list[str] | Unset):
        datasources (list[Any] | Unset):
        guardrails_text (None | str | Unset):
        policies_text (None | str | Unset):
    """

    id: str
    agent_name: str
    description: str
    agent_type: str
    tools: list[SessionToolInfo]
    skills: list[Any]
    interrupt_on: SessionSubAgentInfoInterruptOn
    system_prompt: None | str | Unset = UNSET
    model_id: None | str | Unset = UNSET
    llm_config: LLMExecutionConfig | None | Unset = UNSET
    datasource_ids: list[str] | Unset = UNSET
    datasources: list[Any] | Unset = UNSET
    guardrails_text: None | str | Unset = UNSET
    policies_text: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.llm_execution_config import LLMExecutionConfig  # noqa: PLC0415

        id = self.id

        agent_name = self.agent_name

        description = self.description

        agent_type = self.agent_type

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        skills = self.skills

        interrupt_on = self.interrupt_on.to_dict()

        system_prompt: None | str | Unset
        if isinstance(self.system_prompt, Unset):
            system_prompt = UNSET
        else:
            system_prompt = self.system_prompt

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

        datasource_ids: list[str] | Unset = UNSET
        if not isinstance(self.datasource_ids, Unset):
            datasource_ids = self.datasource_ids

        datasources: list[Any] | Unset = UNSET
        if not isinstance(self.datasources, Unset):
            datasources = self.datasources

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_name": agent_name,
                "description": description,
                "agent_type": agent_type,
                "tools": tools,
                "skills": skills,
                "interrupt_on": interrupt_on,
            }
        )
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if llm_config is not UNSET:
            field_dict["llm_config"] = llm_config
        if datasource_ids is not UNSET:
            field_dict["datasource_ids"] = datasource_ids
        if datasources is not UNSET:
            field_dict["datasources"] = datasources
        if guardrails_text is not UNSET:
            field_dict["guardrails_text"] = guardrails_text
        if policies_text is not UNSET:
            field_dict["policies_text"] = policies_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.llm_execution_config import LLMExecutionConfig  # noqa: PLC0415
        from ..models.session_sub_agent_info_interrupt_on import SessionSubAgentInfoInterruptOn  # noqa: PLC0415
        from ..models.session_tool_info import SessionToolInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        agent_name = d.pop("agent_name")

        description = d.pop("description")

        agent_type = d.pop("agent_type")

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = SessionToolInfo.from_dict(tools_item_data)

            tools.append(tools_item)

        skills = cast(list[Any], d.pop("skills"))

        interrupt_on = SessionSubAgentInfoInterruptOn.from_dict(d.pop("interrupt_on"))

        def _parse_system_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_prompt = _parse_system_prompt(d.pop("system_prompt", UNSET))

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

        datasource_ids = cast(list[str], d.pop("datasource_ids", UNSET))

        datasources = cast(list[Any], d.pop("datasources", UNSET))

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

        session_sub_agent_info = cls(
            id=id,
            agent_name=agent_name,
            description=description,
            agent_type=agent_type,
            tools=tools,
            skills=skills,
            interrupt_on=interrupt_on,
            system_prompt=system_prompt,
            model_id=model_id,
            llm_config=llm_config,
            datasource_ids=datasource_ids,
            datasources=datasources,
            guardrails_text=guardrails_text,
            policies_text=policies_text,
        )

        session_sub_agent_info.additional_properties = d
        return session_sub_agent_info

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
