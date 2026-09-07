from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competitor_response_metadata_type_0 import CompetitorResponseMetadataType0
    from ..models.competitor_response_social_handles_type_0 import CompetitorResponseSocialHandlesType0


T = TypeVar("T", bound="CompetitorResponse")


@_attrs_define
class CompetitorResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        legal_name (None | str):
        website_url (None | str):
        primary_country_code (None | str):
        hq_city (None | str):
        founded_year (int | None):
        employee_count_range (None | str):
        employee_count_exact (int | None):
        funding_total (None | str):
        funding_currency_id (None | UUID):
        public_or_private (None | str):
        stock_ticker (None | str):
        status (str):
        acquired_by (None | str):
        acquired_at (datetime.date | None):
        threat_level (None | str):
        primary_category (None | str):
        description (None | str):
        social_handles (CompetitorResponseSocialHandlesType0 | None):
        logo_asset_id (None | UUID):
        last_verified_at (datetime.datetime | None):
        last_verified_by_bot_id (None | UUID):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (CompetitorResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    name: str
    legal_name: None | str
    website_url: None | str
    primary_country_code: None | str
    hq_city: None | str
    founded_year: int | None
    employee_count_range: None | str
    employee_count_exact: int | None
    funding_total: None | str
    funding_currency_id: None | UUID
    public_or_private: None | str
    stock_ticker: None | str
    status: str
    acquired_by: None | str
    acquired_at: datetime.date | None
    threat_level: None | str
    primary_category: None | str
    description: None | str
    social_handles: CompetitorResponseSocialHandlesType0 | None
    logo_asset_id: None | UUID
    last_verified_at: datetime.datetime | None
    last_verified_by_bot_id: None | UUID
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: CompetitorResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.competitor_response_metadata_type_0 import CompetitorResponseMetadataType0  # noqa: PLC0415
        from ..models.competitor_response_social_handles_type_0 import (
            CompetitorResponseSocialHandlesType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        legal_name: None | str
        legal_name = self.legal_name

        website_url: None | str
        website_url = self.website_url

        primary_country_code: None | str
        primary_country_code = self.primary_country_code

        hq_city: None | str
        hq_city = self.hq_city

        founded_year: int | None
        founded_year = self.founded_year

        employee_count_range: None | str
        employee_count_range = self.employee_count_range

        employee_count_exact: int | None
        employee_count_exact = self.employee_count_exact

        funding_total: None | str
        funding_total = self.funding_total

        funding_currency_id: None | str
        if isinstance(self.funding_currency_id, UUID):
            funding_currency_id = str(self.funding_currency_id)
        else:
            funding_currency_id = self.funding_currency_id

        public_or_private: None | str
        public_or_private = self.public_or_private

        stock_ticker: None | str
        stock_ticker = self.stock_ticker

        status = self.status

        acquired_by: None | str
        acquired_by = self.acquired_by

        acquired_at: None | str
        if isinstance(self.acquired_at, datetime.date):
            acquired_at = self.acquired_at.isoformat()
        else:
            acquired_at = self.acquired_at

        threat_level: None | str
        threat_level = self.threat_level

        primary_category: None | str
        primary_category = self.primary_category

        description: None | str
        description = self.description

        social_handles: dict[str, Any] | None
        if isinstance(self.social_handles, CompetitorResponseSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        logo_asset_id: None | str
        if isinstance(self.logo_asset_id, UUID):
            logo_asset_id = str(self.logo_asset_id)
        else:
            logo_asset_id = self.logo_asset_id

        last_verified_at: None | str
        if isinstance(self.last_verified_at, datetime.datetime):
            last_verified_at = self.last_verified_at.isoformat()
        else:
            last_verified_at = self.last_verified_at

        last_verified_by_bot_id: None | str
        if isinstance(self.last_verified_by_bot_id, UUID):
            last_verified_by_bot_id = str(self.last_verified_by_bot_id)
        else:
            last_verified_by_bot_id = self.last_verified_by_bot_id

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        approved_by_user_id: None | str
        if isinstance(self.approved_by_user_id, UUID):
            approved_by_user_id = str(self.approved_by_user_id)
        else:
            approved_by_user_id = self.approved_by_user_id

        last_modified_by_bot_id: None | str
        if isinstance(self.last_modified_by_bot_id, UUID):
            last_modified_by_bot_id = str(self.last_modified_by_bot_id)
        else:
            last_modified_by_bot_id = self.last_modified_by_bot_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CompetitorResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "name": name,
                "legal_name": legal_name,
                "website_url": website_url,
                "primary_country_code": primary_country_code,
                "hq_city": hq_city,
                "founded_year": founded_year,
                "employee_count_range": employee_count_range,
                "employee_count_exact": employee_count_exact,
                "funding_total": funding_total,
                "funding_currency_id": funding_currency_id,
                "public_or_private": public_or_private,
                "stock_ticker": stock_ticker,
                "status": status,
                "acquired_by": acquired_by,
                "acquired_at": acquired_at,
                "threat_level": threat_level,
                "primary_category": primary_category,
                "description": description,
                "social_handles": social_handles,
                "logo_asset_id": logo_asset_id,
                "last_verified_at": last_verified_at,
                "last_verified_by_bot_id": last_verified_by_bot_id,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "last_modified_by_bot_id": last_modified_by_bot_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competitor_response_metadata_type_0 import CompetitorResponseMetadataType0  # noqa: PLC0415
        from ..models.competitor_response_social_handles_type_0 import (
            CompetitorResponseSocialHandlesType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        def _parse_legal_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        legal_name = _parse_legal_name(d.pop("legal_name"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_primary_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_country_code = _parse_primary_country_code(d.pop("primary_country_code"))

        def _parse_hq_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hq_city = _parse_hq_city(d.pop("hq_city"))

        def _parse_founded_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        founded_year = _parse_founded_year(d.pop("founded_year"))

        def _parse_employee_count_range(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        employee_count_range = _parse_employee_count_range(d.pop("employee_count_range"))

        def _parse_employee_count_exact(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        employee_count_exact = _parse_employee_count_exact(d.pop("employee_count_exact"))

        def _parse_funding_total(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        funding_total = _parse_funding_total(d.pop("funding_total"))

        def _parse_funding_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                funding_currency_id_type_0 = UUID(data)

                return funding_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        funding_currency_id = _parse_funding_currency_id(d.pop("funding_currency_id"))

        def _parse_public_or_private(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_or_private = _parse_public_or_private(d.pop("public_or_private"))

        def _parse_stock_ticker(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        stock_ticker = _parse_stock_ticker(d.pop("stock_ticker"))

        status = d.pop("status")

        def _parse_acquired_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        acquired_by = _parse_acquired_by(d.pop("acquired_by"))

        def _parse_acquired_at(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acquired_at_type_0 = datetime.date.fromisoformat(data)

                return acquired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        acquired_at = _parse_acquired_at(d.pop("acquired_at"))

        def _parse_threat_level(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        threat_level = _parse_threat_level(d.pop("threat_level"))

        def _parse_primary_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_category = _parse_primary_category(d.pop("primary_category"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_social_handles(data: object) -> CompetitorResponseSocialHandlesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = CompetitorResponseSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompetitorResponseSocialHandlesType0 | None, data)

        social_handles = _parse_social_handles(d.pop("social_handles"))

        def _parse_logo_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_asset_id_type_0 = UUID(data)

                return logo_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        logo_asset_id = _parse_logo_asset_id(d.pop("logo_asset_id"))

        def _parse_last_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_verified_at = _parse_last_verified_at(d.pop("last_verified_at"))

        def _parse_last_verified_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_verified_by_bot_id_type_0 = UUID(data)

                return last_verified_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        last_verified_by_bot_id = _parse_last_verified_by_bot_id(d.pop("last_verified_by_bot_id"))

        def _parse_created_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_bot_id_type_0 = UUID(data)

                return created_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        created_by_bot_id = _parse_created_by_bot_id(d.pop("created_by_bot_id"))

        def _parse_approved_by_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_by_user_id_type_0 = UUID(data)

                return approved_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        approved_by_user_id = _parse_approved_by_user_id(d.pop("approved_by_user_id"))

        def _parse_last_modified_by_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_modified_by_bot_id_type_0 = UUID(data)

                return last_modified_by_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        last_modified_by_bot_id = _parse_last_modified_by_bot_id(d.pop("last_modified_by_bot_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        def _parse_metadata(data: object) -> CompetitorResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CompetitorResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompetitorResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        competitor_response = cls(
            id=id,
            org_id=org_id,
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
            acquired_by=acquired_by,
            acquired_at=acquired_at,
            threat_level=threat_level,
            primary_category=primary_category,
            description=description,
            social_handles=social_handles,
            logo_asset_id=logo_asset_id,
            last_verified_at=last_verified_at,
            last_verified_by_bot_id=last_verified_by_bot_id,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        competitor_response.additional_properties = d
        return competitor_response

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
