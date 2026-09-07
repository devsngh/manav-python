from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rate_limit_update_request_limits import RateLimitUpdateRequestLimits


T = TypeVar("T", bound="RateLimitUpdateRequest")


@_attrs_define
class RateLimitUpdateRequest:
    """
    Attributes:
        user_id (str):
        model_id (str):
        limits (RateLimitUpdateRequestLimits):
    """

    user_id: str
    model_id: str
    limits: RateLimitUpdateRequestLimits
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        model_id = self.model_id

        limits = self.limits.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "model_id": model_id,
                "limits": limits,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rate_limit_update_request_limits import RateLimitUpdateRequestLimits  # noqa: PLC0415

        d = dict(src_dict)
        user_id = d.pop("user_id")

        model_id = d.pop("model_id")

        limits = RateLimitUpdateRequestLimits.from_dict(d.pop("limits"))

        rate_limit_update_request = cls(
            user_id=user_id,
            model_id=model_id,
            limits=limits,
        )

        rate_limit_update_request.additional_properties = d
        return rate_limit_update_request

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
