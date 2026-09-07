from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InvoiceMonthPoint")


@_attrs_define
class InvoiceMonthPoint:
    """
    Attributes:
        month (str):
        paid (int):
        open_ (int):
        past_due (int):
        void (int):
    """

    month: str
    paid: int
    open_: int
    past_due: int
    void: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = self.month

        paid = self.paid

        open_ = self.open_

        past_due = self.past_due

        void = self.void

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "paid": paid,
                "open": open_,
                "past_due": past_due,
                "void": void,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = d.pop("month")

        paid = d.pop("paid")

        open_ = d.pop("open")

        past_due = d.pop("past_due")

        void = d.pop("void")

        invoice_month_point = cls(
            month=month,
            paid=paid,
            open_=open_,
            past_due=past_due,
            void=void,
        )

        invoice_month_point.additional_properties = d
        return invoice_month_point

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
