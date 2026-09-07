from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quota_period import QuotaPeriod
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlanQuotaUpdate")


@_attrs_define
class PlanQuotaUpdate:
    """
    Attributes:
        quota_key (None | str | Unset):
        quota_name (None | str | Unset):
        limit_value (int | None | Unset):
        period (None | QuotaPeriod | Unset):
    """

    quota_key: None | str | Unset = UNSET
    quota_name: None | str | Unset = UNSET
    limit_value: int | None | Unset = UNSET
    period: None | QuotaPeriod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quota_key: None | str | Unset
        if isinstance(self.quota_key, Unset):
            quota_key = UNSET
        else:
            quota_key = self.quota_key

        quota_name: None | str | Unset
        if isinstance(self.quota_name, Unset):
            quota_name = UNSET
        else:
            quota_name = self.quota_name

        limit_value: int | None | Unset
        if isinstance(self.limit_value, Unset):
            limit_value = UNSET
        else:
            limit_value = self.limit_value

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        elif isinstance(self.period, QuotaPeriod):
            period = self.period.value
        else:
            period = self.period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quota_key is not UNSET:
            field_dict["quota_key"] = quota_key
        if quota_name is not UNSET:
            field_dict["quota_name"] = quota_name
        if limit_value is not UNSET:
            field_dict["limit_value"] = limit_value
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_quota_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota_key = _parse_quota_key(d.pop("quota_key", UNSET))

        def _parse_quota_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quota_name = _parse_quota_name(d.pop("quota_name", UNSET))

        def _parse_limit_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit_value = _parse_limit_value(d.pop("limit_value", UNSET))

        def _parse_period(data: object) -> None | QuotaPeriod | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_type_0 = QuotaPeriod(data)

                return period_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | QuotaPeriod | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        plan_quota_update = cls(
            quota_key=quota_key,
            quota_name=quota_name,
            limit_value=limit_value,
            period=period,
        )

        plan_quota_update.additional_properties = d
        return plan_quota_update

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
