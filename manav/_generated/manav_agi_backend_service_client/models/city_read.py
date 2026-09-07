from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.city_read_metadata_type_0 import CityReadMetadataType0


T = TypeVar("T", bound="CityRead")


@_attrs_define
class CityRead:
    """
    Attributes:
        name (str):
        country_iso (str):
        id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        state_or_region (None | str | Unset):
        population (int | None | Unset):
        population_metro (int | None | Unset):
        tier_global (None | str | Unset):
        tier_local (None | str | Unset):
        tier_scheme (None | str | Unset):
        lat (None | str | Unset):
        lon (None | str | Unset):
        is_capital (bool | Unset):  Default: False.
        is_financial_hub (bool | Unset):  Default: False.
        is_tech_hub (bool | Unset):  Default: False.
        is_logistics_hub (bool | Unset):  Default: False.
        is_manufacturing_hub (bool | Unset):  Default: False.
        timezone (None | str | Unset):
        metadata (CityReadMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    name: str
    country_iso: str
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    state_or_region: None | str | Unset = UNSET
    population: int | None | Unset = UNSET
    population_metro: int | None | Unset = UNSET
    tier_global: None | str | Unset = UNSET
    tier_local: None | str | Unset = UNSET
    tier_scheme: None | str | Unset = UNSET
    lat: None | str | Unset = UNSET
    lon: None | str | Unset = UNSET
    is_capital: bool | Unset = False
    is_financial_hub: bool | Unset = False
    is_tech_hub: bool | Unset = False
    is_logistics_hub: bool | Unset = False
    is_manufacturing_hub: bool | Unset = False
    timezone: None | str | Unset = UNSET
    metadata: CityReadMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.city_read_metadata_type_0 import CityReadMetadataType0  # noqa: PLC0415

        name = self.name

        country_iso = self.country_iso

        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        state_or_region: None | str | Unset
        if isinstance(self.state_or_region, Unset):
            state_or_region = UNSET
        else:
            state_or_region = self.state_or_region

        population: int | None | Unset
        if isinstance(self.population, Unset):
            population = UNSET
        else:
            population = self.population

        population_metro: int | None | Unset
        if isinstance(self.population_metro, Unset):
            population_metro = UNSET
        else:
            population_metro = self.population_metro

        tier_global: None | str | Unset
        if isinstance(self.tier_global, Unset):
            tier_global = UNSET
        else:
            tier_global = self.tier_global

        tier_local: None | str | Unset
        if isinstance(self.tier_local, Unset):
            tier_local = UNSET
        else:
            tier_local = self.tier_local

        tier_scheme: None | str | Unset
        if isinstance(self.tier_scheme, Unset):
            tier_scheme = UNSET
        else:
            tier_scheme = self.tier_scheme

        lat: None | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lon: None | str | Unset
        if isinstance(self.lon, Unset):
            lon = UNSET
        else:
            lon = self.lon

        is_capital = self.is_capital

        is_financial_hub = self.is_financial_hub

        is_tech_hub = self.is_tech_hub

        is_logistics_hub = self.is_logistics_hub

        is_manufacturing_hub = self.is_manufacturing_hub

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CityReadMetadataType0):
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
                "country_iso": country_iso,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if state_or_region is not UNSET:
            field_dict["state_or_region"] = state_or_region
        if population is not UNSET:
            field_dict["population"] = population
        if population_metro is not UNSET:
            field_dict["population_metro"] = population_metro
        if tier_global is not UNSET:
            field_dict["tier_global"] = tier_global
        if tier_local is not UNSET:
            field_dict["tier_local"] = tier_local
        if tier_scheme is not UNSET:
            field_dict["tier_scheme"] = tier_scheme
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if is_capital is not UNSET:
            field_dict["is_capital"] = is_capital
        if is_financial_hub is not UNSET:
            field_dict["is_financial_hub"] = is_financial_hub
        if is_tech_hub is not UNSET:
            field_dict["is_tech_hub"] = is_tech_hub
        if is_logistics_hub is not UNSET:
            field_dict["is_logistics_hub"] = is_logistics_hub
        if is_manufacturing_hub is not UNSET:
            field_dict["is_manufacturing_hub"] = is_manufacturing_hub
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
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
        from ..models.city_read_metadata_type_0 import CityReadMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        country_iso = d.pop("country_iso")

        id = d.pop("id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_state_or_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_or_region = _parse_state_or_region(d.pop("state_or_region", UNSET))

        def _parse_population(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        population = _parse_population(d.pop("population", UNSET))

        def _parse_population_metro(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        population_metro = _parse_population_metro(d.pop("population_metro", UNSET))

        def _parse_tier_global(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier_global = _parse_tier_global(d.pop("tier_global", UNSET))

        def _parse_tier_local(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier_local = _parse_tier_local(d.pop("tier_local", UNSET))

        def _parse_tier_scheme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier_scheme = _parse_tier_scheme(d.pop("tier_scheme", UNSET))

        def _parse_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_lon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lon = _parse_lon(d.pop("lon", UNSET))

        is_capital = d.pop("is_capital", UNSET)

        is_financial_hub = d.pop("is_financial_hub", UNSET)

        is_tech_hub = d.pop("is_tech_hub", UNSET)

        is_logistics_hub = d.pop("is_logistics_hub", UNSET)

        is_manufacturing_hub = d.pop("is_manufacturing_hub", UNSET)

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        def _parse_metadata(data: object) -> CityReadMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CityReadMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CityReadMetadataType0 | None | Unset, data)

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

        city_read = cls(
            name=name,
            country_iso=country_iso,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            state_or_region=state_or_region,
            population=population,
            population_metro=population_metro,
            tier_global=tier_global,
            tier_local=tier_local,
            tier_scheme=tier_scheme,
            lat=lat,
            lon=lon,
            is_capital=is_capital,
            is_financial_hub=is_financial_hub,
            is_tech_hub=is_tech_hub,
            is_logistics_hub=is_logistics_hub,
            is_manufacturing_hub=is_manufacturing_hub,
            timezone=timezone,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        city_read.additional_properties = d
        return city_read

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
