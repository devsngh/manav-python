from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dialogue_header import DialogueHeader
    from ..models.span_node import SpanNode


T = TypeVar("T", bound="DialogueTreeResponse")


@_attrs_define
class DialogueTreeResponse:
    """
    Attributes:
        header (DialogueHeader): Sticky-top context shown above the execution tree.
        spans (list[SpanNode]):
    """

    header: DialogueHeader
    spans: list[SpanNode]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header = self.header.to_dict()

        spans = []
        for spans_item_data in self.spans:
            spans_item = spans_item_data.to_dict()
            spans.append(spans_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "header": header,
                "spans": spans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dialogue_header import DialogueHeader  # noqa: PLC0415
        from ..models.span_node import SpanNode  # noqa: PLC0415

        d = dict(src_dict)
        header = DialogueHeader.from_dict(d.pop("header"))

        spans = []
        _spans = d.pop("spans")
        for spans_item_data in _spans:
            spans_item = SpanNode.from_dict(spans_item_data)

            spans.append(spans_item)

        dialogue_tree_response = cls(
            header=header,
            spans=spans,
        )

        dialogue_tree_response.additional_properties = d
        return dialogue_tree_response

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
