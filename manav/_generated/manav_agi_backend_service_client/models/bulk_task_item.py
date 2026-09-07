from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_task_item_input_data_type_0 import BulkTaskItemInputDataType0


T = TypeVar("T", bound="BulkTaskItem")


@_attrs_define
class BulkTaskItem:
    """
    Attributes:
        title (str):
        assign_to (None | str | Unset):
        assign_to_bot_id (None | str | Unset):
        priority (str | Unset):  Default: 'normal'.
        input_data (BulkTaskItemInputDataType0 | None | Unset):
    """

    title: str
    assign_to: None | str | Unset = UNSET
    assign_to_bot_id: None | str | Unset = UNSET
    priority: str | Unset = "normal"
    input_data: BulkTaskItemInputDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_task_item_input_data_type_0 import BulkTaskItemInputDataType0  # noqa: PLC0415

        title = self.title

        assign_to: None | str | Unset
        if isinstance(self.assign_to, Unset):
            assign_to = UNSET
        else:
            assign_to = self.assign_to

        assign_to_bot_id: None | str | Unset
        if isinstance(self.assign_to_bot_id, Unset):
            assign_to_bot_id = UNSET
        else:
            assign_to_bot_id = self.assign_to_bot_id

        priority = self.priority

        input_data: dict[str, Any] | None | Unset
        if isinstance(self.input_data, Unset):
            input_data = UNSET
        elif isinstance(self.input_data, BulkTaskItemInputDataType0):
            input_data = self.input_data.to_dict()
        else:
            input_data = self.input_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if assign_to is not UNSET:
            field_dict["assign_to"] = assign_to
        if assign_to_bot_id is not UNSET:
            field_dict["assign_to_bot_id"] = assign_to_bot_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if input_data is not UNSET:
            field_dict["input_data"] = input_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_task_item_input_data_type_0 import BulkTaskItemInputDataType0  # noqa: PLC0415

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_assign_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to = _parse_assign_to(d.pop("assign_to", UNSET))

        def _parse_assign_to_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_bot_id = _parse_assign_to_bot_id(d.pop("assign_to_bot_id", UNSET))

        priority = d.pop("priority", UNSET)

        def _parse_input_data(data: object) -> BulkTaskItemInputDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                input_data_type_0 = BulkTaskItemInputDataType0.from_dict(data)

                return input_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BulkTaskItemInputDataType0 | None | Unset, data)

        input_data = _parse_input_data(d.pop("input_data", UNSET))

        bulk_task_item = cls(
            title=title,
            assign_to=assign_to,
            assign_to_bot_id=assign_to_bot_id,
            priority=priority,
            input_data=input_data,
        )

        bulk_task_item.additional_properties = d
        return bulk_task_item

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
