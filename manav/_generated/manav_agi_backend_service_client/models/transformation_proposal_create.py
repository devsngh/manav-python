from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.target_layer import TargetLayer
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transformation_proposal_create_evidence_chain_item import (
        TransformationProposalCreateEvidenceChainItem,
    )
    from ..models.transformation_proposal_create_expected_impact import TransformationProposalCreateExpectedImpact


T = TypeVar("T", bound="TransformationProposalCreate")


@_attrs_define
class TransformationProposalCreate:
    """
    Attributes:
        authoring_bot_id (UUID):
        target_layer (TargetLayer): parivartan_proposals.target_layer — what stratum the change touches.
        evidence_chain (list[TransformationProposalCreateEvidenceChainItem]):
        specific_change (str):
        expected_impact (TransformationProposalCreateExpectedImpact):
        risk (str):
        rollback_plan (str):
        org_id (UUID):
        counter_argument (None | str | Unset):
    """

    authoring_bot_id: UUID
    target_layer: TargetLayer
    evidence_chain: list[TransformationProposalCreateEvidenceChainItem]
    specific_change: str
    expected_impact: TransformationProposalCreateExpectedImpact
    risk: str
    rollback_plan: str
    org_id: UUID
    counter_argument: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authoring_bot_id = str(self.authoring_bot_id)

        target_layer = self.target_layer.value

        evidence_chain = []
        for evidence_chain_item_data in self.evidence_chain:
            evidence_chain_item = evidence_chain_item_data.to_dict()
            evidence_chain.append(evidence_chain_item)

        specific_change = self.specific_change

        expected_impact = self.expected_impact.to_dict()

        risk = self.risk

        rollback_plan = self.rollback_plan

        org_id = str(self.org_id)

        counter_argument: None | str | Unset
        if isinstance(self.counter_argument, Unset):
            counter_argument = UNSET
        else:
            counter_argument = self.counter_argument

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authoring_bot_id": authoring_bot_id,
                "target_layer": target_layer,
                "evidence_chain": evidence_chain,
                "specific_change": specific_change,
                "expected_impact": expected_impact,
                "risk": risk,
                "rollback_plan": rollback_plan,
                "org_id": org_id,
            }
        )
        if counter_argument is not UNSET:
            field_dict["counter_argument"] = counter_argument

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transformation_proposal_create_evidence_chain_item import (
            TransformationProposalCreateEvidenceChainItem,  # noqa: PLC0415
        )
        from ..models.transformation_proposal_create_expected_impact import (
            TransformationProposalCreateExpectedImpact,  # noqa: PLC0415
        )

        d = dict(src_dict)
        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        target_layer = TargetLayer(d.pop("target_layer"))

        evidence_chain = []
        _evidence_chain = d.pop("evidence_chain")
        for evidence_chain_item_data in _evidence_chain:
            evidence_chain_item = TransformationProposalCreateEvidenceChainItem.from_dict(evidence_chain_item_data)

            evidence_chain.append(evidence_chain_item)

        specific_change = d.pop("specific_change")

        expected_impact = TransformationProposalCreateExpectedImpact.from_dict(d.pop("expected_impact"))

        risk = d.pop("risk")

        rollback_plan = d.pop("rollback_plan")

        org_id = UUID(d.pop("org_id"))

        def _parse_counter_argument(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        counter_argument = _parse_counter_argument(d.pop("counter_argument", UNSET))

        transformation_proposal_create = cls(
            authoring_bot_id=authoring_bot_id,
            target_layer=target_layer,
            evidence_chain=evidence_chain,
            specific_change=specific_change,
            expected_impact=expected_impact,
            risk=risk,
            rollback_plan=rollback_plan,
            org_id=org_id,
            counter_argument=counter_argument,
        )

        transformation_proposal_create.additional_properties = d
        return transformation_proposal_create

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
