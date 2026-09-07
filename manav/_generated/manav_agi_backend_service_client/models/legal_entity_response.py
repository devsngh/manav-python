from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LegalEntityResponse")


@_attrs_define
class LegalEntityResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        code (str):
        name (str):
        legal_name (str):
        country_code (str):
        registration_number (None | str):
        tax_id (None | str):
        base_currency_id (UUID):
        functional_currency_id (None | UUID):
        reporting_currency_id (None | UUID):
        parent_entity_id (None | UUID):
        entity_type (None | str):
        fiscal_year_end_month (int | None):
        is_consolidated (bool):
        status (str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
    """

    id: UUID
    org_id: UUID
    code: str
    name: str
    legal_name: str
    country_code: str
    registration_number: None | str
    tax_id: None | str
    base_currency_id: UUID
    functional_currency_id: None | UUID
    reporting_currency_id: None | UUID
    parent_entity_id: None | UUID
    entity_type: None | str
    fiscal_year_end_month: int | None
    is_consolidated: bool
    status: str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        org_id = str(self.org_id)

        code = self.code

        name = self.name

        legal_name = self.legal_name

        country_code = self.country_code

        registration_number: None | str
        registration_number = self.registration_number

        tax_id: None | str
        tax_id = self.tax_id

        base_currency_id = str(self.base_currency_id)

        functional_currency_id: None | str
        if isinstance(self.functional_currency_id, UUID):
            functional_currency_id = str(self.functional_currency_id)
        else:
            functional_currency_id = self.functional_currency_id

        reporting_currency_id: None | str
        if isinstance(self.reporting_currency_id, UUID):
            reporting_currency_id = str(self.reporting_currency_id)
        else:
            reporting_currency_id = self.reporting_currency_id

        parent_entity_id: None | str
        if isinstance(self.parent_entity_id, UUID):
            parent_entity_id = str(self.parent_entity_id)
        else:
            parent_entity_id = self.parent_entity_id

        entity_type: None | str
        entity_type = self.entity_type

        fiscal_year_end_month: int | None
        fiscal_year_end_month = self.fiscal_year_end_month

        is_consolidated = self.is_consolidated

        status = self.status

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "code": code,
                "name": name,
                "legal_name": legal_name,
                "country_code": country_code,
                "registration_number": registration_number,
                "tax_id": tax_id,
                "base_currency_id": base_currency_id,
                "functional_currency_id": functional_currency_id,
                "reporting_currency_id": reporting_currency_id,
                "parent_entity_id": parent_entity_id,
                "entity_type": entity_type,
                "fiscal_year_end_month": fiscal_year_end_month,
                "is_consolidated": is_consolidated,
                "status": status,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "last_modified_by_bot_id": last_modified_by_bot_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        code = d.pop("code")

        name = d.pop("name")

        legal_name = d.pop("legal_name")

        country_code = d.pop("country_code")

        def _parse_registration_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registration_number = _parse_registration_number(d.pop("registration_number"))

        def _parse_tax_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tax_id = _parse_tax_id(d.pop("tax_id"))

        base_currency_id = UUID(d.pop("base_currency_id"))

        def _parse_functional_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functional_currency_id_type_0 = UUID(data)

                return functional_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        functional_currency_id = _parse_functional_currency_id(d.pop("functional_currency_id"))

        def _parse_reporting_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reporting_currency_id_type_0 = UUID(data)

                return reporting_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        reporting_currency_id = _parse_reporting_currency_id(d.pop("reporting_currency_id"))

        def _parse_parent_entity_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_entity_id_type_0 = UUID(data)

                return parent_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        parent_entity_id = _parse_parent_entity_id(d.pop("parent_entity_id"))

        def _parse_entity_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        entity_type = _parse_entity_type(d.pop("entity_type"))

        def _parse_fiscal_year_end_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        fiscal_year_end_month = _parse_fiscal_year_end_month(d.pop("fiscal_year_end_month"))

        is_consolidated = d.pop("is_consolidated")

        status = d.pop("status")

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

        legal_entity_response = cls(
            id=id,
            org_id=org_id,
            code=code,
            name=name,
            legal_name=legal_name,
            country_code=country_code,
            registration_number=registration_number,
            tax_id=tax_id,
            base_currency_id=base_currency_id,
            functional_currency_id=functional_currency_id,
            reporting_currency_id=reporting_currency_id,
            parent_entity_id=parent_entity_id,
            entity_type=entity_type,
            fiscal_year_end_month=fiscal_year_end_month,
            is_consolidated=is_consolidated,
            status=status,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        legal_entity_response.additional_properties = d
        return legal_entity_response

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
