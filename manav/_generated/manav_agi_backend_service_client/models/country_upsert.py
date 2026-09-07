from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.country_upsert_metadata_type_0 import CountryUpsertMetadataType0


T = TypeVar("T", bound="CountryUpsert")


@_attrs_define
class CountryUpsert:
    """
    Attributes:
        name (str):
        iso_code (str):
        iso_code_3 (None | str | Unset):
        continent (None | str | Unset):
        region (None | str | Unset):
        subregion (None | str | Unset):
        population (int | None | Unset):
        area_sq_km (int | None | Unset):
        gdp_usd (int | None | Unset):
        gdp_per_capita_usd (int | None | Unset):
        hdi (float | None | str | Unset):
        internet_penetration_pct (float | None | str | Unset):
        tier (None | str | Unset):
        business_cycle_phase (None | str | Unset):
        primary_languages (list[str] | None | Unset):
        primary_currency (None | str | Unset):
        timezone_primary (None | str | Unset):
        calling_code (None | str | Unset):
        metadata (CountryUpsertMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    name: str
    iso_code: str
    iso_code_3: None | str | Unset = UNSET
    continent: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    subregion: None | str | Unset = UNSET
    population: int | None | Unset = UNSET
    area_sq_km: int | None | Unset = UNSET
    gdp_usd: int | None | Unset = UNSET
    gdp_per_capita_usd: int | None | Unset = UNSET
    hdi: float | None | str | Unset = UNSET
    internet_penetration_pct: float | None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    business_cycle_phase: None | str | Unset = UNSET
    primary_languages: list[str] | None | Unset = UNSET
    primary_currency: None | str | Unset = UNSET
    timezone_primary: None | str | Unset = UNSET
    calling_code: None | str | Unset = UNSET
    metadata: CountryUpsertMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.country_upsert_metadata_type_0 import CountryUpsertMetadataType0  # noqa: PLC0415

        name = self.name

        iso_code = self.iso_code

        iso_code_3: None | str | Unset
        if isinstance(self.iso_code_3, Unset):
            iso_code_3 = UNSET
        else:
            iso_code_3 = self.iso_code_3

        continent: None | str | Unset
        if isinstance(self.continent, Unset):
            continent = UNSET
        else:
            continent = self.continent

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        subregion: None | str | Unset
        if isinstance(self.subregion, Unset):
            subregion = UNSET
        else:
            subregion = self.subregion

        population: int | None | Unset
        if isinstance(self.population, Unset):
            population = UNSET
        else:
            population = self.population

        area_sq_km: int | None | Unset
        if isinstance(self.area_sq_km, Unset):
            area_sq_km = UNSET
        else:
            area_sq_km = self.area_sq_km

        gdp_usd: int | None | Unset
        if isinstance(self.gdp_usd, Unset):
            gdp_usd = UNSET
        else:
            gdp_usd = self.gdp_usd

        gdp_per_capita_usd: int | None | Unset
        if isinstance(self.gdp_per_capita_usd, Unset):
            gdp_per_capita_usd = UNSET
        else:
            gdp_per_capita_usd = self.gdp_per_capita_usd

        hdi: float | None | str | Unset
        if isinstance(self.hdi, Unset):
            hdi = UNSET
        else:
            hdi = self.hdi

        internet_penetration_pct: float | None | str | Unset
        if isinstance(self.internet_penetration_pct, Unset):
            internet_penetration_pct = UNSET
        else:
            internet_penetration_pct = self.internet_penetration_pct

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        business_cycle_phase: None | str | Unset
        if isinstance(self.business_cycle_phase, Unset):
            business_cycle_phase = UNSET
        else:
            business_cycle_phase = self.business_cycle_phase

        primary_languages: list[str] | None | Unset
        if isinstance(self.primary_languages, Unset):
            primary_languages = UNSET
        elif isinstance(self.primary_languages, list):
            primary_languages = self.primary_languages

        else:
            primary_languages = self.primary_languages

        primary_currency: None | str | Unset
        if isinstance(self.primary_currency, Unset):
            primary_currency = UNSET
        else:
            primary_currency = self.primary_currency

        timezone_primary: None | str | Unset
        if isinstance(self.timezone_primary, Unset):
            timezone_primary = UNSET
        else:
            timezone_primary = self.timezone_primary

        calling_code: None | str | Unset
        if isinstance(self.calling_code, Unset):
            calling_code = UNSET
        else:
            calling_code = self.calling_code

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CountryUpsertMetadataType0):
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
                "name": name,
                "iso_code": iso_code,
            }
        )
        if iso_code_3 is not UNSET:
            field_dict["iso_code_3"] = iso_code_3
        if continent is not UNSET:
            field_dict["continent"] = continent
        if region is not UNSET:
            field_dict["region"] = region
        if subregion is not UNSET:
            field_dict["subregion"] = subregion
        if population is not UNSET:
            field_dict["population"] = population
        if area_sq_km is not UNSET:
            field_dict["area_sq_km"] = area_sq_km
        if gdp_usd is not UNSET:
            field_dict["gdp_usd"] = gdp_usd
        if gdp_per_capita_usd is not UNSET:
            field_dict["gdp_per_capita_usd"] = gdp_per_capita_usd
        if hdi is not UNSET:
            field_dict["hdi"] = hdi
        if internet_penetration_pct is not UNSET:
            field_dict["internet_penetration_pct"] = internet_penetration_pct
        if tier is not UNSET:
            field_dict["tier"] = tier
        if business_cycle_phase is not UNSET:
            field_dict["business_cycle_phase"] = business_cycle_phase
        if primary_languages is not UNSET:
            field_dict["primary_languages"] = primary_languages
        if primary_currency is not UNSET:
            field_dict["primary_currency"] = primary_currency
        if timezone_primary is not UNSET:
            field_dict["timezone_primary"] = timezone_primary
        if calling_code is not UNSET:
            field_dict["calling_code"] = calling_code
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
        from ..models.country_upsert_metadata_type_0 import CountryUpsertMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        iso_code = d.pop("iso_code")

        def _parse_iso_code_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iso_code_3 = _parse_iso_code_3(d.pop("iso_code_3", UNSET))

        def _parse_continent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continent = _parse_continent(d.pop("continent", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_subregion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subregion = _parse_subregion(d.pop("subregion", UNSET))

        def _parse_population(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        population = _parse_population(d.pop("population", UNSET))

        def _parse_area_sq_km(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_sq_km = _parse_area_sq_km(d.pop("area_sq_km", UNSET))

        def _parse_gdp_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gdp_usd = _parse_gdp_usd(d.pop("gdp_usd", UNSET))

        def _parse_gdp_per_capita_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gdp_per_capita_usd = _parse_gdp_per_capita_usd(d.pop("gdp_per_capita_usd", UNSET))

        def _parse_hdi(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        hdi = _parse_hdi(d.pop("hdi", UNSET))

        def _parse_internet_penetration_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        internet_penetration_pct = _parse_internet_penetration_pct(d.pop("internet_penetration_pct", UNSET))

        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_business_cycle_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_cycle_phase = _parse_business_cycle_phase(d.pop("business_cycle_phase", UNSET))

        def _parse_primary_languages(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_languages_type_0 = cast(list[str], data)

                return primary_languages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_languages = _parse_primary_languages(d.pop("primary_languages", UNSET))

        def _parse_primary_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_currency = _parse_primary_currency(d.pop("primary_currency", UNSET))

        def _parse_timezone_primary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone_primary = _parse_timezone_primary(d.pop("timezone_primary", UNSET))

        def _parse_calling_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calling_code = _parse_calling_code(d.pop("calling_code", UNSET))

        def _parse_metadata(data: object) -> CountryUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CountryUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CountryUpsertMetadataType0 | None | Unset, data)

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

        country_upsert = cls(
            name=name,
            iso_code=iso_code,
            iso_code_3=iso_code_3,
            continent=continent,
            region=region,
            subregion=subregion,
            population=population,
            area_sq_km=area_sq_km,
            gdp_usd=gdp_usd,
            gdp_per_capita_usd=gdp_per_capita_usd,
            hdi=hdi,
            internet_penetration_pct=internet_penetration_pct,
            tier=tier,
            business_cycle_phase=business_cycle_phase,
            primary_languages=primary_languages,
            primary_currency=primary_currency,
            timezone_primary=timezone_primary,
            calling_code=calling_code,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        country_upsert.additional_properties = d
        return country_upsert

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
