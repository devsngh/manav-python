from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BackendFileWriteBody")


@_attrs_define
class BackendFileWriteBody:
    """
    Attributes:
        bot_id (str):
        file_path (str):
        content (str):
    """

    bot_id: str
    file_path: str
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_id = self.bot_id

        file_path = self.file_path

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot_id": bot_id,
                "file_path": file_path,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        file_path = d.pop("file_path")

        content = d.pop("content")

        backend_file_write_body = cls(
            bot_id=bot_id,
            file_path=file_path,
            content=content,
        )

        backend_file_write_body.additional_properties = d
        return backend_file_write_body

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
