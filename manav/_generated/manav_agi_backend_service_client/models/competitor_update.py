from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competitor_update_metadata_type_0 import CompetitorUpdateMetadataType0
    from ..models.competitor_update_social_handles_type_0 import CompetitorUpdateSocialHandlesType0


T = TypeVar("T", bound="CompetitorUpdate")


@_attrs_define
class CompetitorUpdate:
    """
    Attributes:
        name (None | str | Unset):
        legal_name (None | str | Unset):
        website_url (None | str | Unset):
        primary_country_code (None | str | Unset):
        hq_city (None | str | Unset):
        founded_year (int | None | Unset):
        employee_count_range (None | str | Unset):
        employee_count_exact (int | None | Unset):
        funding_total (float | None | str | Unset):
        funding_currency_id (None | Unset | UUID):
        public_or_private (None | str | Unset):
        stock_ticker (None | str | Unset):
        status (None | str | Unset):
        threat_level (None | str | Unset):
        primary_category (None | str | Unset):
        description (None | str | Unset):
        social_handles (CompetitorUpdateSocialHandlesType0 | None | Unset):
        logo_asset_id (None | Unset | UUID):
        metadata (CompetitorUpdateMetadataType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    primary_country_code: None | str | Unset = UNSET
    hq_city: None | str | Unset = UNSET
    founded_year: int | None | Unset = UNSET
    employee_count_range: None | str | Unset = UNSET
    employee_count_exact: int | None | Unset = UNSET
    funding_total: float | None | str | Unset = UNSET
    funding_currency_id: None | Unset | UUID = UNSET
    public_or_private: None | str | Unset = UNSET
    stock_ticker: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    threat_level: None | str | Unset = UNSET
    primary_category: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    social_handles: CompetitorUpdateSocialHandlesType0 | None | Unset = UNSET
    logo_asset_id: None | Unset | UUID = UNSET
    metadata: CompetitorUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.competitor_update_metadata_type_0 import CompetitorUpdateMetadataType0  # noqa: PLC0415
        from ..models.competitor_update_social_handles_type_0 import CompetitorUpdateSocialHandlesType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        primary_country_code: None | str | Unset
        if isinstance(self.primary_country_code, Unset):
            primary_country_code = UNSET
        else:
            primary_country_code = self.primary_country_code

        hq_city: None | str | Unset
        if isinstance(self.hq_city, Unset):
            hq_city = UNSET
        else:
            hq_city = self.hq_city

        founded_year: int | None | Unset
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        else:
            founded_year = self.founded_year

        employee_count_range: None | str | Unset
        if isinstance(self.employee_count_range, Unset):
            employee_count_range = UNSET
        else:
            employee_count_range = self.employee_count_range

        employee_count_exact: int | None | Unset
        if isinstance(self.employee_count_exact, Unset):
            employee_count_exact = UNSET
        else:
            employee_count_exact = self.employee_count_exact

        funding_total: float | None | str | Unset
        if isinstance(self.funding_total, Unset):
            funding_total = UNSET
        else:
            funding_total = self.funding_total

        funding_currency_id: None | str | Unset
        if isinstance(self.funding_currency_id, Unset):
            funding_currency_id = UNSET
        elif isinstance(self.funding_currency_id, UUID):
            funding_currency_id = str(self.funding_currency_id)
        else:
            funding_currency_id = self.funding_currency_id

        public_or_private: None | str | Unset
        if isinstance(self.public_or_private, Unset):
            public_or_private = UNSET
        else:
            public_or_private = self.public_or_private

        stock_ticker: None | str | Unset
        if isinstance(self.stock_ticker, Unset):
            stock_ticker = UNSET
        else:
            stock_ticker = self.stock_ticker

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        threat_level: None | str | Unset
        if isinstance(self.threat_level, Unset):
            threat_level = UNSET
        else:
            threat_level = self.threat_level

        primary_category: None | str | Unset
        if isinstance(self.primary_category, Unset):
            primary_category = UNSET
        else:
            primary_category = self.primary_category

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        social_handles: dict[str, Any] | None | Unset
        if isinstance(self.social_handles, Unset):
            social_handles = UNSET
        elif isinstance(self.social_handles, CompetitorUpdateSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        logo_asset_id: None | str | Unset
        if isinstance(self.logo_asset_id, Unset):
            logo_asset_id = UNSET
        elif isinstance(self.logo_asset_id, UUID):
            logo_asset_id = str(self.logo_asset_id)
        else:
            logo_asset_id = self.logo_asset_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CompetitorUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if primary_country_code is not UNSET:
            field_dict["primary_country_code"] = primary_country_code
        if hq_city is not UNSET:
            field_dict["hq_city"] = hq_city
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if employee_count_range is not UNSET:
            field_dict["employee_count_range"] = employee_count_range
        if employee_count_exact is not UNSET:
            field_dict["employee_count_exact"] = employee_count_exact
        if funding_total is not UNSET:
            field_dict["funding_total"] = funding_total
        if funding_currency_id is not UNSET:
            field_dict["funding_currency_id"] = funding_currency_id
        if public_or_private is not UNSET:
            field_dict["public_or_private"] = public_or_private
        if stock_ticker is not UNSET:
            field_dict["stock_ticker"] = stock_ticker
        if status is not UNSET:
            field_dict["status"] = status
        if threat_level is not UNSET:
            field_dict["threat_level"] = threat_level
        if primary_category is not UNSET:
            field_dict["primary_category"] = primary_category
        if description is not UNSET:
            field_dict["description"] = description
        if social_handles is not UNSET:
            field_dict["social_handles"] = social_handles
        if logo_asset_id is not UNSET:
            field_dict["logo_asset_id"] = logo_asset_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competitor_update_metadata_type_0 import CompetitorUpdateMetadataType0  # noqa: PLC0415
        from ..models.competitor_update_social_handles_type_0 import CompetitorUpdateSocialHandlesType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_primary_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_country_code = _parse_primary_country_code(d.pop("primary_country_code", UNSET))

        def _parse_hq_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hq_city = _parse_hq_city(d.pop("hq_city", UNSET))

        def _parse_founded_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        founded_year = _parse_founded_year(d.pop("founded_year", UNSET))

        def _parse_employee_count_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_count_range = _parse_employee_count_range(d.pop("employee_count_range", UNSET))

        def _parse_employee_count_exact(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count_exact = _parse_employee_count_exact(d.pop("employee_count_exact", UNSET))

        def _parse_funding_total(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        funding_total = _parse_funding_total(d.pop("funding_total", UNSET))

        def _parse_funding_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                funding_currency_id_type_0 = UUID(data)

                return funding_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        funding_currency_id = _parse_funding_currency_id(d.pop("funding_currency_id", UNSET))

        def _parse_public_or_private(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_or_private = _parse_public_or_private(d.pop("public_or_private", UNSET))

        def _parse_stock_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_ticker = _parse_stock_ticker(d.pop("stock_ticker", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_threat_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threat_level = _parse_threat_level(d.pop("threat_level", UNSET))

        def _parse_primary_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_category = _parse_primary_category(d.pop("primary_category", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_social_handles(data: object) -> CompetitorUpdateSocialHandlesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = CompetitorUpdateSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompetitorUpdateSocialHandlesType0 | None | Unset, data)

        social_handles = _parse_social_handles(d.pop("social_handles", UNSET))

        def _parse_logo_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_asset_id_type_0 = UUID(data)

                return logo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        logo_asset_id = _parse_logo_asset_id(d.pop("logo_asset_id", UNSET))

        def _parse_metadata(data: object) -> CompetitorUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CompetitorUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompetitorUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        competitor_update = cls(
            name=name,
            legal_name=legal_name,
            website_url=website_url,
            primary_country_code=primary_country_code,
            hq_city=hq_city,
            founded_year=founded_year,
            employee_count_range=employee_count_range,
            employee_count_exact=employee_count_exact,
            funding_total=funding_total,
            funding_currency_id=funding_currency_id,
            public_or_private=public_or_private,
            stock_ticker=stock_ticker,
            status=status,
            threat_level=threat_level,
            primary_category=primary_category,
            description=description,
            social_handles=social_handles,
            logo_asset_id=logo_asset_id,
            metadata=metadata,
        )

        competitor_update.additional_properties = d
        return competitor_update

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
