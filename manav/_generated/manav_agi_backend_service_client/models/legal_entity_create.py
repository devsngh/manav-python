from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalEntityCreate")


@_attrs_define
class LegalEntityCreate:
    """
    Attributes:
        code (str):
        name (str):
        legal_name (str):
        country_code (str):
        base_currency_id (UUID):
        registration_number (None | str | Unset):
        tax_id (None | str | Unset):
        functional_currency_id (None | Unset | UUID):
        reporting_currency_id (None | Unset | UUID):
        parent_entity_id (None | Unset | UUID):
        entity_type (None | str | Unset):
        fiscal_year_end_month (int | None | Unset):
        is_consolidated (bool | Unset):  Default: True.
        status (str | Unset):  Default: 'active'.
    """

    code: str
    name: str
    legal_name: str
    country_code: str
    base_currency_id: UUID
    registration_number: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    functional_currency_id: None | Unset | UUID = UNSET
    reporting_currency_id: None | Unset | UUID = UNSET
    parent_entity_id: None | Unset | UUID = UNSET
    entity_type: None | str | Unset = UNSET
    fiscal_year_end_month: int | None | Unset = UNSET
    is_consolidated: bool | Unset = True
    status: str | Unset = "active"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        legal_name = self.legal_name

        country_code = self.country_code

        base_currency_id = str(self.base_currency_id)

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

        functional_currency_id: None | str | Unset
        if isinstance(self.functional_currency_id, Unset):
            functional_currency_id = UNSET
        elif isinstance(self.functional_currency_id, UUID):
            functional_currency_id = str(self.functional_currency_id)
        else:
            functional_currency_id = self.functional_currency_id

        reporting_currency_id: None | str | Unset
        if isinstance(self.reporting_currency_id, Unset):
            reporting_currency_id = UNSET
        elif isinstance(self.reporting_currency_id, UUID):
            reporting_currency_id = str(self.reporting_currency_id)
        else:
            reporting_currency_id = self.reporting_currency_id

        parent_entity_id: None | str | Unset
        if isinstance(self.parent_entity_id, Unset):
            parent_entity_id = UNSET
        elif isinstance(self.parent_entity_id, UUID):
            parent_entity_id = str(self.parent_entity_id)
        else:
            parent_entity_id = self.parent_entity_id

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        fiscal_year_end_month: int | None | Unset
        if isinstance(self.fiscal_year_end_month, Unset):
            fiscal_year_end_month = UNSET
        else:
            fiscal_year_end_month = self.fiscal_year_end_month

        is_consolidated = self.is_consolidated

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "legal_name": legal_name,
                "country_code": country_code,
                "base_currency_id": base_currency_id,
            }
        )
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if functional_currency_id is not UNSET:
            field_dict["functional_currency_id"] = functional_currency_id
        if reporting_currency_id is not UNSET:
            field_dict["reporting_currency_id"] = reporting_currency_id
        if parent_entity_id is not UNSET:
            field_dict["parent_entity_id"] = parent_entity_id
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if fiscal_year_end_month is not UNSET:
            field_dict["fiscal_year_end_month"] = fiscal_year_end_month
        if is_consolidated is not UNSET:
            field_dict["is_consolidated"] = is_consolidated
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        legal_name = d.pop("legal_name")

        country_code = d.pop("country_code")

        base_currency_id = UUID(d.pop("base_currency_id"))

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

        def _parse_functional_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                functional_currency_id_type_0 = UUID(data)

                return functional_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        functional_currency_id = _parse_functional_currency_id(d.pop("functional_currency_id", UNSET))

        def _parse_reporting_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reporting_currency_id_type_0 = UUID(data)

                return reporting_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        reporting_currency_id = _parse_reporting_currency_id(d.pop("reporting_currency_id", UNSET))

        def _parse_parent_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_entity_id_type_0 = UUID(data)

                return parent_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_entity_id = _parse_parent_entity_id(d.pop("parent_entity_id", UNSET))

        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

        def _parse_fiscal_year_end_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fiscal_year_end_month = _parse_fiscal_year_end_month(d.pop("fiscal_year_end_month", UNSET))

        is_consolidated = d.pop("is_consolidated", UNSET)

        status = d.pop("status", UNSET)

        legal_entity_create = cls(
            code=code,
            name=name,
            legal_name=legal_name,
            country_code=country_code,
            base_currency_id=base_currency_id,
            registration_number=registration_number,
            tax_id=tax_id,
            functional_currency_id=functional_currency_id,
            reporting_currency_id=reporting_currency_id,
            parent_entity_id=parent_entity_id,
            entity_type=entity_type,
            fiscal_year_end_month=fiscal_year_end_month,
            is_consolidated=is_consolidated,
            status=status,
        )

        legal_entity_create.additional_properties = d
        return legal_entity_create

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
