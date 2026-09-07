from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_create_custom_metadata_type_0 import OrganizationCreateCustomMetadataType0


T = TypeVar("T", bound="OrganizationCreate")


@_attrs_define
class OrganizationCreate:
    """Schema for creating organization

    Attributes:
        name (str):
        type_ (str):
        logo_url (None | str | Unset):
        registration_number (None | str | Unset):
        tax_id (None | str | Unset):
        legal_entity_type (None | str | Unset):
        industry (None | str | Unset):
        sector (None | str | Unset):
        email (None | str | Unset):
        phone (None | str | Unset):
        website (None | str | Unset):
        address_line1 (None | str | Unset):
        address_line2 (None | str | Unset):
        city (None | str | Unset):
        state (None | str | Unset):
        country (None | str | Unset):
        postal_code (None | str | Unset):
        established_date (datetime.date | None | Unset):
        employee_count_range (None | str | Unset):
        annual_revenue_range (None | str | Unset):
        description (None | str | Unset):
        tags (list[str] | None | Unset):
        custom_metadata (None | OrganizationCreateCustomMetadataType0 | Unset):
    """

    name: str
    type_: str
    logo_url: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    legal_entity_type: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    sector: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    address_line1: None | str | Unset = UNSET
    address_line2: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    established_date: datetime.date | None | Unset = UNSET
    employee_count_range: None | str | Unset = UNSET
    annual_revenue_range: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    custom_metadata: None | OrganizationCreateCustomMetadataType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_create_custom_metadata_type_0 import (
            OrganizationCreateCustomMetadataType0,  # noqa: PLC0415
        )

        name = self.name

        type_ = self.type_

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id

        legal_entity_type: None | str | Unset
        if isinstance(self.legal_entity_type, Unset):
            legal_entity_type = UNSET
        else:
            legal_entity_type = self.legal_entity_type

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        sector: None | str | Unset
        if isinstance(self.sector, Unset):
            sector = UNSET
        else:
            sector = self.sector

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        address_line1: None | str | Unset
        if isinstance(self.address_line1, Unset):
            address_line1 = UNSET
        else:
            address_line1 = self.address_line1

        address_line2: None | str | Unset
        if isinstance(self.address_line2, Unset):
            address_line2 = UNSET
        else:
            address_line2 = self.address_line2

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        established_date: None | str | Unset
        if isinstance(self.established_date, Unset):
            established_date = UNSET
        elif isinstance(self.established_date, datetime.date):
            established_date = self.established_date.isoformat()
        else:
            established_date = self.established_date

        employee_count_range: None | str | Unset
        if isinstance(self.employee_count_range, Unset):
            employee_count_range = UNSET
        else:
            employee_count_range = self.employee_count_range

        annual_revenue_range: None | str | Unset
        if isinstance(self.annual_revenue_range, Unset):
            annual_revenue_range = UNSET
        else:
            annual_revenue_range = self.annual_revenue_range

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        custom_metadata: dict[str, Any] | None | Unset
        if isinstance(self.custom_metadata, Unset):
            custom_metadata = UNSET
        elif isinstance(self.custom_metadata, OrganizationCreateCustomMetadataType0):
            custom_metadata = self.custom_metadata.to_dict()
        else:
            custom_metadata = self.custom_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if legal_entity_type is not UNSET:
            field_dict["legal_entity_type"] = legal_entity_type
        if industry is not UNSET:
            field_dict["industry"] = industry
        if sector is not UNSET:
            field_dict["sector"] = sector
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if established_date is not UNSET:
            field_dict["established_date"] = established_date
        if employee_count_range is not UNSET:
            field_dict["employee_count_range"] = employee_count_range
        if annual_revenue_range is not UNSET:
            field_dict["annual_revenue_range"] = annual_revenue_range
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if custom_metadata is not UNSET:
            field_dict["custom_metadata"] = custom_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_create_custom_metadata_type_0 import (
            OrganizationCreateCustomMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(d.pop("registration_number", UNSET))

        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("tax_id", UNSET))

        def _parse_legal_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_entity_type = _parse_legal_entity_type(d.pop("legal_entity_type", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_sector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sector = _parse_sector(d.pop("sector", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_address_line1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line1 = _parse_address_line1(d.pop("address_line1", UNSET))

        def _parse_address_line2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_line2 = _parse_address_line2(d.pop("address_line2", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_established_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                established_date_type_0 = datetime.date.fromisoformat(data)

                return established_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        established_date = _parse_established_date(d.pop("established_date", UNSET))

        def _parse_employee_count_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employee_count_range = _parse_employee_count_range(d.pop("employee_count_range", UNSET))

        def _parse_annual_revenue_range(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_revenue_range = _parse_annual_revenue_range(d.pop("annual_revenue_range", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_custom_metadata(data: object) -> None | OrganizationCreateCustomMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_metadata_type_0 = OrganizationCreateCustomMetadataType0.from_dict(data)

                return custom_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationCreateCustomMetadataType0 | Unset, data)

        custom_metadata = _parse_custom_metadata(d.pop("custom_metadata", UNSET))

        organization_create = cls(
            name=name,
            type_=type_,
            logo_url=logo_url,
            registration_number=registration_number,
            tax_id=tax_id,
            legal_entity_type=legal_entity_type,
            industry=industry,
            sector=sector,
            email=email,
            phone=phone,
            website=website,
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            state=state,
            country=country,
            postal_code=postal_code,
            established_date=established_date,
            employee_count_range=employee_count_range,
            annual_revenue_range=annual_revenue_range,
            description=description,
            tags=tags,
            custom_metadata=custom_metadata,
        )

        organization_create.additional_properties = d
        return organization_create

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
