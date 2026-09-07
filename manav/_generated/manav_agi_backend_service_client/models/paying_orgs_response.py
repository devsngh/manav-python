from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PayingOrgsResponse")


@_attrs_define
class PayingOrgsResponse:
    """GET /api/analytics/paying-orgs.

    Attributes:
        paying_orgs (int):
        active_subscriptions (int):
        target (int):
    """

    paying_orgs: int
    active_subscriptions: int
    target: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paying_orgs = self.paying_orgs

        active_subscriptions = self.active_subscriptions

        target = self.target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paying_orgs": paying_orgs,
                "active_subscriptions": active_subscriptions,
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paying_orgs = d.pop("paying_orgs")

        active_subscriptions = d.pop("active_subscriptions")

        target = d.pop("target")

        paying_orgs_response = cls(
            paying_orgs=paying_orgs,
            active_subscriptions=active_subscriptions,
            target=target,
        )

        paying_orgs_response.additional_properties = d
        return paying_orgs_response

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
