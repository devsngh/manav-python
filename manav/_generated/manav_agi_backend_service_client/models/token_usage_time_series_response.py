from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token_usage_point import TokenUsagePoint


T = TypeVar("T", bound="TokenUsageTimeSeriesResponse")


@_attrs_define
class TokenUsageTimeSeriesResponse:
    """
    Attributes:
        data (list[TokenUsagePoint]):
        total_tokens (int):
        total_credits (int):
        total_requests (int):
    """

    data: list[TokenUsagePoint]
    total_tokens: int
    total_credits: int
    total_requests: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total_tokens = self.total_tokens

        total_credits = self.total_credits

        total_requests = self.total_requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "total_tokens": total_tokens,
                "total_credits": total_credits,
                "total_requests": total_requests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_usage_point import TokenUsagePoint  # noqa: PLC0415

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TokenUsagePoint.from_dict(data_item_data)

            data.append(data_item)

        total_tokens = d.pop("total_tokens")

        total_credits = d.pop("total_credits")

        total_requests = d.pop("total_requests")

        token_usage_time_series_response = cls(
            data=data,
            total_tokens=total_tokens,
            total_credits=total_credits,
            total_requests=total_requests,
        )

        token_usage_time_series_response.additional_properties = d
        return token_usage_time_series_response

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
