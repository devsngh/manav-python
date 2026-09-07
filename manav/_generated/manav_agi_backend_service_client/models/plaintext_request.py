from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaintextRequest")


@_attrs_define
class PlaintextRequest:
    """
    Attributes:
        s3_key (str):
        encoding (None | str | Unset): UTF-8 by default, latin-1 fallback
    """

    s3_key: str
    encoding: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        s3_key = self.s3_key

        encoding: None | str | Unset
        if isinstance(self.encoding, Unset):
            encoding = UNSET
        else:
            encoding = self.encoding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "s3_key": s3_key,
            }
        )
        if encoding is not UNSET:
            field_dict["encoding"] = encoding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        s3_key = d.pop("s3_key")

        def _parse_encoding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encoding = _parse_encoding(d.pop("encoding", UNSET))

        plaintext_request = cls(
            s3_key=s3_key,
            encoding=encoding,
        )

        plaintext_request.additional_properties = d
        return plaintext_request

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
