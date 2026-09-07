from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pricing_model import PricingModel
from ..models.purchase_status import PurchaseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_response import ListingResponse
    from ..models.purchase_response_provisioned_data_type_0 import PurchaseResponseProvisionedDataType0


T = TypeVar("T", bound="PurchaseResponse")


@_attrs_define
class PurchaseResponse:
    """
    Attributes:
        id (UUID):
        listing_id (UUID):
        buyer_org_id (None | UUID):
        buyer_user_id (UUID):
        pricing_model (PricingModel):
        amount_paid_cents (int):
        status (PurchaseStatus):
        subscription_start (datetime.datetime | None):
        subscription_end (datetime.datetime | None):
        auto_renew (bool):
        provisioned_data (None | PurchaseResponseProvisionedDataType0):
        created_at (datetime.datetime):
        cancelled_at (datetime.datetime | None):
        listing (ListingResponse | None | Unset):
    """

    id: UUID
    listing_id: UUID
    buyer_org_id: None | UUID
    buyer_user_id: UUID
    pricing_model: PricingModel
    amount_paid_cents: int
    status: PurchaseStatus
    subscription_start: datetime.datetime | None
    subscription_end: datetime.datetime | None
    auto_renew: bool
    provisioned_data: None | PurchaseResponseProvisionedDataType0
    created_at: datetime.datetime
    cancelled_at: datetime.datetime | None
    listing: ListingResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_response import ListingResponse  # noqa: PLC0415
        from ..models.purchase_response_provisioned_data_type_0 import (
            PurchaseResponseProvisionedDataType0,  # noqa: PLC0415
        )

        id = str(self.id)

        listing_id = str(self.listing_id)

        buyer_org_id: None | str
        if isinstance(self.buyer_org_id, UUID):
            buyer_org_id = str(self.buyer_org_id)
        else:
            buyer_org_id = self.buyer_org_id

        buyer_user_id = str(self.buyer_user_id)

        pricing_model = self.pricing_model.value

        amount_paid_cents = self.amount_paid_cents

        status = self.status.value

        subscription_start: None | str
        if isinstance(self.subscription_start, datetime.datetime):
            subscription_start = self.subscription_start.isoformat()
        else:
            subscription_start = self.subscription_start

        subscription_end: None | str
        if isinstance(self.subscription_end, datetime.datetime):
            subscription_end = self.subscription_end.isoformat()
        else:
            subscription_end = self.subscription_end

        auto_renew = self.auto_renew

        provisioned_data: dict[str, Any] | None
        if isinstance(self.provisioned_data, PurchaseResponseProvisionedDataType0):
            provisioned_data = self.provisioned_data.to_dict()
        else:
            provisioned_data = self.provisioned_data

        created_at = self.created_at.isoformat()

        cancelled_at: None | str
        if isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        listing: dict[str, Any] | None | Unset
        if isinstance(self.listing, Unset):
            listing = UNSET
        elif isinstance(self.listing, ListingResponse):
            listing = self.listing.to_dict()
        else:
            listing = self.listing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "listing_id": listing_id,
                "buyer_org_id": buyer_org_id,
                "buyer_user_id": buyer_user_id,
                "pricing_model": pricing_model,
                "amount_paid_cents": amount_paid_cents,
                "status": status,
                "subscription_start": subscription_start,
                "subscription_end": subscription_end,
                "auto_renew": auto_renew,
                "provisioned_data": provisioned_data,
                "created_at": created_at,
                "cancelled_at": cancelled_at,
            }
        )
        if listing is not UNSET:
            field_dict["listing"] = listing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_response import ListingResponse  # noqa: PLC0415
        from ..models.purchase_response_provisioned_data_type_0 import (
            PurchaseResponseProvisionedDataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        listing_id = UUID(d.pop("listing_id"))

        def _parse_buyer_org_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                buyer_org_id_type_0 = UUID(data)

                return buyer_org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        buyer_org_id = _parse_buyer_org_id(d.pop("buyer_org_id"))

        buyer_user_id = UUID(d.pop("buyer_user_id"))

        pricing_model = PricingModel(d.pop("pricing_model"))

        amount_paid_cents = d.pop("amount_paid_cents")

        status = PurchaseStatus(d.pop("status"))

        def _parse_subscription_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_start_type_0 = datetime.datetime.fromisoformat(data)

                return subscription_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        subscription_start = _parse_subscription_start(d.pop("subscription_start"))

        def _parse_subscription_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subscription_end_type_0 = datetime.datetime.fromisoformat(data)

                return subscription_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        subscription_end = _parse_subscription_end(d.pop("subscription_end"))

        auto_renew = d.pop("auto_renew")

        def _parse_provisioned_data(data: object) -> None | PurchaseResponseProvisionedDataType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provisioned_data_type_0 = PurchaseResponseProvisionedDataType0.from_dict(data)

                return provisioned_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PurchaseResponseProvisionedDataType0, data)

        provisioned_data = _parse_provisioned_data(d.pop("provisioned_data"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_cancelled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_at_type_0 = datetime.datetime.fromisoformat(data)

                return cancelled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at"))

        def _parse_listing(data: object) -> ListingResponse | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                listing_type_0 = ListingResponse.from_dict(data)

                return listing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingResponse | None | Unset, data)

        listing = _parse_listing(d.pop("listing", UNSET))

        purchase_response = cls(
            id=id,
            listing_id=listing_id,
            buyer_org_id=buyer_org_id,
            buyer_user_id=buyer_user_id,
            pricing_model=pricing_model,
            amount_paid_cents=amount_paid_cents,
            status=status,
            subscription_start=subscription_start,
            subscription_end=subscription_end,
            auto_renew=auto_renew,
            provisioned_data=provisioned_data,
            created_at=created_at,
            cancelled_at=cancelled_at,
            listing=listing,
        )

        purchase_response.additional_properties = d
        return purchase_response

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
