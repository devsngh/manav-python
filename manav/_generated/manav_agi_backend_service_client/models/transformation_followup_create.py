from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.followup_outcome import FollowupOutcome
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transformation_followup_create_cited_evidence_item import (
        TransformationFollowupCreateCitedEvidenceItem,
    )
    from ..models.transformation_followup_create_observed_impact import TransformationFollowupCreateObservedImpact


T = TypeVar("T", bound="TransformationFollowupCreate")


@_attrs_define
class TransformationFollowupCreate:
    """
    Attributes:
        proposal_id (UUID):
        authoring_bot_id (UUID):
        observed_impact (TransformationFollowupCreateObservedImpact):
        cited_evidence (list[TransformationFollowupCreateCitedEvidenceItem]):
        outcome (FollowupOutcome): parivartan_followups.outcome — did the predicted impact land?
        org_id (UUID):
        followup_window_days (int | Unset):  Default: 30.
        notes (None | str | Unset):
        feeds_back_to_playbook (bool | Unset):  Default: False.
        feeds_back_to_lessons (bool | Unset):  Default: False.
    """

    proposal_id: UUID
    authoring_bot_id: UUID
    observed_impact: TransformationFollowupCreateObservedImpact
    cited_evidence: list[TransformationFollowupCreateCitedEvidenceItem]
    outcome: FollowupOutcome
    org_id: UUID
    followup_window_days: int | Unset = 30
    notes: None | str | Unset = UNSET
    feeds_back_to_playbook: bool | Unset = False
    feeds_back_to_lessons: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = str(self.proposal_id)

        authoring_bot_id = str(self.authoring_bot_id)

        observed_impact = self.observed_impact.to_dict()

        cited_evidence = []
        for cited_evidence_item_data in self.cited_evidence:
            cited_evidence_item = cited_evidence_item_data.to_dict()
            cited_evidence.append(cited_evidence_item)

        outcome = self.outcome.value

        org_id = str(self.org_id)

        followup_window_days = self.followup_window_days

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        feeds_back_to_playbook = self.feeds_back_to_playbook

        feeds_back_to_lessons = self.feeds_back_to_lessons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_id": proposal_id,
                "authoring_bot_id": authoring_bot_id,
                "observed_impact": observed_impact,
                "cited_evidence": cited_evidence,
                "outcome": outcome,
                "org_id": org_id,
            }
        )
        if followup_window_days is not UNSET:
            field_dict["followup_window_days"] = followup_window_days
        if notes is not UNSET:
            field_dict["notes"] = notes
        if feeds_back_to_playbook is not UNSET:
            field_dict["feeds_back_to_playbook"] = feeds_back_to_playbook
        if feeds_back_to_lessons is not UNSET:
            field_dict["feeds_back_to_lessons"] = feeds_back_to_lessons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transformation_followup_create_cited_evidence_item import (
            TransformationFollowupCreateCitedEvidenceItem,  # noqa: PLC0415
        )
        from ..models.transformation_followup_create_observed_impact import (
            TransformationFollowupCreateObservedImpact,  # noqa: PLC0415
        )

        d = dict(src_dict)
        proposal_id = UUID(d.pop("proposal_id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        observed_impact = TransformationFollowupCreateObservedImpact.from_dict(d.pop("observed_impact"))

        cited_evidence = []
        _cited_evidence = d.pop("cited_evidence")
        for cited_evidence_item_data in _cited_evidence:
            cited_evidence_item = TransformationFollowupCreateCitedEvidenceItem.from_dict(cited_evidence_item_data)

            cited_evidence.append(cited_evidence_item)

        outcome = FollowupOutcome(d.pop("outcome"))

        org_id = UUID(d.pop("org_id"))

        followup_window_days = d.pop("followup_window_days", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        feeds_back_to_playbook = d.pop("feeds_back_to_playbook", UNSET)

        feeds_back_to_lessons = d.pop("feeds_back_to_lessons", UNSET)

        transformation_followup_create = cls(
            proposal_id=proposal_id,
            authoring_bot_id=authoring_bot_id,
            observed_impact=observed_impact,
            cited_evidence=cited_evidence,
            outcome=outcome,
            org_id=org_id,
            followup_window_days=followup_window_days,
            notes=notes,
            feeds_back_to_playbook=feeds_back_to_playbook,
            feeds_back_to_lessons=feeds_back_to_lessons,
        )

        transformation_followup_create.additional_properties = d
        return transformation_followup_create

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
