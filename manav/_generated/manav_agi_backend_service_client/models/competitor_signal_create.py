from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompetitorSignalCreate")


@_attrs_define
class CompetitorSignalCreate:
    """
    Attributes:
        signal_type (str): launch / pricing_change / leadership / funding / campaign / content_move / partnership
        signal_summary (str):
        confidence (str): high / medium / low
        evidence_url (None | str | Unset):
        source_description (None | str | Unset):
        detected_in_dept (None | str | Unset):
        observed_at (datetime.datetime | None | Unset):
    """

    signal_type: str
    signal_summary: str
    confidence: str
    evidence_url: None | str | Unset = UNSET
    source_description: None | str | Unset = UNSET
    detected_in_dept: None | str | Unset = UNSET
    observed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signal_type = self.signal_type

        signal_summary = self.signal_summary

        confidence = self.confidence

        evidence_url: None | str | Unset
        if isinstance(self.evidence_url, Unset):
            evidence_url = UNSET
        else:
            evidence_url = self.evidence_url

        source_description: None | str | Unset
        if isinstance(self.source_description, Unset):
            source_description = UNSET
        else:
            source_description = self.source_description

        detected_in_dept: None | str | Unset
        if isinstance(self.detected_in_dept, Unset):
            detected_in_dept = UNSET
        else:
            detected_in_dept = self.detected_in_dept

        observed_at: None | str | Unset
        if isinstance(self.observed_at, Unset):
            observed_at = UNSET
        elif isinstance(self.observed_at, datetime.datetime):
            observed_at = self.observed_at.isoformat()
        else:
            observed_at = self.observed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signal_type": signal_type,
                "signal_summary": signal_summary,
                "confidence": confidence,
            }
        )
        if evidence_url is not UNSET:
            field_dict["evidence_url"] = evidence_url
        if source_description is not UNSET:
            field_dict["source_description"] = source_description
        if detected_in_dept is not UNSET:
            field_dict["detected_in_dept"] = detected_in_dept
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signal_type = d.pop("signal_type")

        signal_summary = d.pop("signal_summary")

        confidence = d.pop("confidence")

        def _parse_evidence_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evidence_url = _parse_evidence_url(d.pop("evidence_url", UNSET))

        def _parse_source_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_description = _parse_source_description(d.pop("source_description", UNSET))

        def _parse_detected_in_dept(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detected_in_dept = _parse_detected_in_dept(d.pop("detected_in_dept", UNSET))

        def _parse_observed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_at_type_0 = datetime.datetime.fromisoformat(data)

                return observed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        observed_at = _parse_observed_at(d.pop("observed_at", UNSET))

        competitor_signal_create = cls(
            signal_type=signal_type,
            signal_summary=signal_summary,
            confidence=confidence,
            evidence_url=evidence_url,
            source_description=source_description,
            detected_in_dept=detected_in_dept,
            observed_at=observed_at,
        )

        competitor_signal_create.additional_properties = d
        return competitor_signal_create

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
