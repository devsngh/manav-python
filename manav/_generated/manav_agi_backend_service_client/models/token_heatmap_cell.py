from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TokenHeatmapCell")


@_attrs_define
class TokenHeatmapCell:
    """
    Attributes:
        dow (int):
        hour (int):
        tokens (int):
    """

    dow: int
    hour: int
    tokens: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dow = self.dow

        hour = self.hour

        tokens = self.tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dow": dow,
                "hour": hour,
                "tokens": tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dow = d.pop("dow")

        hour = d.pop("hour")

        tokens = d.pop("tokens")

        token_heatmap_cell = cls(
            dow=dow,
            hour=hour,
            tokens=tokens,
        )

        token_heatmap_cell.additional_properties = d
        return token_heatmap_cell

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
