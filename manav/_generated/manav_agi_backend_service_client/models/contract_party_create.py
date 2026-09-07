from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractPartyCreate")


@_attrs_define
class ContractPartyCreate:
    """
    Attributes:
        party_role (str): first_party / second_party / guarantor / witness / trustee
        party_name (str):
        party_legal_entity_id (None | Unset | UUID):
        external_party_country (None | str | Unset):
        external_party_tax_id (None | str | Unset):
        signer_name (None | str | Unset):
        signer_title (None | str | Unset):
        signer_email (None | str | Unset):
        signed_at (datetime.datetime | None | Unset):
        signature_asset_id (None | Unset | UUID):
    """

    party_role: str
    party_name: str
    party_legal_entity_id: None | Unset | UUID = UNSET
    external_party_country: None | str | Unset = UNSET
    external_party_tax_id: None | str | Unset = UNSET
    signer_name: None | str | Unset = UNSET
    signer_title: None | str | Unset = UNSET
    signer_email: None | str | Unset = UNSET
    signed_at: datetime.datetime | None | Unset = UNSET
    signature_asset_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_role = self.party_role

        party_name = self.party_name

        party_legal_entity_id: None | str | Unset
        if isinstance(self.party_legal_entity_id, Unset):
            party_legal_entity_id = UNSET
        elif isinstance(self.party_legal_entity_id, UUID):
            party_legal_entity_id = str(self.party_legal_entity_id)
        else:
            party_legal_entity_id = self.party_legal_entity_id

        external_party_country: None | str | Unset
        if isinstance(self.external_party_country, Unset):
            external_party_country = UNSET
        else:
            external_party_country = self.external_party_country

        external_party_tax_id: None | str | Unset
        if isinstance(self.external_party_tax_id, Unset):
            external_party_tax_id = UNSET
        else:
            external_party_tax_id = self.external_party_tax_id

        signer_name: None | str | Unset
        if isinstance(self.signer_name, Unset):
            signer_name = UNSET
        else:
            signer_name = self.signer_name

        signer_title: None | str | Unset
        if isinstance(self.signer_title, Unset):
            signer_title = UNSET
        else:
            signer_title = self.signer_title

        signer_email: None | str | Unset
        if isinstance(self.signer_email, Unset):
            signer_email = UNSET
        else:
            signer_email = self.signer_email

        signed_at: None | str | Unset
        if isinstance(self.signed_at, Unset):
            signed_at = UNSET
        elif isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        signature_asset_id: None | str | Unset
        if isinstance(self.signature_asset_id, Unset):
            signature_asset_id = UNSET
        elif isinstance(self.signature_asset_id, UUID):
            signature_asset_id = str(self.signature_asset_id)
        else:
            signature_asset_id = self.signature_asset_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party_role": party_role,
                "party_name": party_name,
            }
        )
        if party_legal_entity_id is not UNSET:
            field_dict["party_legal_entity_id"] = party_legal_entity_id
        if external_party_country is not UNSET:
            field_dict["external_party_country"] = external_party_country
        if external_party_tax_id is not UNSET:
            field_dict["external_party_tax_id"] = external_party_tax_id
        if signer_name is not UNSET:
            field_dict["signer_name"] = signer_name
        if signer_title is not UNSET:
            field_dict["signer_title"] = signer_title
        if signer_email is not UNSET:
            field_dict["signer_email"] = signer_email
        if signed_at is not UNSET:
            field_dict["signed_at"] = signed_at
        if signature_asset_id is not UNSET:
            field_dict["signature_asset_id"] = signature_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party_role = d.pop("party_role")

        party_name = d.pop("party_name")

        def _parse_party_legal_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                party_legal_entity_id_type_0 = UUID(data)

                return party_legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        party_legal_entity_id = _parse_party_legal_entity_id(d.pop("party_legal_entity_id", UNSET))

        def _parse_external_party_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_party_country = _parse_external_party_country(d.pop("external_party_country", UNSET))

        def _parse_external_party_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_party_tax_id = _parse_external_party_tax_id(d.pop("external_party_tax_id", UNSET))

        def _parse_signer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signer_name = _parse_signer_name(d.pop("signer_name", UNSET))

        def _parse_signer_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signer_title = _parse_signer_title(d.pop("signer_title", UNSET))

        def _parse_signer_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signer_email = _parse_signer_email(d.pop("signer_email", UNSET))

        def _parse_signed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        signed_at = _parse_signed_at(d.pop("signed_at", UNSET))

        def _parse_signature_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signature_asset_id_type_0 = UUID(data)

                return signature_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        signature_asset_id = _parse_signature_asset_id(d.pop("signature_asset_id", UNSET))

        contract_party_create = cls(
            party_role=party_role,
            party_name=party_name,
            party_legal_entity_id=party_legal_entity_id,
            external_party_country=external_party_country,
            external_party_tax_id=external_party_tax_id,
            signer_name=signer_name,
            signer_title=signer_title,
            signer_email=signer_email,
            signed_at=signed_at,
            signature_asset_id=signature_asset_id,
        )

        contract_party_create.additional_properties = d
        return contract_party_create

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
