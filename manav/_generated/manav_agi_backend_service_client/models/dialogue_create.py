from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DialogueCreate")


@_attrs_define
class DialogueCreate:
    """Schema for creating a new dialogue (sending query)

    Attributes:
        thread_id (UUID):
        query (str):
        prefer_bot_id (None | str | Unset):
        file_urls (list[str] | None | Unset):
        image_urls (list[str] | None | Unset):
    """

    thread_id: UUID
    query: str
    prefer_bot_id: None | str | Unset = UNSET
    file_urls: list[str] | None | Unset = UNSET
    image_urls: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        thread_id = str(self.thread_id)

        query = self.query

        prefer_bot_id: None | str | Unset
        if isinstance(self.prefer_bot_id, Unset):
            prefer_bot_id = UNSET
        else:
            prefer_bot_id = self.prefer_bot_id

        file_urls: list[str] | None | Unset
        if isinstance(self.file_urls, Unset):
            file_urls = UNSET
        elif isinstance(self.file_urls, list):
            file_urls = self.file_urls

        else:
            file_urls = self.file_urls

        image_urls: list[str] | None | Unset
        if isinstance(self.image_urls, Unset):
            image_urls = UNSET
        elif isinstance(self.image_urls, list):
            image_urls = self.image_urls

        else:
            image_urls = self.image_urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "thread_id": thread_id,
                "query": query,
            }
        )
        if prefer_bot_id is not UNSET:
            field_dict["prefer_bot_id"] = prefer_bot_id
        if file_urls is not UNSET:
            field_dict["file_urls"] = file_urls
        if image_urls is not UNSET:
            field_dict["image_urls"] = image_urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thread_id = UUID(d.pop("thread_id"))

        query = d.pop("query")

        def _parse_prefer_bot_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prefer_bot_id = _parse_prefer_bot_id(d.pop("prefer_bot_id", UNSET))

        def _parse_file_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                file_urls_type_0 = cast(list[str], data)

                return file_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        file_urls = _parse_file_urls(d.pop("file_urls", UNSET))

        def _parse_image_urls(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                image_urls_type_0 = cast(list[str], data)

                return image_urls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        image_urls = _parse_image_urls(d.pop("image_urls", UNSET))

        dialogue_create = cls(
            thread_id=thread_id,
            query=query,
            prefer_bot_id=prefer_bot_id,
            file_urls=file_urls,
            image_urls=image_urls,
        )

        dialogue_create.additional_properties = d
        return dialogue_create

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
