from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.score_event_create_evidence_refs_type_0_item import ScoreEventCreateEvidenceRefsType0Item
    from ..models.score_event_create_evidence_refs_type_1 import ScoreEventCreateEvidenceRefsType1
    from ..models.score_event_create_multi_party_confirmed_by_type_0_item import (
        ScoreEventCreateMultiPartyConfirmedByType0Item,
    )


T = TypeVar("T", bound="ScoreEventCreate")


@_attrs_define
class ScoreEventCreate:
    """Request body for POST /api/observability/scoring/events.

    Attributes:
        bot_id (UUID):
        event_type (str):
        delta (float):
        reason (str):
        evidence_refs (list[ScoreEventCreateEvidenceRefsType0Item] | ScoreEventCreateEvidenceRefsType1):
        granted_by_id (UUID):
        granted_by_type (str):
        granted_by_role (str):
        org_id (UUID):
        multi_party_confirmed_by (list[ScoreEventCreateMultiPartyConfirmedByType0Item] | None | Unset):
    """

    bot_id: UUID
    event_type: str
    delta: float
    reason: str
    evidence_refs: list[ScoreEventCreateEvidenceRefsType0Item] | ScoreEventCreateEvidenceRefsType1
    granted_by_id: UUID
    granted_by_type: str
    granted_by_role: str
    org_id: UUID
    multi_party_confirmed_by: list[ScoreEventCreateMultiPartyConfirmedByType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        org_id = str(self.org_id)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "event_type": event_type,
                "delta": delta,
                "reason": reason,
                "evidence_refs": evidence_refs,
                "granted_by_id": granted_by_id,
                "granted_by_type": granted_by_type,
                "granted_by_role": granted_by_role,
                "org_id": org_id,
            }
        )
        if multi_party_confirmed_by is not UNSET:
            field_dict["multi_party_confirmed_by"] = multi_party_confirmed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.score_event_create_evidence_refs_type_0_item import (
            ScoreEventCreateEvidenceRefsType0Item,  # noqa: PLC0415
        )
        from ..models.score_event_create_evidence_refs_type_1 import ScoreEventCreateEvidenceRefsType1  # noqa: PLC0415
        from ..models.score_event_create_multi_party_confirmed_by_type_0_item import (
            ScoreEventCreateMultiPartyConfirmedByType0Item,  # noqa: PLC0415
        )

        d = dict(src_dict)
        bot_id = UUID(d.pop("bot_id"))

        event_type = d.pop("event_type")

        delta = d.pop("delta")

        reason = d.pop("reason")

        def _parse_evidence_refs(
            data: object,
        ) -> list[ScoreEventCreateEvidenceRefsType0Item] | ScoreEventCreateEvidenceRefsType1:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_refs_type_0 = []
                _evidence_refs_type_0 = data
                for evidence_refs_type_0_item_data in _evidence_refs_type_0:
                    evidence_refs_type_0_item = ScoreEventCreateEvidenceRefsType0Item.from_dict(
                        evidence_refs_type_0_item_data
                    )

                    evidence_refs_type_0.append(evidence_refs_type_0_item)

                return evidence_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            evidence_refs_type_1 = ScoreEventCreateEvidenceRefsType1.from_dict(data)

            return evidence_refs_type_1

        evidence_refs = _parse_evidence_refs(d.pop("evidence_refs"))

        granted_by_id = UUID(d.pop("granted_by_id"))

        granted_by_type = d.pop("granted_by_type")

        granted_by_role = d.pop("granted_by_role")

        org_id = UUID(d.pop("org_id"))

        def _parse_multi_party_confirmed_by(
            data: object,
        ) -> list[ScoreEventCreateMultiPartyConfirmedByType0Item] | None | Unset:
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
                    multi_party_confirmed_by_type_0_item = ScoreEventCreateMultiPartyConfirmedByType0Item.from_dict(
                        multi_party_confirmed_by_type_0_item_data
                    )

                    multi_party_confirmed_by_type_0.append(multi_party_confirmed_by_type_0_item)

                return multi_party_confirmed_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ScoreEventCreateMultiPartyConfirmedByType0Item] | None | Unset, data)

        multi_party_confirmed_by = _parse_multi_party_confirmed_by(d.pop("multi_party_confirmed_by", UNSET))

        score_event_create = cls(
            bot_id=bot_id,
            event_type=event_type,
            delta=delta,
            reason=reason,
            evidence_refs=evidence_refs,
            granted_by_id=granted_by_id,
            granted_by_type=granted_by_type,
            granted_by_role=granted_by_role,
            org_id=org_id,
            multi_party_confirmed_by=multi_party_confirmed_by,
        )

        score_event_create.additional_properties = d
        return score_event_create

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
