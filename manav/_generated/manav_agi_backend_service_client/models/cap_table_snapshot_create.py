from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_table_snapshot_create_metadata_type_0 import CapTableSnapshotCreateMetadataType0


T = TypeVar("T", bound="CapTableSnapshotCreate")


@_attrs_define
class CapTableSnapshotCreate:
    """
    Attributes:
        legal_entity_id (UUID):
        as_of_date (datetime.date):
        snapshot_basis (str | Unset):  Default: 'current'.
        related_round_id (None | Unset | UUID):
        total_shares_issued (int | Unset):  Default: 0.
        total_shares_authorized (int | Unset):  Default: 0.
        option_pool_size (int | Unset):  Default: 0.
        option_pool_unallocated (int | Unset):  Default: 0.
        fully_diluted_shares (int | Unset):  Default: 0.
        notes (None | str | Unset):
        metadata (CapTableSnapshotCreateMetadataType0 | None | Unset):
    """

    legal_entity_id: UUID
    as_of_date: datetime.date
    snapshot_basis: str | Unset = "current"
    related_round_id: None | Unset | UUID = UNSET
    total_shares_issued: int | Unset = 0
    total_shares_authorized: int | Unset = 0
    option_pool_size: int | Unset = 0
    option_pool_unallocated: int | Unset = 0
    fully_diluted_shares: int | Unset = 0
    notes: None | str | Unset = UNSET
    metadata: CapTableSnapshotCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cap_table_snapshot_create_metadata_type_0 import (
            CapTableSnapshotCreateMetadataType0,  # noqa: PLC0415
        )

        legal_entity_id = str(self.legal_entity_id)

        as_of_date = self.as_of_date.isoformat()

        snapshot_basis = self.snapshot_basis

        related_round_id: None | str | Unset
        if isinstance(self.related_round_id, Unset):
            related_round_id = UNSET
        elif isinstance(self.related_round_id, UUID):
            related_round_id = str(self.related_round_id)
        else:
            related_round_id = self.related_round_id

        total_shares_issued = self.total_shares_issued

        total_shares_authorized = self.total_shares_authorized

        option_pool_size = self.option_pool_size

        option_pool_unallocated = self.option_pool_unallocated

        fully_diluted_shares = self.fully_diluted_shares

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CapTableSnapshotCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_entity_id": legal_entity_id,
                "as_of_date": as_of_date,
            }
        )
        if snapshot_basis is not UNSET:
            field_dict["snapshot_basis"] = snapshot_basis
        if related_round_id is not UNSET:
            field_dict["related_round_id"] = related_round_id
        if total_shares_issued is not UNSET:
            field_dict["total_shares_issued"] = total_shares_issued
        if total_shares_authorized is not UNSET:
            field_dict["total_shares_authorized"] = total_shares_authorized
        if option_pool_size is not UNSET:
            field_dict["option_pool_size"] = option_pool_size
        if option_pool_unallocated is not UNSET:
            field_dict["option_pool_unallocated"] = option_pool_unallocated
        if fully_diluted_shares is not UNSET:
            field_dict["fully_diluted_shares"] = fully_diluted_shares
        if notes is not UNSET:
            field_dict["notes"] = notes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cap_table_snapshot_create_metadata_type_0 import (
            CapTableSnapshotCreateMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        legal_entity_id = UUID(d.pop("legal_entity_id"))

        as_of_date = datetime.date.fromisoformat(d.pop("as_of_date"))

        snapshot_basis = d.pop("snapshot_basis", UNSET)

        def _parse_related_round_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_round_id_type_0 = UUID(data)

                return related_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        related_round_id = _parse_related_round_id(d.pop("related_round_id", UNSET))

        total_shares_issued = d.pop("total_shares_issued", UNSET)

        total_shares_authorized = d.pop("total_shares_authorized", UNSET)

        option_pool_size = d.pop("option_pool_size", UNSET)

        option_pool_unallocated = d.pop("option_pool_unallocated", UNSET)

        fully_diluted_shares = d.pop("fully_diluted_shares", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_metadata(data: object) -> CapTableSnapshotCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CapTableSnapshotCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableSnapshotCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        cap_table_snapshot_create = cls(
            legal_entity_id=legal_entity_id,
            as_of_date=as_of_date,
            snapshot_basis=snapshot_basis,
            related_round_id=related_round_id,
            total_shares_issued=total_shares_issued,
            total_shares_authorized=total_shares_authorized,
            option_pool_size=option_pool_size,
            option_pool_unallocated=option_pool_unallocated,
            fully_diluted_shares=fully_diluted_shares,
            notes=notes,
            metadata=metadata,
        )

        cap_table_snapshot_create.additional_properties = d
        return cap_table_snapshot_create

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
