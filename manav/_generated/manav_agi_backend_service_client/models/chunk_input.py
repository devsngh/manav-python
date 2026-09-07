from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChunkInput")


@_attrs_define
class ChunkInput:
    """
    Attributes:
        chunk_index (int): 0-based index within the document
        raw_text (str): The chunk's text content
        embedding (list[float] | None | Unset): Optional pre-computed embedding
        entity_refs (list[str] | None | Unset): Optional list of entity UUIDs
        metric_refs (list[str] | None | Unset): Optional list of metric UUIDs
        occurred_at (None | str | Unset): ISO 8601 if chunk has its own occurrence time
    """

    chunk_index: int
    raw_text: str
    embedding: list[float] | None | Unset = UNSET
    entity_refs: list[str] | None | Unset = UNSET
    metric_refs: list[str] | None | Unset = UNSET
    occurred_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chunk_index = self.chunk_index

        raw_text = self.raw_text

        embedding: list[float] | None | Unset
        if isinstance(self.embedding, Unset):
            embedding = UNSET
        elif isinstance(self.embedding, list):
            embedding = self.embedding

        else:
            embedding = self.embedding

        entity_refs: list[str] | None | Unset
        if isinstance(self.entity_refs, Unset):
            entity_refs = UNSET
        elif isinstance(self.entity_refs, list):
            entity_refs = self.entity_refs

        else:
            entity_refs = self.entity_refs

        metric_refs: list[str] | None | Unset
        if isinstance(self.metric_refs, Unset):
            metric_refs = UNSET
        elif isinstance(self.metric_refs, list):
            metric_refs = self.metric_refs

        else:
            metric_refs = self.metric_refs

        occurred_at: None | str | Unset
        if isinstance(self.occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = self.occurred_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chunk_index": chunk_index,
                "raw_text": raw_text,
            }
        )
        if embedding is not UNSET:
            field_dict["embedding"] = embedding
        if entity_refs is not UNSET:
            field_dict["entity_refs"] = entity_refs
        if metric_refs is not UNSET:
            field_dict["metric_refs"] = metric_refs
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chunk_index = d.pop("chunk_index")

        raw_text = d.pop("raw_text")

        def _parse_embedding(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                embedding_type_0 = cast(list[float], data)

                return embedding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        embedding = _parse_embedding(d.pop("embedding", UNSET))

        def _parse_entity_refs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entity_refs_type_0 = cast(list[str], data)

                return entity_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entity_refs = _parse_entity_refs(d.pop("entity_refs", UNSET))

        def _parse_metric_refs(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                metric_refs_type_0 = cast(list[str], data)

                return metric_refs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        metric_refs = _parse_metric_refs(d.pop("metric_refs", UNSET))

        def _parse_occurred_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occurred_at = _parse_occurred_at(d.pop("occurred_at", UNSET))

        chunk_input = cls(
            chunk_index=chunk_index,
            raw_text=raw_text,
            embedding=embedding,
            entity_refs=entity_refs,
            metric_refs=metric_refs,
            occurred_at=occurred_at,
        )

        chunk_input.additional_properties = d
        return chunk_input

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
