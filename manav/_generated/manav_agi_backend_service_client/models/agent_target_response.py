from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_target_response_evidence_refs_item import AgentTargetResponseEvidenceRefsItem


T = TypeVar("T", bound="AgentTargetResponse")


@_attrs_define
class AgentTargetResponse:
    """
    Attributes:
        id (UUID):
        agent_id (UUID):
        target_name (str):
        target_value (str):
        target_unit (str):
        due_at (datetime.datetime):
        weight (float):
        direction (str):
        current_value (str):
        status (str):
        at_risk_threshold (float):
        off_track_threshold (float):
        source (str):
        evidence_refs (list[AgentTargetResponseEvidenceRefsItem]):
        set_by_id (UUID):
        set_at (datetime.datetime):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        parent_target_id (None | Unset | UUID):
        time_window (None | str | Unset):
        success_criteria (None | str | Unset):
        metric_source_ref (None | str | Unset):
        aggregation (None | str | Unset):
        reviewed_by_id (None | Unset | UUID):
        reviewed_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
    """

    id: UUID
    agent_id: UUID
    target_name: str
    target_value: str
    target_unit: str
    due_at: datetime.datetime
    weight: float
    direction: str
    current_value: str
    status: str
    at_risk_threshold: float
    off_track_threshold: float
    source: str
    evidence_refs: list[AgentTargetResponseEvidenceRefsItem]
    set_by_id: UUID
    set_at: datetime.datetime
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    parent_target_id: None | Unset | UUID = UNSET
    time_window: None | str | Unset = UNSET
    success_criteria: None | str | Unset = UNSET
    metric_source_ref: None | str | Unset = UNSET
    aggregation: None | str | Unset = UNSET
    reviewed_by_id: None | Unset | UUID = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        target_name = self.target_name

        target_value = self.target_value

        target_unit = self.target_unit

        due_at = self.due_at.isoformat()

        weight = self.weight

        direction = self.direction

        current_value = self.current_value

        status = self.status

        at_risk_threshold = self.at_risk_threshold

        off_track_threshold = self.off_track_threshold

        source = self.source

        evidence_refs = []
        for evidence_refs_item_data in self.evidence_refs:
            evidence_refs_item = evidence_refs_item_data.to_dict()
            evidence_refs.append(evidence_refs_item)

        set_by_id = str(self.set_by_id)

        set_at = self.set_at.isoformat()

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        parent_target_id: None | str | Unset
        if isinstance(self.parent_target_id, Unset):
            parent_target_id = UNSET
        elif isinstance(self.parent_target_id, UUID):
            parent_target_id = str(self.parent_target_id)
        else:
            parent_target_id = self.parent_target_id

        time_window: None | str | Unset
        if isinstance(self.time_window, Unset):
            time_window = UNSET
        else:
            time_window = self.time_window

        success_criteria: None | str | Unset
        if isinstance(self.success_criteria, Unset):
            success_criteria = UNSET
        else:
            success_criteria = self.success_criteria

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

        reviewed_by_id: None | str | Unset
        if isinstance(self.reviewed_by_id, Unset):
            reviewed_by_id = UNSET
        elif isinstance(self.reviewed_by_id, UUID):
            reviewed_by_id = str(self.reviewed_by_id)
        else:
            reviewed_by_id = self.reviewed_by_id

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "agent_id": agent_id,
                "target_name": target_name,
                "target_value": target_value,
                "target_unit": target_unit,
                "due_at": due_at,
                "weight": weight,
                "direction": direction,
                "current_value": current_value,
                "status": status,
                "at_risk_threshold": at_risk_threshold,
                "off_track_threshold": off_track_threshold,
                "source": source,
                "evidence_refs": evidence_refs,
                "set_by_id": set_by_id,
                "set_at": set_at,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parent_target_id is not UNSET:
            field_dict["parent_target_id"] = parent_target_id
        if time_window is not UNSET:
            field_dict["time_window"] = time_window
        if success_criteria is not UNSET:
            field_dict["success_criteria"] = success_criteria
        if metric_source_ref is not UNSET:
            field_dict["metric_source_ref"] = metric_source_ref
        if aggregation is not UNSET:
            field_dict["aggregation"] = aggregation
        if reviewed_by_id is not UNSET:
            field_dict["reviewed_by_id"] = reviewed_by_id
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_target_response_evidence_refs_item import (
            AgentTargetResponseEvidenceRefsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        agent_id = UUID(d.pop("agent_id"))

        target_name = d.pop("target_name")

        target_value = d.pop("target_value")

        target_unit = d.pop("target_unit")

        due_at = datetime.datetime.fromisoformat(d.pop("due_at"))

        weight = d.pop("weight")

        direction = d.pop("direction")

        current_value = d.pop("current_value")

        status = d.pop("status")

        at_risk_threshold = d.pop("at_risk_threshold")

        off_track_threshold = d.pop("off_track_threshold")

        source = d.pop("source")

        evidence_refs = []
        _evidence_refs = d.pop("evidence_refs")
        for evidence_refs_item_data in _evidence_refs:
            evidence_refs_item = AgentTargetResponseEvidenceRefsItem.from_dict(evidence_refs_item_data)

            evidence_refs.append(evidence_refs_item)

        set_by_id = UUID(d.pop("set_by_id"))

        set_at = datetime.datetime.fromisoformat(d.pop("set_at"))

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

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

        def _parse_time_window(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_window = _parse_time_window(d.pop("time_window", UNSET))

        def _parse_success_criteria(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success_criteria = _parse_success_criteria(d.pop("success_criteria", UNSET))

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

        def _parse_reviewed_by_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_by_id_type_0 = UUID(data)

                return reviewed_by_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reviewed_by_id = _parse_reviewed_by_id(d.pop("reviewed_by_id", UNSET))

        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = datetime.datetime.fromisoformat(data)

                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        agent_target_response = cls(
            id=id,
            agent_id=agent_id,
            target_name=target_name,
            target_value=target_value,
            target_unit=target_unit,
            due_at=due_at,
            weight=weight,
            direction=direction,
            current_value=current_value,
            status=status,
            at_risk_threshold=at_risk_threshold,
            off_track_threshold=off_track_threshold,
            source=source,
            evidence_refs=evidence_refs,
            set_by_id=set_by_id,
            set_at=set_at,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            parent_target_id=parent_target_id,
            time_window=time_window,
            success_criteria=success_criteria,
            metric_source_ref=metric_source_ref,
            aggregation=aggregation,
            reviewed_by_id=reviewed_by_id,
            reviewed_at=reviewed_at,
            closed_at=closed_at,
        )

        agent_target_response.additional_properties = d
        return agent_target_response

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
