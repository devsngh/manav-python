from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cabinet_reseed_response_counts import CabinetReseedResponseCounts


T = TypeVar("T", bound="CabinetReseedResponse")


@_attrs_define
class CabinetReseedResponse:
    """
    Attributes:
        agent_name (str):
        counts (CabinetReseedResponseCounts):
    """

    agent_name: str
    counts: CabinetReseedResponseCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_name = self.agent_name

        counts = self.counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_name": agent_name,
                "counts": counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cabinet_reseed_response_counts import CabinetReseedResponseCounts  # noqa: PLC0415

        d = dict(src_dict)
        agent_name = d.pop("agent_name")

        counts = CabinetReseedResponseCounts.from_dict(d.pop("counts"))

        cabinet_reseed_response = cls(
            agent_name=agent_name,
            counts=counts,
        )

        cabinet_reseed_response.additional_properties = d
        return cabinet_reseed_response

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
