from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_create_metadata_type_0 import InvestorCreateMetadataType0


T = TypeVar("T", bound="InvestorCreate")


@_attrs_define
class InvestorCreate:
    """
    Attributes:
        name (str):
        investor_type (str): vc / angel / family_office / corporate / individual / fund_of_funds
        firm_name (None | str | Unset):
        primary_contact_name (None | str | Unset):
        primary_contact_email (None | str | Unset):
        primary_contact_phone (None | str | Unset):
        primary_contact_user_id (None | Unset | UUID):
        investor_stage_focus (list[str] | None | Unset):
        typical_check_size_min (float | None | str | Unset):
        typical_check_size_max (float | None | str | Unset):
        check_currency_id (None | Unset | UUID):
        sector_focus (list[str] | None | Unset):
        geographic_focus (list[str] | None | Unset):
        website_url (None | str | Unset):
        linkedin_url (None | str | Unset):
        country_code (None | str | Unset):
        hq_city (None | str | Unset):
        status (str | Unset):  Default: 'prospect'.
        threat_level_to_competitors (list[UUID] | None | Unset):
        notes (None | str | Unset):
        metadata (InvestorCreateMetadataType0 | None | Unset):
    """

    name: str
    investor_type: str
    firm_name: None | str | Unset = UNSET
    primary_contact_name: None | str | Unset = UNSET
    primary_contact_email: None | str | Unset = UNSET
    primary_contact_phone: None | str | Unset = UNSET
    primary_contact_user_id: None | Unset | UUID = UNSET
    investor_stage_focus: list[str] | None | Unset = UNSET
    typical_check_size_min: float | None | str | Unset = UNSET
    typical_check_size_max: float | None | str | Unset = UNSET
    check_currency_id: None | Unset | UUID = UNSET
    sector_focus: list[str] | None | Unset = UNSET
    geographic_focus: list[str] | None | Unset = UNSET
    website_url: None | str | Unset = UNSET
    linkedin_url: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    hq_city: None | str | Unset = UNSET
    status: str | Unset = "prospect"
    threat_level_to_competitors: list[UUID] | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    metadata: InvestorCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_create_metadata_type_0 import InvestorCreateMetadataType0  # noqa: PLC0415

        name = self.name

        investor_type = self.investor_type

        firm_name: None | str | Unset
        if isinstance(self.firm_name, Unset):
            firm_name = UNSET
        else:
            firm_name = self.firm_name

        primary_contact_name: None | str | Unset
        if isinstance(self.primary_contact_name, Unset):
            primary_contact_name = UNSET
        else:
            primary_contact_name = self.primary_contact_name

        primary_contact_email: None | str | Unset
        if isinstance(self.primary_contact_email, Unset):
            primary_contact_email = UNSET
        else:
            primary_contact_email = self.primary_contact_email

        primary_contact_phone: None | str | Unset
        if isinstance(self.primary_contact_phone, Unset):
            primary_contact_phone = UNSET
        else:
            primary_contact_phone = self.primary_contact_phone

        primary_contact_user_id: None | str | Unset
        if isinstance(self.primary_contact_user_id, Unset):
            primary_contact_user_id = UNSET
        elif isinstance(self.primary_contact_user_id, UUID):
            primary_contact_user_id = str(self.primary_contact_user_id)
        else:
            primary_contact_user_id = self.primary_contact_user_id

        investor_stage_focus: list[str] | None | Unset
        if isinstance(self.investor_stage_focus, Unset):
            investor_stage_focus = UNSET
        elif isinstance(self.investor_stage_focus, list):
            investor_stage_focus = self.investor_stage_focus

        else:
            investor_stage_focus = self.investor_stage_focus

        typical_check_size_min: float | None | str | Unset
        if isinstance(self.typical_check_size_min, Unset):
            typical_check_size_min = UNSET
        else:
            typical_check_size_min = self.typical_check_size_min

        typical_check_size_max: float | None | str | Unset
        if isinstance(self.typical_check_size_max, Unset):
            typical_check_size_max = UNSET
        else:
            typical_check_size_max = self.typical_check_size_max

        check_currency_id: None | str | Unset
        if isinstance(self.check_currency_id, Unset):
            check_currency_id = UNSET
        elif isinstance(self.check_currency_id, UUID):
            check_currency_id = str(self.check_currency_id)
        else:
            check_currency_id = self.check_currency_id

        sector_focus: list[str] | None | Unset
        if isinstance(self.sector_focus, Unset):
            sector_focus = UNSET
        elif isinstance(self.sector_focus, list):
            sector_focus = self.sector_focus

        else:
            sector_focus = self.sector_focus

        geographic_focus: list[str] | None | Unset
        if isinstance(self.geographic_focus, Unset):
            geographic_focus = UNSET
        elif isinstance(self.geographic_focus, list):
            geographic_focus = self.geographic_focus

        else:
            geographic_focus = self.geographic_focus

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        linkedin_url: None | str | Unset
        if isinstance(self.linkedin_url, Unset):
            linkedin_url = UNSET
        else:
            linkedin_url = self.linkedin_url

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

        status = self.status

        threat_level_to_competitors: list[str] | None | Unset
        if isinstance(self.threat_level_to_competitors, Unset):
            threat_level_to_competitors = UNSET
        elif isinstance(self.threat_level_to_competitors, list):
            threat_level_to_competitors = []
            for threat_level_to_competitors_type_0_item_data in self.threat_level_to_competitors:
                threat_level_to_competitors_type_0_item = str(threat_level_to_competitors_type_0_item_data)
                threat_level_to_competitors.append(threat_level_to_competitors_type_0_item)

        else:
            threat_level_to_competitors = self.threat_level_to_competitors

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InvestorCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "investor_type": investor_type,
            }
        )
        if firm_name is not UNSET:
            field_dict["firm_name"] = firm_name
        if primary_contact_name is not UNSET:
            field_dict["primary_contact_name"] = primary_contact_name
        if primary_contact_email is not UNSET:
            field_dict["primary_contact_email"] = primary_contact_email
        if primary_contact_phone is not UNSET:
            field_dict["primary_contact_phone"] = primary_contact_phone
        if primary_contact_user_id is not UNSET:
            field_dict["primary_contact_user_id"] = primary_contact_user_id
        if investor_stage_focus is not UNSET:
            field_dict["investor_stage_focus"] = investor_stage_focus
        if typical_check_size_min is not UNSET:
            field_dict["typical_check_size_min"] = typical_check_size_min
        if typical_check_size_max is not UNSET:
            field_dict["typical_check_size_max"] = typical_check_size_max
        if check_currency_id is not UNSET:
            field_dict["check_currency_id"] = check_currency_id
        if sector_focus is not UNSET:
            field_dict["sector_focus"] = sector_focus
        if geographic_focus is not UNSET:
            field_dict["geographic_focus"] = geographic_focus
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if linkedin_url is not UNSET:
            field_dict["linkedin_url"] = linkedin_url
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if hq_city is not UNSET:
            field_dict["hq_city"] = hq_city
        if status is not UNSET:
            field_dict["status"] = status
        if threat_level_to_competitors is not UNSET:
            field_dict["threat_level_to_competitors"] = threat_level_to_competitors
        if notes is not UNSET:
            field_dict["notes"] = notes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_create_metadata_type_0 import InvestorCreateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        investor_type = d.pop("investor_type")

        def _parse_firm_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        firm_name = _parse_firm_name(d.pop("firm_name", UNSET))

        def _parse_primary_contact_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_contact_name = _parse_primary_contact_name(d.pop("primary_contact_name", UNSET))

        def _parse_primary_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_contact_email = _parse_primary_contact_email(d.pop("primary_contact_email", UNSET))

        def _parse_primary_contact_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_contact_phone = _parse_primary_contact_phone(d.pop("primary_contact_phone", UNSET))

        def _parse_primary_contact_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_contact_user_id_type_0 = UUID(data)

                return primary_contact_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_contact_user_id = _parse_primary_contact_user_id(d.pop("primary_contact_user_id", UNSET))

        def _parse_investor_stage_focus(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_stage_focus_type_0 = cast(list[str], data)

                return investor_stage_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        investor_stage_focus = _parse_investor_stage_focus(d.pop("investor_stage_focus", UNSET))

        def _parse_typical_check_size_min(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        typical_check_size_min = _parse_typical_check_size_min(d.pop("typical_check_size_min", UNSET))

        def _parse_typical_check_size_max(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        typical_check_size_max = _parse_typical_check_size_max(d.pop("typical_check_size_max", UNSET))

        def _parse_check_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_currency_id_type_0 = UUID(data)

                return check_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        check_currency_id = _parse_check_currency_id(d.pop("check_currency_id", UNSET))

        def _parse_sector_focus(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sector_focus_type_0 = cast(list[str], data)

                return sector_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sector_focus = _parse_sector_focus(d.pop("sector_focus", UNSET))

        def _parse_geographic_focus(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                geographic_focus_type_0 = cast(list[str], data)

                return geographic_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        geographic_focus = _parse_geographic_focus(d.pop("geographic_focus", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_linkedin_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedin_url", UNSET))

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

        status = d.pop("status", UNSET)

        def _parse_threat_level_to_competitors(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                threat_level_to_competitors_type_0 = []
                _threat_level_to_competitors_type_0 = data
                for threat_level_to_competitors_type_0_item_data in _threat_level_to_competitors_type_0:
                    threat_level_to_competitors_type_0_item = UUID(threat_level_to_competitors_type_0_item_data)

                    threat_level_to_competitors_type_0.append(threat_level_to_competitors_type_0_item)

                return threat_level_to_competitors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        threat_level_to_competitors = _parse_threat_level_to_competitors(d.pop("threat_level_to_competitors", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_metadata(data: object) -> InvestorCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InvestorCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        investor_create = cls(
            name=name,
            investor_type=investor_type,
            firm_name=firm_name,
            primary_contact_name=primary_contact_name,
            primary_contact_email=primary_contact_email,
            primary_contact_phone=primary_contact_phone,
            primary_contact_user_id=primary_contact_user_id,
            investor_stage_focus=investor_stage_focus,
            typical_check_size_min=typical_check_size_min,
            typical_check_size_max=typical_check_size_max,
            check_currency_id=check_currency_id,
            sector_focus=sector_focus,
            geographic_focus=geographic_focus,
            website_url=website_url,
            linkedin_url=linkedin_url,
            country_code=country_code,
            hq_city=hq_city,
            status=status,
            threat_level_to_competitors=threat_level_to_competitors,
            notes=notes,
            metadata=metadata,
        )

        investor_create.additional_properties = d
        return investor_create

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
