from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChildTraceRef")


@_attrs_define
class ChildTraceRef:
    """One nested subagent invocation reachable from a delegate event.

    Populated by the /child-traces endpoint. The frontend renders these
    as clickable rows in Panel 3's delegate-event detail card; each row
    spawns a NEW AgentTracesTower window scoped to the child's thread.

        Attributes:
            parent_span_id (str):
            child_bot_id (None | str | Unset):
            child_agent_name (None | str | Unset):
            child_source_type (None | str | Unset):
            child_source_id (None | str | Unset):
            child_dialogue_id (None | str | Unset):
            child_trace_id (None | str | Unset):
    """

    parent_span_id: str
    child_bot_id: None | str | Unset = UNSET
    child_agent_name: None | str | Unset = UNSET
    child_source_type: None | str | Unset = UNSET
    child_source_id: None | str | Unset = UNSET
    child_dialogue_id: None | str | Unset = UNSET
    child_trace_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_span_id = self.parent_span_id

        child_bot_id: None | str | Unset
        if isinstance(self.child_bot_id, Unset):
            child_bot_id = UNSET
        else:
            child_bot_id = self.child_bot_id

        child_agent_name: None | str | Unset
        if isinstance(self.child_agent_name, Unset):
            child_agent_name = UNSET
        else:
            child_agent_name = self.child_agent_name

        child_source_type: None | str | Unset
        if isinstance(self.child_source_type, Unset):
            child_source_type = UNSET
        else:
            child_source_type = self.child_source_type

        child_source_id: None | str | Unset
        if isinstance(self.child_source_id, Unset):
            child_source_id = UNSET
        else:
            child_source_id = self.child_source_id

        child_dialogue_id: None | str | Unset
        if isinstance(self.child_dialogue_id, Unset):
            child_dialogue_id = UNSET
        else:
            child_dialogue_id = self.child_dialogue_id

        child_trace_id: None | str | Unset
        if isinstance(self.child_trace_id, Unset):
            child_trace_id = UNSET
        else:
            child_trace_id = self.child_trace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_span_id": parent_span_id,
            }
        )
        if child_bot_id is not UNSET:
            field_dict["child_bot_id"] = child_bot_id
        if child_agent_name is not UNSET:
            field_dict["child_agent_name"] = child_agent_name
        if child_source_type is not UNSET:
            field_dict["child_source_type"] = child_source_type
        if child_source_id is not UNSET:
            field_dict["child_source_id"] = child_source_id
        if child_dialogue_id is not UNSET:
            field_dict["child_dialogue_id"] = child_dialogue_id
        if child_trace_id is not UNSET:
            field_dict["child_trace_id"] = child_trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_span_id = d.pop("parent_span_id")

        def _parse_child_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_bot_id = _parse_child_bot_id(d.pop("child_bot_id", UNSET))

        def _parse_child_agent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_agent_name = _parse_child_agent_name(d.pop("child_agent_name", UNSET))

        def _parse_child_source_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_source_type = _parse_child_source_type(d.pop("child_source_type", UNSET))

        def _parse_child_source_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_source_id = _parse_child_source_id(d.pop("child_source_id", UNSET))

        def _parse_child_dialogue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_dialogue_id = _parse_child_dialogue_id(d.pop("child_dialogue_id", UNSET))

        def _parse_child_trace_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_trace_id = _parse_child_trace_id(d.pop("child_trace_id", UNSET))

        child_trace_ref = cls(
            parent_span_id=parent_span_id,
            child_bot_id=child_bot_id,
            child_agent_name=child_agent_name,
            child_source_type=child_source_type,
            child_source_id=child_source_id,
            child_dialogue_id=child_dialogue_id,
            child_trace_id=child_trace_id,
        )

        child_trace_ref.additional_properties = d
        return child_trace_ref

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
