from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fundraise_round_response_metadata_type_0 import FundraiseRoundResponseMetadataType0


T = TypeVar("T", bound="FundraiseRoundResponse")


@_attrs_define
class FundraiseRoundResponse:
    """
    Attributes:
        id (UUID):
        org_id (UUID):
        round_name (str):
        round_sequence (int | None):
        target_amount (None | str):
        raised_amount (str):
        amount_currency_id (UUID):
        status (str):
        opened_at (datetime.datetime | None):
        closed_at (datetime.datetime | None):
        target_close_date (datetime.date | None):
        pre_money_valuation (None | str):
        post_money_valuation (None | str):
        valuation_currency_id (None | UUID):
        share_class (None | str):
        share_price (None | str):
        shares_offered (int | None):
        lead_investor_id (None | UUID):
        legal_entity_id (None | UUID):
        term_sheet_asset_id (None | UUID):
        final_documents_asset_ids (list[UUID] | None):
        use_of_funds_summary (None | str):
        created_by_bot_id (None | UUID):
        approved_by_user_id (None | UUID):
        last_modified_by_bot_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        deleted_at (datetime.datetime | None):
        metadata (FundraiseRoundResponseMetadataType0 | None | Unset):
    """

    id: UUID
    org_id: UUID
    round_name: str
    round_sequence: int | None
    target_amount: None | str
    raised_amount: str
    amount_currency_id: UUID
    status: str
    opened_at: datetime.datetime | None
    closed_at: datetime.datetime | None
    target_close_date: datetime.date | None
    pre_money_valuation: None | str
    post_money_valuation: None | str
    valuation_currency_id: None | UUID
    share_class: None | str
    share_price: None | str
    shares_offered: int | None
    lead_investor_id: None | UUID
    legal_entity_id: None | UUID
    term_sheet_asset_id: None | UUID
    final_documents_asset_ids: list[UUID] | None
    use_of_funds_summary: None | str
    created_by_bot_id: None | UUID
    approved_by_user_id: None | UUID
    last_modified_by_bot_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    metadata: FundraiseRoundResponseMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fundraise_round_response_metadata_type_0 import (
            FundraiseRoundResponseMetadataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        org_id = str(self.org_id)

        round_name = self.round_name

        round_sequence: int | None
        round_sequence = self.round_sequence

        target_amount: None | str
        target_amount = self.target_amount

        raised_amount = self.raised_amount

        amount_currency_id = str(self.amount_currency_id)

        status = self.status

        opened_at: None | str
        if isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        closed_at: None | str
        if isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        target_close_date: None | str
        if isinstance(self.target_close_date, datetime.date):
            target_close_date = self.target_close_date.isoformat()
        else:
            target_close_date = self.target_close_date

        pre_money_valuation: None | str
        pre_money_valuation = self.pre_money_valuation

        post_money_valuation: None | str
        post_money_valuation = self.post_money_valuation

        valuation_currency_id: None | str
        if isinstance(self.valuation_currency_id, UUID):
            valuation_currency_id = str(self.valuation_currency_id)
        else:
            valuation_currency_id = self.valuation_currency_id

        share_class: None | str
        share_class = self.share_class

        share_price: None | str
        share_price = self.share_price

        shares_offered: int | None
        shares_offered = self.shares_offered

        lead_investor_id: None | str
        if isinstance(self.lead_investor_id, UUID):
            lead_investor_id = str(self.lead_investor_id)
        else:
            lead_investor_id = self.lead_investor_id

        legal_entity_id: None | str
        if isinstance(self.legal_entity_id, UUID):
            legal_entity_id = str(self.legal_entity_id)
        else:
            legal_entity_id = self.legal_entity_id

        term_sheet_asset_id: None | str
        if isinstance(self.term_sheet_asset_id, UUID):
            term_sheet_asset_id = str(self.term_sheet_asset_id)
        else:
            term_sheet_asset_id = self.term_sheet_asset_id

        final_documents_asset_ids: list[str] | None
        if isinstance(self.final_documents_asset_ids, list):
            final_documents_asset_ids = []
            for final_documents_asset_ids_type_0_item_data in self.final_documents_asset_ids:
                final_documents_asset_ids_type_0_item = str(final_documents_asset_ids_type_0_item_data)
                final_documents_asset_ids.append(final_documents_asset_ids_type_0_item)

        else:
            final_documents_asset_ids = self.final_documents_asset_ids

        use_of_funds_summary: None | str
        use_of_funds_summary = self.use_of_funds_summary

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
        elif isinstance(self.metadata, FundraiseRoundResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "round_name": round_name,
                "round_sequence": round_sequence,
                "target_amount": target_amount,
                "raised_amount": raised_amount,
                "amount_currency_id": amount_currency_id,
                "status": status,
                "opened_at": opened_at,
                "closed_at": closed_at,
                "target_close_date": target_close_date,
                "pre_money_valuation": pre_money_valuation,
                "post_money_valuation": post_money_valuation,
                "valuation_currency_id": valuation_currency_id,
                "share_class": share_class,
                "share_price": share_price,
                "shares_offered": shares_offered,
                "lead_investor_id": lead_investor_id,
                "legal_entity_id": legal_entity_id,
                "term_sheet_asset_id": term_sheet_asset_id,
                "final_documents_asset_ids": final_documents_asset_ids,
                "use_of_funds_summary": use_of_funds_summary,
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
        from ..models.fundraise_round_response_metadata_type_0 import (
            FundraiseRoundResponseMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        org_id = UUID(d.pop("org_id"))

        round_name = d.pop("round_name")

        def _parse_round_sequence(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        round_sequence = _parse_round_sequence(d.pop("round_sequence"))

        def _parse_target_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_amount = _parse_target_amount(d.pop("target_amount"))

        raised_amount = d.pop("raised_amount")

        amount_currency_id = UUID(d.pop("amount_currency_id"))

        status = d.pop("status")

        def _parse_opened_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        opened_at = _parse_opened_at(d.pop("opened_at"))

        def _parse_closed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))

        def _parse_target_close_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_close_date_type_0 = datetime.date.fromisoformat(data)

                return target_close_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        target_close_date = _parse_target_close_date(d.pop("target_close_date"))

        def _parse_pre_money_valuation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        pre_money_valuation = _parse_pre_money_valuation(d.pop("pre_money_valuation"))

        def _parse_post_money_valuation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        post_money_valuation = _parse_post_money_valuation(d.pop("post_money_valuation"))

        def _parse_valuation_currency_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valuation_currency_id_type_0 = UUID(data)

                return valuation_currency_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        valuation_currency_id = _parse_valuation_currency_id(d.pop("valuation_currency_id"))

        def _parse_share_class(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        share_class = _parse_share_class(d.pop("share_class"))

        def _parse_share_price(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        share_price = _parse_share_price(d.pop("share_price"))

        def _parse_shares_offered(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        shares_offered = _parse_shares_offered(d.pop("shares_offered"))

        def _parse_lead_investor_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_investor_id_type_0 = UUID(data)

                return lead_investor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        lead_investor_id = _parse_lead_investor_id(d.pop("lead_investor_id"))

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

        def _parse_final_documents_asset_ids(data: object) -> list[UUID] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                final_documents_asset_ids_type_0 = []
                _final_documents_asset_ids_type_0 = data
                for final_documents_asset_ids_type_0_item_data in _final_documents_asset_ids_type_0:
                    final_documents_asset_ids_type_0_item = UUID(final_documents_asset_ids_type_0_item_data)

                    final_documents_asset_ids_type_0.append(final_documents_asset_ids_type_0_item)

                return final_documents_asset_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None, data)

        final_documents_asset_ids = _parse_final_documents_asset_ids(d.pop("final_documents_asset_ids"))

        def _parse_use_of_funds_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        use_of_funds_summary = _parse_use_of_funds_summary(d.pop("use_of_funds_summary"))

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

        def _parse_metadata(data: object) -> FundraiseRoundResponseMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = FundraiseRoundResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FundraiseRoundResponseMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        fundraise_round_response = cls(
            id=id,
            org_id=org_id,
            round_name=round_name,
            round_sequence=round_sequence,
            target_amount=target_amount,
            raised_amount=raised_amount,
            amount_currency_id=amount_currency_id,
            status=status,
            opened_at=opened_at,
            closed_at=closed_at,
            target_close_date=target_close_date,
            pre_money_valuation=pre_money_valuation,
            post_money_valuation=post_money_valuation,
            valuation_currency_id=valuation_currency_id,
            share_class=share_class,
            share_price=share_price,
            shares_offered=shares_offered,
            lead_investor_id=lead_investor_id,
            legal_entity_id=legal_entity_id,
            term_sheet_asset_id=term_sheet_asset_id,
            final_documents_asset_ids=final_documents_asset_ids,
            use_of_funds_summary=use_of_funds_summary,
            created_by_bot_id=created_by_bot_id,
            approved_by_user_id=approved_by_user_id,
            last_modified_by_bot_id=last_modified_by_bot_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            metadata=metadata,
        )

        fundraise_round_response.additional_properties = d
        return fundraise_round_response

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
