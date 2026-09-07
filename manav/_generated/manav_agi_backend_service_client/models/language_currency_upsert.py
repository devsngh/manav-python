from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.language_currency_upsert_metadata_type_0 import LanguageCurrencyUpsertMetadataType0


T = TypeVar("T", bound="LanguageCurrencyUpsert")


@_attrs_define
class LanguageCurrencyUpsert:
    """
    Attributes:
        code (str):
        kind (str):
        name (str):
        symbol (None | str | Unset):
        script (None | str | Unset):
        countries_using_primary (list[str] | None | Unset):
        countries_using_secondary (list[str] | None | Unset):
        is_active (bool | Unset):  Default: True.
        is_reserve_currency (bool | Unset):  Default: False.
        metadata (LanguageCurrencyUpsertMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    code: str
    kind: str
    name: str
    symbol: None | str | Unset = UNSET
    script: None | str | Unset = UNSET
    countries_using_primary: list[str] | None | Unset = UNSET
    countries_using_secondary: list[str] | None | Unset = UNSET
    is_active: bool | Unset = True
    is_reserve_currency: bool | Unset = False
    metadata: LanguageCurrencyUpsertMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.language_currency_upsert_metadata_type_0 import (
            LanguageCurrencyUpsertMetadataType0,  # noqa: PLC0415
        )

        code = self.code

        kind = self.kind

        name = self.name

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        script: None | str | Unset
        if isinstance(self.script, Unset):
            script = UNSET
        else:
            script = self.script

        countries_using_primary: list[str] | None | Unset
        if isinstance(self.countries_using_primary, Unset):
            countries_using_primary = UNSET
        elif isinstance(self.countries_using_primary, list):
            countries_using_primary = self.countries_using_primary

        else:
            countries_using_primary = self.countries_using_primary

        countries_using_secondary: list[str] | None | Unset
        if isinstance(self.countries_using_secondary, Unset):
            countries_using_secondary = UNSET
        elif isinstance(self.countries_using_secondary, list):
            countries_using_secondary = self.countries_using_secondary

        else:
            countries_using_secondary = self.countries_using_secondary

        is_active = self.is_active

        is_reserve_currency = self.is_reserve_currency

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, LanguageCurrencyUpsertMetadataType0):
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
                "code": code,
                "kind": kind,
                "name": name,
            }
        )
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if script is not UNSET:
            field_dict["script"] = script
        if countries_using_primary is not UNSET:
            field_dict["countries_using_primary"] = countries_using_primary
        if countries_using_secondary is not UNSET:
            field_dict["countries_using_secondary"] = countries_using_secondary
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_reserve_currency is not UNSET:
            field_dict["is_reserve_currency"] = is_reserve_currency
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
        from ..models.language_currency_upsert_metadata_type_0 import (
            LanguageCurrencyUpsertMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = d.pop("code")

        kind = d.pop("kind")

        name = d.pop("name")

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))

        def _parse_script(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        script = _parse_script(d.pop("script", UNSET))

        def _parse_countries_using_primary(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                countries_using_primary_type_0 = cast(list[str], data)

                return countries_using_primary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        countries_using_primary = _parse_countries_using_primary(d.pop("countries_using_primary", UNSET))

        def _parse_countries_using_secondary(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                countries_using_secondary_type_0 = cast(list[str], data)

                return countries_using_secondary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        countries_using_secondary = _parse_countries_using_secondary(d.pop("countries_using_secondary", UNSET))

        is_active = d.pop("is_active", UNSET)

        is_reserve_currency = d.pop("is_reserve_currency", UNSET)

        def _parse_metadata(data: object) -> LanguageCurrencyUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LanguageCurrencyUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LanguageCurrencyUpsertMetadataType0 | None | Unset, data)

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

        language_currency_upsert = cls(
            code=code,
            kind=kind,
            name=name,
            symbol=symbol,
            script=script,
            countries_using_primary=countries_using_primary,
            countries_using_secondary=countries_using_secondary,
            is_active=is_active,
            is_reserve_currency=is_reserve_currency,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        language_currency_upsert.additional_properties = d
        return language_currency_upsert

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
