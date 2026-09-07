from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contract_response_metadata_type_0 import ContractResponseMetadataType0


T = TypeVar("T", bound="ContractResponse")


@_attrs_define
class ContractResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        contract_number (str):
        title (str):
        contract_type (str):
        status (str):
        effective_date (datetime.date | None):
        expiry_date (datetime.date | None):
        auto_renew (bool):
        notice_period_days (int | None):
        total_value (None | str):
        value_currency_id (None | UUID):
        governing_law_country (None | str):
        governing_law_jurisdiction (None | str):
        primary_document_asset_id (None | UUID):
        signed_document_asset_id (None | UUID):
        legal_entity_id (None | UUID):
        related_account_id (None | UUID):
        related_supplier_id (None | UUID):
        related_product_id (None | UUID):
        owner_user_id (None | UUID):
        owner_bot_id (None | UUID):
        signed_at (datetime.datetime | None):
        terminated_at (datetime.datetime | None):
        termination_reason (None | str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (ContractResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    contract_number: str
    title: str
    contract_type: str
    status: str
    effective_date: datetime.date | None
    expiry_date: datetime.date | None
    auto_renew: bool
    notice_period_days: int | None
    total_value: None | str
    value_currency_id: None | UUID
    governing_law_country: None | str
    governing_law_jurisdiction: None | str
    primary_document_asset_id: None | UUID
    signed_document_asset_id: None | UUID
    legal_entity_id: None | UUID
    related_account_id: None | UUID
    related_supplier_id: None | UUID
    related_product_id: None | UUID
    owner_user_id: None | UUID
    owner_bot_id: None | UUID
    signed_at: datetime.datetime | None
    terminated_at: datetime.datetime | None
    termination_reason: None | str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: ContractResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contract_response_metadata_type_0 import ContractResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        contract_number = self.contract_number

        title = self.title

        contract_type = self.contract_type

        status = self.status

        effective_date: None | str
        if isinstance(self.effective_date, datetime.date):
            effective_date = self.effective_date.isoformat()
        else:
            effective_date = self.effective_date

        expiry_date: None | str
        if isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        auto_renew = self.auto_renew

        notice_period_days: int | None
        notice_period_days = self.notice_period_days

        total_value: None | str
        total_value = self.total_value

        value_currency_id: None | str
        if isinstance(self.value_currency_id, UUID):
            value_currency_id = str(self.value_currency_id)
        else:
            value_currency_id = self.value_currency_id

        governing_law_country: None | str
        governing_law_country = self.governing_law_country

        governing_law_jurisdiction: None | str
        governing_law_jurisdiction = self.governing_law_jurisdiction

        primary_document_asset_id: None | str
        if isinstance(self.primary_document_asset_id, UUID):
            primary_document_asset_id = str(self.primary_document_asset_id)
        else:
            primary_document_asset_id = self.primary_document_asset_id

        signed_document_asset_id: None | str
        if isinstance(self.signed_document_asset_id, UUID):
            signed_document_asset_id = str(self.signed_document_asset_id)
        else:
            signed_document_asset_id = self.signed_document_asset_id

        legal_entity_id: None | str
        if isinstance(self.legal_entity_id, UUID):
            legal_entity_id = str(self.legal_entity_id)
        else:
            legal_entity_id = self.legal_entity_id

        related_account_id: None | str
        if isinstance(self.related_account_id, UUID):
            related_account_id = str(self.related_account_id)
        else:
            related_account_id = self.related_account_id

        related_supplier_id: None | str
        if isinstance(self.related_supplier_id, UUID):
            related_supplier_id = str(self.related_supplier_id)
        else:
            related_supplier_id = self.related_supplier_id

        related_product_id: None | str
        if isinstance(self.related_product_id, UUID):
            related_product_id = str(self.related_product_id)
        else:
            related_product_id = self.related_product_id

        owner_user_id: None | str
        if isinstance(self.owner_user_id, UUID):
            owner_user_id = str(self.owner_user_id)
        else:
            owner_user_id = self.owner_user_id

        owner_bot_id: None | str
        if isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        signed_at: None | str
        if isinstance(self.signed_at, datetime.datetime):
            signed_at = self.signed_at.isoformat()
        else:
            signed_at = self.signed_at

        terminated_at: None | str
        if isinstance(self.terminated_at, datetime.datetime):
            terminated_at = self.terminated_at.isoformat()
        else:
            terminated_at = self.terminated_at

        termination_reason: None | str
        termination_reason = self.termination_reason

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
        elif isinstance(self.metadata, ContractResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "contract_number": contract_number,
                "title": title,
                "contract_type": contract_type,
                "status": status,
                "effective_date": effective_date,
                "expiry_date": expiry_date,
                "auto_renew": auto_renew,
                "notice_period_days": notice_period_days,
                "total_value": total_value,
                "value_currency_id": value_currency_id,
                "governing_law_country": governing_law_country,
                "governing_law_jurisdiction": governing_law_jurisdiction,
                "primary_document_asset_id": primary_document_asset_id,
                "signed_document_asset_id": signed_document_asset_id,
                "legal_entity_id": legal_entity_id,
                "related_account_id": related_account_id,
                "related_supplier_id": related_supplier_id,
                "related_product_id": related_product_id,
                "owner_user_id": owner_user_id,
                "owner_bot_id": owner_bot_id,
                "signed_at": signed_at,
                "terminated_at": terminated_at,
                "termination_reason": termination_reason,
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
        from ..models.contract_response_metadata_type_0 import ContractResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        contract_number = d.pop("contract_number")

        title = d.pop("title")

        contract_type = d.pop("contract_type")

        status = d.pop("status")

        def _parse_effective_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_date_type_0 = datetime.date.fromisoformat(data)

                return effective_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        effective_date = _parse_effective_date(d.pop("effective_date"))

        def _parse_expiry_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = datetime.date.fromisoformat(data)

                return expiry_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date"))

        auto_renew = d.pop("auto_renew")

        def _parse_notice_period_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        notice_period_days = _parse_notice_period_days(d.pop("notice_period_days"))

        def _parse_total_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        def _parse_value_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_currency_id_type_0 = UUID(data)

                return value_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        value_currency_id = _parse_value_currency_id(d.pop("value_currency_id"))

        def _parse_governing_law_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        governing_law_country = _parse_governing_law_country(d.pop("governing_law_country"))

        def _parse_governing_law_jurisdiction(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        governing_law_jurisdiction = _parse_governing_law_jurisdiction(d.pop("governing_law_jurisdiction"))

        def _parse_primary_document_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                primary_document_asset_id_type_0 = UUID(data)

                return primary_document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        primary_document_asset_id = _parse_primary_document_asset_id(d.pop("primary_document_asset_id"))

        def _parse_signed_document_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signed_document_asset_id_type_0 = UUID(data)

                return signed_document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        signed_document_asset_id = _parse_signed_document_asset_id(d.pop("signed_document_asset_id"))

        def _parse_legal_entity_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                legal_entity_id_type_0 = UUID(data)

                return legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        legal_entity_id = _parse_legal_entity_id(d.pop("legal_entity_id"))

        def _parse_related_account_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_account_id_type_0 = UUID(data)

                return related_account_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        related_account_id = _parse_related_account_id(d.pop("related_account_id"))

        def _parse_related_supplier_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_supplier_id_type_0 = UUID(data)

                return related_supplier_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        related_supplier_id = _parse_related_supplier_id(d.pop("related_supplier_id"))

        def _parse_related_product_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_product_id_type_0 = UUID(data)

                return related_product_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        related_product_id = _parse_related_product_id(d.pop("related_product_id"))

        def _parse_owner_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_user_id_type_0 = UUID(data)

                return owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id"))

        def _parse_owner_bot_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id"))

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

        def _parse_terminated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                terminated_at_type_0 = datetime.datetime.fromisoformat(data)

                return terminated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        terminated_at = _parse_terminated_at(d.pop("terminated_at"))

        def _parse_termination_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        termination_reason = _parse_termination_reason(d.pop("termination_reason"))

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

        def _parse_metadata(data: object) -> ContractResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = ContractResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContractResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        contract_response = cls(
            id=id,
            org_id=org_id,
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
            signed_at=signed_at,
            terminated_at=terminated_at,
            termination_reason=termination_reason,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        contract_response.additional_properties = d
        return contract_response

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
