from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.monthly_revenue_point import MonthlyRevenuePoint


T = TypeVar("T", bound="MarketplaceSummaryResponse")


@_attrs_define
class MarketplaceSummaryResponse:
    """GET /api/analytics/marketplace/summary — KPIs + GMV/platform/publisher trend.

    Attributes:
        gmv_total (float):
        platform_revenue (float):
        publisher_payout (float):
        gmv_current_month (float):
        platform_current_month (float):
        publisher_current_month (float):
        active_listings (int):
        active_subscriptions (int):
        liquidity_pct (float):
        avg_rating (float):
        rated_listings_count (int):
        trend (list[MonthlyRevenuePoint]):
    """

    gmv_total: float
    platform_revenue: float
    publisher_payout: float
    gmv_current_month: float
    platform_current_month: float
    publisher_current_month: float
    active_listings: int
    active_subscriptions: int
    liquidity_pct: float
    avg_rating: float
    rated_listings_count: int
    trend: list[MonthlyRevenuePoint]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmv_total = self.gmv_total

        platform_revenue = self.platform_revenue

        publisher_payout = self.publisher_payout

        gmv_current_month = self.gmv_current_month

        platform_current_month = self.platform_current_month

        publisher_current_month = self.publisher_current_month

        active_listings = self.active_listings

        active_subscriptions = self.active_subscriptions

        liquidity_pct = self.liquidity_pct

        avg_rating = self.avg_rating

        rated_listings_count = self.rated_listings_count

        trend = []
        for trend_item_data in self.trend:
            trend_item = trend_item_data.to_dict()
            trend.append(trend_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gmv_total": gmv_total,
                "platform_revenue": platform_revenue,
                "publisher_payout": publisher_payout,
                "gmv_current_month": gmv_current_month,
                "platform_current_month": platform_current_month,
                "publisher_current_month": publisher_current_month,
                "active_listings": active_listings,
                "active_subscriptions": active_subscriptions,
                "liquidity_pct": liquidity_pct,
                "avg_rating": avg_rating,
                "rated_listings_count": rated_listings_count,
                "trend": trend,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monthly_revenue_point import MonthlyRevenuePoint  # noqa: PLC0415

        d = dict(src_dict)
        gmv_total = d.pop("gmv_total")

        platform_revenue = d.pop("platform_revenue")

        publisher_payout = d.pop("publisher_payout")

        gmv_current_month = d.pop("gmv_current_month")

        platform_current_month = d.pop("platform_current_month")

        publisher_current_month = d.pop("publisher_current_month")

        active_listings = d.pop("active_listings")

        active_subscriptions = d.pop("active_subscriptions")

        liquidity_pct = d.pop("liquidity_pct")

        avg_rating = d.pop("avg_rating")

        rated_listings_count = d.pop("rated_listings_count")

        trend = []
        _trend = d.pop("trend")
        for trend_item_data in _trend:
            trend_item = MonthlyRevenuePoint.from_dict(trend_item_data)

            trend.append(trend_item)

        marketplace_summary_response = cls(
            gmv_total=gmv_total,
            platform_revenue=platform_revenue,
            publisher_payout=publisher_payout,
            gmv_current_month=gmv_current_month,
            platform_current_month=platform_current_month,
            publisher_current_month=publisher_current_month,
            active_listings=active_listings,
            active_subscriptions=active_subscriptions,
            liquidity_pct=liquidity_pct,
            avg_rating=avg_rating,
            rated_listings_count=rated_listings_count,
            trend=trend,
        )

        marketplace_summary_response.additional_properties = d
        return marketplace_summary_response

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
