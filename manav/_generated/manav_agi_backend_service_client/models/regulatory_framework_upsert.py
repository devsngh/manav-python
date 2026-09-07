from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regulatory_framework_upsert_key_requirements_type_0 import (
        RegulatoryFrameworkUpsertKeyRequirementsType0,
    )
    from ..models.regulatory_framework_upsert_metadata_type_0 import RegulatoryFrameworkUpsertMetadataType0


T = TypeVar("T", bound="RegulatoryFrameworkUpsert")


@_attrs_define
class RegulatoryFrameworkUpsert:
    """
    Attributes:
        country_iso (str):
        domain (str):
        framework_name (str):
        abbreviation (None | str | Unset):
        effective_date (datetime.date | None | Unset):
        last_amended_date (datetime.date | None | Unset):
        enforcement_body (None | str | Unset):
        summary (None | str | Unset):
        key_requirements (None | RegulatoryFrameworkUpsertKeyRequirementsType0 | Unset):
        penalties_summary (None | str | Unset):
        applicable_to (list[str] | None | Unset):
        metadata (None | RegulatoryFrameworkUpsertMetadataType0 | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    country_iso: str
    domain: str
    framework_name: str
    abbreviation: None | str | Unset = UNSET
    effective_date: datetime.date | None | Unset = UNSET
    last_amended_date: datetime.date | None | Unset = UNSET
    enforcement_body: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    key_requirements: None | RegulatoryFrameworkUpsertKeyRequirementsType0 | Unset = UNSET
    penalties_summary: None | str | Unset = UNSET
    applicable_to: list[str] | None | Unset = UNSET
    metadata: None | RegulatoryFrameworkUpsertMetadataType0 | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.regulatory_framework_upsert_key_requirements_type_0 import (
            RegulatoryFrameworkUpsertKeyRequirementsType0,  # noqa: PLC0415
        )
        from ..models.regulatory_framework_upsert_metadata_type_0 import (
            RegulatoryFrameworkUpsertMetadataType0,  # noqa: PLC0415
        )

        country_iso = self.country_iso

        domain = self.domain

        framework_name = self.framework_name

        abbreviation: None | str | Unset
        if isinstance(self.abbreviation, Unset):
            abbreviation = UNSET
        else:
            abbreviation = self.abbreviation

        effective_date: None | str | Unset
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        elif isinstance(self.effective_date, datetime.date):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        last_amended_date: None | str | Unset
        if isinstance(self.last_amended_date, Unset):
            last_amended_date = UNSET
        elif isinstance(self.last_amended_date, datetime.date):
            last_amended_date = self.last_amended_date.isoformat()
        else:
            last_amended_date = self.last_amended_date

        enforcement_body: None | str | Unset
        if isinstance(self.enforcement_body, Unset):
            enforcement_body = UNSET
        else:
            enforcement_body = self.enforcement_body

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        key_requirements: dict[str, Any] | None | Unset
        if isinstance(self.key_requirements, Unset):
            key_requirements = UNSET
        elif isinstance(self.key_requirements, RegulatoryFrameworkUpsertKeyRequirementsType0):
            key_requirements = self.key_requirements.to_dict()
        else:
            key_requirements = self.key_requirements

        penalties_summary: None | str | Unset
        if isinstance(self.penalties_summary, Unset):
            penalties_summary = UNSET
        else:
            penalties_summary = self.penalties_summary

        applicable_to: list[str] | None | Unset
        if isinstance(self.applicable_to, Unset):
            applicable_to = UNSET
        elif isinstance(self.applicable_to, list):
            applicable_to = self.applicable_to

        else:
            applicable_to = self.applicable_to

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, RegulatoryFrameworkUpsertMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        last_refreshed: None | str | Unset
        if isinstance(self.last_refreshed, Unset):
            last_refreshed = UNSET
        elif isinstance(self.last_refreshed, datetime.datetime):
            last_refreshed = self.last_refreshed.isoformat()
        else:
            last_refreshed = self.last_refreshed

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
                "country_iso": country_iso,
                "domain": domain,
                "framework_name": framework_name,
            }
        )
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if last_amended_date is not UNSET:
            field_dict["last_amended_date"] = last_amended_date
        if enforcement_body is not UNSET:
            field_dict["enforcement_body"] = enforcement_body
        if summary is not UNSET:
            field_dict["summary"] = summary
        if key_requirements is not UNSET:
            field_dict["key_requirements"] = key_requirements
        if penalties_summary is not UNSET:
            field_dict["penalties_summary"] = penalties_summary
        if applicable_to is not UNSET:
            field_dict["applicable_to"] = applicable_to
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if last_refreshed is not UNSET:
            field_dict["last_refreshed"] = last_refreshed
        if source is not UNSET:
            field_dict["source"] = source
        if source_url is not UNSET:
            field_dict["source_url"] = source_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regulatory_framework_upsert_key_requirements_type_0 import (
            RegulatoryFrameworkUpsertKeyRequirementsType0,  # noqa: PLC0415
        )
        from ..models.regulatory_framework_upsert_metadata_type_0 import (
            RegulatoryFrameworkUpsertMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        country_iso = d.pop("country_iso")

        domain = d.pop("domain")

        framework_name = d.pop("framework_name")

        def _parse_abbreviation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abbreviation = _parse_abbreviation(d.pop("abbreviation", UNSET))

        def _parse_effective_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = datetime.date.fromisoformat(data)

                return effective_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_date = _parse_effective_date(d.pop("effective_date", UNSET))

        def _parse_last_amended_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_amended_date_type_0 = datetime.date.fromisoformat(data)

                return last_amended_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_amended_date = _parse_last_amended_date(d.pop("last_amended_date", UNSET))

        def _parse_enforcement_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enforcement_body = _parse_enforcement_body(d.pop("enforcement_body", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_key_requirements(data: object) -> None | RegulatoryFrameworkUpsertKeyRequirementsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_requirements_type_0 = RegulatoryFrameworkUpsertKeyRequirementsType0.from_dict(data)

                return key_requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegulatoryFrameworkUpsertKeyRequirementsType0 | Unset, data)

        key_requirements = _parse_key_requirements(d.pop("key_requirements", UNSET))

        def _parse_penalties_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        penalties_summary = _parse_penalties_summary(d.pop("penalties_summary", UNSET))

        def _parse_applicable_to(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applicable_to_type_0 = cast(list[str], data)

                return applicable_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        applicable_to = _parse_applicable_to(d.pop("applicable_to", UNSET))

        def _parse_metadata(data: object) -> None | RegulatoryFrameworkUpsertMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = RegulatoryFrameworkUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RegulatoryFrameworkUpsertMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_last_refreshed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_refreshed_type_0 = datetime.datetime.fromisoformat(data)

                return last_refreshed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_refreshed = _parse_last_refreshed(d.pop("last_refreshed", UNSET))

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

        regulatory_framework_upsert = cls(
            country_iso=country_iso,
            domain=domain,
            framework_name=framework_name,
            abbreviation=abbreviation,
            effective_date=effective_date,
            last_amended_date=last_amended_date,
            enforcement_body=enforcement_body,
            summary=summary,
            key_requirements=key_requirements,
            penalties_summary=penalties_summary,
            applicable_to=applicable_to,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        regulatory_framework_upsert.additional_properties = d
        return regulatory_framework_upsert

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
