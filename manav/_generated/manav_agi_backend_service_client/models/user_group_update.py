from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroupUpdate")


@_attrs_define
class UserGroupUpdate:
    """Schema for updating a user group

    Attributes:
        group_name (None | str | Unset):
        group_description (None | str | Unset):
        group_avatar_url (None | str | Unset):
        is_private (bool | None | Unset):
    """

    group_name: None | str | Unset = UNSET
    group_description: None | str | Unset = UNSET
    group_avatar_url: None | str | Unset = UNSET
    is_private: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        group_description: None | str | Unset
        if isinstance(self.group_description, Unset):
            group_description = UNSET
        else:
            group_description = self.group_description

        group_avatar_url: None | str | Unset
        if isinstance(self.group_avatar_url, Unset):
            group_avatar_url = UNSET
        else:
            group_avatar_url = self.group_avatar_url

        is_private: bool | None | Unset
        if isinstance(self.is_private, Unset):
            is_private = UNSET
        else:
            is_private = self.is_private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if group_description is not UNSET:
            field_dict["group_description"] = group_description
        if group_avatar_url is not UNSET:
            field_dict["group_avatar_url"] = group_avatar_url
        if is_private is not UNSET:
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("group_name", UNSET))

        def _parse_group_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_description = _parse_group_description(d.pop("group_description", UNSET))

        def _parse_group_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_avatar_url = _parse_group_avatar_url(d.pop("group_avatar_url", UNSET))

        def _parse_is_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_private = _parse_is_private(d.pop("is_private", UNSET))

        user_group_update = cls(
            group_name=group_name,
            group_description=group_description,
            group_avatar_url=group_avatar_url,
            is_private=is_private,
        )

        user_group_update.additional_properties = d
        return user_group_update

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
