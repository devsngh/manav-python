from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublisherItem")


@_attrs_define
class PublisherItem:
    """
    Attributes:
        publisher_user_id (str):
        listing_count (int):
        active_subscribers (int):
        monthly_earnings (float):
        total_earnings (float):
        publisher_email (None | str | Unset):
        avg_rating (float | None | Unset):
    """

    publisher_user_id: str
    listing_count: int
    active_subscribers: int
    monthly_earnings: float
    total_earnings: float
    publisher_email: None | str | Unset = UNSET
    avg_rating: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        publisher_user_id = self.publisher_user_id

        listing_count = self.listing_count

        active_subscribers = self.active_subscribers

        monthly_earnings = self.monthly_earnings

        total_earnings = self.total_earnings

        publisher_email: None | str | Unset
        if isinstance(self.publisher_email, Unset):
            publisher_email = UNSET
        else:
            publisher_email = self.publisher_email

        avg_rating: float | None | Unset
        if isinstance(self.avg_rating, Unset):
            avg_rating = UNSET
        else:
            avg_rating = self.avg_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publisher_user_id": publisher_user_id,
                "listing_count": listing_count,
                "active_subscribers": active_subscribers,
                "monthly_earnings": monthly_earnings,
                "total_earnings": total_earnings,
            }
        )
        if publisher_email is not UNSET:
            field_dict["publisher_email"] = publisher_email
        if avg_rating is not UNSET:
            field_dict["avg_rating"] = avg_rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publisher_user_id = d.pop("publisher_user_id")

        listing_count = d.pop("listing_count")

        active_subscribers = d.pop("active_subscribers")

        monthly_earnings = d.pop("monthly_earnings")

        total_earnings = d.pop("total_earnings")

        def _parse_publisher_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher_email = _parse_publisher_email(d.pop("publisher_email", UNSET))

        def _parse_avg_rating(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_rating = _parse_avg_rating(d.pop("avg_rating", UNSET))

        publisher_item = cls(
            publisher_user_id=publisher_user_id,
            listing_count=listing_count,
            active_subscribers=active_subscribers,
            monthly_earnings=monthly_earnings,
            total_earnings=total_earnings,
            publisher_email=publisher_email,
            avg_rating=avg_rating,
        )

        publisher_item.additional_properties = d
        return publisher_item

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
