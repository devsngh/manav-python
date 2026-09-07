from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.industry_read_metadata_type_0 import IndustryReadMetadataType0


T = TypeVar("T", bound="IndustryRead")


@_attrs_define
class IndustryRead:
    """
    Attributes:
        name (str):
        naics_code (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        sic_code (None | str | Unset):
        gics_sector (None | str | Unset):
        parent_code (None | str | Unset):
        description (None | str | Unset):
        typical_cycle (None | str | Unset):
        keywords (list[str] | None | Unset):
        metadata (IndustryReadMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    name: str
    naics_code: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    sic_code: None | str | Unset = UNSET
    gics_sector: None | str | Unset = UNSET
    parent_code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    typical_cycle: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    metadata: IndustryReadMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.industry_read_metadata_type_0 import IndustryReadMetadataType0  # noqa: PLC0415

        name = self.name

        naics_code = self.naics_code

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        sic_code: None | str | Unset
        if isinstance(self.sic_code, Unset):
            sic_code = UNSET
        else:
            sic_code = self.sic_code

        gics_sector: None | str | Unset
        if isinstance(self.gics_sector, Unset):
            gics_sector = UNSET
        else:
            gics_sector = self.gics_sector

        parent_code: None | str | Unset
        if isinstance(self.parent_code, Unset):
            parent_code = UNSET
        else:
            parent_code = self.parent_code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        typical_cycle: None | str | Unset
        if isinstance(self.typical_cycle, Unset):
            typical_cycle = UNSET
        else:
            typical_cycle = self.typical_cycle

        keywords: list[str] | None | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        elif isinstance(self.keywords, list):
            keywords = self.keywords

        else:
            keywords = self.keywords

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, IndustryReadMetadataType0):
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
                "naics_code": naics_code,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if sic_code is not UNSET:
            field_dict["sic_code"] = sic_code
        if gics_sector is not UNSET:
            field_dict["gics_sector"] = gics_sector
        if parent_code is not UNSET:
            field_dict["parent_code"] = parent_code
        if description is not UNSET:
            field_dict["description"] = description
        if typical_cycle is not UNSET:
            field_dict["typical_cycle"] = typical_cycle
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
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
        from ..models.industry_read_metadata_type_0 import IndustryReadMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        naics_code = d.pop("naics_code")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_sic_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sic_code = _parse_sic_code(d.pop("sic_code", UNSET))

        def _parse_gics_sector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gics_sector = _parse_gics_sector(d.pop("gics_sector", UNSET))

        def _parse_parent_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_code = _parse_parent_code(d.pop("parent_code", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_typical_cycle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typical_cycle = _parse_typical_cycle(d.pop("typical_cycle", UNSET))

        def _parse_keywords(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keywords_type_0 = cast(list[str], data)

                return keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))

        def _parse_metadata(data: object) -> IndustryReadMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = IndustryReadMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IndustryReadMetadataType0 | None | Unset, data)

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

        industry_read = cls(
            name=name,
            naics_code=naics_code,
            created_at=created_at,
            updated_at=updated_at,
            sic_code=sic_code,
            gics_sector=gics_sector,
            parent_code=parent_code,
            description=description,
            typical_cycle=typical_cycle,
            keywords=keywords,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        industry_read.additional_properties = d
        return industry_read

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
