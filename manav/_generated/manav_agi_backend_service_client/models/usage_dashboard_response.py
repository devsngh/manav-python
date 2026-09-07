from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_dashboard_response_by_metric_item import UsageDashboardResponseByMetricItem


T = TypeVar("T", bound="UsageDashboardResponse")


@_attrs_define
class UsageDashboardResponse:
    """
    Attributes:
        total_credits_used (int):
        total_requests (int):
        credits_remaining (int):
        by_metric (list[UsageDashboardResponseByMetricItem]):
        period_start (datetime.datetime | None | Unset):
        period_end (datetime.datetime | None | Unset):
    """

    total_credits_used: int
    total_requests: int
    credits_remaining: int
    by_metric: list[UsageDashboardResponseByMetricItem]
    period_start: datetime.datetime | None | Unset = UNSET
    period_end: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_credits_used = self.total_credits_used

        total_requests = self.total_requests

        credits_remaining = self.credits_remaining

        by_metric = []
        for by_metric_item_data in self.by_metric:
            by_metric_item = by_metric_item_data.to_dict()
            by_metric.append(by_metric_item)

        period_start: None | str | Unset
        if isinstance(self.period_start, Unset):
            period_start = UNSET
        elif isinstance(self.period_start, datetime.datetime):
            period_start = self.period_start.isoformat()
        else:
            period_start = self.period_start

        period_end: None | str | Unset
        if isinstance(self.period_end, Unset):
            period_end = UNSET
        elif isinstance(self.period_end, datetime.datetime):
            period_end = self.period_end.isoformat()
        else:
            period_end = self.period_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_credits_used": total_credits_used,
                "total_requests": total_requests,
                "credits_remaining": credits_remaining,
                "by_metric": by_metric,
            }
        )
        if period_start is not UNSET:
            field_dict["period_start"] = period_start
        if period_end is not UNSET:
            field_dict["period_end"] = period_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usage_dashboard_response_by_metric_item import UsageDashboardResponseByMetricItem  # noqa: PLC0415

        d = dict(src_dict)
        total_credits_used = d.pop("total_credits_used")

        total_requests = d.pop("total_requests")

        credits_remaining = d.pop("credits_remaining")

        by_metric = []
        _by_metric = d.pop("by_metric")
        for by_metric_item_data in _by_metric:
            by_metric_item = UsageDashboardResponseByMetricItem.from_dict(by_metric_item_data)

            by_metric.append(by_metric_item)

        def _parse_period_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_start_type_0 = datetime.datetime.fromisoformat(data)

                return period_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_start = _parse_period_start(d.pop("period_start", UNSET))

        def _parse_period_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_end_type_0 = datetime.datetime.fromisoformat(data)

                return period_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        period_end = _parse_period_end(d.pop("period_end", UNSET))

        usage_dashboard_response = cls(
            total_credits_used=total_credits_used,
            total_requests=total_requests,
            credits_remaining=credits_remaining,
            by_metric=by_metric,
            period_start=period_start,
            period_end=period_end,
        )

        usage_dashboard_response.additional_properties = d
        return usage_dashboard_response

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
