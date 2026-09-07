from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AgentScoreItem")


@_attrs_define
class AgentScoreItem:
    """
    Attributes:
        bot_id (str):
        bot_name (str):
        eval_count (int):
        avg_score (float):
        avg_latency_ms (float):
        avg_llm_latency_ms (float):
        avg_mcp_latency_ms (float):
        avg_overhead_latency_ms (float):
        total_tokens (int):
        avg_tool_precision (float):
        avg_tool_error_rate (float):
        avg_step_efficiency (float):
        passed_count (int):
        subagent_calls (int):
    """

    bot_id: str
    bot_name: str
    eval_count: int
    avg_score: float
    avg_latency_ms: float
    avg_llm_latency_ms: float
    avg_mcp_latency_ms: float
    avg_overhead_latency_ms: float
    total_tokens: int
    avg_tool_precision: float
    avg_tool_error_rate: float
    avg_step_efficiency: float
    passed_count: int
    subagent_calls: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = self.bot_id

        bot_name = self.bot_name

        eval_count = self.eval_count

        avg_score = self.avg_score

        avg_latency_ms = self.avg_latency_ms

        avg_llm_latency_ms = self.avg_llm_latency_ms

        avg_mcp_latency_ms = self.avg_mcp_latency_ms

        avg_overhead_latency_ms = self.avg_overhead_latency_ms

        total_tokens = self.total_tokens

        avg_tool_precision = self.avg_tool_precision

        avg_tool_error_rate = self.avg_tool_error_rate

        avg_step_efficiency = self.avg_step_efficiency

        passed_count = self.passed_count

        subagent_calls = self.subagent_calls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "bot_name": bot_name,
                "eval_count": eval_count,
                "avg_score": avg_score,
                "avg_latency_ms": avg_latency_ms,
                "avg_llm_latency_ms": avg_llm_latency_ms,
                "avg_mcp_latency_ms": avg_mcp_latency_ms,
                "avg_overhead_latency_ms": avg_overhead_latency_ms,
                "total_tokens": total_tokens,
                "avg_tool_precision": avg_tool_precision,
                "avg_tool_error_rate": avg_tool_error_rate,
                "avg_step_efficiency": avg_step_efficiency,
                "passed_count": passed_count,
                "subagent_calls": subagent_calls,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        bot_name = d.pop("bot_name")

        eval_count = d.pop("eval_count")

        avg_score = d.pop("avg_score")

        avg_latency_ms = d.pop("avg_latency_ms")

        avg_llm_latency_ms = d.pop("avg_llm_latency_ms")

        avg_mcp_latency_ms = d.pop("avg_mcp_latency_ms")

        avg_overhead_latency_ms = d.pop("avg_overhead_latency_ms")

        total_tokens = d.pop("total_tokens")

        avg_tool_precision = d.pop("avg_tool_precision")

        avg_tool_error_rate = d.pop("avg_tool_error_rate")

        avg_step_efficiency = d.pop("avg_step_efficiency")

        passed_count = d.pop("passed_count")

        subagent_calls = d.pop("subagent_calls")

        agent_score_item = cls(
            bot_id=bot_id,
            bot_name=bot_name,
            eval_count=eval_count,
            avg_score=avg_score,
            avg_latency_ms=avg_latency_ms,
            avg_llm_latency_ms=avg_llm_latency_ms,
            avg_mcp_latency_ms=avg_mcp_latency_ms,
            avg_overhead_latency_ms=avg_overhead_latency_ms,
            total_tokens=total_tokens,
            avg_tool_precision=avg_tool_precision,
            avg_tool_error_rate=avg_tool_error_rate,
            avg_step_efficiency=avg_step_efficiency,
            passed_count=passed_count,
            subagent_calls=subagent_calls,
        )

        agent_score_item.additional_properties = d
        return agent_score_item

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
