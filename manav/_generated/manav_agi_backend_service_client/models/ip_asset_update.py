from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_asset_update_metadata_type_0 import IPAssetUpdateMetadataType0


T = TypeVar("T", bound="IPAssetUpdate")


@_attrs_define
class IPAssetUpdate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        jurisdiction (None | str | Unset):
        registration_number (None | str | Unset):
        filing_date (datetime.date | None | Unset):
        registration_date (datetime.date | None | Unset):
        expiry_date (datetime.date | None | Unset):
        status (None | str | Unset):
        owner_legal_entity_id (None | Unset | UUID):
        related_product_id (None | Unset | UUID):
        document_asset_id (None | Unset | UUID):
        metadata (IPAssetUpdateMetadataType0 | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    jurisdiction: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    filing_date: datetime.date | None | Unset = UNSET
    registration_date: datetime.date | None | Unset = UNSET
    expiry_date: datetime.date | None | Unset = UNSET
    status: None | str | Unset = UNSET
    owner_legal_entity_id: None | Unset | UUID = UNSET
    related_product_id: None | Unset | UUID = UNSET
    document_asset_id: None | Unset | UUID = UNSET
    metadata: IPAssetUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ip_asset_update_metadata_type_0 import IPAssetUpdateMetadataType0  # noqa: PLC0415

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        jurisdiction: None | str | Unset
        if isinstance(self.jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = self.jurisdiction

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        filing_date: None | str | Unset
        if isinstance(self.filing_date, Unset):
            filing_date = UNSET
        elif isinstance(self.filing_date, datetime.date):
            filing_date = self.filing_date.isoformat()
        else:
            filing_date = self.filing_date

        registration_date: None | str | Unset
        if isinstance(self.registration_date, Unset):
            registration_date = UNSET
        elif isinstance(self.registration_date, datetime.date):
            registration_date = self.registration_date.isoformat()
        else:
            registration_date = self.registration_date

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        owner_legal_entity_id: None | str | Unset
        if isinstance(self.owner_legal_entity_id, Unset):
            owner_legal_entity_id = UNSET
        elif isinstance(self.owner_legal_entity_id, UUID):
            owner_legal_entity_id = str(self.owner_legal_entity_id)
        else:
            owner_legal_entity_id = self.owner_legal_entity_id

        related_product_id: None | str | Unset
        if isinstance(self.related_product_id, Unset):
            related_product_id = UNSET
        elif isinstance(self.related_product_id, UUID):
            related_product_id = str(self.related_product_id)
        else:
            related_product_id = self.related_product_id

        document_asset_id: None | str | Unset
        if isinstance(self.document_asset_id, Unset):
            document_asset_id = UNSET
        elif isinstance(self.document_asset_id, UUID):
            document_asset_id = str(self.document_asset_id)
        else:
            document_asset_id = self.document_asset_id

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, IPAssetUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if filing_date is not UNSET:
            field_dict["filing_date"] = filing_date
        if registration_date is not UNSET:
            field_dict["registration_date"] = registration_date
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if status is not UNSET:
            field_dict["status"] = status
        if owner_legal_entity_id is not UNSET:
            field_dict["owner_legal_entity_id"] = owner_legal_entity_id
        if related_product_id is not UNSET:
            field_dict["related_product_id"] = related_product_id
        if document_asset_id is not UNSET:
            field_dict["document_asset_id"] = document_asset_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_asset_update_metadata_type_0 import IPAssetUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_jurisdiction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jurisdiction = _parse_jurisdiction(d.pop("jurisdiction", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(d.pop("registration_number", UNSET))

        def _parse_filing_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                filing_date_type_0 = datetime.date.fromisoformat(data)

                return filing_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        filing_date = _parse_filing_date(d.pop("filing_date", UNSET))

        def _parse_registration_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                registration_date_type_0 = datetime.date.fromisoformat(data)

                return registration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        registration_date = _parse_registration_date(d.pop("registration_date", UNSET))

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

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_owner_legal_entity_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_legal_entity_id_type_0 = UUID(data)

                return owner_legal_entity_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_legal_entity_id = _parse_owner_legal_entity_id(d.pop("owner_legal_entity_id", UNSET))

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

        def _parse_document_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                document_asset_id_type_0 = UUID(data)

                return document_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        document_asset_id = _parse_document_asset_id(d.pop("document_asset_id", UNSET))

        def _parse_metadata(data: object) -> IPAssetUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = IPAssetUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IPAssetUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        ip_asset_update = cls(
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
            metadata=metadata,
        )

        ip_asset_update.additional_properties = d
        return ip_asset_update

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
