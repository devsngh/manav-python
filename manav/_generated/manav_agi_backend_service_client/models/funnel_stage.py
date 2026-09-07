from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FunnelStage")


@_attrs_define
class FunnelStage:
    """
    Attributes:
        stage (str):
        count (int):
        pct_of_signups (float):
    """

    stage: str
    count: int
    pct_of_signups: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage = self.stage

        count = self.count

        pct_of_signups = self.pct_of_signups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage": stage,
                "count": count,
                "pct_of_signups": pct_of_signups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage = d.pop("stage")

        count = d.pop("count")

        pct_of_signups = d.pop("pct_of_signups")

        funnel_stage = cls(
            stage=stage,
            count=count,
            pct_of_signups=pct_of_signups,
        )

        funnel_stage.additional_properties = d
        return funnel_stage

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
