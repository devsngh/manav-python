from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.supplier_update_metadata_type_0 import SupplierUpdateMetadataType0


T = TypeVar("T", bound="SupplierUpdate")


@_attrs_define
class SupplierUpdate:
    """
    Attributes:
        name (None | str | Unset):
        legal_name (None | str | Unset):
        supplier_code (None | str | Unset):
        category (None | str | Unset):
        status (None | str | Unset):
        country_code (None | str | Unset):
        hq_city (None | str | Unset):
        tax_id (None | str | Unset):
        registration_number (None | str | Unset):
        website_url (None | str | Unset):
        primary_currency_id (None | Unset | UUID):
        payment_terms_days (int | None | Unset):
        is_preferred (bool | None | Unset):
        is_diversity_owned (bool | None | Unset):
        diversity_categories (list[str] | None | Unset):
        metadata (None | SupplierUpdateMetadataType0 | Unset):
    """

    name: None | str | Unset = UNSET
    legal_name: None | str | Unset = UNSET
    supplier_code: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    hq_city: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    primary_currency_id: None | Unset | UUID = UNSET
    payment_terms_days: int | None | Unset = UNSET
    is_preferred: bool | None | Unset = UNSET
    is_diversity_owned: bool | None | Unset = UNSET
    diversity_categories: list[str] | None | Unset = UNSET
    metadata: None | SupplierUpdateMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.supplier_update_metadata_type_0 import SupplierUpdateMetadataType0  # noqa: PLC0415

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

        supplier_code: None | str | Unset
        if isinstance(self.supplier_code, Unset):
            supplier_code = UNSET
        else:
            supplier_code = self.supplier_code

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

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

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        primary_currency_id: None | str | Unset
        if isinstance(self.primary_currency_id, Unset):
            primary_currency_id = UNSET
        elif isinstance(self.primary_currency_id, UUID):
            primary_currency_id = str(self.primary_currency_id)
        else:
            primary_currency_id = self.primary_currency_id

        payment_terms_days: int | None | Unset
        if isinstance(self.payment_terms_days, Unset):
            payment_terms_days = UNSET
        else:
            payment_terms_days = self.payment_terms_days

        is_preferred: bool | None | Unset
        if isinstance(self.is_preferred, Unset):
            is_preferred = UNSET
        else:
            is_preferred = self.is_preferred

        is_diversity_owned: bool | None | Unset
        if isinstance(self.is_diversity_owned, Unset):
            is_diversity_owned = UNSET
        else:
            is_diversity_owned = self.is_diversity_owned

        diversity_categories: list[str] | None | Unset
        if isinstance(self.diversity_categories, Unset):
            diversity_categories = UNSET
        elif isinstance(self.diversity_categories, list):
            diversity_categories = self.diversity_categories

        else:
            diversity_categories = self.diversity_categories

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SupplierUpdateMetadataType0):
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
        if supplier_code is not UNSET:
            field_dict["supplier_code"] = supplier_code
        if category is not UNSET:
            field_dict["category"] = category
        if status is not UNSET:
            field_dict["status"] = status
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if hq_city is not UNSET:
            field_dict["hq_city"] = hq_city
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if primary_currency_id is not UNSET:
            field_dict["primary_currency_id"] = primary_currency_id
        if payment_terms_days is not UNSET:
            field_dict["payment_terms_days"] = payment_terms_days
        if is_preferred is not UNSET:
            field_dict["is_preferred"] = is_preferred
        if is_diversity_owned is not UNSET:
            field_dict["is_diversity_owned"] = is_diversity_owned
        if diversity_categories is not UNSET:
            field_dict["diversity_categories"] = diversity_categories
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supplier_update_metadata_type_0 import SupplierUpdateMetadataType0  # noqa: PLC0415

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

        def _parse_supplier_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supplier_code = _parse_supplier_code(d.pop("supplier_code", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("tax_id", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(d.pop("registration_number", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_primary_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_currency_id_type_0 = UUID(data)

                return primary_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_currency_id = _parse_primary_currency_id(d.pop("primary_currency_id", UNSET))

        def _parse_payment_terms_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payment_terms_days = _parse_payment_terms_days(d.pop("payment_terms_days", UNSET))

        def _parse_is_preferred(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_preferred = _parse_is_preferred(d.pop("is_preferred", UNSET))

        def _parse_is_diversity_owned(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_diversity_owned = _parse_is_diversity_owned(d.pop("is_diversity_owned", UNSET))

        def _parse_diversity_categories(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                diversity_categories_type_0 = cast(list[str], data)

                return diversity_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        diversity_categories = _parse_diversity_categories(d.pop("diversity_categories", UNSET))

        def _parse_metadata(data: object) -> None | SupplierUpdateMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SupplierUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SupplierUpdateMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        supplier_update = cls(
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
            metadata=metadata,
        )

        supplier_update.additional_properties = d
        return supplier_update

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
