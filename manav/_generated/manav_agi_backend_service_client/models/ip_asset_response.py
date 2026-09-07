from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_asset_response_metadata_type_0 import IPAssetResponseMetadataType0


T = TypeVar("T", bound="IPAssetResponse")


@_attrs_define
class IPAssetResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        ip_type (str):
        name (str):
        description (None | str):
        jurisdiction (None | str):
        registration_number (None | str):
        filing_date (datetime.date | None):
        registration_date (datetime.date | None):
        expiry_date (datetime.date | None):
        status (str):
        owner_legal_entity_id (None | UUID):
        related_product_id (None | UUID):
        document_asset_id (None | UUID):
        created_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (IPAssetResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    ip_type: str
    name: str
    description: None | str
    jurisdiction: None | str
    registration_number: None | str
    filing_date: datetime.date | None
    registration_date: datetime.date | None
    expiry_date: datetime.date | None
    status: str
    owner_legal_entity_id: None | UUID
    related_product_id: None | UUID
    document_asset_id: None | UUID
    created_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: IPAssetResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_asset_response_metadata_type_0 import IPAssetResponseMetadataType0  # noqa: PLC0415

        id = str(self.id)

        org_id = str(self.org_id)

        ip_type = self.ip_type

        name = self.name

        description: None | str
        description = self.description

        jurisdiction: None | str
        jurisdiction = self.jurisdiction

        registration_number: None | str
        registration_number = self.registration_number

        filing_date: None | str
        if isinstance(self.filing_date, datetime.date):
            filing_date = self.filing_date.isoformat()
        else:
            filing_date = self.filing_date

        registration_date: None | str
        if isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        expiry_date: None | str
        if isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        status = self.status

        owner_legal_entity_id: None | str
        if isinstance(self.owner_legal_entity_id, UUID):
            owner_legal_entity_id = str(self.owner_legal_entity_id)
        else:
            owner_legal_entity_id = self.owner_legal_entity_id

        related_product_id: None | str
        if isinstance(self.related_product_id, UUID):
            related_product_id = str(self.related_product_id)
        else:
            related_product_id = self.related_product_id

        document_asset_id: None | str
        if isinstance(self.document_asset_id, UUID):
            document_asset_id = str(self.document_asset_id)
        else:
            document_asset_id = self.document_asset_id

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

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
        elif isinstance(self.metadata, IPAssetResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "ip_type": ip_type,
                "name": name,
                "description": description,
                "jurisdiction": jurisdiction,
                "registration_number": registration_number,
                "filing_date": filing_date,
                "registration_date": registration_date,
                "expiry_date": expiry_date,
                "status": status,
                "owner_legal_entity_id": owner_legal_entity_id,
                "related_product_id": related_product_id,
                "document_asset_id": document_asset_id,
                "created_by_bot_id": created_by_bot_id,
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
        from ..models.ip_asset_response_metadata_type_0 import IPAssetResponseMetadataType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        ip_type = d.pop("ip_type")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_jurisdiction(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        jurisdiction = _parse_jurisdiction(d.pop("jurisdiction"))

        def _parse_registration_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        registration_number = _parse_registration_number(d.pop("registration_number"))

        def _parse_filing_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filing_date_type_0 = datetime.date.fromisoformat(data)

                return filing_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        filing_date = _parse_filing_date(d.pop("filing_date"))

        def _parse_registration_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = datetime.date.fromisoformat(data)

                return registration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        registration_date = _parse_registration_date(d.pop("registration_date"))

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

        status = d.pop("status")

        def _parse_owner_legal_entity_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_legal_entity_id_type_0 = UUID(data)

                return owner_legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        owner_legal_entity_id = _parse_owner_legal_entity_id(d.pop("owner_legal_entity_id"))

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

        def _parse_document_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                document_asset_id_type_0 = UUID(data)

                return document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        document_asset_id = _parse_document_asset_id(d.pop("document_asset_id"))

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

        def _parse_metadata(data: object) -> IPAssetResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = IPAssetResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAssetResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        ip_asset_response = cls(
            id=id,
            org_id=org_id,
            ip_type=ip_type,
            name=name,
            description=description,
            jurisdiction=jurisdiction,
            registration_number=registration_number,
            filing_date=filing_date,
            registration_date=registration_date,
            expiry_date=expiry_date,
            status=status,
            owner_legal_entity_id=owner_legal_entity_id,
            related_product_id=related_product_id,
            document_asset_id=document_asset_id,
            created_by_bot_id=created_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        ip_asset_response.additional_properties = d
        return ip_asset_response

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
