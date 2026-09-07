from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompetitorSignalResponse")


@_attrs_define
class CompetitorSignalResponse:
    """
    Attributes:
        id (UUID):
        competitor_id (UUID):
        observed_at (datetime.datetime):
        signal_type (str):
        signal_summary (str):
        evidence_url (None | str):
        source_description (None | str):
        confidence (str):
        detected_by_bot_id (None | UUID):
        detected_in_dept (None | str):
        created_at (datetime.datetime):
    """

    id: UUID
    competitor_id: UUID
    observed_at: datetime.datetime
    signal_type: str
    signal_summary: str
    evidence_url: None | str
    source_description: None | str
    confidence: str
    detected_by_bot_id: None | UUID
    detected_in_dept: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        competitor_id = str(self.competitor_id)

        observed_at = self.observed_at.isoformat()

        signal_type = self.signal_type

        signal_summary = self.signal_summary

        evidence_url: None | str
        evidence_url = self.evidence_url

        source_description: None | str
        source_description = self.source_description

        confidence = self.confidence

        detected_by_bot_id: None | str
        if isinstance(self.detected_by_bot_id, UUID):
            detected_by_bot_id = str(self.detected_by_bot_id)
        else:
            detected_by_bot_id = self.detected_by_bot_id

        detected_in_dept: None | str
        detected_in_dept = self.detected_in_dept

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "competitor_id": competitor_id,
                "observed_at": observed_at,
                "signal_type": signal_type,
                "signal_summary": signal_summary,
                "evidence_url": evidence_url,
                "source_description": source_description,
                "confidence": confidence,
                "detected_by_bot_id": detected_by_bot_id,
                "detected_in_dept": detected_in_dept,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        competitor_id = UUID(d.pop("competitor_id"))

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        signal_type = d.pop("signal_type")

        signal_summary = d.pop("signal_summary")

        def _parse_evidence_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evidence_url = _parse_evidence_url(d.pop("evidence_url"))

        def _parse_source_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source_description = _parse_source_description(d.pop("source_description"))

        confidence = d.pop("confidence")

        def _parse_detected_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                detected_by_bot_id_type_0 = UUID(data)

                return detected_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        detected_by_bot_id = _parse_detected_by_bot_id(d.pop("detected_by_bot_id"))

        def _parse_detected_in_dept(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        detected_in_dept = _parse_detected_in_dept(d.pop("detected_in_dept"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        competitor_signal_response = cls(
            id=id,
            competitor_id=competitor_id,
            observed_at=observed_at,
            signal_type=signal_type,
            signal_summary=signal_summary,
            evidence_url=evidence_url,
            source_description=source_description,
            confidence=confidence,
            detected_by_bot_id=detected_by_bot_id,
            detected_in_dept=detected_in_dept,
            created_at=created_at,
        )

        competitor_signal_response.additional_properties = d
        return competitor_signal_response

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
