from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubtaskSummary")


@_attrs_define
class SubtaskSummary:
    """
    Attributes:
        id (str):
        title (str):
        status (str):
        assigned_to_bot_id (None | str):
    """

    id: str
    title: str
    status: str
    assigned_to_bot_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        status = self.status

        assigned_to_bot_id: None | str
        assigned_to_bot_id = self.assigned_to_bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "status": status,
                "assigned_to_bot_id": assigned_to_bot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        status = d.pop("status")

        def _parse_assigned_to_bot_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        assigned_to_bot_id = _parse_assigned_to_bot_id(d.pop("assigned_to_bot_id"))

        subtask_summary = cls(
            id=id,
            title=title,
            status=status,
            assigned_to_bot_id=assigned_to_bot_id,
        )

        subtask_summary.additional_properties = d
        return subtask_summary

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
