from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_turn import ConversationTurn


T = TypeVar("T", bound="ConversationResponse")


@_attrs_define
class ConversationResponse:
    """
    Attributes:
        source_type (str):
        source_id (UUID):
        turns (list[ConversationTurn]):
        title (str | Unset):  Default: ''.
    """

    source_type: str
    source_id: UUID
    turns: list[ConversationTurn]
    title: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_type = self.source_type

        source_id = str(self.source_id)

        turns = []
        for turns_item_data in self.turns:
            turns_item = turns_item_data.to_dict()
            turns.append(turns_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_type": source_type,
                "source_id": source_id,
                "turns": turns,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_turn import ConversationTurn  # noqa: PLC0415

        d = dict(src_dict)
        source_type = d.pop("source_type")

        source_id = UUID(d.pop("source_id"))

        turns = []
        _turns = d.pop("turns")
        for turns_item_data in _turns:
            turns_item = ConversationTurn.from_dict(turns_item_data)

            turns.append(turns_item)

        title = d.pop("title", UNSET)

        conversation_response = cls(
            source_type=source_type,
            source_id=source_id,
            turns=turns,
            title=title,
        )

        conversation_response.additional_properties = d
        return conversation_response

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
