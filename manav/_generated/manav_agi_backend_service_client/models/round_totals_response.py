from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RoundTotalsResponse")


@_attrs_define
class RoundTotalsResponse:
    """
    Attributes:
        fundraise_round_id (UUID):
        total_committed (str):
        total_wired (str):
    """

    fundraise_round_id: UUID
    total_committed: str
    total_wired: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fundraise_round_id = str(self.fundraise_round_id)

        total_committed = self.total_committed

        total_wired = self.total_wired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fundraise_round_id": fundraise_round_id,
                "total_committed": total_committed,
                "total_wired": total_wired,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fundraise_round_id = UUID(d.pop("fundraise_round_id"))

        total_committed = d.pop("total_committed")

        total_wired = d.pop("total_wired")

        round_totals_response = cls(
            fundraise_round_id=fundraise_round_id,
            total_committed=total_committed,
            total_wired=total_wired,
        )

        round_totals_response.additional_properties = d
        return round_totals_response

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
