from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentTargetCreate")


@_attrs_define
class AgentTargetCreate:
    """
    Attributes:
        agent_id (UUID):
        target_name (str):
        target_value (float | str):
        target_unit (str):
        due_at (datetime.datetime):
        set_by_id (UUID):
        org_id (UUID):
        time_window (None | str | Unset):
        parent_target_id (None | Unset | UUID):
        success_criteria (None | str | Unset):
        weight (float | Unset):  Default: 1.0.
        direction (str | Unset):  Default: 'higher_is_better'.
        at_risk_threshold (float | Unset):  Default: 0.6.
        off_track_threshold (float | Unset):  Default: 0.4.
        source (str | Unset):  Default: 'manual'.
        metric_source_ref (None | str | Unset):
        aggregation (None | str | Unset):
    """

    agent_id: UUID
    target_name: str
    target_value: float | str
    target_unit: str
    due_at: datetime.datetime
    set_by_id: UUID
    org_id: UUID
    time_window: None | str | Unset = UNSET
    parent_target_id: None | Unset | UUID = UNSET
    success_criteria: None | str | Unset = UNSET
    weight: float | Unset = 1.0
    direction: str | Unset = "higher_is_better"
    at_risk_threshold: float | Unset = 0.6
    off_track_threshold: float | Unset = 0.4
    source: str | Unset = "manual"
    metric_source_ref: None | str | Unset = UNSET
    aggregation: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_id = str(self.agent_id)

        target_name = self.target_name

        target_value: float | str
        target_value = self.target_value

        target_unit = self.target_unit

        due_at = self.due_at.isoformat()

        set_by_id = str(self.set_by_id)

        org_id = str(self.org_id)

        time_window: None | str | Unset
        if isinstance(self.time_window, Unset):
            time_window = UNSET
        else:
            time_window = self.time_window

        parent_target_id: None | str | Unset
        if isinstance(self.parent_target_id, Unset):
            parent_target_id = UNSET
        elif isinstance(self.parent_target_id, UUID):
            parent_target_id = str(self.parent_target_id)
        else:
            parent_target_id = self.parent_target_id

        success_criteria: None | str | Unset
        if isinstance(self.success_criteria, Unset):
            success_criteria = UNSET
        else:
            success_criteria = self.success_criteria

        weight = self.weight

        direction = self.direction

        at_risk_threshold = self.at_risk_threshold

        off_track_threshold = self.off_track_threshold

        source = self.source

        metric_source_ref: None | str | Unset
        if isinstance(self.metric_source_ref, Unset):
            metric_source_ref = UNSET
        else:
            metric_source_ref = self.metric_source_ref

        aggregation: None | str | Unset
        if isinstance(self.aggregation, Unset):
            aggregation = UNSET
        else:
            aggregation = self.aggregation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_id": agent_id,
                "target_name": target_name,
                "target_value": target_value,
                "target_unit": target_unit,
                "due_at": due_at,
                "set_by_id": set_by_id,
                "org_id": org_id,
            }
        )
        if time_window is not UNSET:
            field_dict["time_window"] = time_window
        if parent_target_id is not UNSET:
            field_dict["parent_target_id"] = parent_target_id
        if success_criteria is not UNSET:
            field_dict["success_criteria"] = success_criteria
        if weight is not UNSET:
            field_dict["weight"] = weight
        if direction is not UNSET:
            field_dict["direction"] = direction
        if at_risk_threshold is not UNSET:
            field_dict["at_risk_threshold"] = at_risk_threshold
        if off_track_threshold is not UNSET:
            field_dict["off_track_threshold"] = off_track_threshold
        if source is not UNSET:
            field_dict["source"] = source
        if metric_source_ref is not UNSET:
            field_dict["metric_source_ref"] = metric_source_ref
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))

        target_name = d.pop("target_name")

        def _parse_target_value(data: object) -> float | str:
            return cast(float | str, data)

        target_value = _parse_target_value(d.pop("target_value"))

        target_unit = d.pop("target_unit")

        due_at = datetime.datetime.fromisoformat(d.pop("due_at"))

        set_by_id = UUID(d.pop("set_by_id"))

        org_id = UUID(d.pop("org_id"))

        def _parse_time_window(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_window = _parse_time_window(d.pop("time_window", UNSET))

        def _parse_parent_target_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_target_id_type_0 = UUID(data)

                return parent_target_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_target_id = _parse_parent_target_id(d.pop("parent_target_id", UNSET))

        def _parse_success_criteria(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success_criteria = _parse_success_criteria(d.pop("success_criteria", UNSET))

        weight = d.pop("weight", UNSET)

        direction = d.pop("direction", UNSET)

        at_risk_threshold = d.pop("at_risk_threshold", UNSET)

        off_track_threshold = d.pop("off_track_threshold", UNSET)

        source = d.pop("source", UNSET)

        def _parse_metric_source_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metric_source_ref = _parse_metric_source_ref(d.pop("metric_source_ref", UNSET))

        def _parse_aggregation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aggregation = _parse_aggregation(d.pop("aggregation", UNSET))

        agent_target_create = cls(
            agent_id=agent_id,
            target_name=target_name,
            target_value=target_value,
            target_unit=target_unit,
            due_at=due_at,
            set_by_id=set_by_id,
            org_id=org_id,
            time_window=time_window,
            parent_target_id=parent_target_id,
            success_criteria=success_criteria,
            weight=weight,
            direction=direction,
            at_risk_threshold=at_risk_threshold,
            off_track_threshold=off_track_threshold,
            source=source,
            metric_source_ref=metric_source_ref,
            aggregation=aggregation,
        )

        agent_target_create.additional_properties = d
        return agent_target_create

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
