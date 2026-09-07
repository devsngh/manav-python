from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract_update_metadata_type_0 import ContractUpdateMetadataType0


T = TypeVar("T", bound="ContractUpdate")


@_attrs_define
class ContractUpdate:
    """
    Attributes:
        contract_number (None | str | Unset):
        title (None | str | Unset):
        contract_type (None | str | Unset):
        status (None | str | Unset):
        effective_date (datetime.date | None | Unset):
        expiry_date (datetime.date | None | Unset):
        auto_renew (bool | None | Unset):
        notice_period_days (int | None | Unset):
        total_value (float | None | str | Unset):
        value_currency_id (None | Unset | UUID):
        governing_law_country (None | str | Unset):
        governing_law_jurisdiction (None | str | Unset):
        primary_document_asset_id (None | Unset | UUID):
        signed_document_asset_id (None | Unset | UUID):
        legal_entity_id (None | Unset | UUID):
        related_account_id (None | Unset | UUID):
        related_supplier_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_bot_id (None | Unset | UUID):
        metadata (ContractUpdateMetadataType0 | None | Unset):
    """

    contract_number: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    contract_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    effective_date: datetime.date | None | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    auto_renew: bool | None | Unset = UNSET
    notice_period_days: int | None | Unset = UNSET
    total_value: float | None | str | Unset = UNSET
    value_currency_id: None | Unset | UUID = UNSET
    governing_law_country: None | str | Unset = UNSET
    governing_law_jurisdiction: None | str | Unset = UNSET
    primary_document_asset_id: None | Unset | UUID = UNSET
    signed_document_asset_id: None | Unset | UUID = UNSET
    legal_entity_id: None | Unset | UUID = UNSET
    related_account_id: None | Unset | UUID = UNSET
    related_supplier_id: None | Unset | UUID = UNSET
    related_product_id: None | Unset | UUID = UNSET
    owner_user_id: None | Unset | UUID = UNSET
    owner_bot_id: None | Unset | UUID = UNSET
    metadata: ContractUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contract_update_metadata_type_0 import ContractUpdateMetadataType0  # noqa: PLC0415

        contract_number: None | str | Unset
        if isinstance(self.contract_number, Unset):
            contract_number = UNSET
        else:
            contract_number = self.contract_number

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        contract_type: None | str | Unset
        if isinstance(self.contract_type, Unset):
            contract_type = UNSET
        else:
            contract_type = self.contract_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        effective_date: None | str | Unset
        if isinstance(self.effective_date, Unset):
            effective_date = UNSET
        elif isinstance(self.effective_date, datetime.date):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        auto_renew: bool | None | Unset
        if isinstance(self.auto_renew, Unset):
            auto_renew = UNSET
        else:
            auto_renew = self.auto_renew

        notice_period_days: int | None | Unset
        if isinstance(self.notice_period_days, Unset):
            notice_period_days = UNSET
        else:
            notice_period_days = self.notice_period_days

        total_value: float | None | str | Unset
        if isinstance(self.total_value, Unset):
            total_value = UNSET
        else:
            total_value = self.total_value

        value_currency_id: None | str | Unset
        if isinstance(self.value_currency_id, Unset):
            value_currency_id = UNSET
        elif isinstance(self.value_currency_id, UUID):
            value_currency_id = str(self.value_currency_id)
        else:
            value_currency_id = self.value_currency_id

        governing_law_country: None | str | Unset
        if isinstance(self.governing_law_country, Unset):
            governing_law_country = UNSET
        else:
            governing_law_country = self.governing_law_country

        governing_law_jurisdiction: None | str | Unset
        if isinstance(self.governing_law_jurisdiction, Unset):
            governing_law_jurisdiction = UNSET
        else:
            governing_law_jurisdiction = self.governing_law_jurisdiction

        primary_document_asset_id: None | str | Unset
        if isinstance(self.primary_document_asset_id, Unset):
            primary_document_asset_id = UNSET
        elif isinstance(self.primary_document_asset_id, UUID):
            primary_document_asset_id = str(self.primary_document_asset_id)
        else:
            primary_document_asset_id = self.primary_document_asset_id

        signed_document_asset_id: None | str | Unset
        if isinstance(self.signed_document_asset_id, Unset):
            signed_document_asset_id = UNSET
        elif isinstance(self.signed_document_asset_id, UUID):
            signed_document_asset_id = str(self.signed_document_asset_id)
        else:
            signed_document_asset_id = self.signed_document_asset_id

        legal_entity_id: None | str | Unset
        if isinstance(self.legal_entity_id, Unset):
            legal_entity_id = UNSET
        elif isinstance(self.legal_entity_id, UUID):
            legal_entity_id = str(self.legal_entity_id)
        else:
            legal_entity_id = self.legal_entity_id

        related_account_id: None | str | Unset
        if isinstance(self.related_account_id, Unset):
            related_account_id = UNSET
        elif isinstance(self.related_account_id, UUID):
            related_account_id = str(self.related_account_id)
        else:
            related_account_id = self.related_account_id

        related_supplier_id: None | str | Unset
        if isinstance(self.related_supplier_id, Unset):
            related_supplier_id = UNSET
        elif isinstance(self.related_supplier_id, UUID):
            related_supplier_id = str(self.related_supplier_id)
        else:
            related_supplier_id = self.related_supplier_id

        related_product_id: None | str | Unset
        if isinstance(self.related_product_id, Unset):
            related_product_id = UNSET
        elif isinstance(self.related_product_id, UUID):
            related_product_id = str(self.related_product_id)
        else:
            related_product_id = self.related_product_id

        owner_user_id: None | str | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        elif isinstance(self.owner_user_id, UUID):
            owner_user_id = str(self.owner_user_id)
        else:
            owner_user_id = self.owner_user_id

        owner_bot_id: None | str | Unset
        if isinstance(self.owner_bot_id, Unset):
            owner_bot_id = UNSET
        elif isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, ContractUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contract_number is not UNSET:
            field_dict["contract_number"] = contract_number
        if title is not UNSET:
            field_dict["title"] = title
        if contract_type is not UNSET:
            field_dict["contract_type"] = contract_type
        if status is not UNSET:
            field_dict["status"] = status
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if auto_renew is not UNSET:
            field_dict["auto_renew"] = auto_renew
        if notice_period_days is not UNSET:
            field_dict["notice_period_days"] = notice_period_days
        if total_value is not UNSET:
            field_dict["total_value"] = total_value
        if value_currency_id is not UNSET:
            field_dict["value_currency_id"] = value_currency_id
        if governing_law_country is not UNSET:
            field_dict["governing_law_country"] = governing_law_country
        if governing_law_jurisdiction is not UNSET:
            field_dict["governing_law_jurisdiction"] = governing_law_jurisdiction
        if primary_document_asset_id is not UNSET:
            field_dict["primary_document_asset_id"] = primary_document_asset_id
        if signed_document_asset_id is not UNSET:
            field_dict["signed_document_asset_id"] = signed_document_asset_id
        if legal_entity_id is not UNSET:
            field_dict["legal_entity_id"] = legal_entity_id
        if related_account_id is not UNSET:
            field_dict["related_account_id"] = related_account_id
        if related_supplier_id is not UNSET:
            field_dict["related_supplier_id"] = related_supplier_id
        if related_product_id is not UNSET:
            field_dict["related_product_id"] = related_product_id
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if owner_bot_id is not UNSET:
            field_dict["owner_bot_id"] = owner_bot_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contract_update_metadata_type_0 import ContractUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_contract_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_number = _parse_contract_number(d.pop("contract_number", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_contract_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_type = _parse_contract_type(d.pop("contract_type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_effective_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = datetime.date.fromisoformat(data)

                return effective_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        effective_date = _parse_effective_date(d.pop("effective_date", UNSET))

        def _parse_expiry_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        def _parse_auto_renew(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_renew = _parse_auto_renew(d.pop("auto_renew", UNSET))

        def _parse_notice_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        notice_period_days = _parse_notice_period_days(d.pop("notice_period_days", UNSET))

        def _parse_total_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_value = _parse_total_value(d.pop("total_value", UNSET))

        def _parse_value_currency_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_currency_id_type_0 = UUID(data)

                return value_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        value_currency_id = _parse_value_currency_id(d.pop("value_currency_id", UNSET))

        def _parse_governing_law_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        governing_law_country = _parse_governing_law_country(d.pop("governing_law_country", UNSET))

        def _parse_governing_law_jurisdiction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        governing_law_jurisdiction = _parse_governing_law_jurisdiction(d.pop("governing_law_jurisdiction", UNSET))

        def _parse_primary_document_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_document_asset_id_type_0 = UUID(data)

                return primary_document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        primary_document_asset_id = _parse_primary_document_asset_id(d.pop("primary_document_asset_id", UNSET))

        def _parse_signed_document_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_document_asset_id_type_0 = UUID(data)

                return signed_document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        signed_document_asset_id = _parse_signed_document_asset_id(d.pop("signed_document_asset_id", UNSET))

        def _parse_legal_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legal_entity_id_type_0 = UUID(data)

                return legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        legal_entity_id = _parse_legal_entity_id(d.pop("legal_entity_id", UNSET))

        def _parse_related_account_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_account_id_type_0 = UUID(data)

                return related_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_account_id = _parse_related_account_id(d.pop("related_account_id", UNSET))

        def _parse_related_supplier_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_supplier_id_type_0 = UUID(data)

                return related_supplier_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_supplier_id = _parse_related_supplier_id(d.pop("related_supplier_id", UNSET))

        def _parse_related_product_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_product_id_type_0 = UUID(data)

                return related_product_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_product_id = _parse_related_product_id(d.pop("related_product_id", UNSET))

        def _parse_owner_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_user_id_type_0 = UUID(data)

                return owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        def _parse_owner_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id", UNSET))

        def _parse_metadata(data: object) -> ContractUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ContractUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContractUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        contract_update = cls(
            contract_number=contract_number,
            title=title,
            contract_type=contract_type,
            status=status,
            effective_date=effective_date,
            expiry_date=expiry_date,
            auto_renew=auto_renew,
            notice_period_days=notice_period_days,
            total_value=total_value,
            value_currency_id=value_currency_id,
            governing_law_country=governing_law_country,
            governing_law_jurisdiction=governing_law_jurisdiction,
            primary_document_asset_id=primary_document_asset_id,
            signed_document_asset_id=signed_document_asset_id,
            legal_entity_id=legal_entity_id,
            related_account_id=related_account_id,
            related_supplier_id=related_supplier_id,
            related_product_id=related_product_id,
            owner_user_id=owner_user_id,
            owner_bot_id=owner_bot_id,
            metadata=metadata,
        )

        contract_update.additional_properties = d
        return contract_update

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
