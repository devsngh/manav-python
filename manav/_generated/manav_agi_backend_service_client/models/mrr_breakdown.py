from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MrrBreakdown")


@_attrs_define
class MrrBreakdown:
    """
    Attributes:
        subscriptions (float):
        marketplace (float):
        credits_ (float):
        api (float):
    """

    subscriptions: float
    marketplace: float
    credits_: float
    api: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriptions = self.subscriptions

        marketplace = self.marketplace

        credits_ = self.credits_

        api = self.api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriptions": subscriptions,
                "marketplace": marketplace,
                "credits": credits_,
                "api": api,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscriptions = d.pop("subscriptions")

        marketplace = d.pop("marketplace")

        credits_ = d.pop("credits")

        api = d.pop("api")

        mrr_breakdown = cls(
            subscriptions=subscriptions,
            marketplace=marketplace,
            credits_=credits_,
            api=api,
        )

        mrr_breakdown.additional_properties = d
        return mrr_breakdown

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
