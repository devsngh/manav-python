from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0
    from ..models.account_response_social_handles_type_0 import AccountResponseSocialHandlesType0


T = TypeVar("T", bound="AccountResponse")


@_attrs_define
class AccountResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        legal_name (None | str):
        account_type (None | str):
        industry (None | str):
        size_segment (None | str):
        website_url (None | str):
        country_code (None | str):
        hq_city (None | str):
        employee_count (int | None):
        annual_revenue (None | str):
        revenue_currency_id (None | UUID):
        parent_account_id (None | UUID):
        primary_owner_user_id (None | UUID):
        primary_owner_bot_id (None | UUID):
        status (str):
        source (None | str):
        tier (None | str):
        social_handles (AccountResponseSocialHandlesType0 | None):
        created_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (AccountResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    name: str
    legal_name: None | str
    account_type: None | str
    industry: None | str
    size_segment: None | str
    website_url: None | str
    country_code: None | str
    hq_city: None | str
    employee_count: int | None
    annual_revenue: None | str
    revenue_currency_id: None | UUID
    parent_account_id: None | UUID
    primary_owner_user_id: None | UUID
    primary_owner_bot_id: None | UUID
    status: str
    source: None | str
    tier: None | str
    social_handles: AccountResponseSocialHandlesType0 | None
    created_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: AccountResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0  # noqa: PLC0415
        from ..models.account_response_social_handles_type_0 import AccountResponseSocialHandlesType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        legal_name: None | str
        legal_name = self.legal_name

        account_type: None | str
        account_type = self.account_type

        industry: None | str
        industry = self.industry

        size_segment: None | str
        size_segment = self.size_segment

        website_url: None | str
        website_url = self.website_url

        country_code: None | str
        country_code = self.country_code

        hq_city: None | str
        hq_city = self.hq_city

        employee_count: int | None
        employee_count = self.employee_count

        annual_revenue: None | str
        annual_revenue = self.annual_revenue

        revenue_currency_id: None | str
        if isinstance(self.revenue_currency_id, UUID):
            revenue_currency_id = str(self.revenue_currency_id)
        else:
            revenue_currency_id = self.revenue_currency_id

        parent_account_id: None | str
        if isinstance(self.parent_account_id, UUID):
            parent_account_id = str(self.parent_account_id)
        else:
            parent_account_id = self.parent_account_id

        primary_owner_user_id: None | str
        if isinstance(self.primary_owner_user_id, UUID):
            primary_owner_user_id = str(self.primary_owner_user_id)
        else:
            primary_owner_user_id = self.primary_owner_user_id

        primary_owner_bot_id: None | str
        if isinstance(self.primary_owner_bot_id, UUID):
            primary_owner_bot_id = str(self.primary_owner_bot_id)
        else:
            primary_owner_bot_id = self.primary_owner_bot_id

        status = self.status

        source: None | str
        source = self.source

        tier: None | str
        tier = self.tier

        social_handles: dict[str, Any] | None
        if isinstance(self.social_handles, AccountResponseSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

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
        elif isinstance(self.metadata, AccountResponseMetadataType0):
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
                "account_type": account_type,
                "industry": industry,
                "size_segment": size_segment,
                "website_url": website_url,
                "country_code": country_code,
                "hq_city": hq_city,
                "employee_count": employee_count,
                "annual_revenue": annual_revenue,
                "revenue_currency_id": revenue_currency_id,
                "parent_account_id": parent_account_id,
                "primary_owner_user_id": primary_owner_user_id,
                "primary_owner_bot_id": primary_owner_bot_id,
                "status": status,
                "source": source,
                "tier": tier,
                "social_handles": social_handles,
                "created_by_bot_id": created_by_bot_id,
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
        from ..models.account_response_metadata_type_0 import AccountResponseMetadataType0  # noqa: PLC0415
        from ..models.account_response_social_handles_type_0 import AccountResponseSocialHandlesType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        def _parse_legal_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        legal_name = _parse_legal_name(d.pop("legal_name"))

        def _parse_account_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_type = _parse_account_type(d.pop("account_type"))

        def _parse_industry(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        industry = _parse_industry(d.pop("industry"))

        def _parse_size_segment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        size_segment = _parse_size_segment(d.pop("size_segment"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_country_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country_code = _parse_country_code(d.pop("country_code"))

        def _parse_hq_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        hq_city = _parse_hq_city(d.pop("hq_city"))

        def _parse_employee_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        employee_count = _parse_employee_count(d.pop("employee_count"))

        def _parse_annual_revenue(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        annual_revenue = _parse_annual_revenue(d.pop("annual_revenue"))

        def _parse_revenue_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revenue_currency_id_type_0 = UUID(data)

                return revenue_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        revenue_currency_id = _parse_revenue_currency_id(d.pop("revenue_currency_id"))

        def _parse_parent_account_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_account_id_type_0 = UUID(data)

                return parent_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_account_id = _parse_parent_account_id(d.pop("parent_account_id"))

        def _parse_primary_owner_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_owner_user_id_type_0 = UUID(data)

                return primary_owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        primary_owner_user_id = _parse_primary_owner_user_id(d.pop("primary_owner_user_id"))

        def _parse_primary_owner_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_owner_bot_id_type_0 = UUID(data)

                return primary_owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        primary_owner_bot_id = _parse_primary_owner_bot_id(d.pop("primary_owner_bot_id"))

        status = d.pop("status")

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        def _parse_tier(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier = _parse_tier(d.pop("tier"))

        def _parse_social_handles(data: object) -> AccountResponseSocialHandlesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = AccountResponseSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountResponseSocialHandlesType0 | None, data)

        social_handles = _parse_social_handles(d.pop("social_handles"))

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

        def _parse_metadata(data: object) -> AccountResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AccountResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        account_response = cls(
            id=id,
            org_id=org_id,
            name=name,
            legal_name=legal_name,
            account_type=account_type,
            industry=industry,
            size_segment=size_segment,
            website_url=website_url,
            country_code=country_code,
            hq_city=hq_city,
            employee_count=employee_count,
            annual_revenue=annual_revenue,
            revenue_currency_id=revenue_currency_id,
            parent_account_id=parent_account_id,
            primary_owner_user_id=primary_owner_user_id,
            primary_owner_bot_id=primary_owner_bot_id,
            status=status,
            source=source,
            tier=tier,
            social_handles=social_handles,
            created_by_bot_id=created_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        account_response.additional_properties = d
        return account_response

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
