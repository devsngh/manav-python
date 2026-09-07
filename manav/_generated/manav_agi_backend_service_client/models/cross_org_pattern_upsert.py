from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cross_org_pattern_upsert_metadata_type_0 import CrossOrgPatternUpsertMetadataType0


T = TypeVar("T", bound="CrossOrgPatternUpsert")


@_attrs_define
class CrossOrgPatternUpsert:
    """
    Attributes:
        pattern_kind (str):
        pattern_summary (str):
        industry_naics (None | str | Unset):
        country_iso (None | str | Unset):
        observed_in_orgs (int | Unset):  Default: 1.
        first_observed (datetime.date | None | Unset):
        last_confirmed (datetime.date | None | Unset):
        evidence_finding_ids (list[str] | None | Unset):
        pattern_strength (float | None | str | Unset):
        ratified_by_manav (bool | Unset):  Default: False.
        ratified_date (datetime.date | None | Unset):
        superseded_by_id (None | str | Unset):
        metadata (CrossOrgPatternUpsertMetadataType0 | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    pattern_kind: str
    pattern_summary: str
    industry_naics: None | str | Unset = UNSET
    country_iso: None | str | Unset = UNSET
    observed_in_orgs: int | Unset = 1
    first_observed: datetime.date | None | Unset = UNSET
    last_confirmed: datetime.date | None | Unset = UNSET
    evidence_finding_ids: list[str] | None | Unset = UNSET
    pattern_strength: float | None | str | Unset = UNSET
    ratified_by_manav: bool | Unset = False
    ratified_date: datetime.date | None | Unset = UNSET
    superseded_by_id: None | str | Unset = UNSET
    metadata: CrossOrgPatternUpsertMetadataType0 | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cross_org_pattern_upsert_metadata_type_0 import (
            CrossOrgPatternUpsertMetadataType0,  # noqa: PLC0415
        )

        pattern_kind = self.pattern_kind

        pattern_summary = self.pattern_summary

        industry_naics: None | str | Unset
        if isinstance(self.industry_naics, Unset):
            industry_naics = UNSET
        else:
            industry_naics = self.industry_naics

        country_iso: None | str | Unset
        if isinstance(self.country_iso, Unset):
            country_iso = UNSET
        else:
            country_iso = self.country_iso

        observed_in_orgs = self.observed_in_orgs

        first_observed: None | str | Unset
        if isinstance(self.first_observed, Unset):
            first_observed = UNSET
        elif isinstance(self.first_observed, datetime.date):
            first_observed = self.first_observed.isoformat()
        else:
            first_observed = self.first_observed

        last_confirmed: None | str | Unset
        if isinstance(self.last_confirmed, Unset):
            last_confirmed = UNSET
        elif isinstance(self.last_confirmed, datetime.date):
            last_confirmed = self.last_confirmed.isoformat()
        else:
            last_confirmed = self.last_confirmed

        evidence_finding_ids: list[str] | None | Unset
        if isinstance(self.evidence_finding_ids, Unset):
            evidence_finding_ids = UNSET
        elif isinstance(self.evidence_finding_ids, list):
            evidence_finding_ids = self.evidence_finding_ids

        else:
            evidence_finding_ids = self.evidence_finding_ids

        pattern_strength: float | None | str | Unset
        if isinstance(self.pattern_strength, Unset):
            pattern_strength = UNSET
        else:
            pattern_strength = self.pattern_strength

        ratified_by_manav = self.ratified_by_manav

        ratified_date: None | str | Unset
        if isinstance(self.ratified_date, Unset):
            ratified_date = UNSET
        elif isinstance(self.ratified_date, datetime.date):
            ratified_date = self.ratified_date.isoformat()
        else:
            ratified_date = self.ratified_date

        superseded_by_id: None | str | Unset
        if isinstance(self.superseded_by_id, Unset):
            superseded_by_id = UNSET
        else:
            superseded_by_id = self.superseded_by_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CrossOrgPatternUpsertMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pattern_kind": pattern_kind,
                "pattern_summary": pattern_summary,
            }
        )
        if industry_naics is not UNSET:
            field_dict["industry_naics"] = industry_naics
        if country_iso is not UNSET:
            field_dict["country_iso"] = country_iso
        if observed_in_orgs is not UNSET:
            field_dict["observed_in_orgs"] = observed_in_orgs
        if first_observed is not UNSET:
            field_dict["first_observed"] = first_observed
        if last_confirmed is not UNSET:
            field_dict["last_confirmed"] = last_confirmed
        if evidence_finding_ids is not UNSET:
            field_dict["evidence_finding_ids"] = evidence_finding_ids
        if pattern_strength is not UNSET:
            field_dict["pattern_strength"] = pattern_strength
        if ratified_by_manav is not UNSET:
            field_dict["ratified_by_manav"] = ratified_by_manav
        if ratified_date is not UNSET:
            field_dict["ratified_date"] = ratified_date
        if superseded_by_id is not UNSET:
            field_dict["superseded_by_id"] = superseded_by_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cross_org_pattern_upsert_metadata_type_0 import (
            CrossOrgPatternUpsertMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        pattern_kind = d.pop("pattern_kind")

        pattern_summary = d.pop("pattern_summary")

        def _parse_industry_naics(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry_naics = _parse_industry_naics(d.pop("industry_naics", UNSET))

        def _parse_country_iso(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_iso = _parse_country_iso(d.pop("country_iso", UNSET))

        observed_in_orgs = d.pop("observed_in_orgs", UNSET)

        def _parse_first_observed(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_observed_type_0 = datetime.date.fromisoformat(data)

                return first_observed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        first_observed = _parse_first_observed(d.pop("first_observed", UNSET))

        def _parse_last_confirmed(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_confirmed_type_0 = datetime.date.fromisoformat(data)

                return last_confirmed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_confirmed = _parse_last_confirmed(d.pop("last_confirmed", UNSET))

        def _parse_evidence_finding_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_finding_ids_type_0 = cast(list[str], data)

                return evidence_finding_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        evidence_finding_ids = _parse_evidence_finding_ids(d.pop("evidence_finding_ids", UNSET))

        def _parse_pattern_strength(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pattern_strength = _parse_pattern_strength(d.pop("pattern_strength", UNSET))

        ratified_by_manav = d.pop("ratified_by_manav", UNSET)

        def _parse_ratified_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ratified_date_type_0 = datetime.date.fromisoformat(data)

                return ratified_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        ratified_date = _parse_ratified_date(d.pop("ratified_date", UNSET))

        def _parse_superseded_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        superseded_by_id = _parse_superseded_by_id(d.pop("superseded_by_id", UNSET))

        def _parse_metadata(data: object) -> CrossOrgPatternUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CrossOrgPatternUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CrossOrgPatternUpsertMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        cross_org_pattern_upsert = cls(
            pattern_kind=pattern_kind,
            pattern_summary=pattern_summary,
            industry_naics=industry_naics,
            country_iso=country_iso,
            observed_in_orgs=observed_in_orgs,
            first_observed=first_observed,
            last_confirmed=last_confirmed,
            evidence_finding_ids=evidence_finding_ids,
            pattern_strength=pattern_strength,
            ratified_by_manav=ratified_by_manav,
            ratified_date=ratified_date,
            superseded_by_id=superseded_by_id,
            metadata=metadata,
            source=source,
            source_url=source_url,
        )

        cross_org_pattern_upsert.additional_properties = d
        return cross_org_pattern_upsert

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
