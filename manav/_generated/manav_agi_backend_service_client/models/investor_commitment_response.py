from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investor_commitment_response_metadata_type_0 import InvestorCommitmentResponseMetadataType0


T = TypeVar("T", bound="InvestorCommitmentResponse")


@_attrs_define
class InvestorCommitmentResponse:
    """
    Attributes:
        id (UUID):
        fundraise_round_id (UUID):
        investor_id (UUID):
        committed_amount (str):
        committed_currency_id (UUID):
        commitment_status (str):
        committed_at (datetime.datetime | None):
        wired_at (datetime.datetime | None):
        wired_amount (None | str):
        shares_allocated (int | None):
        share_class (None | str):
        term_sheet_signed_at (datetime.datetime | None):
        term_sheet_asset_id (None | UUID):
        subscription_doc_signed_at (datetime.datetime | None):
        subscription_doc_asset_id (None | UUID):
        pro_rata_rights (bool):
        board_seat (bool):
        notes (None | str):
        created_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        metadata (InvestorCommitmentResponseMetadataType0 | None | Unset):
    """

    id: UUID
    fundraise_round_id: UUID
    investor_id: UUID
    committed_amount: str
    committed_currency_id: UUID
    commitment_status: str
    committed_at: datetime.datetime | None
    wired_at: datetime.datetime | None
    wired_amount: None | str
    shares_allocated: int | None
    share_class: None | str
    term_sheet_signed_at: datetime.datetime | None
    term_sheet_asset_id: None | UUID
    subscription_doc_signed_at: datetime.datetime | None
    subscription_doc_asset_id: None | UUID
    pro_rata_rights: bool
    board_seat: bool
    notes: None | str
    created_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata: InvestorCommitmentResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.investor_commitment_response_metadata_type_0 import (
            InvestorCommitmentResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        fundraise_round_id = str(self.fundraise_round_id)

        investor_id = str(self.investor_id)

        committed_amount = self.committed_amount

        committed_currency_id = str(self.committed_currency_id)

        commitment_status = self.commitment_status

        committed_at: None | str
        if isinstance(self.committed_at, datetime.datetime):
            committed_at = self.committed_at.isoformat()
        else:
            committed_at = self.committed_at

        wired_at: None | str
        if isinstance(self.wired_at, datetime.datetime):
            wired_at = self.wired_at.isoformat()
        else:
            wired_at = self.wired_at

        wired_amount: None | str
        wired_amount = self.wired_amount

        shares_allocated: int | None
        shares_allocated = self.shares_allocated

        share_class: None | str
        share_class = self.share_class

        term_sheet_signed_at: None | str
        if isinstance(self.term_sheet_signed_at, datetime.datetime):
            term_sheet_signed_at = self.term_sheet_signed_at.isoformat()
        else:
            term_sheet_signed_at = self.term_sheet_signed_at

        term_sheet_asset_id: None | str
        if isinstance(self.term_sheet_asset_id, UUID):
            term_sheet_asset_id = str(self.term_sheet_asset_id)
        else:
            term_sheet_asset_id = self.term_sheet_asset_id

        subscription_doc_signed_at: None | str
        if isinstance(self.subscription_doc_signed_at, datetime.datetime):
            subscription_doc_signed_at = self.subscription_doc_signed_at.isoformat()
        else:
            subscription_doc_signed_at = self.subscription_doc_signed_at

        subscription_doc_asset_id: None | str
        if isinstance(self.subscription_doc_asset_id, UUID):
            subscription_doc_asset_id = str(self.subscription_doc_asset_id)
        else:
            subscription_doc_asset_id = self.subscription_doc_asset_id

        pro_rata_rights = self.pro_rata_rights

        board_seat = self.board_seat

        notes: None | str
        notes = self.notes

        created_by_bot_id: None | str
        if isinstance(self.created_by_bot_id, UUID):
            created_by_bot_id = str(self.created_by_bot_id)
        else:
            created_by_bot_id = self.created_by_bot_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, InvestorCommitmentResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fundraise_round_id": fundraise_round_id,
                "investor_id": investor_id,
                "committed_amount": committed_amount,
                "committed_currency_id": committed_currency_id,
                "commitment_status": commitment_status,
                "committed_at": committed_at,
                "wired_at": wired_at,
                "wired_amount": wired_amount,
                "shares_allocated": shares_allocated,
                "share_class": share_class,
                "term_sheet_signed_at": term_sheet_signed_at,
                "term_sheet_asset_id": term_sheet_asset_id,
                "subscription_doc_signed_at": subscription_doc_signed_at,
                "subscription_doc_asset_id": subscription_doc_asset_id,
                "pro_rata_rights": pro_rata_rights,
                "board_seat": board_seat,
                "notes": notes,
                "created_by_bot_id": created_by_bot_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investor_commitment_response_metadata_type_0 import (
            InvestorCommitmentResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        fundraise_round_id = UUID(d.pop("fundraise_round_id"))

        investor_id = UUID(d.pop("investor_id"))

        committed_amount = d.pop("committed_amount")

        committed_currency_id = UUID(d.pop("committed_currency_id"))

        commitment_status = d.pop("commitment_status")

        def _parse_committed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                committed_at_type_0 = datetime.datetime.fromisoformat(data)

                return committed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        committed_at = _parse_committed_at(d.pop("committed_at"))

        def _parse_wired_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wired_at_type_0 = datetime.datetime.fromisoformat(data)

                return wired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        wired_at = _parse_wired_at(d.pop("wired_at"))

        def _parse_wired_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        wired_amount = _parse_wired_amount(d.pop("wired_amount"))

        def _parse_shares_allocated(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        shares_allocated = _parse_shares_allocated(d.pop("shares_allocated"))

        def _parse_share_class(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        share_class = _parse_share_class(d.pop("share_class"))

        def _parse_term_sheet_signed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_sheet_signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return term_sheet_signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        term_sheet_signed_at = _parse_term_sheet_signed_at(d.pop("term_sheet_signed_at"))

        def _parse_term_sheet_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_sheet_asset_id_type_0 = UUID(data)

                return term_sheet_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        term_sheet_asset_id = _parse_term_sheet_asset_id(d.pop("term_sheet_asset_id"))

        def _parse_subscription_doc_signed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_doc_signed_at_type_0 = datetime.datetime.fromisoformat(data)

                return subscription_doc_signed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        subscription_doc_signed_at = _parse_subscription_doc_signed_at(d.pop("subscription_doc_signed_at"))

        def _parse_subscription_doc_asset_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_doc_asset_id_type_0 = UUID(data)

                return subscription_doc_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        subscription_doc_asset_id = _parse_subscription_doc_asset_id(d.pop("subscription_doc_asset_id"))

        pro_rata_rights = d.pop("pro_rata_rights")

        board_seat = d.pop("board_seat")

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

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_metadata(data: object) -> InvestorCommitmentResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = InvestorCommitmentResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(InvestorCommitmentResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        investor_commitment_response = cls(
            id=id,
            fundraise_round_id=fundraise_round_id,
            investor_id=investor_id,
            committed_amount=committed_amount,
            committed_currency_id=committed_currency_id,
            commitment_status=commitment_status,
            committed_at=committed_at,
            wired_at=wired_at,
            wired_amount=wired_amount,
            shares_allocated=shares_allocated,
            share_class=share_class,
            term_sheet_signed_at=term_sheet_signed_at,
            term_sheet_asset_id=term_sheet_asset_id,
            subscription_doc_signed_at=subscription_doc_signed_at,
            subscription_doc_asset_id=subscription_doc_asset_id,
            pro_rata_rights=pro_rata_rights,
            board_seat=board_seat,
            notes=notes,
            created_by_bot_id=created_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            metadata=metadata,
        )

        investor_commitment_response.additional_properties = d
        return investor_commitment_response

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
