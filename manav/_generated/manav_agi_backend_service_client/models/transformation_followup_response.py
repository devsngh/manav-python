from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transformation_followup_response_cited_evidence_item import (
        TransformationFollowupResponseCitedEvidenceItem,
    )
    from ..models.transformation_followup_response_observed_impact import TransformationFollowupResponseObservedImpact


T = TypeVar("T", bound="TransformationFollowupResponse")


@_attrs_define
class TransformationFollowupResponse:
    """
    Attributes:
        id (UUID):
        proposal_id (UUID):
        authoring_bot_id (UUID):
        followup_window_days (int):
        observed_impact (TransformationFollowupResponseObservedImpact):
        cited_evidence (list[TransformationFollowupResponseCitedEvidenceItem]):
        outcome (str):
        feeds_back_to_playbook (bool):
        feeds_back_to_lessons (bool):
        org_id (UUID):
        created_at (datetime.datetime):
        notes (None | str | Unset):
    """

    id: UUID
    proposal_id: UUID
    authoring_bot_id: UUID
    followup_window_days: int
    observed_impact: TransformationFollowupResponseObservedImpact
    cited_evidence: list[TransformationFollowupResponseCitedEvidenceItem]
    outcome: str
    feeds_back_to_playbook: bool
    feeds_back_to_lessons: bool
    org_id: UUID
    created_at: datetime.datetime
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        proposal_id = str(self.proposal_id)

        authoring_bot_id = str(self.authoring_bot_id)

        followup_window_days = self.followup_window_days

        observed_impact = self.observed_impact.to_dict()

        cited_evidence = []
        for cited_evidence_item_data in self.cited_evidence:
            cited_evidence_item = cited_evidence_item_data.to_dict()
            cited_evidence.append(cited_evidence_item)

        outcome = self.outcome

        feeds_back_to_playbook = self.feeds_back_to_playbook

        feeds_back_to_lessons = self.feeds_back_to_lessons

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "proposal_id": proposal_id,
                "authoring_bot_id": authoring_bot_id,
                "followup_window_days": followup_window_days,
                "observed_impact": observed_impact,
                "cited_evidence": cited_evidence,
                "outcome": outcome,
                "feeds_back_to_playbook": feeds_back_to_playbook,
                "feeds_back_to_lessons": feeds_back_to_lessons,
                "org_id": org_id,
                "created_at": created_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transformation_followup_response_cited_evidence_item import (
            TransformationFollowupResponseCitedEvidenceItem,  # noqa: PLC0415
        )
        from ..models.transformation_followup_response_observed_impact import (
            TransformationFollowupResponseObservedImpact,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        proposal_id = UUID(d.pop("proposal_id"))

        authoring_bot_id = UUID(d.pop("authoring_bot_id"))

        followup_window_days = d.pop("followup_window_days")

        observed_impact = TransformationFollowupResponseObservedImpact.from_dict(d.pop("observed_impact"))

        cited_evidence = []
        _cited_evidence = d.pop("cited_evidence")
        for cited_evidence_item_data in _cited_evidence:
            cited_evidence_item = TransformationFollowupResponseCitedEvidenceItem.from_dict(cited_evidence_item_data)

            cited_evidence.append(cited_evidence_item)

        outcome = d.pop("outcome")

        feeds_back_to_playbook = d.pop("feeds_back_to_playbook")

        feeds_back_to_lessons = d.pop("feeds_back_to_lessons")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        transformation_followup_response = cls(
            id=id,
            proposal_id=proposal_id,
            authoring_bot_id=authoring_bot_id,
            followup_window_days=followup_window_days,
            observed_impact=observed_impact,
            cited_evidence=cited_evidence,
            outcome=outcome,
            feeds_back_to_playbook=feeds_back_to_playbook,
            feeds_back_to_lessons=feeds_back_to_lessons,
            org_id=org_id,
            created_at=created_at,
            notes=notes,
        )

        transformation_followup_response.additional_properties = d
        return transformation_followup_response

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
