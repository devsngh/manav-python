from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cohort_retention_row import CohortRetentionRow


T = TypeVar("T", bound="CohortRetentionResponse")


@_attrs_define
class CohortRetentionResponse:
    """GET /api/analytics/growth/cohort-retention

    Attributes:
        cohorts (list[CohortRetentionRow]):
    """

    cohorts: list[CohortRetentionRow]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cohorts = []
        for cohorts_item_data in self.cohorts:
            cohorts_item = cohorts_item_data.to_dict()
            cohorts.append(cohorts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cohorts": cohorts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cohort_retention_row import CohortRetentionRow  # noqa: PLC0415

        d = dict(src_dict)
        cohorts = []
        _cohorts = d.pop("cohorts")
        for cohorts_item_data in _cohorts:
            cohorts_item = CohortRetentionRow.from_dict(cohorts_item_data)

            cohorts.append(cohorts_item)

        cohort_retention_response = cls(
            cohorts=cohorts,
        )

        cohort_retention_response.additional_properties = d
        return cohort_retention_response

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
