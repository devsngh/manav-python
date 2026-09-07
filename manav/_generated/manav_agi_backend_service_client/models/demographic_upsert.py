from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.demographic_upsert_metadata_type_0 import DemographicUpsertMetadataType0


T = TypeVar("T", bound="DemographicUpsert")


@_attrs_define
class DemographicUpsert:
    """
    Attributes:
        country_iso (str):
        year (int):
        age_band (None | str | Unset):
        gender (None | str | Unset):
        religion (None | str | Unset):
        population_count (int | None | Unset):
        percentage_of_country (float | None | str | Unset):
        median_income_usd (int | None | Unset):
        education_level (None | str | Unset):
        metadata (DemographicUpsertMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    country_iso: str
    year: int
    age_band: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    religion: None | str | Unset = UNSET
    population_count: int | None | Unset = UNSET
    percentage_of_country: float | None | str | Unset = UNSET
    median_income_usd: int | None | Unset = UNSET
    education_level: None | str | Unset = UNSET
    metadata: DemographicUpsertMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.demographic_upsert_metadata_type_0 import DemographicUpsertMetadataType0  # noqa: PLC0415

        country_iso = self.country_iso

        year = self.year

        age_band: None | str | Unset
        if isinstance(self.age_band, Unset):
            age_band = UNSET
        else:
            age_band = self.age_band

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        religion: None | str | Unset
        if isinstance(self.religion, Unset):
            religion = UNSET
        else:
            religion = self.religion

        population_count: int | None | Unset
        if isinstance(self.population_count, Unset):
            population_count = UNSET
        else:
            population_count = self.population_count

        percentage_of_country: float | None | str | Unset
        if isinstance(self.percentage_of_country, Unset):
            percentage_of_country = UNSET
        else:
            percentage_of_country = self.percentage_of_country

        median_income_usd: int | None | Unset
        if isinstance(self.median_income_usd, Unset):
            median_income_usd = UNSET
        else:
            median_income_usd = self.median_income_usd

        education_level: None | str | Unset
        if isinstance(self.education_level, Unset):
            education_level = UNSET
        else:
            education_level = self.education_level

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DemographicUpsertMetadataType0):
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
                "year": year,
            }
        )
        if age_band is not UNSET:
            field_dict["age_band"] = age_band
        if gender is not UNSET:
            field_dict["gender"] = gender
        if religion is not UNSET:
            field_dict["religion"] = religion
        if population_count is not UNSET:
            field_dict["population_count"] = population_count
        if percentage_of_country is not UNSET:
            field_dict["percentage_of_country"] = percentage_of_country
        if median_income_usd is not UNSET:
            field_dict["median_income_usd"] = median_income_usd
        if education_level is not UNSET:
            field_dict["education_level"] = education_level
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
        from ..models.demographic_upsert_metadata_type_0 import DemographicUpsertMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        country_iso = d.pop("country_iso")

        year = d.pop("year")

        def _parse_age_band(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age_band = _parse_age_band(d.pop("age_band", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_religion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        religion = _parse_religion(d.pop("religion", UNSET))

        def _parse_population_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        population_count = _parse_population_count(d.pop("population_count", UNSET))

        def _parse_percentage_of_country(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        percentage_of_country = _parse_percentage_of_country(d.pop("percentage_of_country", UNSET))

        def _parse_median_income_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        median_income_usd = _parse_median_income_usd(d.pop("median_income_usd", UNSET))

        def _parse_education_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level = _parse_education_level(d.pop("education_level", UNSET))

        def _parse_metadata(data: object) -> DemographicUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DemographicUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DemographicUpsertMetadataType0 | None | Unset, data)

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

        demographic_upsert = cls(
            country_iso=country_iso,
            year=year,
            age_band=age_band,
            gender=gender,
            religion=religion,
            population_count=population_count,
            percentage_of_country=percentage_of_country,
            median_income_usd=median_income_usd,
            education_level=education_level,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        demographic_upsert.additional_properties = d
        return demographic_upsert

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
