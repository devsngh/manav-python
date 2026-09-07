from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_target_update_evidence_refs_type_0_item import AgentTargetUpdateEvidenceRefsType0Item


T = TypeVar("T", bound="AgentTargetUpdate")


@_attrs_define
class AgentTargetUpdate:
    """Patch — set any subset.

    Attributes:
        current_value (float | None | str | Unset):
        status (None | str | Unset):
        evidence_refs (list[AgentTargetUpdateEvidenceRefsType0Item] | None | Unset):
        reviewed_by_id (None | Unset | UUID):
        target_value (float | None | str | Unset):
        due_at (datetime.datetime | None | Unset):
    """

    current_value: float | None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    evidence_refs: list[AgentTargetUpdateEvidenceRefsType0Item] | None | Unset = UNSET
    reviewed_by_id: None | Unset | UUID = UNSET
    target_value: float | None | str | Unset = UNSET
    due_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_value: float | None | str | Unset
        if isinstance(self.current_value, Unset):
            current_value = UNSET
        else:
            current_value = self.current_value

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        evidence_refs: list[dict[str, Any]] | None | Unset
        if isinstance(self.evidence_refs, Unset):
            evidence_refs = UNSET
        elif isinstance(self.evidence_refs, list):
            evidence_refs = []
            for evidence_refs_type_0_item_data in self.evidence_refs:
                evidence_refs_type_0_item = evidence_refs_type_0_item_data.to_dict()
                evidence_refs.append(evidence_refs_type_0_item)

        else:
            evidence_refs = self.evidence_refs

        reviewed_by_id: None | str | Unset
        if isinstance(self.reviewed_by_id, Unset):
            reviewed_by_id = UNSET
        elif isinstance(self.reviewed_by_id, UUID):
            reviewed_by_id = str(self.reviewed_by_id)
        else:
            reviewed_by_id = self.reviewed_by_id

        target_value: float | None | str | Unset
        if isinstance(self.target_value, Unset):
            target_value = UNSET
        else:
            target_value = self.target_value

        due_at: None | str | Unset
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.datetime):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if status is not UNSET:
            field_dict["status"] = status
        if evidence_refs is not UNSET:
            field_dict["evidence_refs"] = evidence_refs
        if reviewed_by_id is not UNSET:
            field_dict["reviewed_by_id"] = reviewed_by_id
        if target_value is not UNSET:
            field_dict["target_value"] = target_value
        if due_at is not UNSET:
            field_dict["due_at"] = due_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_target_update_evidence_refs_type_0_item import (
            AgentTargetUpdateEvidenceRefsType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_current_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        current_value = _parse_current_value(d.pop("current_value", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_evidence_refs(data: object) -> list[AgentTargetUpdateEvidenceRefsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_refs_type_0 = []
                _evidence_refs_type_0 = data
                for evidence_refs_type_0_item_data in _evidence_refs_type_0:
                    evidence_refs_type_0_item = AgentTargetUpdateEvidenceRefsType0Item.from_dict(
                        evidence_refs_type_0_item_data
                    )

                    evidence_refs_type_0.append(evidence_refs_type_0_item)

                return evidence_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentTargetUpdateEvidenceRefsType0Item] | None | Unset, data)

        evidence_refs = _parse_evidence_refs(d.pop("evidence_refs", UNSET))

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

        def _parse_target_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        target_value = _parse_target_value(d.pop("target_value", UNSET))

        def _parse_due_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = datetime.datetime.fromisoformat(data)

                return due_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        agent_target_update = cls(
            current_value=current_value,
            status=status,
            evidence_refs=evidence_refs,
            reviewed_by_id=reviewed_by_id,
            target_value=target_value,
            due_at=due_at,
        )

        agent_target_update.additional_properties = d
        return agent_target_update

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
