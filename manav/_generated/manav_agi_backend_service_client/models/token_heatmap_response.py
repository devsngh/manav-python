from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token_heatmap_cell import TokenHeatmapCell


T = TypeVar("T", bound="TokenHeatmapResponse")


@_attrs_define
class TokenHeatmapResponse:
    """GET /api/analytics/billing/token-heatmap — 7×24 token-usage matrix.

    Attributes:
        cells (list[TokenHeatmapCell]):
    """

    cells: list[TokenHeatmapCell]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()
            cells.append(cells_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cells": cells,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_heatmap_cell import TokenHeatmapCell  # noqa: PLC0415

        d = dict(src_dict)
        cells = []
        _cells = d.pop("cells")
        for cells_item_data in _cells:
            cells_item = TokenHeatmapCell.from_dict(cells_item_data)

            cells.append(cells_item)

        token_heatmap_response = cls(
            cells=cells,
        )

        token_heatmap_response.additional_properties = d
        return token_heatmap_response

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
