from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quota_period import QuotaPeriod

T = TypeVar("T", bound="PlanQuotaCreate")


@_attrs_define
class PlanQuotaCreate:
    """
    Attributes:
        quota_key (str):
        quota_name (str):
        limit_value (int):
        period (QuotaPeriod):
    """

    quota_key: str
    quota_name: str
    limit_value: int
    period: QuotaPeriod
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_key = self.quota_key

        quota_name = self.quota_name

        limit_value = self.limit_value

        period = self.period.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quota_key": quota_key,
                "quota_name": quota_name,
                "limit_value": limit_value,
                "period": period,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quota_key = d.pop("quota_key")

        quota_name = d.pop("quota_name")

        limit_value = d.pop("limit_value")

        period = QuotaPeriod(d.pop("period"))

        plan_quota_create = cls(
            quota_key=quota_key,
            quota_name=quota_name,
            limit_value=limit_value,
            period=period,
        )

        plan_quota_create.additional_properties = d
        return plan_quota_create

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
