from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_update_metadata_type_0 import AccountUpdateMetadataType0
    from ..models.account_update_social_handles_type_0 import AccountUpdateSocialHandlesType0


T = TypeVar("T", bound="AccountUpdate")


@_attrs_define
class AccountUpdate:
    """
    Attributes:
        name (None | str | Unset):
        legal_name (None | str | Unset):
        account_type (None | str | Unset):
        industry (None | str | Unset):
        size_segment (None | str | Unset):
        website_url (None | str | Unset):
        country_code (None | str | Unset):
        hq_city (None | str | Unset):
        employee_count (int | None | Unset):
        annual_revenue (float | None | str | Unset):
        revenue_currency_id (None | Unset | UUID):
        parent_account_id (None | Unset | UUID):
        primary_owner_user_id (None | Unset | UUID):
        primary_owner_bot_id (None | Unset | UUID):
        status (None | str | Unset):
        source (None | str | Unset):
        tier (None | str | Unset):
        social_handles (AccountUpdateSocialHandlesType0 | None | Unset):
        metadata (AccountUpdateMetadataType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    account_type: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    size_segment: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    hq_city: None | str | Unset = UNSET
    employee_count: int | None | Unset = UNSET
    annual_revenue: float | None | str | Unset = UNSET
    revenue_currency_id: None | Unset | UUID = UNSET
    parent_account_id: None | Unset | UUID = UNSET
    primary_owner_user_id: None | Unset | UUID = UNSET
    primary_owner_bot_id: None | Unset | UUID = UNSET
    status: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    tier: None | str | Unset = UNSET
    social_handles: AccountUpdateSocialHandlesType0 | None | Unset = UNSET
    metadata: AccountUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.account_update_metadata_type_0 import AccountUpdateMetadataType0  # noqa: PLC0415
        from ..models.account_update_social_handles_type_0 import AccountUpdateSocialHandlesType0  # noqa: PLC0415

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

        account_type: None | str | Unset
        if isinstance(self.account_type, Unset):
            account_type = UNSET
        else:
            account_type = self.account_type

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        size_segment: None | str | Unset
        if isinstance(self.size_segment, Unset):
            size_segment = UNSET
        else:
            size_segment = self.size_segment

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        hq_city: None | str | Unset
        if isinstance(self.hq_city, Unset):
            hq_city = UNSET
        else:
            hq_city = self.hq_city

        employee_count: int | None | Unset
        if isinstance(self.employee_count, Unset):
            employee_count = UNSET
        else:
            employee_count = self.employee_count

        annual_revenue: float | None | str | Unset
        if isinstance(self.annual_revenue, Unset):
            annual_revenue = UNSET
        else:
            annual_revenue = self.annual_revenue

        revenue_currency_id: None | str | Unset
        if isinstance(self.revenue_currency_id, Unset):
            revenue_currency_id = UNSET
        elif isinstance(self.revenue_currency_id, UUID):
            revenue_currency_id = str(self.revenue_currency_id)
        else:
            revenue_currency_id = self.revenue_currency_id

        parent_account_id: None | str | Unset
        if isinstance(self.parent_account_id, Unset):
            parent_account_id = UNSET
        elif isinstance(self.parent_account_id, UUID):
            parent_account_id = str(self.parent_account_id)
        else:
            parent_account_id = self.parent_account_id

        primary_owner_user_id: None | str | Unset
        if isinstance(self.primary_owner_user_id, Unset):
            primary_owner_user_id = UNSET
        elif isinstance(self.primary_owner_user_id, UUID):
            primary_owner_user_id = str(self.primary_owner_user_id)
        else:
            primary_owner_user_id = self.primary_owner_user_id

        primary_owner_bot_id: None | str | Unset
        if isinstance(self.primary_owner_bot_id, Unset):
            primary_owner_bot_id = UNSET
        elif isinstance(self.primary_owner_bot_id, UUID):
            primary_owner_bot_id = str(self.primary_owner_bot_id)
        else:
            primary_owner_bot_id = self.primary_owner_bot_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        tier: None | str | Unset
        if isinstance(self.tier, Unset):
            tier = UNSET
        else:
            tier = self.tier

        social_handles: dict[str, Any] | None | Unset
        if isinstance(self.social_handles, Unset):
            social_handles = UNSET
        elif isinstance(self.social_handles, AccountUpdateSocialHandlesType0):
            social_handles = self.social_handles.to_dict()
        else:
            social_handles = self.social_handles

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AccountUpdateMetadataType0):
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
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if industry is not UNSET:
            field_dict["industry"] = industry
        if size_segment is not UNSET:
            field_dict["size_segment"] = size_segment
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if hq_city is not UNSET:
            field_dict["hq_city"] = hq_city
        if employee_count is not UNSET:
            field_dict["employee_count"] = employee_count
        if annual_revenue is not UNSET:
            field_dict["annual_revenue"] = annual_revenue
        if revenue_currency_id is not UNSET:
            field_dict["revenue_currency_id"] = revenue_currency_id
        if parent_account_id is not UNSET:
            field_dict["parent_account_id"] = parent_account_id
        if primary_owner_user_id is not UNSET:
            field_dict["primary_owner_user_id"] = primary_owner_user_id
        if primary_owner_bot_id is not UNSET:
            field_dict["primary_owner_bot_id"] = primary_owner_bot_id
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if tier is not UNSET:
            field_dict["tier"] = tier
        if social_handles is not UNSET:
            field_dict["social_handles"] = social_handles
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_update_metadata_type_0 import AccountUpdateMetadataType0  # noqa: PLC0415
        from ..models.account_update_social_handles_type_0 import AccountUpdateSocialHandlesType0  # noqa: PLC0415

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

        def _parse_account_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_type = _parse_account_type(d.pop("account_type", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_size_segment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        size_segment = _parse_size_segment(d.pop("size_segment", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_hq_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hq_city = _parse_hq_city(d.pop("hq_city", UNSET))

        def _parse_employee_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employee_count = _parse_employee_count(d.pop("employee_count", UNSET))

        def _parse_annual_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        annual_revenue = _parse_annual_revenue(d.pop("annual_revenue", UNSET))

        def _parse_revenue_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revenue_currency_id_type_0 = UUID(data)

                return revenue_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        revenue_currency_id = _parse_revenue_currency_id(d.pop("revenue_currency_id", UNSET))

        def _parse_parent_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_account_id_type_0 = UUID(data)

                return parent_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_account_id = _parse_parent_account_id(d.pop("parent_account_id", UNSET))

        def _parse_primary_owner_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_owner_user_id_type_0 = UUID(data)

                return primary_owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_owner_user_id = _parse_primary_owner_user_id(d.pop("primary_owner_user_id", UNSET))

        def _parse_primary_owner_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_owner_bot_id_type_0 = UUID(data)

                return primary_owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_owner_bot_id = _parse_primary_owner_bot_id(d.pop("primary_owner_bot_id", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_tier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tier = _parse_tier(d.pop("tier", UNSET))

        def _parse_social_handles(data: object) -> AccountUpdateSocialHandlesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_handles_type_0 = AccountUpdateSocialHandlesType0.from_dict(data)

                return social_handles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountUpdateSocialHandlesType0 | None | Unset, data)

        social_handles = _parse_social_handles(d.pop("social_handles", UNSET))

        def _parse_metadata(data: object) -> AccountUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AccountUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccountUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        account_update = cls(
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
            metadata=metadata,
        )

        account_update.additional_properties = d
        return account_update

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
