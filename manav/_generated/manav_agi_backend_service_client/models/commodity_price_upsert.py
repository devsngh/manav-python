from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commodity_price_upsert_metadata_type_0 import CommodityPriceUpsertMetadataType0


T = TypeVar("T", bound="CommodityPriceUpsert")


@_attrs_define
class CommodityPriceUpsert:
    """
    Attributes:
        commodity (str):
        date (datetime.date):
        price_usd (float | None | str | Unset):
        unit (None | str | Unset):
        exchange (None | str | Unset):
        source (None | str | Unset):
        metadata (CommodityPriceUpsertMetadataType0 | None | Unset):
    """

    commodity: str
    date: datetime.date
    price_usd: float | None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    metadata: CommodityPriceUpsertMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.commodity_price_upsert_metadata_type_0 import CommodityPriceUpsertMetadataType0  # noqa: PLC0415

        commodity = self.commodity

        date = self.date.isoformat()

        price_usd: float | None | str | Unset
        if isinstance(self.price_usd, Unset):
            price_usd = UNSET
        else:
            price_usd = self.price_usd

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        exchange: None | str | Unset
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CommodityPriceUpsertMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commodity": commodity,
                "date": date,
            }
        )
        if price_usd is not UNSET:
            field_dict["price_usd"] = price_usd
        if unit is not UNSET:
            field_dict["unit"] = unit
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if source is not UNSET:
            field_dict["source"] = source
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.commodity_price_upsert_metadata_type_0 import CommodityPriceUpsertMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        commodity = d.pop("commodity")

        date = datetime.date.fromisoformat(d.pop("date"))

        def _parse_price_usd(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        price_usd = _parse_price_usd(d.pop("price_usd", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_metadata(data: object) -> CommodityPriceUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CommodityPriceUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommodityPriceUpsertMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        commodity_price_upsert = cls(
            commodity=commodity,
            date=date,
            price_usd=price_usd,
            unit=unit,
            exchange=exchange,
            source=source,
            metadata=metadata,
        )

        commodity_price_upsert.additional_properties = d
        return commodity_price_upsert

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
