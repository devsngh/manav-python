from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trading_route_upsert_metadata_type_0 import TradingRouteUpsertMetadataType0


T = TypeVar("T", bound="TradingRouteUpsert")


@_attrs_define
class TradingRouteUpsert:
    """
    Attributes:
        from_country_iso (str):
        to_country_iso (str):
        route_type (str):
        name (None | str | Unset):
        primary_commodities (list[str] | None | Unset):
        annual_volume_usd (int | None | Unset):
        annual_volume_tons (int | None | Unset):
        ports_or_hubs (list[str] | None | Unset):
        chokepoints (list[str] | None | Unset):
        metadata (None | TradingRouteUpsertMetadataType0 | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    from_country_iso: str
    to_country_iso: str
    route_type: str
    name: None | str | Unset = UNSET
    primary_commodities: list[str] | None | Unset = UNSET
    annual_volume_usd: int | None | Unset = UNSET
    annual_volume_tons: int | None | Unset = UNSET
    ports_or_hubs: list[str] | None | Unset = UNSET
    chokepoints: list[str] | None | Unset = UNSET
    metadata: None | TradingRouteUpsertMetadataType0 | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trading_route_upsert_metadata_type_0 import TradingRouteUpsertMetadataType0  # noqa: PLC0415

        from_country_iso = self.from_country_iso

        to_country_iso = self.to_country_iso

        route_type = self.route_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        primary_commodities: list[str] | None | Unset
        if isinstance(self.primary_commodities, Unset):
            primary_commodities = UNSET
        elif isinstance(self.primary_commodities, list):
            primary_commodities = self.primary_commodities

        else:
            primary_commodities = self.primary_commodities

        annual_volume_usd: int | None | Unset
        if isinstance(self.annual_volume_usd, Unset):
            annual_volume_usd = UNSET
        else:
            annual_volume_usd = self.annual_volume_usd

        annual_volume_tons: int | None | Unset
        if isinstance(self.annual_volume_tons, Unset):
            annual_volume_tons = UNSET
        else:
            annual_volume_tons = self.annual_volume_tons

        ports_or_hubs: list[str] | None | Unset
        if isinstance(self.ports_or_hubs, Unset):
            ports_or_hubs = UNSET
        elif isinstance(self.ports_or_hubs, list):
            ports_or_hubs = self.ports_or_hubs

        else:
            ports_or_hubs = self.ports_or_hubs

        chokepoints: list[str] | None | Unset
        if isinstance(self.chokepoints, Unset):
            chokepoints = UNSET
        elif isinstance(self.chokepoints, list):
            chokepoints = self.chokepoints

        else:
            chokepoints = self.chokepoints

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, TradingRouteUpsertMetadataType0):
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
                "from_country_iso": from_country_iso,
                "to_country_iso": to_country_iso,
                "route_type": route_type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if primary_commodities is not UNSET:
            field_dict["primary_commodities"] = primary_commodities
        if annual_volume_usd is not UNSET:
            field_dict["annual_volume_usd"] = annual_volume_usd
        if annual_volume_tons is not UNSET:
            field_dict["annual_volume_tons"] = annual_volume_tons
        if ports_or_hubs is not UNSET:
            field_dict["ports_or_hubs"] = ports_or_hubs
        if chokepoints is not UNSET:
            field_dict["chokepoints"] = chokepoints
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
        from ..models.trading_route_upsert_metadata_type_0 import TradingRouteUpsertMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        from_country_iso = d.pop("from_country_iso")

        to_country_iso = d.pop("to_country_iso")

        route_type = d.pop("route_type")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_primary_commodities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                primary_commodities_type_0 = cast(list[str], data)

                return primary_commodities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        primary_commodities = _parse_primary_commodities(d.pop("primary_commodities", UNSET))

        def _parse_annual_volume_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        annual_volume_usd = _parse_annual_volume_usd(d.pop("annual_volume_usd", UNSET))

        def _parse_annual_volume_tons(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        annual_volume_tons = _parse_annual_volume_tons(d.pop("annual_volume_tons", UNSET))

        def _parse_ports_or_hubs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ports_or_hubs_type_0 = cast(list[str], data)

                return ports_or_hubs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ports_or_hubs = _parse_ports_or_hubs(d.pop("ports_or_hubs", UNSET))

        def _parse_chokepoints(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chokepoints_type_0 = cast(list[str], data)

                return chokepoints_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        chokepoints = _parse_chokepoints(d.pop("chokepoints", UNSET))

        def _parse_metadata(data: object) -> None | TradingRouteUpsertMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = TradingRouteUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradingRouteUpsertMetadataType0 | Unset, data)

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

        trading_route_upsert = cls(
            from_country_iso=from_country_iso,
            to_country_iso=to_country_iso,
            route_type=route_type,
            name=name,
            primary_commodities=primary_commodities,
            annual_volume_usd=annual_volume_usd,
            annual_volume_tons=annual_volume_tons,
            ports_or_hubs=ports_or_hubs,
            chokepoints=chokepoints,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        trading_route_upsert.additional_properties = d
        return trading_route_upsert

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
