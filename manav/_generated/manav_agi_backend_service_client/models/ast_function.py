from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AstFunction")


@_attrs_define
class AstFunction:
    """
    Attributes:
        name (str):
        line_start (int):
        line_end (int):
        source (str):
        docstring (None | str | Unset):
        is_async (bool | Unset):  Default: False.
    """

    name: str
    line_start: int
    line_end: int
    source: str
    docstring: None | str | Unset = UNSET
    is_async: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        line_start = self.line_start

        line_end = self.line_end

        source = self.source

        docstring: None | str | Unset
        if isinstance(self.docstring, Unset):
            docstring = UNSET
        else:
            docstring = self.docstring

        is_async = self.is_async

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "line_start": line_start,
                "line_end": line_end,
                "source": source,
            }
        )
        if docstring is not UNSET:
            field_dict["docstring"] = docstring
        if is_async is not UNSET:
            field_dict["is_async"] = is_async

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        line_start = d.pop("line_start")

        line_end = d.pop("line_end")

        source = d.pop("source")

        def _parse_docstring(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docstring = _parse_docstring(d.pop("docstring", UNSET))

        is_async = d.pop("is_async", UNSET)

        ast_function = cls(
            name=name,
            line_start=line_start,
            line_end=line_end,
            source=source,
            docstring=docstring,
            is_async=is_async,
        )

        ast_function.additional_properties = d
        return ast_function

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
