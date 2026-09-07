from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.region_revenue import RegionRevenue


T = TypeVar("T", bound="RevenueByRegionResponse")


@_attrs_define
class RevenueByRegionResponse:
    """GET /api/analytics/revenue-by-region — MRR grouped by org.pricing_region.

    Attributes:
        regions (list[RegionRevenue]):
        total_mrr (float):
    """

    regions: list[RegionRevenue]
    total_mrr: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()
            regions.append(regions_item)

        total_mrr = self.total_mrr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "regions": regions,
                "total_mrr": total_mrr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_revenue import RegionRevenue  # noqa: PLC0415

        d = dict(src_dict)
        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = RegionRevenue.from_dict(regions_item_data)

            regions.append(regions_item)

        total_mrr = d.pop("total_mrr")

        revenue_by_region_response = cls(
            regions=regions,
            total_mrr=total_mrr,
        )

        revenue_by_region_response.additional_properties = d
        return revenue_by_region_response

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
