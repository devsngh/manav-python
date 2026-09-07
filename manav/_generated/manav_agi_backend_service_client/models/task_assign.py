from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskAssign")


@_attrs_define
class TaskAssign:
    """
    Attributes:
        assigned_to_user_id (None | Unset | UUID):
        assigned_to_bot_id (None | Unset | UUID):
    """

    assigned_to_user_id: None | Unset | UUID = UNSET
    assigned_to_bot_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assigned_to_user_id: None | str | Unset
        if isinstance(self.assigned_to_user_id, Unset):
            assigned_to_user_id = UNSET
        elif isinstance(self.assigned_to_user_id, UUID):
            assigned_to_user_id = str(self.assigned_to_user_id)
        else:
            assigned_to_user_id = self.assigned_to_user_id

        assigned_to_bot_id: None | str | Unset
        if isinstance(self.assigned_to_bot_id, Unset):
            assigned_to_bot_id = UNSET
        elif isinstance(self.assigned_to_bot_id, UUID):
            assigned_to_bot_id = str(self.assigned_to_bot_id)
        else:
            assigned_to_bot_id = self.assigned_to_bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_bot_id is not UNSET:
            field_dict["assigned_to_bot_id"] = assigned_to_bot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assigned_to_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_user_id_type_0 = UUID(data)

                return assigned_to_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to_user_id = _parse_assigned_to_user_id(d.pop("assigned_to_user_id", UNSET))

        def _parse_assigned_to_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_to_bot_id_type_0 = UUID(data)

                return assigned_to_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assigned_to_bot_id = _parse_assigned_to_bot_id(d.pop("assigned_to_bot_id", UNSET))

        task_assign = cls(
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_bot_id=assigned_to_bot_id,
        )

        task_assign.additional_properties = d
        return task_assign

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
