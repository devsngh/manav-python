from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.credit_pack_month_point import CreditPackMonthPoint


T = TypeVar("T", bound="CreditPacksResponse")


@_attrs_define
class CreditPacksResponse:
    """GET /api/analytics/billing/credit-packs — monthly pack-purchase trend.

    Attributes:
        months (list[CreditPackMonthPoint]):
        total_credits (int):
        total_purchases (int):
    """

    months: list[CreditPackMonthPoint]
    total_credits: int
    total_purchases: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        months = []
        for months_item_data in self.months:
            months_item = months_item_data.to_dict()
            months.append(months_item)

        total_credits = self.total_credits

        total_purchases = self.total_purchases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "months": months,
                "total_credits": total_credits,
                "total_purchases": total_purchases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_pack_month_point import CreditPackMonthPoint  # noqa: PLC0415

        d = dict(src_dict)
        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = CreditPackMonthPoint.from_dict(months_item_data)

            months.append(months_item)

        total_credits = d.pop("total_credits")

        total_purchases = d.pop("total_purchases")

        credit_packs_response = cls(
            months=months,
            total_credits=total_credits,
            total_purchases=total_purchases,
        )

        credit_packs_response.additional_properties = d
        return credit_packs_response

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
