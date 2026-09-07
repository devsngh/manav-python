from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observer_finding_response_evidence_trace_ids_item import ObserverFindingResponseEvidenceTraceIdsItem
    from ..models.observer_finding_response_findings import ObserverFindingResponseFindings


T = TypeVar("T", bound="ObserverFindingResponse")


@_attrs_define
class ObserverFindingResponse:
    """
    Attributes:
        id (UUID):
        observed_bot_id (UUID):
        observer_id (UUID):
        observer_type (str):
        observer_role (str):
        finding_type (str):
        severity (str):
        findings (ObserverFindingResponseFindings):
        evidence_trace_ids (list[ObserverFindingResponseEvidenceTraceIdsItem]):
        org_id (UUID):
        created_at (datetime.datetime):
        training_round_id (None | Unset | UUID):
    """

    id: UUID
    observed_bot_id: UUID
    observer_id: UUID
    observer_type: str
    observer_role: str
    finding_type: str
    severity: str
    findings: ObserverFindingResponseFindings
    evidence_trace_ids: list[ObserverFindingResponseEvidenceTraceIdsItem]
    org_id: UUID
    created_at: datetime.datetime
    training_round_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        observed_bot_id = str(self.observed_bot_id)

        observer_id = str(self.observer_id)

        observer_type = self.observer_type

        observer_role = self.observer_role

        finding_type = self.finding_type

        severity = self.severity

        findings = self.findings.to_dict()

        evidence_trace_ids = []
        for evidence_trace_ids_item_data in self.evidence_trace_ids:
            evidence_trace_ids_item = evidence_trace_ids_item_data.to_dict()
            evidence_trace_ids.append(evidence_trace_ids_item)

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        training_round_id: None | str | Unset
        if isinstance(self.training_round_id, Unset):
            training_round_id = UNSET
        elif isinstance(self.training_round_id, UUID):
            training_round_id = str(self.training_round_id)
        else:
            training_round_id = self.training_round_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "observed_bot_id": observed_bot_id,
                "observer_id": observer_id,
                "observer_type": observer_type,
                "observer_role": observer_role,
                "finding_type": finding_type,
                "severity": severity,
                "findings": findings,
                "evidence_trace_ids": evidence_trace_ids,
                "org_id": org_id,
                "created_at": created_at,
            }
        )
        if training_round_id is not UNSET:
            field_dict["training_round_id"] = training_round_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observer_finding_response_evidence_trace_ids_item import (
            ObserverFindingResponseEvidenceTraceIdsItem,  # noqa: PLC0415
        )
        from ..models.observer_finding_response_findings import ObserverFindingResponseFindings  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        observed_bot_id = UUID(d.pop("observed_bot_id"))

        observer_id = UUID(d.pop("observer_id"))

        observer_type = d.pop("observer_type")

        observer_role = d.pop("observer_role")

        finding_type = d.pop("finding_type")

        severity = d.pop("severity")

        findings = ObserverFindingResponseFindings.from_dict(d.pop("findings"))

        evidence_trace_ids = []
        _evidence_trace_ids = d.pop("evidence_trace_ids")
        for evidence_trace_ids_item_data in _evidence_trace_ids:
            evidence_trace_ids_item = ObserverFindingResponseEvidenceTraceIdsItem.from_dict(
                evidence_trace_ids_item_data
            )

            evidence_trace_ids.append(evidence_trace_ids_item)

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_training_round_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                training_round_id_type_0 = UUID(data)

                return training_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        training_round_id = _parse_training_round_id(d.pop("training_round_id", UNSET))

        observer_finding_response = cls(
            id=id,
            observed_bot_id=observed_bot_id,
            observer_id=observer_id,
            observer_type=observer_type,
            observer_role=observer_role,
            finding_type=finding_type,
            severity=severity,
            findings=findings,
            evidence_trace_ids=evidence_trace_ids,
            org_id=org_id,
            created_at=created_at,
            training_round_id=training_round_id,
        )

        observer_finding_response.additional_properties = d
        return observer_finding_response

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
