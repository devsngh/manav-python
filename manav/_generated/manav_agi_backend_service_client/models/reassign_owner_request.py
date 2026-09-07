from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReassignOwnerRequest")


@_attrs_define
class ReassignOwnerRequest:
    """
    Attributes:
        new_user_id (None | Unset | UUID):
        new_bot_id (None | Unset | UUID):
    """

    new_user_id: None | Unset | UUID = UNSET
    new_bot_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_user_id: None | str | Unset
        if isinstance(self.new_user_id, Unset):
            new_user_id = UNSET
        elif isinstance(self.new_user_id, UUID):
            new_user_id = str(self.new_user_id)
        else:
            new_user_id = self.new_user_id

        new_bot_id: None | str | Unset
        if isinstance(self.new_bot_id, Unset):
            new_bot_id = UNSET
        elif isinstance(self.new_bot_id, UUID):
            new_bot_id = str(self.new_bot_id)
        else:
            new_bot_id = self.new_bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_user_id is not UNSET:
            field_dict["new_user_id"] = new_user_id
        if new_bot_id is not UNSET:
            field_dict["new_bot_id"] = new_bot_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_new_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_user_id_type_0 = UUID(data)

                return new_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        new_user_id = _parse_new_user_id(d.pop("new_user_id", UNSET))

        def _parse_new_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_bot_id_type_0 = UUID(data)

                return new_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        new_bot_id = _parse_new_bot_id(d.pop("new_bot_id", UNSET))

        reassign_owner_request = cls(
            new_user_id=new_user_id,
            new_bot_id=new_bot_id,
        )

        reassign_owner_request.additional_properties = d
        return reassign_owner_request

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
