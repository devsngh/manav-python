from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_commitment_create_metadata_type_0 import InvestorCommitmentCreateMetadataType0


T = TypeVar("T", bound="InvestorCommitmentCreate")


@_attrs_define
class InvestorCommitmentCreate:
    """
    Attributes:
        investor_id (UUID):
        committed_amount (float | str):
        committed_currency_id (UUID):
        commitment_status (str | Unset):  Default: 'verbal'.
        committed_at (datetime.datetime | None | Unset):
        shares_allocated (int | None | Unset):
        share_class (None | str | Unset):
        pro_rata_rights (bool | Unset):  Default: False.
        board_seat (bool | Unset):  Default: False.
        notes (None | str | Unset):
        metadata (InvestorCommitmentCreateMetadataType0 | None | Unset):
    """

    investor_id: UUID
    committed_amount: float | str
    committed_currency_id: UUID
    commitment_status: str | Unset = "verbal"
    committed_at: datetime.datetime | None | Unset = UNSET
    shares_allocated: int | None | Unset = UNSET
    share_class: None | str | Unset = UNSET
    pro_rata_rights: bool | Unset = False
    board_seat: bool | Unset = False
    notes: None | str | Unset = UNSET
    metadata: InvestorCommitmentCreateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_commitment_create_metadata_type_0 import (
            InvestorCommitmentCreateMetadataType0,  # noqa: PLC0415
        )

        investor_id = str(self.investor_id)

        committed_amount: float | str
        committed_amount = self.committed_amount

        committed_currency_id = str(self.committed_currency_id)

        commitment_status = self.commitment_status

        committed_at: None | str | Unset
        if isinstance(self.committed_at, Unset):
            committed_at = UNSET
        elif isinstance(self.committed_at, datetime.datetime):
            committed_at = self.committed_at.isoformat()
        else:
            committed_at = self.committed_at

        shares_allocated: int | None | Unset
        if isinstance(self.shares_allocated, Unset):
            shares_allocated = UNSET
        else:
            shares_allocated = self.shares_allocated

        share_class: None | str | Unset
        if isinstance(self.share_class, Unset):
            share_class = UNSET
        else:
            share_class = self.share_class

        pro_rata_rights = self.pro_rata_rights

        board_seat = self.board_seat

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InvestorCommitmentCreateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "investor_id": investor_id,
                "committed_amount": committed_amount,
                "committed_currency_id": committed_currency_id,
            }
        )
        if commitment_status is not UNSET:
            field_dict["commitment_status"] = commitment_status
        if committed_at is not UNSET:
            field_dict["committed_at"] = committed_at
        if shares_allocated is not UNSET:
            field_dict["shares_allocated"] = shares_allocated
        if share_class is not UNSET:
            field_dict["share_class"] = share_class
        if pro_rata_rights is not UNSET:
            field_dict["pro_rata_rights"] = pro_rata_rights
        if board_seat is not UNSET:
            field_dict["board_seat"] = board_seat
        if notes is not UNSET:
            field_dict["notes"] = notes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_commitment_create_metadata_type_0 import (
            InvestorCommitmentCreateMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        investor_id = UUID(d.pop("investor_id"))

        def _parse_committed_amount(data: object) -> float | str:
            return cast(float | str, data)

        committed_amount = _parse_committed_amount(d.pop("committed_amount"))

        committed_currency_id = UUID(d.pop("committed_currency_id"))

        commitment_status = d.pop("commitment_status", UNSET)

        def _parse_committed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_at_type_0 = datetime.datetime.fromisoformat(data)

                return committed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        committed_at = _parse_committed_at(d.pop("committed_at", UNSET))

        def _parse_shares_allocated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shares_allocated = _parse_shares_allocated(d.pop("shares_allocated", UNSET))

        def _parse_share_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_class = _parse_share_class(d.pop("share_class", UNSET))

        pro_rata_rights = d.pop("pro_rata_rights", UNSET)

        board_seat = d.pop("board_seat", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_metadata(data: object) -> InvestorCommitmentCreateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InvestorCommitmentCreateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorCommitmentCreateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        investor_commitment_create = cls(
            investor_id=investor_id,
            committed_amount=committed_amount,
            committed_currency_id=committed_currency_id,
            commitment_status=commitment_status,
            committed_at=committed_at,
            shares_allocated=shares_allocated,
            share_class=share_class,
            pro_rata_rights=pro_rata_rights,
            board_seat=board_seat,
            notes=notes,
            metadata=metadata,
        )

        investor_commitment_create.additional_properties = d
        return investor_commitment_create

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
