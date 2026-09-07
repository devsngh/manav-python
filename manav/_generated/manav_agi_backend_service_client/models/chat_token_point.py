from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatTokenPoint")


@_attrs_define
class ChatTokenPoint:
    """
    Attributes:
        query_tokens (int):
        response_tokens (int):
        bot_id (str):
    """

    query_tokens: int
    response_tokens: int
    bot_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_tokens = self.query_tokens

        response_tokens = self.response_tokens

        bot_id = self.bot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query_tokens": query_tokens,
                "response_tokens": response_tokens,
                "bot_id": bot_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query_tokens = d.pop("query_tokens")

        response_tokens = d.pop("response_tokens")

        bot_id = d.pop("bot_id")

        chat_token_point = cls(
            query_tokens=query_tokens,
            response_tokens=response_tokens,
            bot_id=bot_id,
        )

        chat_token_point.additional_properties = d
        return chat_token_point

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
