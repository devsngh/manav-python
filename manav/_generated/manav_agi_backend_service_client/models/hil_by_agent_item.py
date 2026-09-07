from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HilByAgentItem")


@_attrs_define
class HilByAgentItem:
    """
    Attributes:
        bot_id (str):
        bot_name (str):
        total (int):
        approved (int):
        rejected (int):
        pending (int):
        approval_rate (float):
    """

    bot_id: str
    bot_name: str
    total: int
    approved: int
    rejected: int
    pending: int
    approval_rate: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = self.bot_id

        bot_name = self.bot_name

        total = self.total

        approved = self.approved

        rejected = self.rejected

        pending = self.pending

        approval_rate = self.approval_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "bot_name": bot_name,
                "total": total,
                "approved": approved,
                "rejected": rejected,
                "pending": pending,
                "approval_rate": approval_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        bot_name = d.pop("bot_name")

        total = d.pop("total")

        approved = d.pop("approved")

        rejected = d.pop("rejected")

        pending = d.pop("pending")

        approval_rate = d.pop("approval_rate")

        hil_by_agent_item = cls(
            bot_id=bot_id,
            bot_name=bot_name,
            total=total,
            approved=approved,
            rejected=rejected,
            pending=pending,
            approval_rate=approval_rate,
        )

        hil_by_agent_item.additional_properties = d
        return hil_by_agent_item

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
