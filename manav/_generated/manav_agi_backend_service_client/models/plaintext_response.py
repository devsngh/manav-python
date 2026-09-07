from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PlaintextResponse")


@_attrs_define
class PlaintextResponse:
    """
    Attributes:
        text (str):
        encoding (str):
        char_count (int):
    """

    text: str
    encoding: str
    char_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        encoding = self.encoding

        char_count = self.char_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "encoding": encoding,
                "char_count": char_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        encoding = d.pop("encoding")

        char_count = d.pop("char_count")

        plaintext_response = cls(
            text=text,
            encoding=encoding,
            char_count=char_count,
        )

        plaintext_response.additional_properties = d
        return plaintext_response

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
