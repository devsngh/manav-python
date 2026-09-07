from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.activation_cohort import ActivationCohort


T = TypeVar("T", bound="ActivationRateResponse")


@_attrs_define
class ActivationRateResponse:
    """GET /api/analytics/growth/activation-rate

    Attributes:
        cohorts (list[ActivationCohort]):
        overall_rate (float):
        window_days (int):
    """

    cohorts: list[ActivationCohort]
    overall_rate: float
    window_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cohorts = []
        for cohorts_item_data in self.cohorts:
            cohorts_item = cohorts_item_data.to_dict()
            cohorts.append(cohorts_item)

        overall_rate = self.overall_rate

        window_days = self.window_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cohorts": cohorts,
                "overall_rate": overall_rate,
                "window_days": window_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activation_cohort import ActivationCohort  # noqa: PLC0415

        d = dict(src_dict)
        cohorts = []
        _cohorts = d.pop("cohorts")
        for cohorts_item_data in _cohorts:
            cohorts_item = ActivationCohort.from_dict(cohorts_item_data)

            cohorts.append(cohorts_item)

        overall_rate = d.pop("overall_rate")

        window_days = d.pop("window_days")

        activation_rate_response = cls(
            cohorts=cohorts,
            overall_rate=overall_rate,
            window_days=window_days,
        )

        activation_rate_response.additional_properties = d
        return activation_rate_response

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
