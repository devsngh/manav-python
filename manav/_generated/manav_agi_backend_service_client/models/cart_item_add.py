from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.selected_period import SelectedPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CartItemAdd")


@_attrs_define
class CartItemAdd:
    """
    Attributes:
        listing_id (UUID):
        selected_period (SelectedPeriod | Unset):  Default: SelectedPeriod.MONTHLY.
    """

    listing_id: UUID
    selected_period: SelectedPeriod | Unset = SelectedPeriod.MONTHLY
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        listing_id = str(self.listing_id)

        selected_period: str | Unset = UNSET
        if not isinstance(self.selected_period, Unset):
            selected_period = self.selected_period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "listing_id": listing_id,
            }
        )
        if selected_period is not UNSET:
            field_dict["selected_period"] = selected_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = UUID(d.pop("listing_id"))

        _selected_period = d.pop("selected_period", UNSET)
        selected_period: SelectedPeriod | Unset
        if isinstance(_selected_period, Unset):
            selected_period = UNSET
        else:
            selected_period = SelectedPeriod(_selected_period)

        cart_item_add = cls(
            listing_id=listing_id,
            selected_period=selected_period,
        )

        cart_item_add.additional_properties = d
        return cart_item_add

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
