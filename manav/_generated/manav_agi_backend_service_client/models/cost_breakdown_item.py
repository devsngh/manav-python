from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostBreakdownItem")


@_attrs_define
class CostBreakdownItem:
    """
    Attributes:
        model_id (str):
        total_tokens (int):
        total_credits (int):
        request_count (int):
        pct_of_total (float):
    """

    model_id: str
    total_tokens: int
    total_credits: int
    request_count: int
    pct_of_total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        total_tokens = self.total_tokens

        total_credits = self.total_credits

        request_count = self.request_count

        pct_of_total = self.pct_of_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_id": model_id,
                "total_tokens": total_tokens,
                "total_credits": total_credits,
                "request_count": request_count,
                "pct_of_total": pct_of_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_id = d.pop("model_id")

        total_tokens = d.pop("total_tokens")

        total_credits = d.pop("total_credits")

        request_count = d.pop("request_count")

        pct_of_total = d.pop("pct_of_total")

        cost_breakdown_item = cls(
            model_id=model_id,
            total_tokens=total_tokens,
            total_credits=total_credits,
            request_count=request_count,
            pct_of_total=pct_of_total,
        )

        cost_breakdown_item.additional_properties = d
        return cost_breakdown_item

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
