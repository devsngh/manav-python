from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawFK")


@_attrs_define
class RawFK:
    """
    Attributes:
        from_table (str):
        from_column (str):
        to_table (str):
        to_column (str):
        constraint_name (None | str | Unset):
    """

    from_table: str
    from_column: str
    to_table: str
    to_column: str
    constraint_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_table = self.from_table

        from_column = self.from_column

        to_table = self.to_table

        to_column = self.to_column

        constraint_name: None | str | Unset
        if isinstance(self.constraint_name, Unset):
            constraint_name = UNSET
        else:
            constraint_name = self.constraint_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from_table": from_table,
                "from_column": from_column,
                "to_table": to_table,
                "to_column": to_column,
            }
        )
        if constraint_name is not UNSET:
            field_dict["constraint_name"] = constraint_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_table = d.pop("from_table")

        from_column = d.pop("from_column")

        to_table = d.pop("to_table")

        to_column = d.pop("to_column")

        def _parse_constraint_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constraint_name = _parse_constraint_name(d.pop("constraint_name", UNSET))

        raw_fk = cls(
            from_table=from_table,
            from_column=from_column,
            to_table=to_table,
            to_column=to_column,
            constraint_name=constraint_name,
        )

        raw_fk.additional_properties = d
        return raw_fk

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
