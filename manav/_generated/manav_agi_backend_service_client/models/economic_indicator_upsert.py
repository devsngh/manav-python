from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.economic_indicator_upsert_metadata_type_0 import EconomicIndicatorUpsertMetadataType0


T = TypeVar("T", bound="EconomicIndicatorUpsert")


@_attrs_define
class EconomicIndicatorUpsert:
    """
    Attributes:
        country_iso (str):
        indicator (str):
        date (datetime.date):
        value (float | None | str | Unset):
        unit (None | str | Unset):
        frequency (None | str | Unset):
        source (None | str | Unset):
        metadata (EconomicIndicatorUpsertMetadataType0 | None | Unset):
    """

    country_iso: str
    indicator: str
    date: datetime.date
    value: float | None | str | Unset = UNSET
    unit: None | str | Unset = UNSET
    frequency: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    metadata: EconomicIndicatorUpsertMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.economic_indicator_upsert_metadata_type_0 import (
            EconomicIndicatorUpsertMetadataType0,  # noqa: PLC0415
        )

        country_iso = self.country_iso

        indicator = self.indicator

        date = self.date.isoformat()

        value: float | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        unit: None | str | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        frequency: None | str | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, EconomicIndicatorUpsertMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_iso": country_iso,
                "indicator": indicator,
                "date": date,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if source is not UNSET:
            field_dict["source"] = source
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.economic_indicator_upsert_metadata_type_0 import (
            EconomicIndicatorUpsertMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        country_iso = d.pop("country_iso")

        indicator = d.pop("indicator")

        date = datetime.date.fromisoformat(d.pop("date"))

        def _parse_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_frequency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_metadata(data: object) -> EconomicIndicatorUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = EconomicIndicatorUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EconomicIndicatorUpsertMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        economic_indicator_upsert = cls(
            country_iso=country_iso,
            indicator=indicator,
            date=date,
            value=value,
            unit=unit,
            frequency=frequency,
            source=source,
            metadata=metadata,
        )

        economic_indicator_upsert.additional_properties = d
        return economic_indicator_upsert

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
