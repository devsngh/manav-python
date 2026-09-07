from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dialogue_response import DialogueResponse


T = TypeVar("T", bound="DialogueListResponse")


@_attrs_define
class DialogueListResponse:
    """Schema for dialogue list in a thread

    Attributes:
        dialogues (list[DialogueResponse]):
        total (int):
        thread_id (UUID):
    """

    dialogues: list[DialogueResponse]
    total: int
    thread_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dialogues = []
        for dialogues_item_data in self.dialogues:
            dialogues_item = dialogues_item_data.to_dict()
            dialogues.append(dialogues_item)

        total = self.total

        thread_id = str(self.thread_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialogues": dialogues,
                "total": total,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dialogue_response import DialogueResponse  # noqa: PLC0415

        d = dict(src_dict)
        dialogues = []
        _dialogues = d.pop("dialogues")
        for dialogues_item_data in _dialogues:
            dialogues_item = DialogueResponse.from_dict(dialogues_item_data)

            dialogues.append(dialogues_item)

        total = d.pop("total")

        thread_id = UUID(d.pop("thread_id"))

        dialogue_list_response = cls(
            dialogues=dialogues,
            total=total,
            thread_id=thread_id,
        )

        dialogue_list_response.additional_properties = d
        return dialogue_list_response

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
