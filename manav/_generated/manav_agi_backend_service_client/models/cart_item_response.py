from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.selected_period import SelectedPeriod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_response import ListingResponse


T = TypeVar("T", bound="CartItemResponse")


@_attrs_define
class CartItemResponse:
    """
    Attributes:
        id (UUID):
        listing_id (UUID):
        selected_period (SelectedPeriod):
        created_at (datetime.datetime):
        listing (ListingResponse | None | Unset):
    """

    id: UUID
    listing_id: UUID
    selected_period: SelectedPeriod
    created_at: datetime.datetime
    listing: ListingResponse | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_response import ListingResponse  # noqa: PLC0415

        id = str(self.id)

        listing_id = str(self.listing_id)

        selected_period = self.selected_period.value

        created_at = self.created_at.isoformat()

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
                "selected_period": selected_period,
                "created_at": created_at,
            }
        )
        if listing is not UNSET:
            field_dict["listing"] = listing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_response import ListingResponse  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        listing_id = UUID(d.pop("listing_id"))

        selected_period = SelectedPeriod(d.pop("selected_period"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

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

        cart_item_response = cls(
            id=id,
            listing_id=listing_id,
            selected_period=selected_period,
            created_at=created_at,
            listing=listing,
        )

        cart_item_response.additional_properties = d
        return cart_item_response

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
