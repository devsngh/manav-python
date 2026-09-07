from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenUsagePoint")


@_attrs_define
class TokenUsagePoint:
    """
    Attributes:
        date (datetime.date):
        total_tokens (int):
        total_credits (int):
        request_count (int):
        model_id (None | str | Unset):
    """

    date: datetime.date
    total_tokens: int
    total_credits: int
    request_count: int
    model_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        total_tokens = self.total_tokens

        total_credits = self.total_credits

        request_count = self.request_count

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "total_tokens": total_tokens,
                "total_credits": total_credits,
                "request_count": request_count,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        total_tokens = d.pop("total_tokens")

        total_credits = d.pop("total_credits")

        request_count = d.pop("request_count")

        def _parse_model_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        token_usage_point = cls(
            date=date,
            total_tokens=total_tokens,
            total_credits=total_credits,
            request_count=request_count,
            model_id=model_id,
        )

        token_usage_point.additional_properties = d
        return token_usage_point

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
