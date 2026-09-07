from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.conversion_cohort import ConversionCohort
    from ..models.lag_bucket import LagBucket


T = TypeVar("T", bound="ConversionResponse")


@_attrs_define
class ConversionResponse:
    """GET /api/analytics/growth/conversion

    Attributes:
        cohorts (list[ConversionCohort]):
        overall_rate (float):
        lag_buckets (list[LagBucket]):
    """

    cohorts: list[ConversionCohort]
    overall_rate: float
    lag_buckets: list[LagBucket]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cohorts = []
        for cohorts_item_data in self.cohorts:
            cohorts_item = cohorts_item_data.to_dict()
            cohorts.append(cohorts_item)

        overall_rate = self.overall_rate

        lag_buckets = []
        for lag_buckets_item_data in self.lag_buckets:
            lag_buckets_item = lag_buckets_item_data.to_dict()
            lag_buckets.append(lag_buckets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cohorts": cohorts,
                "overall_rate": overall_rate,
                "lag_buckets": lag_buckets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversion_cohort import ConversionCohort  # noqa: PLC0415
        from ..models.lag_bucket import LagBucket  # noqa: PLC0415

        d = dict(src_dict)
        cohorts = []
        _cohorts = d.pop("cohorts")
        for cohorts_item_data in _cohorts:
            cohorts_item = ConversionCohort.from_dict(cohorts_item_data)

            cohorts.append(cohorts_item)

        overall_rate = d.pop("overall_rate")

        lag_buckets = []
        _lag_buckets = d.pop("lag_buckets")
        for lag_buckets_item_data in _lag_buckets:
            lag_buckets_item = LagBucket.from_dict(lag_buckets_item_data)

            lag_buckets.append(lag_buckets_item)

        conversion_response = cls(
            cohorts=cohorts,
            overall_rate=overall_rate,
            lag_buckets=lag_buckets,
        )

        conversion_response.additional_properties = d
        return conversion_response

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
