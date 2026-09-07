from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chunk_input import ChunkInput


T = TypeVar("T", bound="WriteChunkRequest")


@_attrs_define
class WriteChunkRequest:
    """
    Attributes:
        document_id (str):
        chunk (ChunkInput):
        total_chunks (int | None | Unset): If set, also updates ingestion_documents.total_chunks
    """

    document_id: str
    chunk: ChunkInput
    total_chunks: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = self.document_id

        chunk = self.chunk.to_dict()

        total_chunks: int | None | Unset
        if isinstance(self.total_chunks, Unset):
            total_chunks = UNSET
        else:
            total_chunks = self.total_chunks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "chunk": chunk,
            }
        )
        if total_chunks is not UNSET:
            field_dict["total_chunks"] = total_chunks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chunk_input import ChunkInput  # noqa: PLC0415

        d = dict(src_dict)
        document_id = d.pop("document_id")

        chunk = ChunkInput.from_dict(d.pop("chunk"))

        def _parse_total_chunks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_chunks = _parse_total_chunks(d.pop("total_chunks", UNSET))

        write_chunk_request = cls(
            document_id=document_id,
            chunk=chunk,
            total_chunks=total_chunks,
        )

        write_chunk_request.additional_properties = d
        return write_chunk_request

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
