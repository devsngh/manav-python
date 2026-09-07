from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopUserItem")


@_attrs_define
class TopUserItem:
    """
    Attributes:
        user_id (str):
        total_tokens (int):
        total_credits (int):
        request_count (int):
        user_email (None | str | Unset):
    """

    user_id: str
    total_tokens: int
    total_credits: int
    request_count: int
    user_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        total_tokens = self.total_tokens

        total_credits = self.total_credits

        request_count = self.request_count

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "total_tokens": total_tokens,
                "total_credits": total_credits,
                "request_count": request_count,
            }
        )
        if user_email is not UNSET:
            field_dict["user_email"] = user_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        total_tokens = d.pop("total_tokens")

        total_credits = d.pop("total_credits")

        request_count = d.pop("request_count")

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        top_user_item = cls(
            user_id=user_id,
            total_tokens=total_tokens,
            total_credits=total_credits,
            request_count=request_count,
            user_email=user_email,
        )

        top_user_item.additional_properties = d
        return top_user_item

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
