from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PendingHILSummary")


@_attrs_define
class PendingHILSummary:
    """
    Attributes:
        event_id (str):
        tool_name (str):
        review_message (None | str):
        created_at (datetime.datetime):
    """

    event_id: str
    tool_name: str
    review_message: None | str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_id = self.event_id

        tool_name = self.tool_name

        review_message: None | str
        review_message = self.review_message

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_id": event_id,
                "tool_name": tool_name,
                "review_message": review_message,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_id = d.pop("event_id")

        tool_name = d.pop("tool_name")

        def _parse_review_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        review_message = _parse_review_message(d.pop("review_message"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        pending_hil_summary = cls(
            event_id=event_id,
            tool_name=tool_name,
            review_message=review_message,
            created_at=created_at,
        )

        pending_hil_summary.additional_properties = d
        return pending_hil_summary

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
