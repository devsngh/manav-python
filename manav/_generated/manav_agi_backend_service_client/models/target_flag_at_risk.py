from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TargetFlagAtRisk")


@_attrs_define
class TargetFlagAtRisk:
    """POST .../flag-at-risk — agent self-flags.

    Attributes:
        reason (str):
        flagged_by_id (UUID):
    """

    reason: str
    flagged_by_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        flagged_by_id = str(self.flagged_by_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reason": reason,
                "flagged_by_id": flagged_by_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason")

        flagged_by_id = UUID(d.pop("flagged_by_id"))

        target_flag_at_risk = cls(
            reason=reason,
            flagged_by_id=flagged_by_id,
        )

        target_flag_at_risk.additional_properties = d
        return target_flag_at_risk

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
