from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WriteChunkResponse")


@_attrs_define
class WriteChunkResponse:
    """
    Attributes:
        chunk_id (str):
        document_id (str):
        chunk_index (int):
    """

    chunk_id: str
    document_id: str
    chunk_index: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_id = self.chunk_id

        document_id = self.document_id

        chunk_index = self.chunk_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_id": chunk_id,
                "document_id": document_id,
                "chunk_index": chunk_index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_id = d.pop("chunk_id")

        document_id = d.pop("document_id")

        chunk_index = d.pop("chunk_index")

        write_chunk_response = cls(
            chunk_id=chunk_id,
            document_id=document_id,
            chunk_index=chunk_index,
        )

        write_chunk_response.additional_properties = d
        return write_chunk_response

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
