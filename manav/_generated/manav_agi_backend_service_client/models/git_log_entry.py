from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GitLogEntry")


@_attrs_define
class GitLogEntry:
    """
    Attributes:
        hash_ (str):
        short_hash (str):
        message (str):
        author (str):
        date (str):
    """

    hash_: str
    short_hash: str
    message: str
    author: str
    date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        short_hash = self.short_hash

        message = self.message

        author = self.author

        date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
                "short_hash": short_hash,
                "message": message,
                "author": author,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash")

        short_hash = d.pop("short_hash")

        message = d.pop("message")

        author = d.pop("author")

        date = d.pop("date")

        git_log_entry = cls(
            hash_=hash_,
            short_hash=short_hash,
            message=message,
            author=author,
            date=date,
        )

        git_log_entry.additional_properties = d
        return git_log_entry

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
