from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BotGroupCreate")


@_attrs_define
class BotGroupCreate:
    """Schema for creating a bot group

    Attributes:
        group_name (str):
        group_description (None | str | Unset):
        org_id (None | Unset | UUID):
        member_bot_ids (list[UUID] | Unset):
    """

    group_name: str
    group_description: None | str | Unset = UNSET
    org_id: None | Unset | UUID = UNSET
    member_bot_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        group_description: None | str | Unset
        if isinstance(self.group_description, Unset):
            group_description = UNSET
        else:
            group_description = self.group_description

        org_id: None | str | Unset
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, UUID):
            org_id = str(self.org_id)
        else:
            org_id = self.org_id

        member_bot_ids: list[str] | Unset = UNSET
        if not isinstance(self.member_bot_ids, Unset):
            member_bot_ids = []
            for member_bot_ids_item_data in self.member_bot_ids:
                member_bot_ids_item = str(member_bot_ids_item_data)
                member_bot_ids.append(member_bot_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_name": group_name,
            }
        )
        if group_description is not UNSET:
            field_dict["group_description"] = group_description
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if member_bot_ids is not UNSET:
            field_dict["member_bot_ids"] = member_bot_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_name = d.pop("group_name")

        def _parse_group_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_description = _parse_group_description(d.pop("group_description", UNSET))

        def _parse_org_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                org_id_type_0 = UUID(data)

                return org_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        _member_bot_ids = d.pop("member_bot_ids", UNSET)
        member_bot_ids: list[UUID] | Unset = UNSET
        if _member_bot_ids is not UNSET:
            member_bot_ids = []
            for member_bot_ids_item_data in _member_bot_ids:
                member_bot_ids_item = UUID(member_bot_ids_item_data)

                member_bot_ids.append(member_bot_ids_item)

        bot_group_create = cls(
            group_name=group_name,
            group_description=group_description,
            org_id=org_id,
            member_bot_ids=member_bot_ids,
        )

        bot_group_create.additional_properties = d
        return bot_group_create

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
