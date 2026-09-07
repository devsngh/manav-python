from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.score_event_response_evidence_refs_type_0_item import ScoreEventResponseEvidenceRefsType0Item
    from ..models.score_event_response_evidence_refs_type_1 import ScoreEventResponseEvidenceRefsType1
    from ..models.score_event_response_multi_party_confirmed_by_type_0_item import (
        ScoreEventResponseMultiPartyConfirmedByType0Item,
    )


T = TypeVar("T", bound="ScoreEventResponse")


@_attrs_define
class ScoreEventResponse:
    """
    Attributes:
        id (UUID):
        bot_id (UUID):
        event_type (str):
        delta (float):
        reason (str):
        evidence_refs (list[ScoreEventResponseEvidenceRefsType0Item] | ScoreEventResponseEvidenceRefsType1):
        granted_by_id (UUID):
        granted_by_type (str):
        granted_by_role (str):
        multi_party_required (bool):
        org_id (UUID):
        created_at (datetime.datetime):
        multi_party_confirmed_by (list[ScoreEventResponseMultiPartyConfirmedByType0Item] | None | Unset):
        applied_at (datetime.datetime | None | Unset):
    """

    id: UUID
    bot_id: UUID
    event_type: str
    delta: float
    reason: str
    evidence_refs: list[ScoreEventResponseEvidenceRefsType0Item] | ScoreEventResponseEvidenceRefsType1
    granted_by_id: UUID
    granted_by_type: str
    granted_by_role: str
    multi_party_required: bool
    org_id: UUID
    created_at: datetime.datetime
    multi_party_confirmed_by: list[ScoreEventResponseMultiPartyConfirmedByType0Item] | None | Unset = UNSET
    applied_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        bot_id = str(self.bot_id)

        event_type = self.event_type

        delta = self.delta

        reason = self.reason

        evidence_refs: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.evidence_refs, list):
            evidence_refs = []
            for evidence_refs_type_0_item_data in self.evidence_refs:
                evidence_refs_type_0_item = evidence_refs_type_0_item_data.to_dict()
                evidence_refs.append(evidence_refs_type_0_item)

        else:
            evidence_refs = self.evidence_refs.to_dict()

        granted_by_id = str(self.granted_by_id)

        granted_by_type = self.granted_by_type

        granted_by_role = self.granted_by_role

        multi_party_required = self.multi_party_required

        org_id = str(self.org_id)

        created_at = self.created_at.isoformat()

        multi_party_confirmed_by: list[dict[str, Any]] | None | Unset
        if isinstance(self.multi_party_confirmed_by, Unset):
            multi_party_confirmed_by = UNSET
        elif isinstance(self.multi_party_confirmed_by, list):
            multi_party_confirmed_by = []
            for multi_party_confirmed_by_type_0_item_data in self.multi_party_confirmed_by:
                multi_party_confirmed_by_type_0_item = multi_party_confirmed_by_type_0_item_data.to_dict()
                multi_party_confirmed_by.append(multi_party_confirmed_by_type_0_item)

        else:
            multi_party_confirmed_by = self.multi_party_confirmed_by

        applied_at: None | str | Unset
        if isinstance(self.applied_at, Unset):
            applied_at = UNSET
        elif isinstance(self.applied_at, datetime.datetime):
            applied_at = self.applied_at.isoformat()
        else:
            applied_at = self.applied_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "bot_id": bot_id,
                "event_type": event_type,
                "delta": delta,
                "reason": reason,
                "evidence_refs": evidence_refs,
                "granted_by_id": granted_by_id,
                "granted_by_type": granted_by_type,
                "granted_by_role": granted_by_role,
                "multi_party_required": multi_party_required,
                "org_id": org_id,
                "created_at": created_at,
            }
        )
        if multi_party_confirmed_by is not UNSET:
            field_dict["multi_party_confirmed_by"] = multi_party_confirmed_by
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.score_event_response_evidence_refs_type_0_item import (
            ScoreEventResponseEvidenceRefsType0Item,  # noqa: PLC0415
        )
        from ..models.score_event_response_evidence_refs_type_1 import (
            ScoreEventResponseEvidenceRefsType1,  # noqa: PLC0415
        )
        from ..models.score_event_response_multi_party_confirmed_by_type_0_item import (
            ScoreEventResponseMultiPartyConfirmedByType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        bot_id = UUID(d.pop("bot_id"))

        event_type = d.pop("event_type")

        delta = d.pop("delta")

        reason = d.pop("reason")

        def _parse_evidence_refs(
            data: object,
        ) -> list[ScoreEventResponseEvidenceRefsType0Item] | ScoreEventResponseEvidenceRefsType1:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_refs_type_0 = []
                _evidence_refs_type_0 = data
                for evidence_refs_type_0_item_data in _evidence_refs_type_0:
                    evidence_refs_type_0_item = ScoreEventResponseEvidenceRefsType0Item.from_dict(
                        evidence_refs_type_0_item_data
                    )

                    evidence_refs_type_0.append(evidence_refs_type_0_item)

                return evidence_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            evidence_refs_type_1 = ScoreEventResponseEvidenceRefsType1.from_dict(data)

            return evidence_refs_type_1

        evidence_refs = _parse_evidence_refs(d.pop("evidence_refs"))

        granted_by_id = UUID(d.pop("granted_by_id"))

        granted_by_type = d.pop("granted_by_type")

        granted_by_role = d.pop("granted_by_role")

        multi_party_required = d.pop("multi_party_required")

        org_id = UUID(d.pop("org_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_multi_party_confirmed_by(
            data: object,
        ) -> list[ScoreEventResponseMultiPartyConfirmedByType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                multi_party_confirmed_by_type_0 = []
                _multi_party_confirmed_by_type_0 = data
                for multi_party_confirmed_by_type_0_item_data in _multi_party_confirmed_by_type_0:
                    multi_party_confirmed_by_type_0_item = ScoreEventResponseMultiPartyConfirmedByType0Item.from_dict(
                        multi_party_confirmed_by_type_0_item_data
                    )

                    multi_party_confirmed_by_type_0.append(multi_party_confirmed_by_type_0_item)

                return multi_party_confirmed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ScoreEventResponseMultiPartyConfirmedByType0Item] | None | Unset, data)

        multi_party_confirmed_by = _parse_multi_party_confirmed_by(d.pop("multi_party_confirmed_by", UNSET))

        def _parse_applied_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        applied_at = _parse_applied_at(d.pop("applied_at", UNSET))

        score_event_response = cls(
            id=id,
            bot_id=bot_id,
            event_type=event_type,
            delta=delta,
            reason=reason,
            evidence_refs=evidence_refs,
            granted_by_id=granted_by_id,
            granted_by_type=granted_by_type,
            granted_by_role=granted_by_role,
            multi_party_required=multi_party_required,
            org_id=org_id,
            created_at=created_at,
            multi_party_confirmed_by=multi_party_confirmed_by,
            applied_at=applied_at,
        )

        score_event_response.additional_properties = d
        return score_event_response

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
