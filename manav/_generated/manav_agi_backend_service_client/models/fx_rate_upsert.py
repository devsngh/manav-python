from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fx_rate_upsert_metadata_type_0 import FxRateUpsertMetadataType0


T = TypeVar("T", bound="FxRateUpsert")


@_attrs_define
class FxRateUpsert:
    """
    Attributes:
        pair (str):
        date (datetime.date):
        open_rate (float | None | str | Unset):
        close_rate (float | None | str | Unset):
        high_rate (float | None | str | Unset):
        low_rate (float | None | str | Unset):
        volume (int | None | Unset):
        source (None | str | Unset):
        metadata (FxRateUpsertMetadataType0 | None | Unset):
    """

    pair: str
    date: datetime.date
    open_rate: float | None | str | Unset = UNSET
    close_rate: float | None | str | Unset = UNSET
    high_rate: float | None | str | Unset = UNSET
    low_rate: float | None | str | Unset = UNSET
    volume: int | None | Unset = UNSET
    source: None | str | Unset = UNSET
    metadata: FxRateUpsertMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fx_rate_upsert_metadata_type_0 import FxRateUpsertMetadataType0  # noqa: PLC0415

        pair = self.pair

        date = self.date.isoformat()

        open_rate: float | None | str | Unset
        if isinstance(self.open_rate, Unset):
            open_rate = UNSET
        else:
            open_rate = self.open_rate

        close_rate: float | None | str | Unset
        if isinstance(self.close_rate, Unset):
            close_rate = UNSET
        else:
            close_rate = self.close_rate

        high_rate: float | None | str | Unset
        if isinstance(self.high_rate, Unset):
            high_rate = UNSET
        else:
            high_rate = self.high_rate

        low_rate: float | None | str | Unset
        if isinstance(self.low_rate, Unset):
            low_rate = UNSET
        else:
            low_rate = self.low_rate

        volume: int | None | Unset
        if isinstance(self.volume, Unset):
            volume = UNSET
        else:
            volume = self.volume

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, FxRateUpsertMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pair": pair,
                "date": date,
            }
        )
        if open_rate is not UNSET:
            field_dict["open_rate"] = open_rate
        if close_rate is not UNSET:
            field_dict["close_rate"] = close_rate
        if high_rate is not UNSET:
            field_dict["high_rate"] = high_rate
        if low_rate is not UNSET:
            field_dict["low_rate"] = low_rate
        if volume is not UNSET:
            field_dict["volume"] = volume
        if source is not UNSET:
            field_dict["source"] = source
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fx_rate_upsert_metadata_type_0 import FxRateUpsertMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        pair = d.pop("pair")

        date = datetime.date.fromisoformat(d.pop("date"))

        def _parse_open_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        open_rate = _parse_open_rate(d.pop("open_rate", UNSET))

        def _parse_close_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        close_rate = _parse_close_rate(d.pop("close_rate", UNSET))

        def _parse_high_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        high_rate = _parse_high_rate(d.pop("high_rate", UNSET))

        def _parse_low_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        low_rate = _parse_low_rate(d.pop("low_rate", UNSET))

        def _parse_volume(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        volume = _parse_volume(d.pop("volume", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_metadata(data: object) -> FxRateUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = FxRateUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FxRateUpsertMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        fx_rate_upsert = cls(
            pair=pair,
            date=date,
            open_rate=open_rate,
            close_rate=close_rate,
            high_rate=high_rate,
            low_rate=low_rate,
            volume=volume,
            source=source,
            metadata=metadata,
        )

        fx_rate_upsert.additional_properties = d
        return fx_rate_upsert

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
