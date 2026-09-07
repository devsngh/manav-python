from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContractPartyResponse")


@_attrs_define
class ContractPartyResponse:
    """
    Attributes:
        id (UUID):
        contract_id (UUID):
        party_role (str):
        party_name (str):
        party_legal_entity_id (None | UUID):
        external_party_country (None | str):
        external_party_tax_id (None | str):
        signer_name (None | str):
        signer_title (None | str):
        signer_email (None | str):
        signed_at (datetime.datetime | None):
        signature_asset_id (None | UUID):
        created_at (datetime.datetime):
    """

    id: UUID
    contract_id: UUID
    party_role: str
    party_name: str
    party_legal_entity_id: None | UUID
    external_party_country: None | str
    external_party_tax_id: None | str
    signer_name: None | str
    signer_title: None | str
    signer_email: None | str
    signed_at: datetime.datetime | None
    signature_asset_id: None | UUID
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        contract_id = str(self.contract_id)

        party_role = self.party_role

        party_name = self.party_name

        party_legal_entity_id: None | str
        if isinstance(self.party_legal_entity_id, UUID):
            party_legal_entity_id = str(self.party_legal_entity_id)
        else:
            party_legal_entity_id = self.party_legal_entity_id

        external_party_country: None | str
        external_party_country = self.external_party_country

        external_party_tax_id: None | str
        external_party_tax_id = self.external_party_tax_id

        signer_name: None | str
        signer_name = self.signer_name

        signer_title: None | str
        signer_title = self.signer_title

        signer_email: None | str
        signer_email = self.signer_email

        signed_at: None | str
        if isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        signature_asset_id: None | str
        if isinstance(self.signature_asset_id, UUID):
            signature_asset_id = str(self.signature_asset_id)
        else:
            signature_asset_id = self.signature_asset_id

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contract_id": contract_id,
                "party_role": party_role,
                "party_name": party_name,
                "party_legal_entity_id": party_legal_entity_id,
                "external_party_country": external_party_country,
                "external_party_tax_id": external_party_tax_id,
                "signer_name": signer_name,
                "signer_title": signer_title,
                "signer_email": signer_email,
                "signed_at": signed_at,
                "signature_asset_id": signature_asset_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        contract_id = UUID(d.pop("contract_id"))

        party_role = d.pop("party_role")

        party_name = d.pop("party_name")

        def _parse_party_legal_entity_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                party_legal_entity_id_type_0 = UUID(data)

                return party_legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        party_legal_entity_id = _parse_party_legal_entity_id(d.pop("party_legal_entity_id"))

        def _parse_external_party_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_party_country = _parse_external_party_country(d.pop("external_party_country"))

        def _parse_external_party_tax_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_party_tax_id = _parse_external_party_tax_id(d.pop("external_party_tax_id"))

        def _parse_signer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signer_name = _parse_signer_name(d.pop("signer_name"))

        def _parse_signer_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signer_title = _parse_signer_title(d.pop("signer_title"))

        def _parse_signer_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signer_email = _parse_signer_email(d.pop("signer_email"))

        def _parse_signed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        signed_at = _parse_signed_at(d.pop("signed_at"))

        def _parse_signature_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signature_asset_id_type_0 = UUID(data)

                return signature_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        signature_asset_id = _parse_signature_asset_id(d.pop("signature_asset_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        contract_party_response = cls(
            id=id,
            contract_id=contract_id,
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
            created_at=created_at,
        )

        contract_party_response.additional_properties = d
        return contract_party_response

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
