from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.invoice_month_point import InvoiceMonthPoint
    from ..models.invoice_status_count import InvoiceStatusCount


T = TypeVar("T", bound="InvoicesResponse")


@_attrs_define
class InvoicesResponse:
    """GET /api/analytics/billing/invoices — outstanding + monthly status timeline.

    Attributes:
        outstanding_count (int):
        outstanding_amount (float):
        by_status (list[InvoiceStatusCount]):
        timeline (list[InvoiceMonthPoint]):
    """

    outstanding_count: int
    outstanding_amount: float
    by_status: list[InvoiceStatusCount]
    timeline: list[InvoiceMonthPoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        outstanding_count = self.outstanding_count

        outstanding_amount = self.outstanding_amount

        by_status = []
        for by_status_item_data in self.by_status:
            by_status_item = by_status_item_data.to_dict()
            by_status.append(by_status_item)

        timeline = []
        for timeline_item_data in self.timeline:
            timeline_item = timeline_item_data.to_dict()
            timeline.append(timeline_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "outstanding_count": outstanding_count,
                "outstanding_amount": outstanding_amount,
                "by_status": by_status,
                "timeline": timeline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice_month_point import InvoiceMonthPoint  # noqa: PLC0415
        from ..models.invoice_status_count import InvoiceStatusCount  # noqa: PLC0415

        d = dict(src_dict)
        outstanding_count = d.pop("outstanding_count")

        outstanding_amount = d.pop("outstanding_amount")

        by_status = []
        _by_status = d.pop("by_status")
        for by_status_item_data in _by_status:
            by_status_item = InvoiceStatusCount.from_dict(by_status_item_data)

            by_status.append(by_status_item)

        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in _timeline:
            timeline_item = InvoiceMonthPoint.from_dict(timeline_item_data)

            timeline.append(timeline_item)

        invoices_response = cls(
            outstanding_count=outstanding_count,
            outstanding_amount=outstanding_amount,
            by_status=by_status,
            timeline=timeline,
        )

        invoices_response.additional_properties = d
        return invoices_response

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
