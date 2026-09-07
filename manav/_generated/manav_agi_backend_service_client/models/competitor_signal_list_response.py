from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.competitor_signal_response import CompetitorSignalResponse


T = TypeVar("T", bound="CompetitorSignalListResponse")


@_attrs_define
class CompetitorSignalListResponse:
    """
    Attributes:
        signals (list[CompetitorSignalResponse]):
        total (int):
    """

    signals: list[CompetitorSignalResponse]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signals = []
        for signals_item_data in self.signals:
            signals_item = signals_item_data.to_dict()
            signals.append(signals_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "signals": signals,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competitor_signal_response import CompetitorSignalResponse  # noqa: PLC0415

        d = dict(src_dict)
        signals = []
        _signals = d.pop("signals")
        for signals_item_data in _signals:
            signals_item = CompetitorSignalResponse.from_dict(signals_item_data)

            signals.append(signals_item)

        total = d.pop("total")

        competitor_signal_list_response = cls(
            signals=signals,
            total=total,
        )

        competitor_signal_list_response.additional_properties = d
        return competitor_signal_list_response

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
