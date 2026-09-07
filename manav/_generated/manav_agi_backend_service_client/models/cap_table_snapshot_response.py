from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cap_table_snapshot_response_metadata_type_0 import CapTableSnapshotResponseMetadataType0


T = TypeVar("T", bound="CapTableSnapshotResponse")


@_attrs_define
class CapTableSnapshotResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        legal_entity_id (UUID):
        as_of_date (datetime.date):
        snapshot_basis (str):
        related_round_id (None | UUID):
        total_shares_issued (int):
        total_shares_authorized (int):
        option_pool_size (int):
        option_pool_unallocated (int):
        fully_diluted_shares (int):
        notes (None | str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        created_at (datetime.datetime):
        metadata (CapTableSnapshotResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    legal_entity_id: UUID
    as_of_date: datetime.date
    snapshot_basis: str
    related_round_id: None | UUID
    total_shares_issued: int
    total_shares_authorized: int
    option_pool_size: int
    option_pool_unallocated: int
    fully_diluted_shares: int
    notes: None | str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    created_at: datetime.datetime
    metadata: CapTableSnapshotResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cap_table_snapshot_response_metadata_type_0 import (
            CapTableSnapshotResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        legal_entity_id = str(self.legal_entity_id)

        as_of_date = self.as_of_date.isoformat()

        snapshot_basis = self.snapshot_basis

        related_round_id: None | str
        if isinstance(self.related_round_id, UUID):
            related_round_id = str(self.related_round_id)
        else:
            related_round_id = self.related_round_id

        total_shares_issued = self.total_shares_issued

        total_shares_authorized = self.total_shares_authorized

        option_pool_size = self.option_pool_size

        option_pool_unallocated = self.option_pool_unallocated

        fully_diluted_shares = self.fully_diluted_shares

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

        created_at = self.created_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CapTableSnapshotResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "legal_entity_id": legal_entity_id,
                "as_of_date": as_of_date,
                "snapshot_basis": snapshot_basis,
                "related_round_id": related_round_id,
                "total_shares_issued": total_shares_issued,
                "total_shares_authorized": total_shares_authorized,
                "option_pool_size": option_pool_size,
                "option_pool_unallocated": option_pool_unallocated,
                "fully_diluted_shares": fully_diluted_shares,
                "notes": notes,
                "created_by_bot_id": created_by_bot_id,
                "approved_by_user_id": approved_by_user_id,
                "created_at": created_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cap_table_snapshot_response_metadata_type_0 import (
            CapTableSnapshotResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        legal_entity_id = UUID(d.pop("legal_entity_id"))

        as_of_date = datetime.date.fromisoformat(d.pop("as_of_date"))

        snapshot_basis = d.pop("snapshot_basis")

        def _parse_related_round_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                related_round_id_type_0 = UUID(data)

                return related_round_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        related_round_id = _parse_related_round_id(d.pop("related_round_id"))

        total_shares_issued = d.pop("total_shares_issued")

        total_shares_authorized = d.pop("total_shares_authorized")

        option_pool_size = d.pop("option_pool_size")

        option_pool_unallocated = d.pop("option_pool_unallocated")

        fully_diluted_shares = d.pop("fully_diluted_shares")

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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_metadata(data: object) -> CapTableSnapshotResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CapTableSnapshotResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CapTableSnapshotResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        cap_table_snapshot_response = cls(
            id=id,
            org_id=org_id,
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
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            created_at=created_at,
            metadata=metadata,
        )

        cap_table_snapshot_response.additional_properties = d
        return cap_table_snapshot_response

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
