from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.market_intelligence_upsert_metadata_type_0 import MarketIntelligenceUpsertMetadataType0


T = TypeVar("T", bound="MarketIntelligenceUpsert")


@_attrs_define
class MarketIntelligenceUpsert:
    """
    Attributes:
        company_name (str):
        legal_name (None | str | Unset):
        ticker (None | str | Unset):
        exchange (None | str | Unset):
        country_iso (None | str | Unset):
        hq_city_id (None | str | Unset):
        industry_naics (None | str | Unset):
        founded_year (int | None | Unset):
        headcount (int | None | Unset):
        revenue_usd (int | None | Unset):
        revenue_year (int | None | Unset):
        funding_total_usd (int | None | Unset):
        funding_stage (None | str | Unset):
        valuation_usd (int | None | Unset):
        valuation_date (datetime.date | None | Unset):
        acquired_by (None | str | Unset):
        acquired_date (datetime.date | None | Unset):
        parent_company (None | str | Unset):
        website (None | str | Unset):
        description (None | str | Unset):
        business_model (None | str | Unset):
        keywords (list[str] | None | Unset):
        metadata (MarketIntelligenceUpsertMetadataType0 | None | Unset):
        last_refreshed (datetime.datetime | None | Unset):
        source (None | str | Unset):
        source_url (None | str | Unset):
    """

    company_name: str
    legal_name: None | str | Unset = UNSET
    ticker: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    country_iso: None | str | Unset = UNSET
    hq_city_id: None | str | Unset = UNSET
    industry_naics: None | str | Unset = UNSET
    founded_year: int | None | Unset = UNSET
    headcount: int | None | Unset = UNSET
    revenue_usd: int | None | Unset = UNSET
    revenue_year: int | None | Unset = UNSET
    funding_total_usd: int | None | Unset = UNSET
    funding_stage: None | str | Unset = UNSET
    valuation_usd: int | None | Unset = UNSET
    valuation_date: datetime.date | None | Unset = UNSET
    acquired_by: None | str | Unset = UNSET
    acquired_date: datetime.date | None | Unset = UNSET
    parent_company: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    business_model: None | str | Unset = UNSET
    keywords: list[str] | None | Unset = UNSET
    metadata: MarketIntelligenceUpsertMetadataType0 | None | Unset = UNSET
    last_refreshed: datetime.datetime | None | Unset = UNSET
    source: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.market_intelligence_upsert_metadata_type_0 import (
            MarketIntelligenceUpsertMetadataType0,  # noqa: PLC0415
        )

        company_name = self.company_name

        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        ticker: None | str | Unset
        if isinstance(self.ticker, Unset):
            ticker = UNSET
        else:
            ticker = self.ticker

        exchange: None | str | Unset
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange

        country_iso: None | str | Unset
        if isinstance(self.country_iso, Unset):
            country_iso = UNSET
        else:
            country_iso = self.country_iso

        hq_city_id: None | str | Unset
        if isinstance(self.hq_city_id, Unset):
            hq_city_id = UNSET
        else:
            hq_city_id = self.hq_city_id

        industry_naics: None | str | Unset
        if isinstance(self.industry_naics, Unset):
            industry_naics = UNSET
        else:
            industry_naics = self.industry_naics

        founded_year: int | None | Unset
        if isinstance(self.founded_year, Unset):
            founded_year = UNSET
        else:
            founded_year = self.founded_year

        headcount: int | None | Unset
        if isinstance(self.headcount, Unset):
            headcount = UNSET
        else:
            headcount = self.headcount

        revenue_usd: int | None | Unset
        if isinstance(self.revenue_usd, Unset):
            revenue_usd = UNSET
        else:
            revenue_usd = self.revenue_usd

        revenue_year: int | None | Unset
        if isinstance(self.revenue_year, Unset):
            revenue_year = UNSET
        else:
            revenue_year = self.revenue_year

        funding_total_usd: int | None | Unset
        if isinstance(self.funding_total_usd, Unset):
            funding_total_usd = UNSET
        else:
            funding_total_usd = self.funding_total_usd

        funding_stage: None | str | Unset
        if isinstance(self.funding_stage, Unset):
            funding_stage = UNSET
        else:
            funding_stage = self.funding_stage

        valuation_usd: int | None | Unset
        if isinstance(self.valuation_usd, Unset):
            valuation_usd = UNSET
        else:
            valuation_usd = self.valuation_usd

        valuation_date: None | str | Unset
        if isinstance(self.valuation_date, Unset):
            valuation_date = UNSET
        elif isinstance(self.valuation_date, datetime.date):
            valuation_date = self.valuation_date.isoformat()
        else:
            valuation_date = self.valuation_date

        acquired_by: None | str | Unset
        if isinstance(self.acquired_by, Unset):
            acquired_by = UNSET
        else:
            acquired_by = self.acquired_by

        acquired_date: None | str | Unset
        if isinstance(self.acquired_date, Unset):
            acquired_date = UNSET
        elif isinstance(self.acquired_date, datetime.date):
            acquired_date = self.acquired_date.isoformat()
        else:
            acquired_date = self.acquired_date

        parent_company: None | str | Unset
        if isinstance(self.parent_company, Unset):
            parent_company = UNSET
        else:
            parent_company = self.parent_company

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        business_model: None | str | Unset
        if isinstance(self.business_model, Unset):
            business_model = UNSET
        else:
            business_model = self.business_model

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
        elif isinstance(self.metadata, MarketIntelligenceUpsertMetadataType0):
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
                "company_name": company_name,
            }
        )
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if ticker is not UNSET:
            field_dict["ticker"] = ticker
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if country_iso is not UNSET:
            field_dict["country_iso"] = country_iso
        if hq_city_id is not UNSET:
            field_dict["hq_city_id"] = hq_city_id
        if industry_naics is not UNSET:
            field_dict["industry_naics"] = industry_naics
        if founded_year is not UNSET:
            field_dict["founded_year"] = founded_year
        if headcount is not UNSET:
            field_dict["headcount"] = headcount
        if revenue_usd is not UNSET:
            field_dict["revenue_usd"] = revenue_usd
        if revenue_year is not UNSET:
            field_dict["revenue_year"] = revenue_year
        if funding_total_usd is not UNSET:
            field_dict["funding_total_usd"] = funding_total_usd
        if funding_stage is not UNSET:
            field_dict["funding_stage"] = funding_stage
        if valuation_usd is not UNSET:
            field_dict["valuation_usd"] = valuation_usd
        if valuation_date is not UNSET:
            field_dict["valuation_date"] = valuation_date
        if acquired_by is not UNSET:
            field_dict["acquired_by"] = acquired_by
        if acquired_date is not UNSET:
            field_dict["acquired_date"] = acquired_date
        if parent_company is not UNSET:
            field_dict["parent_company"] = parent_company
        if website is not UNSET:
            field_dict["website"] = website
        if description is not UNSET:
            field_dict["description"] = description
        if business_model is not UNSET:
            field_dict["business_model"] = business_model
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
        from ..models.market_intelligence_upsert_metadata_type_0 import (
            MarketIntelligenceUpsertMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        company_name = d.pop("company_name")

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

        def _parse_ticker(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ticker = _parse_ticker(d.pop("ticker", UNSET))

        def _parse_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))

        def _parse_country_iso(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_iso = _parse_country_iso(d.pop("country_iso", UNSET))

        def _parse_hq_city_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hq_city_id = _parse_hq_city_id(d.pop("hq_city_id", UNSET))

        def _parse_industry_naics(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry_naics = _parse_industry_naics(d.pop("industry_naics", UNSET))

        def _parse_founded_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        founded_year = _parse_founded_year(d.pop("founded_year", UNSET))

        def _parse_headcount(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        headcount = _parse_headcount(d.pop("headcount", UNSET))

        def _parse_revenue_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revenue_usd = _parse_revenue_usd(d.pop("revenue_usd", UNSET))

        def _parse_revenue_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revenue_year = _parse_revenue_year(d.pop("revenue_year", UNSET))

        def _parse_funding_total_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        funding_total_usd = _parse_funding_total_usd(d.pop("funding_total_usd", UNSET))

        def _parse_funding_stage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        funding_stage = _parse_funding_stage(d.pop("funding_stage", UNSET))

        def _parse_valuation_usd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valuation_usd = _parse_valuation_usd(d.pop("valuation_usd", UNSET))

        def _parse_valuation_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valuation_date_type_0 = datetime.date.fromisoformat(data)

                return valuation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        valuation_date = _parse_valuation_date(d.pop("valuation_date", UNSET))

        def _parse_acquired_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acquired_by = _parse_acquired_by(d.pop("acquired_by", UNSET))

        def _parse_acquired_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquired_date_type_0 = datetime.date.fromisoformat(data)

                return acquired_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        acquired_date = _parse_acquired_date(d.pop("acquired_date", UNSET))

        def _parse_parent_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_company = _parse_parent_company(d.pop("parent_company", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_business_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_model = _parse_business_model(d.pop("business_model", UNSET))

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

        def _parse_metadata(data: object) -> MarketIntelligenceUpsertMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = MarketIntelligenceUpsertMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarketIntelligenceUpsertMetadataType0 | None | Unset, data)

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

        market_intelligence_upsert = cls(
            company_name=company_name,
            legal_name=legal_name,
            ticker=ticker,
            exchange=exchange,
            country_iso=country_iso,
            hq_city_id=hq_city_id,
            industry_naics=industry_naics,
            founded_year=founded_year,
            headcount=headcount,
            revenue_usd=revenue_usd,
            revenue_year=revenue_year,
            funding_total_usd=funding_total_usd,
            funding_stage=funding_stage,
            valuation_usd=valuation_usd,
            valuation_date=valuation_date,
            acquired_by=acquired_by,
            acquired_date=acquired_date,
            parent_company=parent_company,
            website=website,
            description=description,
            business_model=business_model,
            keywords=keywords,
            metadata=metadata,
            last_refreshed=last_refreshed,
            source=source,
            source_url=source_url,
        )

        market_intelligence_upsert.additional_properties = d
        return market_intelligence_upsert

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
