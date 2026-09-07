from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_response_metadata_type_0 import InvestorResponseMetadataType0


T = TypeVar("T", bound="InvestorResponse")


@_attrs_define
class InvestorResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        name (str):
        investor_type (str):
        firm_name (None | str):
        primary_contact_name (None | str):
        primary_contact_email (None | str):
        primary_contact_phone (None | str):
        primary_contact_user_id (None | UUID):
        investor_stage_focus (list[str] | None):
        typical_check_size_min (None | str):
        typical_check_size_max (None | str):
        check_currency_id (None | UUID):
        sector_focus (list[str] | None):
        geographic_focus (list[str] | None):
        website_url (None | str):
        linkedin_url (None | str):
        country_code (None | str):
        hq_city (None | str):
        status (str):
        threat_level_to_competitors (list[UUID] | None):
        notes (None | str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (InvestorResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    name: str
    investor_type: str
    firm_name: None | str
    primary_contact_name: None | str
    primary_contact_email: None | str
    primary_contact_phone: None | str
    primary_contact_user_id: None | UUID
    investor_stage_focus: list[str] | None
    typical_check_size_min: None | str
    typical_check_size_max: None | str
    check_currency_id: None | UUID
    sector_focus: list[str] | None
    geographic_focus: list[str] | None
    website_url: None | str
    linkedin_url: None | str
    country_code: None | str
    hq_city: None | str
    status: str
    threat_level_to_competitors: list[UUID] | None
    notes: None | str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: InvestorResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_response_metadata_type_0 import InvestorResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        name = self.name

        investor_type = self.investor_type

        firm_name: None | str
        firm_name = self.firm_name

        primary_contact_name: None | str
        primary_contact_name = self.primary_contact_name

        primary_contact_email: None | str
        primary_contact_email = self.primary_contact_email

        primary_contact_phone: None | str
        primary_contact_phone = self.primary_contact_phone

        primary_contact_user_id: None | str
        if isinstance(self.primary_contact_user_id, UUID):
            primary_contact_user_id = str(self.primary_contact_user_id)
        else:
            primary_contact_user_id = self.primary_contact_user_id

        investor_stage_focus: list[str] | None
        if isinstance(self.investor_stage_focus, list):
            investor_stage_focus = self.investor_stage_focus

        else:
            investor_stage_focus = self.investor_stage_focus

        typical_check_size_min: None | str
        typical_check_size_min = self.typical_check_size_min

        typical_check_size_max: None | str
        typical_check_size_max = self.typical_check_size_max

        check_currency_id: None | str
        if isinstance(self.check_currency_id, UUID):
            check_currency_id = str(self.check_currency_id)
        else:
            check_currency_id = self.check_currency_id

        sector_focus: list[str] | None
        if isinstance(self.sector_focus, list):
            sector_focus = self.sector_focus

        else:
            sector_focus = self.sector_focus

        geographic_focus: list[str] | None
        if isinstance(self.geographic_focus, list):
            geographic_focus = self.geographic_focus

        else:
            geographic_focus = self.geographic_focus

        website_url: None | str
        website_url = self.website_url

        linkedin_url: None | str
        linkedin_url = self.linkedin_url

        country_code: None | str
        country_code = self.country_code

        hq_city: None | str
        hq_city = self.hq_city

        status = self.status

        threat_level_to_competitors: list[str] | None
        if isinstance(self.threat_level_to_competitors, list):
            threat_level_to_competitors = []
            for threat_level_to_competitors_type_0_item_data in self.threat_level_to_competitors:
                threat_level_to_competitors_type_0_item = str(threat_level_to_competitors_type_0_item_data)
                threat_level_to_competitors.append(threat_level_to_competitors_type_0_item)

        else:
            threat_level_to_competitors = self.threat_level_to_competitors

        notes: None | str
        notes = self.notes

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
        elif isinstance(self.metadata, InvestorResponseMetadataType0):
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
                "investor_type": investor_type,
                "firm_name": firm_name,
                "primary_contact_name": primary_contact_name,
                "primary_contact_email": primary_contact_email,
                "primary_contact_phone": primary_contact_phone,
                "primary_contact_user_id": primary_contact_user_id,
                "investor_stage_focus": investor_stage_focus,
                "typical_check_size_min": typical_check_size_min,
                "typical_check_size_max": typical_check_size_max,
                "check_currency_id": check_currency_id,
                "sector_focus": sector_focus,
                "geographic_focus": geographic_focus,
                "website_url": website_url,
                "linkedin_url": linkedin_url,
                "country_code": country_code,
                "hq_city": hq_city,
                "status": status,
                "threat_level_to_competitors": threat_level_to_competitors,
                "notes": notes,
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
        from ..models.investor_response_metadata_type_0 import InvestorResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        name = d.pop("name")

        investor_type = d.pop("investor_type")

        def _parse_firm_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        firm_name = _parse_firm_name(d.pop("firm_name"))

        def _parse_primary_contact_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_contact_name = _parse_primary_contact_name(d.pop("primary_contact_name"))

        def _parse_primary_contact_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_contact_email = _parse_primary_contact_email(d.pop("primary_contact_email"))

        def _parse_primary_contact_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        primary_contact_phone = _parse_primary_contact_phone(d.pop("primary_contact_phone"))

        def _parse_primary_contact_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_contact_user_id_type_0 = UUID(data)

                return primary_contact_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        primary_contact_user_id = _parse_primary_contact_user_id(d.pop("primary_contact_user_id"))

        def _parse_investor_stage_focus(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                investor_stage_focus_type_0 = cast(list[str], data)

                return investor_stage_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        investor_stage_focus = _parse_investor_stage_focus(d.pop("investor_stage_focus"))

        def _parse_typical_check_size_min(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        typical_check_size_min = _parse_typical_check_size_min(d.pop("typical_check_size_min"))

        def _parse_typical_check_size_max(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        typical_check_size_max = _parse_typical_check_size_max(d.pop("typical_check_size_max"))

        def _parse_check_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_currency_id_type_0 = UUID(data)

                return check_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        check_currency_id = _parse_check_currency_id(d.pop("check_currency_id"))

        def _parse_sector_focus(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sector_focus_type_0 = cast(list[str], data)

                return sector_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        sector_focus = _parse_sector_focus(d.pop("sector_focus"))

        def _parse_geographic_focus(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                geographic_focus_type_0 = cast(list[str], data)

                return geographic_focus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        geographic_focus = _parse_geographic_focus(d.pop("geographic_focus"))

        def _parse_website_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website_url = _parse_website_url(d.pop("website_url"))

        def _parse_linkedin_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linkedin_url = _parse_linkedin_url(d.pop("linkedin_url"))

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

        status = d.pop("status")

        def _parse_threat_level_to_competitors(data: object) -> list[UUID] | None:
            if data is None:
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
            return cast(list[UUID] | None, data)

        threat_level_to_competitors = _parse_threat_level_to_competitors(d.pop("threat_level_to_competitors"))

        def _parse_notes(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        notes = _parse_notes(d.pop("notes"))

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

        def _parse_metadata(data: object) -> InvestorResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InvestorResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        investor_response = cls(
            id=id,
            org_id=org_id,
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
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        investor_response.additional_properties = d
        return investor_response

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
