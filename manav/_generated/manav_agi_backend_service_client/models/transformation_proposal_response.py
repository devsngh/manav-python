from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transformation_proposal_response_evidence_chain_item import (
        TransformationProposalResponseEvidenceChainItem,
    )
    from ..models.transformation_proposal_response_expected_impact import TransformationProposalResponseExpectedImpact


T = TypeVar("T", bound="TransformationProposalResponse")


@_attrs_define
class TransformationProposalResponse:
    """
    Attributes:
        id (UUID):
        authoring_bot_id (UUID):
        target_layer (str):
        evidence_chain (list[TransformationProposalResponseEvidenceChainItem]):
        specific_change (str):
        expected_impact (TransformationProposalResponseExpectedImpact):
        risk (str):
        rollback_plan (str):
        status (str):
        org_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        counter_argument (None | str | Unset):
        surfaced_at (datetime.datetime | None | Unset):
        ratified_at (datetime.datetime | None | Unset):
        ratified_by (None | Unset | UUID):
        committed_at (datetime.datetime | None | Unset):
        committed_deepagent_id (None | Unset | UUID):
        certified_at (datetime.datetime | None | Unset):
        certification_round_id (None | Unset | UUID):
        rejected_reason (None | str | Unset):
        withdrawn_reason (None | str | Unset):
    """

    id: UUID
    authoring_bot_id: UUID
    target_layer: str
    evidence_chain: list[TransformationProposalResponseEvidenceChainItem]
    specific_change: str
    expected_impact: TransformationProposalResponseExpectedImpact
    risk: str
    rollback_plan: str
    status: str
    org_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    counter_argument: None | str | Unset = UNSET
    surfaced_at: datetime.datetime | None | Unset = UNSET
    ratified_at: datetime.datetime | None | Unset = UNSET
    ratified_by: None | Unset | UUID = UNSET
    committed_at: datetime.datetime | None | Unset = UNSET
    committed_deepagent_id: None | Unset | UUID = UNSET
    certified_at: datetime.datetime | None | Unset = UNSET
    certification_round_id: None | Unset | UUID = UNSET
    rejected_reason: None | str | Unset = UNSET
    withdrawn_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        authoring_bot_id = str(self.authoring_bot_id)

        target_layer = self.target_layer

        evidence_chain = []
        for evidence_chain_item_data in self.evidence_chain:
            evidence_chain_item = evidence_chain_item_data.to_dict()
            evidence_chain.append(evidence_chain_item)

        specific_change = self.specific_change

        expected_impact = self.expected_impact.to_dict()

        risk = self.risk

        rollback_plan = self.rollback_plan

        status = self.status

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        counter_argument: None | str | Unset
        if isinstance(self.counter_argument, Unset):
            counter_argument = UNSET
        else:
            counter_argument = self.counter_argument

        surfaced_at: None | str | Unset
        if isinstance(self.surfaced_at, Unset):
            surfaced_at = UNSET
        elif isinstance(self.surfaced_at, datetime.datetime):
            surfaced_at = self.surfaced_at.isoformat()
        else:
            surfaced_at = self.surfaced_at

        ratified_at: None | str | Unset
        if isinstance(self.ratified_at, Unset):
            ratified_at = UNSET
        elif isinstance(self.ratified_at, datetime.datetime):
            ratified_at = self.ratified_at.isoformat()
        else:
            ratified_at = self.ratified_at

        ratified_by: None | str | Unset
        if isinstance(self.ratified_by, Unset):
            ratified_by = UNSET
        elif isinstance(self.ratified_by, UUID):
            ratified_by = str(self.ratified_by)
        else:
            ratified_by = self.ratified_by

        committed_at: None | str | Unset
        if isinstance(self.committed_at, Unset):
            committed_at = UNSET
        elif isinstance(self.committed_at, datetime.datetime):
            committed_at = self.committed_at.isoformat()
        else:
            committed_at = self.committed_at

        committed_deepagent_id: None | str | Unset
        if isinstance(self.committed_deepagent_id, Unset):
            committed_deepagent_id = UNSET
        elif isinstance(self.committed_deepagent_id, UUID):
            committed_deepagent_id = str(self.committed_deepagent_id)
        else:
            committed_deepagent_id = self.committed_deepagent_id

        certified_at: None | str | Unset
        if isinstance(self.certified_at, Unset):
            certified_at = UNSET
        elif isinstance(self.certified_at, datetime.datetime):
            certified_at = self.certified_at.isoformat()
        else:
            certified_at = self.certified_at

        certification_round_id: None | str | Unset
        if isinstance(self.certification_round_id, Unset):
            certification_round_id = UNSET
        elif isinstance(self.certification_round_id, UUID):
            certification_round_id = str(self.certification_round_id)
        else:
            certification_round_id = self.certification_round_id

        rejected_reason: None | str | Unset
        if isinstance(self.rejected_reason, Unset):
            rejected_reason = UNSET
        else:
            rejected_reason = self.rejected_reason

        withdrawn_reason: None | str | Unset
        if isinstance(self.withdrawn_reason, Unset):
            withdrawn_reason = UNSET
        else:
            withdrawn_reason = self.withdrawn_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "authoring_bot_id": authoring_bot_id,
                "target_layer": target_layer,
                "evidence_chain": evidence_chain,
                "specific_change": specific_change,
                "expected_impact": expected_impact,
                "risk": risk,
                "rollback_plan": rollback_plan,
                "status": status,
                "org_id": org_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if counter_argument is not UNSET:
            field_dict["counter_argument"] = counter_argument
        if surfaced_at is not UNSET:
            field_dict["surfaced_at"] = surfaced_at
        if ratified_at is not UNSET:
            field_dict["ratified_at"] = ratified_at
        if ratified_by is not UNSET:
            field_dict["ratified_by"] = ratified_by
        if committed_at is not UNSET:
            field_dict["committed_at"] = committed_at
        if committed_deepagent_id is not UNSET:
            field_dict["committed_deepagent_id"] = committed_deepagent_id
        if certified_at is not UNSET:
            field_dict["certified_at"] = certified_at
        if certification_round_id is not UNSET:
            field_dict["certification_round_id"] = certification_round_id
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if withdrawn_reason is not UNSET:
            field_dict["withdrawn_reason"] = withdrawn_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transformation_proposal_response_evidence_chain_item import (
            TransformationProposalResponseEvidenceChainItem,  # noqa: PLC0415
        )
        from ..models.transformation_proposal_response_expected_impact import (
            TransformationProposalResponseExpectedImpact,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        target_layer = d.pop("target_layer")

        evidence_chain = []
        _evidence_chain = d.pop("evidence_chain")
        for evidence_chain_item_data in _evidence_chain:
            evidence_chain_item = TransformationProposalResponseEvidenceChainItem.from_dict(evidence_chain_item_data)

            evidence_chain.append(evidence_chain_item)

        specific_change = d.pop("specific_change")

        expected_impact = TransformationProposalResponseExpectedImpact.from_dict(d.pop("expected_impact"))

        risk = d.pop("risk")

        rollback_plan = d.pop("rollback_plan")

        status = d.pop("status")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_counter_argument(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counter_argument = _parse_counter_argument(d.pop("counter_argument", UNSET))

        def _parse_surfaced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                surfaced_at_type_0 = datetime.datetime.fromisoformat(data)

                return surfaced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        surfaced_at = _parse_surfaced_at(d.pop("surfaced_at", UNSET))

        def _parse_ratified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ratified_at_type_0 = datetime.datetime.fromisoformat(data)

                return ratified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ratified_at = _parse_ratified_at(d.pop("ratified_at", UNSET))

        def _parse_ratified_by(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ratified_by_type_0 = UUID(data)

                return ratified_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        ratified_by = _parse_ratified_by(d.pop("ratified_by", UNSET))

        def _parse_committed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_at_type_0 = datetime.datetime.fromisoformat(data)

                return committed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        committed_at = _parse_committed_at(d.pop("committed_at", UNSET))

        def _parse_committed_deepagent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_deepagent_id_type_0 = UUID(data)

                return committed_deepagent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        committed_deepagent_id = _parse_committed_deepagent_id(d.pop("committed_deepagent_id", UNSET))

        def _parse_certified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certified_at_type_0 = datetime.datetime.fromisoformat(data)

                return certified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        certified_at = _parse_certified_at(d.pop("certified_at", UNSET))

        def _parse_certification_round_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                certification_round_id_type_0 = UUID(data)

                return certification_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        certification_round_id = _parse_certification_round_id(d.pop("certification_round_id", UNSET))

        def _parse_rejected_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejected_reason = _parse_rejected_reason(d.pop("rejected_reason", UNSET))

        def _parse_withdrawn_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        withdrawn_reason = _parse_withdrawn_reason(d.pop("withdrawn_reason", UNSET))

        transformation_proposal_response = cls(
            id=id,
            authoring_bot_id=authoring_bot_id,
            target_layer=target_layer,
            evidence_chain=evidence_chain,
            specific_change=specific_change,
            expected_impact=expected_impact,
            risk=risk,
            rollback_plan=rollback_plan,
            status=status,
            org_id=org_id,
            created_at=created_at,
            updated_at=updated_at,
            counter_argument=counter_argument,
            surfaced_at=surfaced_at,
            ratified_at=ratified_at,
            ratified_by=ratified_by,
            committed_at=committed_at,
            committed_deepagent_id=committed_deepagent_id,
            certified_at=certified_at,
            certification_round_id=certification_round_id,
            rejected_reason=rejected_reason,
            withdrawn_reason=withdrawn_reason,
        )

        transformation_proposal_response.additional_properties = d
        return transformation_proposal_response

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
