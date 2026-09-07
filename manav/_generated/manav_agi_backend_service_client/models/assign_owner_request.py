from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignOwnerRequest")


@_attrs_define
class AssignOwnerRequest:
    """
    Attributes:
        owner_type (str): org / bot / human
        owner_bot_id (None | Unset | UUID):
        owner_user_id (None | Unset | UUID):
        owner_persona_id (None | Unset | UUID):
        is_primary (bool | Unset):  Default: True.
    """

    owner_type: str
    owner_bot_id: None | Unset | UUID = UNSET
    owner_user_id: None | Unset | UUID = UNSET
    owner_persona_id: None | Unset | UUID = UNSET
    is_primary: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_type = self.owner_type

        owner_bot_id: None | str | Unset
        if isinstance(self.owner_bot_id, Unset):
            owner_bot_id = UNSET
        elif isinstance(self.owner_bot_id, UUID):
            owner_bot_id = str(self.owner_bot_id)
        else:
            owner_bot_id = self.owner_bot_id

        owner_user_id: None | str | Unset
        if isinstance(self.owner_user_id, Unset):
            owner_user_id = UNSET
        elif isinstance(self.owner_user_id, UUID):
            owner_user_id = str(self.owner_user_id)
        else:
            owner_user_id = self.owner_user_id

        owner_persona_id: None | str | Unset
        if isinstance(self.owner_persona_id, Unset):
            owner_persona_id = UNSET
        elif isinstance(self.owner_persona_id, UUID):
            owner_persona_id = str(self.owner_persona_id)
        else:
            owner_persona_id = self.owner_persona_id

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "owner_type": owner_type,
            }
        )
        if owner_bot_id is not UNSET:
            field_dict["owner_bot_id"] = owner_bot_id
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if owner_persona_id is not UNSET:
            field_dict["owner_persona_id"] = owner_persona_id
        if is_primary is not UNSET:
            field_dict["is_primary"] = is_primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        owner_type = d.pop("owner_type")

        def _parse_owner_bot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_bot_id_type_0 = UUID(data)

                return owner_bot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_bot_id = _parse_owner_bot_id(d.pop("owner_bot_id", UNSET))

        def _parse_owner_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_user_id_type_0 = UUID(data)

                return owner_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_user_id = _parse_owner_user_id(d.pop("owner_user_id", UNSET))

        def _parse_owner_persona_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                owner_persona_id_type_0 = UUID(data)

                return owner_persona_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        owner_persona_id = _parse_owner_persona_id(d.pop("owner_persona_id", UNSET))

        is_primary = d.pop("is_primary", UNSET)

        assign_owner_request = cls(
            owner_type=owner_type,
            owner_bot_id=owner_bot_id,
            owner_user_id=owner_user_id,
            owner_persona_id=owner_persona_id,
            is_primary=is_primary,
        )

        assign_owner_request.additional_properties = d
        return assign_owner_request

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
