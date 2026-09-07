from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewResponse")


@_attrs_define
class ReviewResponse:
    """
    Attributes:
        id (UUID):
        listing_id (UUID):
        user_id (UUID):
        rating (int):
        title (None | str):
        body (None | str):
        created_at (datetime.datetime):
        reviewer_name (None | str | Unset):
        reviewer_avatar_url (None | str | Unset):
    """

    id: UUID
    listing_id: UUID
    user_id: UUID
    rating: int
    title: None | str
    body: None | str
    created_at: datetime.datetime
    reviewer_name: None | str | Unset = UNSET
    reviewer_avatar_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        listing_id = str(self.listing_id)

        user_id = str(self.user_id)

        rating = self.rating

        title: None | str
        title = self.title

        body: None | str
        body = self.body

        created_at = self.created_at.isoformat()

        reviewer_name: None | str | Unset
        if isinstance(self.reviewer_name, Unset):
            reviewer_name = UNSET
        else:
            reviewer_name = self.reviewer_name

        reviewer_avatar_url: None | str | Unset
        if isinstance(self.reviewer_avatar_url, Unset):
            reviewer_avatar_url = UNSET
        else:
            reviewer_avatar_url = self.reviewer_avatar_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "listing_id": listing_id,
                "user_id": user_id,
                "rating": rating,
                "title": title,
                "body": body,
                "created_at": created_at,
            }
        )
        if reviewer_name is not UNSET:
            field_dict["reviewer_name"] = reviewer_name
        if reviewer_avatar_url is not UNSET:
            field_dict["reviewer_avatar_url"] = reviewer_avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        listing_id = UUID(d.pop("listing_id"))

        user_id = UUID(d.pop("user_id"))

        rating = d.pop("rating")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_body(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body = _parse_body(d.pop("body"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_reviewer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewer_name = _parse_reviewer_name(d.pop("reviewer_name", UNSET))

        def _parse_reviewer_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reviewer_avatar_url = _parse_reviewer_avatar_url(d.pop("reviewer_avatar_url", UNSET))

        review_response = cls(
            id=id,
            listing_id=listing_id,
            user_id=user_id,
            rating=rating,
            title=title,
            body=body,
            created_at=created_at,
            reviewer_name=reviewer_name,
            reviewer_avatar_url=reviewer_avatar_url,
        )

        review_response.additional_properties = d
        return review_response

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
