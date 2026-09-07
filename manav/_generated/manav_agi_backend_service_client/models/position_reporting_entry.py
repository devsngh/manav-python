from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionReportingEntry")


@_attrs_define
class PositionReportingEntry:
    """A position with its bot info, used in reporting hierarchy responses

    Attributes:
        position_id (str):
        title (str):
        department (None | str | Unset):
        bot_id (None | str | Unset):
        bot_name (None | str | Unset):
        user_id (None | str | Unset):
        user_name (None | str | Unset):
    """

    position_id: str
    title: str
    department: None | str | Unset = UNSET
    bot_id: None | str | Unset = UNSET
    bot_name: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position_id = self.position_id

        title = self.title

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        bot_id: None | str | Unset
        if isinstance(self.bot_id, Unset):
            bot_id = UNSET
        else:
            bot_id = self.bot_id

        bot_name: None | str | Unset
        if isinstance(self.bot_name, Unset):
            bot_name = UNSET
        else:
            bot_name = self.bot_name

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position_id": position_id,
                "title": title,
            }
        )
        if department is not UNSET:
            field_dict["department"] = department
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_name is not UNSET:
            field_dict["bot_name"] = bot_name
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position_id = d.pop("position_id")

        title = d.pop("title")

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_id = _parse_bot_id(d.pop("bot_id", UNSET))

        def _parse_bot_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bot_name = _parse_bot_name(d.pop("bot_name", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        position_reporting_entry = cls(
            position_id=position_id,
            title=title,
            department=department,
            bot_id=bot_id,
            bot_name=bot_name,
            user_id=user_id,
            user_name=user_name,
        )

        position_reporting_entry.additional_properties = d
        return position_reporting_entry

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
