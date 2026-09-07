from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fundraise_round_update_metadata_type_0 import FundraiseRoundUpdateMetadataType0


T = TypeVar("T", bound="FundraiseRoundUpdate")


@_attrs_define
class FundraiseRoundUpdate:
    """
    Attributes:
        target_amount (float | None | str | Unset):
        raised_amount (float | None | str | Unset):
        status (None | str | Unset):
        target_close_date (datetime.date | None | Unset):
        pre_money_valuation (float | None | str | Unset):
        post_money_valuation (float | None | str | Unset):
        share_class (None | str | Unset):
        share_price (float | None | str | Unset):
        shares_offered (int | None | Unset):
        lead_investor_id (None | Unset | UUID):
        term_sheet_asset_id (None | Unset | UUID):
        final_documents_asset_ids (list[UUID] | None | Unset):
        use_of_funds_summary (None | str | Unset):
        metadata (FundraiseRoundUpdateMetadataType0 | None | Unset):
    """

    target_amount: float | None | str | Unset = UNSET
    raised_amount: float | None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    target_close_date: datetime.date | None | Unset = UNSET
    pre_money_valuation: float | None | str | Unset = UNSET
    post_money_valuation: float | None | str | Unset = UNSET
    share_class: None | str | Unset = UNSET
    share_price: float | None | str | Unset = UNSET
    shares_offered: int | None | Unset = UNSET
    lead_investor_id: None | Unset | UUID = UNSET
    term_sheet_asset_id: None | Unset | UUID = UNSET
    final_documents_asset_ids: list[UUID] | None | Unset = UNSET
    use_of_funds_summary: None | str | Unset = UNSET
    metadata: FundraiseRoundUpdateMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fundraise_round_update_metadata_type_0 import FundraiseRoundUpdateMetadataType0  # noqa: PLC0415

        target_amount: float | None | str | Unset
        if isinstance(self.target_amount, Unset):
            target_amount = UNSET
        else:
            target_amount = self.target_amount

        raised_amount: float | None | str | Unset
        if isinstance(self.raised_amount, Unset):
            raised_amount = UNSET
        else:
            raised_amount = self.raised_amount

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        target_close_date: None | str | Unset
        if isinstance(self.target_close_date, Unset):
            target_close_date = UNSET
        elif isinstance(self.target_close_date, datetime.date):
            target_close_date = self.target_close_date.isoformat()
        else:
            target_close_date = self.target_close_date

        pre_money_valuation: float | None | str | Unset
        if isinstance(self.pre_money_valuation, Unset):
            pre_money_valuation = UNSET
        else:
            pre_money_valuation = self.pre_money_valuation

        post_money_valuation: float | None | str | Unset
        if isinstance(self.post_money_valuation, Unset):
            post_money_valuation = UNSET
        else:
            post_money_valuation = self.post_money_valuation

        share_class: None | str | Unset
        if isinstance(self.share_class, Unset):
            share_class = UNSET
        else:
            share_class = self.share_class

        share_price: float | None | str | Unset
        if isinstance(self.share_price, Unset):
            share_price = UNSET
        else:
            share_price = self.share_price

        shares_offered: int | None | Unset
        if isinstance(self.shares_offered, Unset):
            shares_offered = UNSET
        else:
            shares_offered = self.shares_offered

        lead_investor_id: None | str | Unset
        if isinstance(self.lead_investor_id, Unset):
            lead_investor_id = UNSET
        elif isinstance(self.lead_investor_id, UUID):
            lead_investor_id = str(self.lead_investor_id)
        else:
            lead_investor_id = self.lead_investor_id

        term_sheet_asset_id: None | str | Unset
        if isinstance(self.term_sheet_asset_id, Unset):
            term_sheet_asset_id = UNSET
        elif isinstance(self.term_sheet_asset_id, UUID):
            term_sheet_asset_id = str(self.term_sheet_asset_id)
        else:
            term_sheet_asset_id = self.term_sheet_asset_id

        final_documents_asset_ids: list[str] | None | Unset
        if isinstance(self.final_documents_asset_ids, Unset):
            final_documents_asset_ids = UNSET
        elif isinstance(self.final_documents_asset_ids, list):
            final_documents_asset_ids = []
            for final_documents_asset_ids_type_0_item_data in self.final_documents_asset_ids:
                final_documents_asset_ids_type_0_item = str(final_documents_asset_ids_type_0_item_data)
                final_documents_asset_ids.append(final_documents_asset_ids_type_0_item)

        else:
            final_documents_asset_ids = self.final_documents_asset_ids

        use_of_funds_summary: None | str | Unset
        if isinstance(self.use_of_funds_summary, Unset):
            use_of_funds_summary = UNSET
        else:
            use_of_funds_summary = self.use_of_funds_summary

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, FundraiseRoundUpdateMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_amount is not UNSET:
            field_dict["target_amount"] = target_amount
        if raised_amount is not UNSET:
            field_dict["raised_amount"] = raised_amount
        if status is not UNSET:
            field_dict["status"] = status
        if target_close_date is not UNSET:
            field_dict["target_close_date"] = target_close_date
        if pre_money_valuation is not UNSET:
            field_dict["pre_money_valuation"] = pre_money_valuation
        if post_money_valuation is not UNSET:
            field_dict["post_money_valuation"] = post_money_valuation
        if share_class is not UNSET:
            field_dict["share_class"] = share_class
        if share_price is not UNSET:
            field_dict["share_price"] = share_price
        if shares_offered is not UNSET:
            field_dict["shares_offered"] = shares_offered
        if lead_investor_id is not UNSET:
            field_dict["lead_investor_id"] = lead_investor_id
        if term_sheet_asset_id is not UNSET:
            field_dict["term_sheet_asset_id"] = term_sheet_asset_id
        if final_documents_asset_ids is not UNSET:
            field_dict["final_documents_asset_ids"] = final_documents_asset_ids
        if use_of_funds_summary is not UNSET:
            field_dict["use_of_funds_summary"] = use_of_funds_summary
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fundraise_round_update_metadata_type_0 import FundraiseRoundUpdateMetadataType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_target_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        target_amount = _parse_target_amount(d.pop("target_amount", UNSET))

        def _parse_raised_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        raised_amount = _parse_raised_amount(d.pop("raised_amount", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_target_close_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                target_close_date_type_0 = datetime.date.fromisoformat(data)

                return target_close_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        target_close_date = _parse_target_close_date(d.pop("target_close_date", UNSET))

        def _parse_pre_money_valuation(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pre_money_valuation = _parse_pre_money_valuation(d.pop("pre_money_valuation", UNSET))

        def _parse_post_money_valuation(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        post_money_valuation = _parse_post_money_valuation(d.pop("post_money_valuation", UNSET))

        def _parse_share_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_class = _parse_share_class(d.pop("share_class", UNSET))

        def _parse_share_price(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        share_price = _parse_share_price(d.pop("share_price", UNSET))

        def _parse_shares_offered(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        shares_offered = _parse_shares_offered(d.pop("shares_offered", UNSET))

        def _parse_lead_investor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lead_investor_id_type_0 = UUID(data)

                return lead_investor_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        lead_investor_id = _parse_lead_investor_id(d.pop("lead_investor_id", UNSET))

        def _parse_term_sheet_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_sheet_asset_id_type_0 = UUID(data)

                return term_sheet_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        term_sheet_asset_id = _parse_term_sheet_asset_id(d.pop("term_sheet_asset_id", UNSET))

        def _parse_final_documents_asset_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
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
            return cast(list[UUID] | None | Unset, data)

        final_documents_asset_ids = _parse_final_documents_asset_ids(d.pop("final_documents_asset_ids", UNSET))

        def _parse_use_of_funds_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_of_funds_summary = _parse_use_of_funds_summary(d.pop("use_of_funds_summary", UNSET))

        def _parse_metadata(data: object) -> FundraiseRoundUpdateMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = FundraiseRoundUpdateMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FundraiseRoundUpdateMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        fundraise_round_update = cls(
            target_amount=target_amount,
            raised_amount=raised_amount,
            status=status,
            target_close_date=target_close_date,
            pre_money_valuation=pre_money_valuation,
            post_money_valuation=post_money_valuation,
            share_class=share_class,
            share_price=share_price,
            shares_offered=shares_offered,
            lead_investor_id=lead_investor_id,
            term_sheet_asset_id=term_sheet_asset_id,
            final_documents_asset_ids=final_documents_asset_ids,
            use_of_funds_summary=use_of_funds_summary,
            metadata=metadata,
        )

        fundraise_round_update.additional_properties = d
        return fundraise_round_update

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
