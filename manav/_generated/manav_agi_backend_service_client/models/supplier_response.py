from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_response_metadata_type_0 import SupplierResponseMetadataType0


T = TypeVar("T", bound="SupplierResponse")


@_attrs_define
class SupplierResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        legal_name (None | str):
        supplier_code (None | str):
        category (None | str):
        status (str):
        country_code (None | str):
        hq_city (None | str):
        tax_id (None | str):
        registration_number (None | str):
        website_url (None | str):
        primary_currency_id (None | UUID):
        payment_terms_days (int | None):
        is_preferred (bool):
        is_diversity_owned (bool | None):
        diversity_categories (list[str] | None):
        sanctions_check_status (None | str):
        sanctions_checked_at (datetime.datetime | None):
        performance_score (float | None):
        risk_score (float | None):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        approved_at (datetime.datetime | None):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (None | SupplierResponseMetadataType0 | Unset):
    """

    id: UUID
    org_id: UUID
    name: str
    legal_name: None | str
    supplier_code: None | str
    category: None | str
    status: str
    country_code: None | str
    hq_city: None | str
    tax_id: None | str
    registration_number: None | str
    website_url: None | str
    primary_currency_id: None | UUID
    payment_terms_days: int | None
    is_preferred: bool
    is_diversity_owned: bool | None
    diversity_categories: list[str] | None
    sanctions_check_status: None | str
    sanctions_checked_at: datetime.datetime | None
    performance_score: float | None
    risk_score: float | None
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    approved_at: datetime.datetime | None
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: None | SupplierResponseMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.supplier_response_metadata_type_0 import SupplierResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        legal_name: None | str
        legal_name = self.legal_name

        supplier_code: None | str
        supplier_code = self.supplier_code

        category: None | str
        category = self.category

        status = self.status

        country_code: None | str
        country_code = self.country_code

        hq_city: None | str
        hq_city = self.hq_city

        tax_id: None | str
        tax_id = self.tax_id

        registration_number: None | str
        registration_number = self.registration_number

        website_url: None | str
        website_url = self.website_url

        primary_currency_id: None | str
        if isinstance(self.primary_currency_id, UUID):
            primary_currency_id = str(self.primary_currency_id)
        else:
            primary_currency_id = self.primary_currency_id

        payment_terms_days: int | None
        payment_terms_days = self.payment_terms_days

        is_preferred = self.is_preferred

        is_diversity_owned: bool | None
        is_diversity_owned = self.is_diversity_owned

        diversity_categories: list[str] | None
        if isinstance(self.diversity_categories, list):
            diversity_categories = self.diversity_categories

        else:
            diversity_categories = self.diversity_categories

        sanctions_check_status: None | str
        sanctions_check_status = self.sanctions_check_status

        sanctions_checked_at: None | str
        if isinstance(self.sanctions_checked_at, datetime.datetime):
            sanctions_checked_at = self.sanctions_checked_at.isoformat()
        else:
            sanctions_checked_at = self.sanctions_checked_at

        performance_score: float | None
        performance_score = self.performance_score

        risk_score: float | None
        risk_score = self.risk_score

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

        approved_at: None | str
        if isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

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
        elif isinstance(self.metadata, SupplierResponseMetadataType0):
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
                "supplier_code": supplier_code,
                "category": category,
                "status": status,
                "country_code": country_code,
                "hq_city": hq_city,
                "tax_id": tax_id,
                "registration_number": registration_number,
                "website_url": website_url,
                "primary_currency_id": primary_currency_id,
                "payment_terms_days": payment_terms_days,
                "is_preferred": is_preferred,
                "is_diversity_owned": is_diversity_owned,
                "diversity_categories": diversity_categories,
                "sanctions_check_status": sanctions_check_status,
                "sanctions_checked_at": sanctions_checked_at,
                "performance_score": performance_score,
                "risk_score": risk_score,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "approved_at": approved_at,
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
        from ..models.supplier_response_metadata_type_0 import SupplierResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        def _parse_legal_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        legal_name = _parse_legal_name(d.pop("legal_name"))

        def _parse_supplier_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        supplier_code = _parse_supplier_code(d.pop("supplier_code"))

        def _parse_category(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        category = _parse_category(d.pop("category"))

        status = d.pop("status")

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

        def _parse_tax_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tax_id = _parse_tax_id(d.pop("tax_id"))

        def _parse_registration_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registration_number = _parse_registration_number(d.pop("registration_number"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_primary_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_currency_id_type_0 = UUID(data)

                return primary_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        primary_currency_id = _parse_primary_currency_id(d.pop("primary_currency_id"))

        def _parse_payment_terms_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payment_terms_days = _parse_payment_terms_days(d.pop("payment_terms_days"))

        is_preferred = d.pop("is_preferred")

        def _parse_is_diversity_owned(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        is_diversity_owned = _parse_is_diversity_owned(d.pop("is_diversity_owned"))

        def _parse_diversity_categories(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diversity_categories_type_0 = cast(list[str], data)

                return diversity_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        diversity_categories = _parse_diversity_categories(d.pop("diversity_categories"))

        def _parse_sanctions_check_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sanctions_check_status = _parse_sanctions_check_status(d.pop("sanctions_check_status"))

        def _parse_sanctions_checked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sanctions_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return sanctions_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        sanctions_checked_at = _parse_sanctions_checked_at(d.pop("sanctions_checked_at"))

        def _parse_performance_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        performance_score = _parse_performance_score(d.pop("performance_score"))

        def _parse_risk_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        risk_score = _parse_risk_score(d.pop("risk_score"))

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

        def _parse_approved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        approved_at = _parse_approved_at(d.pop("approved_at"))

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

        def _parse_metadata(data: object) -> None | SupplierResponseMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SupplierResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SupplierResponseMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        supplier_response = cls(
            id=id,
            org_id=org_id,
            name=name,
            legal_name=legal_name,
            supplier_code=supplier_code,
            category=category,
            status=status,
            country_code=country_code,
            hq_city=hq_city,
            tax_id=tax_id,
            registration_number=registration_number,
            website_url=website_url,
            primary_currency_id=primary_currency_id,
            payment_terms_days=payment_terms_days,
            is_preferred=is_preferred,
            is_diversity_owned=is_diversity_owned,
            diversity_categories=diversity_categories,
            sanctions_check_status=sanctions_check_status,
            sanctions_checked_at=sanctions_checked_at,
            performance_score=performance_score,
            risk_score=risk_score,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            approved_at=approved_at,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        supplier_response.additional_properties = d
        return supplier_response

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
